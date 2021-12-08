
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
export { camera };

camera.position.z = 25;

document.onkeydown = checkKey;

var x = 0, y = 0, z = 0;
var zoom = 1;
const step = 0.1;

const speed = 0.2;
function checkKey(e) {
   
    e = e || window.event;

    if (e.keyCode == '87') {
        // W
        camera.position.y = camera.position.y + speed * zoom;
        y += speed * zoom;
    }
    else if (e.keyCode == '83') {
        // S
        camera.position.y = camera.position.y - speed * zoom;
        y -= speed * zoom;
    }
    else if (e.keyCode == '65') {
       // A
       camera.position.x = camera.position.x - speed*zoom;
       x -= speed * zoom;
    }
    else if (e.keyCode == '68') {
       // D
       camera.position.x = camera.position.x + speed*zoom;
       x += speed * zoom;
    }
    else if (e.keyCode == '69') {
        // E
        if(z - speed > -24.5)
        {
         camera.position.z = camera.position.z - speed;
         z -= speed;
         zoom -= 0.007;
        }
        
        //console.log(camera.position.z)
     }
     else if (e.keyCode == '81') {
        // Q

        camera.position.z = camera.position.z + speed;
        z += speed;
        zoom += 0.007;
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

      console.log(x,y,z);
      console.log(zoom);
}