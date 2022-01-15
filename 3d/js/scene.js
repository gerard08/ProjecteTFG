//import {camera} from "./movement.js";
//import {FlyControls} from "./threejs/examples/js/controls/FlyControls.js";
function createMaterialArray(filename) {
    const skyboxImagepaths = createPathStrings(filename);
    const materialArray = skyboxImagepaths.map(image => {
      let texture = new THREE.TextureLoader().load(image);
      return new THREE.MeshBasicMaterial({ map: texture, side: THREE.BackSide }); // <---
    });
    return materialArray;
  }
  function createPathStrings(filename) {
    const basePath = "img/clouds/";
    const baseFilename = basePath + filename;
    const fileType = ".png";
    const sides = ["front", "back", "up", "down", "right", "left"];
    const pathStings = sides.map(side => {
      return baseFilename + "_" + side + fileType;
    });
    return pathStings;
  }
 

import {loadTerrain} from "./terrain.js";
import './threejs/examples/js/controls/FlyControls.js'

var r = 1366/768;
//var minXcoord = 42.169, minYcoord = 1.453, maxXcoord = 43.569, maxYcoord = 2.953, step=0.5;

function loadInitialImages()
{
    //dalt2
    loadTerrain('../img/sat/20_sat.jpg', '../img/rel/20_rel.jpg', new THREE.Vector3(-20,20,0));
    loadTerrain('../img/sat/21_sat.jpg', '../img/rel/21_rel.jpg', new THREE.Vector3(-10,20,0));
    loadTerrain('../img/sat/22_sat.jpg', '../img/rel/22_rel.jpg', new THREE.Vector3(0,20,0));
    loadTerrain('../img/sat/23_sat.jpg', '../img/rel/23_rel.jpg', new THREE.Vector3(10,20,0));
    loadTerrain('../img/sat/24_sat.jpg', '../img/rel/24_rel.jpg', new THREE.Vector3(20,20,0));

    //dalt1
    loadTerrain('../img/sat/15_sat.jpg', '../img/rel/15_rel.jpg', new THREE.Vector3(-20,10,0));
    loadTerrain('../img/sat/16_sat.jpg', '../img/rel/16_rel.jpg', new THREE.Vector3(-10,10,0));
    loadTerrain('../img/sat/17_sat.jpg', '../img/rel/17_rel.jpg', new THREE.Vector3(0,10,0));
    loadTerrain('../img/sat/18_sat.jpg', '../img/rel/18_rel.jpg', new THREE.Vector3(10,10,0));
    loadTerrain('../img/sat/19_sat.jpg', '../img/rel/19_rel.jpg', new THREE.Vector3(20,10,0));

    //mitg
    loadTerrain('../img/sat/10_sat.jpg', '../img/rel/10_rel.jpg', new THREE.Vector3(-20,0,0));
    loadTerrain('../img/sat/11_sat.jpg', '../img/rel/11_rel.jpg', new THREE.Vector3(-10,0,0));
    loadTerrain('../img/sat/12_sat.jpg', '../img/rel/12_rel.jpg', new THREE.Vector3(0,0,0));
    loadTerrain('../img/sat/13_sat.jpg', '../img/rel/13_rel.jpg', new THREE.Vector3(10,0,0));
    loadTerrain('../img/sat/14_sat.jpg', '../img/rel/14_rel.jpg', new THREE.Vector3(20,0,0));

    //baix1
    loadTerrain('../img/sat/5_sat.jpg', '../img/rel/5_rel.jpg', new THREE.Vector3(-20,-10,0));
    loadTerrain('../img/sat/6_sat.jpg', '../img/rel/6_rel.jpg', new THREE.Vector3(-10,-10,0));
    loadTerrain('../img/sat/7_sat.jpg', '../img/rel/7_rel.jpg', new THREE.Vector3(0,-10,0));
    loadTerrain('../img/sat/8_sat.jpg', '../img/rel/8_rel.jpg', new THREE.Vector3(10,-10,0));
    loadTerrain('../img/sat/9_sat.jpg', '../img/rel/9_rel.jpg', new THREE.Vector3(20,-10,0));

    //baix2
    loadTerrain('../img/sat/0_sat.jpg', '../img/rel/0_rel.jpg', new THREE.Vector3(-20,-20,0));
    loadTerrain('../img/sat/1_sat.jpg', '../img/rel/1_rel.jpg', new THREE.Vector3(-10,-20,0));
    loadTerrain('../img/sat/2_sat.jpg', '../img/rel/2_rel.jpg', new THREE.Vector3(0,-20,0));
    loadTerrain('../img/sat/3_sat.jpg', '../img/rel/3_rel.jpg', new THREE.Vector3(10,-20,0));
    loadTerrain('../img/sat/4_sat.jpg', '../img/rel/4_rel.jpg', new THREE.Vector3(20,-20,0));
}

const scene = new THREE.Scene();
export {scene};//, minXcoord, minYcoord, maxXcoord, maxYcoord, step};
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.01, 1000 );
camera.position.x = 0;
camera.position.y = 0;
camera.position.z = 1;
camera.rotation.x = 90 * Math.PI / 180

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

const skyboxImage = 'sky';
const materialArray = createMaterialArray(skyboxImage);
var skyboxGeo = new THREE.BoxGeometry(1000, 1000, 1000);
var skybox = new THREE.Mesh(skyboxGeo, materialArray);
scene.add(skybox);
skybox.position.x = 0;
skybox.position.y = 0;
skybox.position.z = 200;



var controls = new THREE.FlyControls(camera, renderer.domElement);
controls.dragToLook = true;
controls.movementSpeed = 2.7;
controls.rollSpeed = 0.5;


//carreguem les 9 imatges inicials
loadInitialImages();

import { checkload } from "./checkload.js";
var lt = new Date();
var x = camera.position.x;
var y = camera.position.y;

var maxX = 20, minX = -20, maxY = 20, minY = -20;
function animate() {
    renderer.setSize( window.innerWidth, window.innerWidth/r );
	requestAnimationFrame( animate );
    var now = new Date(),
    secs = (now - lt) / 1000;
    lt = now;
    controls.update(1 * secs);
    skybox.rotation.x += 0.00007;
    skybox.rotation.y += 0.00003;
    x = camera.position.x;
    y = camera.position.y;
	  renderer.render( scene, camera );
    [minX, minY, maxX, maxY] = checkload(x, y, minX, minY, maxX, maxY);
    //console.log(maxX);
}
animate();