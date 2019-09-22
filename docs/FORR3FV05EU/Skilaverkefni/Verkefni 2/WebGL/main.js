"use strict";

// ########################## HTML Krækjur ##########################
const WebGL_Canvas = document.getElementById("WebGL_Canvas");
const gl = WebGL_Canvas.getContext("webgl");


// ============================= Shaders =============================
const fragmentShaderSource = `
    void main() {
        gl_FragColor = vec4(1.0, 1.0, 1.0, 1.0);
    }
`;
const vertexShaderSource = `
    attribute vec4 aVertexPosition;

    uniform mat4 uModelViewMatrix;
    uniform mat4 uProjectionMatrix;

    void main() {
        gl_Position = uProjectionMatrix * uModelViewMatrix * aVertexPosition;
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

    // Hérna er liturinn gerður

        
    // Hérna ákvað ég að senda lengt líka með vegna þess að þetta var núþegar object og þá þarf ég ekki stöðugt að uppfæra hversu margar verticies ég er með.
    return { position: stadsetningarBuffer, length: stadsetningar.length / 2 };
}
// Þeta setir einn lit yfir allt formið
let geraFlatLit = (gl, buffers, color) => {
    const colorBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, colorBuffer);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array(color), gl.STATIC_DRAW);

    buffers.color = colorBuffer;

    return buffers;
}
// Þetta teiknar allt
let drawScene = (gl, programInfo, buffers) => {

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
    mat4.perspective(
        projectionMatrix,
        fieldOfView,
        aspect,
        zNear,
        zFar
    );

    // Set the drawing position to the "identity" point, which is
    // the center of the scene.
    const modelViewMatrix = mat4.create();

    // Now move the drawing position a bit to where we want to
    // start drawing the square.

    mat4.translate(
        modelViewMatrix,     // destination matrix
        modelViewMatrix,     // matrix to translate
        [-0.0, 0.0, -6.0]    // amount to translate
    );

    // Tell WebGL how to pull out the positions from the position
    // buffer into the vertexPosition attribute.
    {
        const numComponents = 2;  // pull out 2 values per iteration
        const type = gl.FLOAT;    // the data in the buffer is 32bit floats
        const normalize = false;  // don't normalize
        const stride = 0;         // how many bytes to get from one set of values to the next
                                // 0 = use type and numComponents above
        const offset = 0;         // how many bytes inside the buffer to start from
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
        const vertexCount = buffers.length;
        gl.drawArrays(gl.TRIANGLE_STRIP, offset, vertexCount);
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

buffers = geraFlatLit(gl, buffers, [
    1.0,  0.0,  0.0,  1.0
]);

// let buffers2 = gera2DForm(gl, [
//     1.7, 1.7,
//     1.7, -1.7,
//     1.0, 1.0
// ]);

drawScene(gl, shaderForritaUpplysingar, buffers);