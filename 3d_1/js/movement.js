const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
export { camera };
camera.position.z = 25;

document.onkeydown = checkKey;

function checkKey(e) {

    e = e || window.event;

    if (e.keyCode == '87') {
        // W
        camera.position.y = camera.position.y + 0.2
    }
    else if (e.keyCode == '83') {
        // S
        camera.position.y = camera.position.y - 0.2
    }
    else if (e.keyCode == '65') {
       // A
       camera.position.x = camera.position.x - 0.2
    }
    else if (e.keyCode == '68') {
       // D
       camera.position.x = camera.position.x + 0.2
    }
    else if (e.keyCode == '69') {
        // E
        camera.position.z = camera.position.z - 0.2
        //console.log(camera.position.z)
     }
     else if (e.keyCode == '81') {
        // Q
        camera.position.z = camera.position.z + 0.2
        //console.log(camera.position.z)
     }
     else if (e.keyCode == '38') {
        // up
        camera.rotation.x = camera.rotation.x + 0.02; 
     }
     else if (e.keyCode == '40') {
        // down
        camera.rotation.x = camera.rotation.x - 0.02; 
     }
     else if (e.keyCode == '37') {
         // left
         camera.rotation.y = camera.rotation.y + 0.02; 
      }
      else if (e.keyCode == '39') {
         // right
         camera.rotation.y = camera.rotation.y - 0.02;
      }
}