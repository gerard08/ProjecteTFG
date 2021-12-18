//import {camera} from "./movement.js";
//import {FlyControls} from "./threejs/examples/js/controls/FlyControls.js";
import {loadTerrain} from "./terrain.js";
import './threejs/examples/js/controls/FlyControls.js'

var r = 1366/768;
//var minXcoord = 42.169, minYcoord = 1.453, maxXcoord = 43.569, maxYcoord = 2.953, step=0.5;

function loadInitialImages()
{
    //mitg
    loadTerrain('../img/3_sat.jpg', '../img/0.jpg', new THREE.Vector3(-10,0,0));
    loadTerrain('../img/4_sat.jpg', '../img/0.jpg', new THREE.Vector3(0,0,0));
    loadTerrain('../img/5_sat.jpg', '../img/0.jpg', new THREE.Vector3(10,0,0));
    //dalt
    loadTerrain('../img/6_sat.jpg', '../img/0.jpg', new THREE.Vector3(-10,10,0));
    loadTerrain('../img/7_sat.jpg', '../img/0.jpg', new THREE.Vector3(0,10,0));
    loadTerrain('../img/8_sat.jpg', '../img/0.jpg', new THREE.Vector3(10,10,0));
    //baix
    loadTerrain('../img/0_sat.jpg', '../img/0.jpg', new THREE.Vector3(-10,-10,0));
    loadTerrain('../img/1_sat.jpg', '../img/0.jpg', new THREE.Vector3(0,-10,0));
    loadTerrain('../img/2_sat.jpg', '../img/0.jpg', new THREE.Vector3(10,-10,0));
}

const scene = new THREE.Scene();
export {scene};//, minXcoord, minYcoord, maxXcoord, maxYcoord, step};
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.01, 1000 );
camera.position.z = 0.21;

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );


//require('three-fly-controls')(THREE);
//const OrbitControls = require('three-orbit-controls')(THREE);
var controls = new THREE.FlyControls(camera, renderer.domElement);
controls.dragToLook = true;
controls.movementSpeed = 1.7;
controls.rollSpeed = 0.5;


//carreguem les 9 imatges inicials
loadInitialImages();

import { checkload } from "./checkload.js";
var lt = new Date();
var x = camera.position.x;
var y = camera.position.y;

var maxX = 10, minX = -10, maxY = 10, minY = -10;
function animate() {
    renderer.setSize( window.innerWidth, window.innerWidth/r );
	requestAnimationFrame( animate );
    var now = new Date(),
    secs = (now - lt) / 1000;
    lt = now;
    controls.update(1 * secs);
    x = camera.position.x;
    y = camera.position.y;
    [minX, minY, maxX, maxY] = checkload(x, y, minX, minY, maxX, maxY);
	renderer.render( scene, camera );
    //console.log(maxX);
}
animate();