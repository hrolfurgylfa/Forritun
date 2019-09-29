"use strict";

// ########################## HTML Krækjur ##########################
const WebGL_Canvas = document.getElementById("WebGL_Canvas");
const gl = WebGL_Canvas.getContext("webgl");


// ============================= Shaders =============================
// Þessi shader tekur litinn frá vertex shaderinum og setir hann yfir allt formið.
const fragmentShaderSource = `
    varying lowp vec4 vColor;

    void main(void) {
        gl_FragColor = vColor;
    }
`;
// Hérna er vertex shaderinn, hann keyrir einu sinni fyrir hver hnit og gefur út staðsetningu og lit.
const vertexShaderSource = `
    attribute vec4 aVertexPosition;
    attribute vec4 aVertexColor;

    uniform mat4 uModelViewMatrix;
    uniform mat4 uProjectionMatrix;

    varying lowp vec4 vColor;

    void main(void) {
        gl_Position = uProjectionMatrix * uModelViewMatrix * aVertexPosition;
        vColor = aVertexColor;
    }
`;


// <-><-><-><-><-><-><-><-><-><-> Föll <-><-><-><-><-><-><-><-><-><->

// Þetta fall býr til shader
let hladaShader = (gl, gerd, source) => {

    // Búa til shaderinn
    let shader = gl.createShader(gerd);

    // Þetta setir sorourceinn í shaderinn
    gl.shaderSource(shader, source);
  
    // Compila shaderinn
    gl.compileShader(shader);
  
    // Þetta varar við ef eitthvað klikkar í því að búa til shaderinn
    if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
        alert('Ekki tókst að hlaða shader:  ' + gl.getShaderInfoLog(shader));
        gl.deleteShader(shader);
        return null;
    }

    // Skila shaderinum
    return shader;
}
// Þetta fall býr til shader forrit úr vertex shader og fragment shader
let geraShaderForrit = (gl, vertexShaderSource, fragmentShaderSource) => {

    // Gera shaderana
    let vertexShader = hladaShader(gl, gl.VERTEX_SHADER, vertexShaderSource);
    let fragmentShader = hladaShader(gl, gl.FRAGMENT_SHADER, fragmentShaderSource);
  
    // Búa til shader forritið
    let shaderForrit = gl.createProgram();

    // Setja shaderana á shader forritið
    gl.attachShader(shaderForrit, vertexShader);
    gl.attachShader(shaderForrit, fragmentShader);

    // Segja WebGL að nota shader forritið
    gl.linkProgram(shaderForrit);
  
    // Þetta varar við ef eitthvað klikkar í því að búa til shader forritið
    if (!gl.getProgramParameter(shaderForrit, gl.LINK_STATUS)) {
        alert('Það tókst ekki að búa til Shader forrit: ' + gl.getProgramInfoLog(shaderForrit));
        return null;
    }
    
    // Skila shader forritinu
    return shaderForrit;
}
// Þetta fall gerir bufferana
let gera2DForm = (gl, stadsetningar) => {

    // Gera buffer fyrir staðsetningu kassans
    let stadsetningarBuffer = gl.createBuffer();
  
    // Hérna er sagt gl að setja breytingar á staðsetningar bufferinum
    // í breytuna stadsetningarBuffer
    gl.bindBuffer(gl.ARRAY_BUFFER, stadsetningarBuffer);
  
    // Hérna er sett staðsetningarnar sem Float32Array í bufferinn stadsetningarBuffer
    gl.bufferData(
        gl.ARRAY_BUFFER,
        new Float32Array(stadsetningar),
        gl.STATIC_DRAW
    );

    // Hérna ákvað ég að senda length líka með vegna þess að þetta var núþegar object
    // og þá þarf ég ekki stöðugt að uppfæra hversu margar verticies ég er með þegar
    // ég breyti lögun formsins.
    return { position: stadsetningarBuffer, length: stadsetningar.length / 2 };
}
// Þeta setir einn lit yfir allt formið og skilar lita bufferinum í buffers objectinn
let geraFlatLit = (gl, buffers, color) => {

    const colorBuffer = gl.createBuffer();// Buffer búin til

    // Þetta margfaldar lita listann sem kemur inn til þess að hann sé með einn lita lista fyrir hvert hnit.
    let colorFinal = [];
    for(let i = 0; i < buffers.length; i++) {
        colorFinal = colorFinal.concat(color);
    }
    
    // Þetta setir litinn á colorBufferinn
    gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(colorFinal), gl.STATIC_DRAW);

    // Þetta setir litinn í buffers objectinn þar sem hann verður svo sóttur í drawScene fallinu.
    buffers.color = colorBuffer;
}
// Þetta teiknar allt
let drawScene = (gl, programInfo, buffers, snuningur = 0.0) => {

    // Gera svartan bakgrunn
    gl.clearColor(0.0, 0.0, 0.0, 1.0);
    // Þetta lætur hluti sem eru nálægt fela hluti sem eru langt í burtu
    gl.depthFunc(gl.LEQUAL);
    // Hreinsa canvasinn
    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

    // Hérna er field of view reiknaður vegna þess að WebGL tekur
    // field of view inn í radians, ekki gráðum.
    const fieldOfView = 45 * Math.PI / 180;
    // Hérna er aspect racioinn reiknaður
    const aspect = gl.canvas.clientWidth / gl.canvas.clientHeight;
    // Þetta er staðurinn þar sem myndavélin byrjar að sjá
    const zNear = 0.1;
    // Þetta er staðurinn þar sem myndavélin hættir að sjá
    const zFar = 100.0;
    // Hérna er projection matrixinn búinn til
    const projectionMatrix = mat4.create();

    // Hérna er sjónarhornið sett í projection matrixinn sem var búin til að ofan
    // með stillingunum sem eru líka settar að ofan.
    mat4.perspective(projectionMatrix,
                    fieldOfView,
                    aspect,
                    zNear,
                    zFar);

    // Setja miðju senunar
    const modelViewMatrix = mat4.create();

    // Færa senuna þangað sem við viljum hafa hana
    mat4.translate(modelViewMatrix,     // Hingað verður niðurstaðan sett
                    modelViewMatrix,    // Þetta er það sem verður fært
                    [-0.0, 0.0, -6.0]); // Hversu mikið á að færa
    
    // Þetta snýr hlutnum
    mat4.rotate(modelViewMatrix, // Hingað verður niðurstaðan sett
        modelViewMatrix,         // Þetta er það sem verður snúið
        snuningur,               // Hversu mikið á að snúa í radians
        [0, 0, 1]);              // Í kring um hvaða átt á að snúa
    
    // Hérna segi ég WebGL hvernig það á að færa staðsetningarnar
    // úr buffers.position í vertexPosition
    {
        const numComponents = 2;
        const type = gl.FLOAT;
        const normalize = false;
        const stride = 0;
        const offset = 0;
        gl.bindBuffer(gl.ARRAY_BUFFER, buffers.position);
        gl.vertexAttribPointer(
            programInfo.attribLocations.vertexPosition,
            numComponents,
            type,
            normalize,
            stride,
            offset);
        gl.enableVertexAttribArray(programInfo.attribLocations.vertexPosition);
    }

    // Hérna segi ég WebGL hvernig það á að færa litina
    // úr buffers.color í vertexColor
    {
        const numComponents = 4;
        const type = gl.FLOAT;
        const normalize = false;
        const stride = 0;
        const offset = 0;
        gl.bindBuffer(gl.ARRAY_BUFFER, buffers.color);
        gl.vertexAttribPointer(
            programInfo.attribLocations.vertexColor,
            numComponents,
            type,
            normalize,
            stride,
            offset);
        gl.enableVertexAttribArray(
            programInfo.attribLocations.vertexColor);
    }

    // Hérna segi ég WebGL að nota shader forritið sem ég er búinn að gera til þess að teikna formið
    gl.useProgram(programInfo.program);

    // Setja shader uniforms
    gl.uniformMatrix4fv(
        programInfo.uniformLocations.projectionMatrix,
        false,
        projectionMatrix);
    gl.uniformMatrix4fv(
        programInfo.uniformLocations.modelViewMatrix,
        false,
        modelViewMatrix);

    // Hérna segi ég WebGL að teikna
    {
        const offset = 0;
        gl.drawArrays(gl.TRIANGLE_STRIP, offset, buffers.length);
    }
}


