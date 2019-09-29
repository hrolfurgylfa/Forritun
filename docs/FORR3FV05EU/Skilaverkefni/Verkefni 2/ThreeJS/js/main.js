// Ná í hleður textann til þess að sé hægt að eyða honum þegar það er búið að hlaða.
const hledur_texti = document.getElementById("hledur_texti");
// Ná í body sem verður sett onClickListiner á
const body = document.getElementById("body");
console.log(body);

// Byrja senuna
let scene = new THREE.Scene();

// Setja upp myndavélina
let camera = new THREE.PerspectiveCamera( 75, window.innerWidth/window.innerHeight, 0.1, 500 );
camera.position.z = 3;// Staðsetning myndavélarinnar sett

// Setja upp rendererinn
let renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );// Sett stærð rendererins á stærð gluggans
document.body.appendChild( renderer.domElement );// Bætt rendererinum við DOM tréð

// Ljósið sett upp
let light = new THREE.DirectionalLight(new THREE.Color('hsl(30, 100%, 75%)'), 1.0);
light.position.set(-100, 0, 100);// Ljósið sett á ákveðina staðsetningu
light.name = "adal_ljos"// Nafn sett á ljósið
scene.add(light);// Ljósinu bætt við senuna

let objLoader = new THREE.OBJLoader();// OBJ Loader initializaður
objLoader.setPath('models/');// path sett fyrir loader
objLoader.load('api.obj', api => {// loadað módelinu

    // Eyða hleður texta
    hledur_texti.remove()

    api.name = "api";// Setja nafn á módelið
    scene.add(api);// Bæta apanum við í senuna
    api.position.y = 0;// Setja staðsetninu apans á y = 0

    // Þetta er allt inni í þessu falli vegna þess að annars kom villa
    // þegar ég reyndi að ná í þennan hlut í sceninu en núna get ég notað
    // hann eðlilega

    // Þessi breyta geymir hvenær síðasti rammi let renderaður
    // og er notað til þess að reikna Delta Time.
    let then = 0;

    // Þetta teiknar senuna aftur og after, hvern einasta ramma
    let render = now => {

        now *= 0.001;  // Breyta í sekúndur
        
        // Reika Delta Time
        const deltaTime = now - then;
        then = now;

        // Þetta bætir snúningnum við apan.
        // Ég deili deltatime með 1.5 til þess að apinn snúist hægar.
        api.rotation.y += deltaTime / 1.5;

        // Þetta teiknar senuna
        renderer.render(scene, camera);

        // Þetta segir vafranum að keyra þetta fall aftur þegar mæsti rammi er reiknaður.
        requestAnimationFrame(render);
    }
    // Þetta keyrir fallið render á næsta ramma
    requestAnimationFrame(render);

    // Þetta keyrir ef það er ýtt á apann
    body.addEventListener("click", evt => {

        let fljuga_i_burtu = () => {

            // Færa myndavélina
            camera.position.z *= 1.05;

            // Þetta segir vafranum að keyra þetta fall aftur þegar næsti
            // rammi er reiknaður ef myndavélin er ekki komin 500 units í
            // burtu frá myðjuni.
            if (camera.position.z < 500){
                requestAnimationFrame(fljuga_i_burtu);
            } else {
                // Myndavélin er sett fyrir aftan apan
                camera.position.z = -5;
                // Vafrinn keyrir fallið fljuga_til_baka á næsta ramma
                requestAnimationFrame(fljuga_til_baka);
            }
        }
        let fljuga_til_baka = () => {

            // Myndavélin er færð áfram
            camera.position.z += 0.1;
            console.log(camera.position.z);

            // Þetta segir vafranum að keyra þetta fall aftur þegar næsti
            // rammi er reiknaður ef myndavélin er ekki komin 5 units í
            // burtu frá myðjuni.
            if (camera.position.z < 5){
                requestAnimationFrame(fljuga_til_baka);
            }
        }
        // Þetta keyrir fallið fljuga_i_burtu á næsta ramma
        requestAnimationFrame(fljuga_i_burtu);
    });
});