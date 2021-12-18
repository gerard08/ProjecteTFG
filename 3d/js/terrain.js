    //return array with height data from img
    function getHeightData(img,scale) {
     
        if (scale == undefined) scale=1;
        
           var canvas = document.createElement( 'canvas' );
           canvas.width = img.width;
           canvas.height = img.height;
           var context = canvas.getContext( '2d' );
   
           var size = img.width * img.height;
           var data = new Float32Array( size );
   
           context.drawImage(img,0,0);
   
           for ( var i = 0; i < size; i ++ ) {
               data[i] = 0
           }
   
           var imgd = context.getImageData(0, 0, img.width, img.height);
           var pix = imgd.data;
   
           var j=0;
           for (var i = 0; i<pix.length; i +=4) {
               var all = pix[i]+pix[i+1]+pix[i+2];
               data[j++] = all/(12*scale);
           }
           
           return data;
       }

    function pp(plane)
    {
        plane.position(1,0,1);
        return plane;
    }

    import {scene} from './scene.js'
    function loadTerrain(imatge, relleu, position)
    {
        var img = new Image();
        img.onload = function () 
        {
        //get height data from img
        //var data = getHeightData(relleu);
        // plane
        var geometry = new THREE.PlaneGeometry(10,10,10,10);
        //geometry.position.copy(position)
        var texture = new THREE.TextureLoader().load(imatge);
        var material = new THREE.MeshBasicMaterial( { map: texture } );
        // set height of vertices
         //for ( var i = 2; i<300; i+=3 ) {
         //     geometry.attributes.position.array[i] = data[i]*1;
         //}

        var plane = new THREE.Mesh( geometry, material );
        plane.position.copy(position);
        //plane = pp(plane);
        scene.add(plane);
        //console.log(geometry.attributes.position);

        };

        img.src = relleu;

        //return img;
    }


 export {loadTerrain};
