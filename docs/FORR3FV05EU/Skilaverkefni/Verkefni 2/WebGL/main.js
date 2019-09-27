"use strict";

// ########################## HTML Krækjur ##########################
const WebGL_Canvas = document.getElementById("WebGL_Canvas");
const gl = WebGL_Canvas.getContext("webgl");


// ============================= Shaders =============================
const fragmentShaderSource = `
    varying lowp vec4 vColor;

    void main(void) {
        gl_FragColor = vColor;
    }
`;
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
    gl.attachShader(shaderForrit, vertexShader);
    gl.attachShader(shaderForrit, fragmentShader);
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
  
    // Select the positionBuffer as the one to apply buffer operations to from here out.
    gl.bindBuffer(gl.ARRAY_BUFFER, stadsetningarBuffer);
  
    // Now pass the list of positions into WebGL to build the
    // shape. We do this by creating a Float32Array from the
    // JavaScript array, then use it to fill the current buffer.
    gl.bufferData(
        gl.ARRAY_BUFFER,
        new Float32Array(stadsetningar),
        gl.STATIC_DRAW
    );

    // Hérna ákvað ég að senda lengt líka með vegna þess að þetta var núþegar object og þá þarf ég ekki stöðugt að uppfæra hversu margar verticies ég er með.
    return { position: stadsetningarBuffer, length: stadsetningar.length / 2 };
}
// Þeta setir einn lit yfir allt formið
let geraFlatLit = (gl, buffers, color) => {
    

    const colorBuffer = gl.createBuffer();

    console.log("color:\n",color);
    let colorFinal = [];
    for(let i = 0; i < buffers.length; i++) {
        colorFinal = colorFinal.concat(color);
        console.log("i: ",i);
    }
    console.log("colorFinal:\n",colorFinal);
    
    gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(color), gl.STATIC_DRAW);

    buffers.color = colorBuffer;
}
// Þetta teiknar allt
let drawScene = (gl, programInfo, buffers, snuningur = 0.0) => {

    gl.clearColor(0.0, 0.0, 0.0, 1.0);  // Clear to black, fully opaque
    gl.clearDepth(1.0);                 // Clear everything
    gl.enable(gl.DEPTH_TEST);           // Enable depth testing
    gl.depthFunc(gl.LEQUAL);            // Near things obscure far things

    // Clear the canvas before we start drawing on it.

    gl.clear(gl.COLOR_BUFFER_BIT | gl.DEPTH_BUFFER_BIT);

    // Create a perspective matrix, a special matrix that is
    // used to simulate the distortion of perspective in a camera.
    // Our field of view is 45 degrees, with a width/height
    // ratio that matches the display size of the canvas
    // and we only want to see objects between 0.1 units
    // and 100 units away from the camera.

    const fieldOfView = 45 * Math.PI / 180;   // in radians
    const aspect = gl.canvas.clientWidth / gl.canvas.clientHeight;
    const zNear = 0.1;
    const zFar = 100.0;
    const projectionMatrix = mat4.create();

    // note: glmatrix.js always has the first argument
    // as the destination to receive the result.
    mat4.perspective(projectionMatrix,
                    fieldOfView,
                    aspect,
                    zNear,
                    zFar);

    // Set the drawing position to the "identity" point, which is
    // the center of the scene.
    const modelViewMatrix = mat4.create();

    // Now move the drawing position a bit to where we want to
    // start drawing the square.

    mat4.translate(modelViewMatrix,     // destination matrix
                    modelViewMatrix,     // matrix to translate
                    [-0.0, 0.0, -6.0]);  // amount to translate
    
    // Þetta snýr hlutnum
    mat4.rotate(modelViewMatrix,  // destination matrix
        modelViewMatrix,  // matrix to rotate
        snuningur,   // amount to rotate in radians
        [0, 0, 1]);       // axis to rotate around
    
    
    // Tell WebGL how to pull out the positions from the position
    // buffer into the vertexPosition attribute
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

    // Tell WebGL how to pull out the colors from the color buffer
    // into the vertexColor attribute.    
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

    // Tell WebGL to use our program when drawing

    gl.useProgram(programInfo.program);

    // Set the shader uniforms

    gl.uniformMatrix4fv(
        programInfo.uniformLocations.projectionMatrix,
        false,
        projectionMatrix);
    gl.uniformMatrix4fv(
        programInfo.uniformLocations.modelViewMatrix,
        false,
        modelViewMatrix);

    {
        const offset = 0;
        gl.drawArrays(gl.TRIANGLE_STRIP, offset, buffers.length);
    }
}

// Kóði

// Þetta passar að JavaScriptið keyri bara ef vafrinn styður WebGL
if (gl === null) {
    alert("Vafrinn þinn styður ekki WebGL, vinsamlegast notaðu nýrri vafra.");
    exit();
}

gl.clearColor(0.0, 0.0, 0.0, 1.0);
gl.clear(gl.COLOR_BUFFER_BIT);

let shaderForrit = geraShaderForrit(gl, vertexShaderSource, fragmentShaderSource);

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

let buffers = gera2DForm(gl, [
    -1.0, -1.0,
    0.0,   1.0,
    1.0,  -1.0,
    0.0,  -1.7,
    -1.0, -1.0
]);

// let buffers = gera2DForm(gl, [
//     -1.0, -1.0,
//     -1.0,  1.0,
//     1.0,   1.0, 
//     1.0,  -1.0,
//     -1.0, -1.0
// ]);

geraFlatLit(gl, buffers, [
    1.0,  0.0,  0.0,  1.0
]);

console.log(buffers);

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