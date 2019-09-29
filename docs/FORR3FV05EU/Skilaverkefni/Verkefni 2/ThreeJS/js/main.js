var scene = new THREE.Scene();

var camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 1000 );
camera.position.z = 3;

var renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

var light = new THREE.DirectionalLight(new THREE.Color('hsl(30, 100%, 75%)'), 1.0);
light.position.set(-100, 0, 100);

// var fillLight = new THREE.DirectionalLight(new THREE.Color('hsl(240, 100%, 75%)'), 0.75);
// fillLight.position.set(100, 0, 100);

// var backLight = new THREE.DirectionalLight(0xffffff, 1.0);
// backLight.position.set(100, 0, -100).normalize();

scene.add(light);
// scene.add(fillLight);
// scene.add(backLight);

var objLoader = new THREE.OBJLoader();
objLoader.setPath('models/');
objLoader.load('api.obj', object => {

    scene.add(object);
    object.position.y = 0;

});

var animate = () => {
	requestAnimationFrame( animate );
	renderer.render(scene, camera);
};

animate();