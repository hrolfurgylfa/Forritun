// Ná í hleður textann til þess að sé hægt að eyða honum þegar það er búið að hlaða.
const hledur_texti = document.getElementById("hledur_texti");
// Ná í body sem verður sett onClickListiner á
const body = document.getElementById("body");
console.log(body);

// Byrja senuna
let scene = new THREE.Scene();

// Setja upp myndavélina
let camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 500 );
camera.position.z = 3;

// Setja upp rendererinn
let renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

let light = new THREE.DirectionalLight(new THREE.Color('hsl(30, 100%, 75%)'), 1.0);
light.position.set(-100, 0, 100);
light.name = "adal_ljos"
// let fillLight = new THREE.DirectionalLight(new THREE.Color('hsl(240, 100%, 75%)'), 0.75);
// fillLight.position.set(100, 0, 100);

// let backLight = new THREE.DirectionalLight(0xffffff, 1.0);
// backLight.position.set(100, 0, -100).normalize();

scene.add(light);
// scene.add(fillLight);
// scene.add(backLight);

let objLoader = new THREE.OBJLoader();
objLoader.setPath('models/');
objLoader.load('api.obj', api => {

    // Eyða hleður texta
    hledur_texti.remove()

    api.name = "api";
    scene.add(api);
    api.position.y = 0;

    // Þetta er allt inni í þessu falli vegna þess að annars kom villa
    // þegar ég reyndi að ná í þennan hlut í sceninu en núna get ég notað
    // hann eðlilega

    // Þessi breyta geymir hvenær síðasti rammi let renderaður og er notað til þess að reikna Delta Time.
    let then = 0;
    let snuningur = 0;

    // Þetta teiknar senuna aftur og after, hvern einasta ramma
    let render = now => {

        now *= 0.001;  // Breyta í sekúndur
        
        // Reika Delta Time
        const deltaTime = now - then;
        then = now;
        
        // Þetta er snúnings hraðinn

        // Hérna bæti ég delta time við snúninginn til þess að snúningurinn sé alltaf jafn haraður, sama hversu mikinn tíma tað tekur að teikna rammann. Ég deili deltatime með 1.5 til þess að apinn snúist hægar.
        snuningur += deltaTime / 1.5;

        // Þetta bætir snúningnum við apan
        api.rotation.y = snuningur;

        // Þetta teiknar senuna
        renderer.render(scene, camera);

        // Þetta segir vafranum að keyra fallið sem er sent inn í þetta fall þegar það er renderað næsta ramma.
        requestAnimationFrame(render);
    }
    requestAnimationFrame(render);

    // Þetta keyrir ef það er ýtt á apann
    body.addEventListener("click", evt => {

        let myndavela_stadsetning = camera.position.z;
        
        let fljuga_i_burtu = () => {

            // Hérna bæti ég aðeins við myndavéla staðsetninguna
            myndavela_stadsetning *= 1.05;
            console.log(myndavela_stadsetning);
            
            // Færa myndavélina
            camera.position.z = myndavela_stadsetning;

            // Þetta segir vafranum að keyra fallið sem er sent inn í þetta fall þegar það er renderað næsta ramma ef apinn er ekki búinn að snúast í 1 hring.
            if (myndavela_stadsetning < 500){
                requestAnimationFrame(fljuga_i_burtu);
            } else {
                camera.position.z = -5;
                requestAnimationFrame(fljuga_til_baka);
            }
        }
        let fljuga_til_baka = () => {

            camera.position.z += 0.1;
            console.log(camera.position.z);

            // Þetta segir vafranum að keyra fallið sem er sent inn í þetta fall þegar það er renderað næsta ramma ef apinn er ekki búinn að snúast í 1 hring.
            if (camera.position.z < 5){
                requestAnimationFrame(fljuga_til_baka);
            }
        }
        requestAnimationFrame(fljuga_i_burtu);
    });
});