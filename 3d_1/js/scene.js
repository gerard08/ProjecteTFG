
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera( 75, window.innerWidth / window.innerHeight, 0.1, 1000 );
var mouseDown = false, mouseX = 0, mouseY = 0;

function moveCamera()
{
    // movement - please calibrate these values
    var Speed = 0.0002;

    document.addEventListener("keydown", onDocumentKeyDown, false);
    function onDocumentKeyDown(event) {
        var keyCode = event.which;
        if (keyCode == 87) {
            camera.translateZ(-Speed);
            //camera.position.z -= ySpeed;
        } else if (keyCode == 83) {
            camera.translateZ(Speed);
        } else if (keyCode == 65) {
            camera.translateX(-Speed);
        } else if (keyCode == 68) {
            camera.translateX(Speed);
        } else if (keyCode == 32) {
            camera.position.set(0, 0, 0);
        } else if (keyCode == 69) {
            camera.translateY(Speed);
        } else if (keyCode == 81) {
            camera.translateY(-Speed);
        }
        
    };
    
    rotateCamera();
}

function rotateCamera()
{
    document.addEventListener('mousemove', function(event) {
        if(!mouseDown){return}
        event.preventDefault();
        var deltaX = event.clientX - mouseX,
            deltaY = event.clientY - mouseY;
        mouseX = event.clientX;
        mouseY = event.clientY;
        dragAction(deltaX, deltaY, camera);
    }, false);

    document.body.addEventListener("mousedown", function(event) {
        event.preventDefault();
        mouseDown = true
        //console.log("mouse down")
        mouseX = event.clientX;
        mouseY = event.clientY;
    }, false);

    document.body.addEventListener("mouseup", function(event) {
        event.preventDefault();
        mouseDown = false
    }, false);


    //camera.rotation.set(0);
    //console.log(camera.rotation.x, camera.rotation.y, camera.rotation.z);
}

function dragAction(deltaX, deltaY, object)
{
    console.log(object.rotation);

    //object.rotation.x = deltaX;
    //object.rotation.y = deltaY;
    //object.rotation.z = 0;
    //object.rotation = new THREE.Vector3(deltaX, deltaY, 1);
    //object.rotation
    //object.rotateY(-deltaX/100);
    //object.rotateX(-deltaY/100);
    //object.rotateY(-deltaX);
    
    //camera.up.set(0, 0, 1);
    //camera.updateProjectionMatrix();
}

function updateWindowSize()
{
    renderer.setSize( window.innerWidth, window.innerHeight );
    document.body.appendChild( renderer.domElement );
    camera.aspect = window.innerWidth / window.innerHeight;
	camera.updateProjectionMatrix();
}

const renderer = new THREE.WebGLRenderer();
renderer.setSize( window.innerWidth, window.innerHeight );
document.body.appendChild( renderer.domElement );

const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
var mesh = new THREE.Mesh( new THREE.PlaneBufferGeometry( 10000, 10000 ), material );
mesh.position.y = -1.0;
mesh.rotation.x = - Math.PI / 2;
//const geometry = new THREE.Plane( new THREE.Vector3(0,1,0), 1.0 );
//const geometry = new THREE.BoxGeometry();
//const material = new THREE.MeshBasicMaterial( { color: 0x00ff00 } );
//const cube = new THREE.Mesh( geometry, material );
scene.add( mesh );

// camera.position.z = 5;
// camera.rotation.x = 0;
// camera.rotation.y = 0;
//const controls = new OrbitControls(camera, renderer.domElement );
function animate() 
{
    updateWindowSize();
    moveCamera();
    requestAnimationFrame( animate );
    //cube.rotation.x += 0.01;
    //cube.rotation.y += 0.01;
    renderer.render( scene, camera );
}
animate();
