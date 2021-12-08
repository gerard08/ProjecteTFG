import {camera} from "./movement.js";
import {getHeightData} from "./terrain.js";

//definim les coordenades i la proximitat (step)
// terrain
var img = new Image();
img.onload = function () {
 
    //get height data from img
    //var data = getHeightData(img);
    // plane
    var geometry = new THREE.PlaneGeometry(10,10,9,9);
    var texture = new THREE.TextureLoader().load( 'img/0sat.png' );
    var material = new THREE.MeshBasicMaterial( { map: texture } );
    //set height of vertices
    // for ( var i = 2; i<300; i+=3 ) {
    //      geometry.attributes.position.array[i] = data[i]*1;
    // }

    var plane = new THREE.Mesh( geometry, material );
    scene.add(plane);
    console.log(geometry.attributes.position);

};



const scene = new THREE.Scene();
//export {scene};

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

var image;
// load img source via AJAX
//  if(x==10) {
//     window.alert('10');
//     x++;
// }
   
 //window.alert(image)
 img.src = "img/0.jpg";

 var r = 1366/768;

function animate() {
    renderer.setSize( window.innerWidth, window.innerWidth/r );
	requestAnimationFrame( animate );
	renderer.render( scene, camera );
}
animate();