// :-::-::-::-::-::-::-::-::-::-: Kóði :-::-::-::-::-::-::-::-::-::-:

// Þetta passar að JavaScriptið keyri bara ef vafrinn styður WebGL
if (gl === null) {
    alert("Vafrinn þinn styður ekki WebGL, vinsamlegast notaðu nýrri vafra.");
    exit();
}

gl.clearColor(0.0, 0.0, 0.0, 1.0);
gl.clear(gl.COLOR_BUFFER_BIT);

let shaderForrit = geraShaderForrit(gl, vertexShaderSource, fragmentShaderSource);

// Þetta geymir upplýsingar um shader forritið sem ég er búinn að búa til
const shaderForritaUpplysingar = {
    program: shaderForrit,
    attribLocations: {
        vertexPosition: gl.getAttribLocation(shaderForrit, 'aVertexPosition'),
        vertexColor: gl.getAttribLocation(shaderForrit, 'aVertexColor'),
    },
    uniformLocations: {
        projectionMatrix: gl.getUniformLocation(shaderForrit, 'uProjectionMatrix'),
        modelViewMatrix: gl.getUniformLocation(shaderForrit, 'uModelViewMatrix'),
    },
};

// Gera formið
let buffers = gera2DForm(gl, [
    -1.0, -1.0,
    0.0,   1.0,
    1.0,  -1.0,
    0.0,  -1.7,
    -1.0, -1.0
]);

// Geta flatan lit
geraFlatLit(gl, buffers, [
    0.0,  0.0,  1.0,  1.0
]);

// Þetta geymir snúning hlutsins sem er verið að rendera.
let snuningur = 0.0;

// Þessi breyta geymir hvenær síðasti rammi var renderaður og er notað til þess að reikna Delta Time.
let then = 0;

// Þetta teiknar senuna aftur og after, hvern einasta ramma
let render = now => {

    now *= 0.001;  // Breyta í sekúndur
    
    // Reika Delta Time
    const deltaTime = now - then;
    then = now;

    // Hérna bæti ég delta time við snúninginn til þess að snúningurinn sé alltaf jafn haraður, sama hversu mikinn tíma tað tekur að teikna rammann.
    snuningur += deltaTime;

    // Þetta teiknar senuna
    drawScene(gl, shaderForritaUpplysingar, buffers, snuningur);

    // Þetta segir vafranum að keyra fallið sem er sent inn í þetta fall þegar það er renderað næsta ramma.
    requestAnimationFrame(render);
}
requestAnimationFrame(render);