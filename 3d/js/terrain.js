    //return array with height data from img
    function getHeightData(img,scale) {
        //console.log(img);
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

    // function pp(plane)
    // {
    //     plane.position(1,0,1);
    //     return plane;
    // }

    import {scene} from './scene.js'
    function loadTerrain(imatge, relleu, position)
    {
        var img = new Image();
        img.onload = function () 
        {
        //get height data from img
        var data = getHeightData(img);
        // plane
        //console.log(data);
        var geometry = new THREE.PlaneGeometry(10,10,499,499);
        //geometry.position.copy(position)
        var texture = new THREE.TextureLoader().load(imatge);
        var material = new THREE.MeshBasicMaterial( { map: texture } );
        var plane = new THREE.Mesh( geometry, material );
        
        //set height of vertices
        var l = plane.geometry.attributes.position.count;
        var j = 2;
            for ( var i = 0; i<l; i++ ) {
                plane.geometry.attributes.position.array[j] = data[i]*0.035;
                j+=3;
            }
        //console.log(plane.geometry.attributes.position);
        // var plane = new THREE.Mesh( geometry, material );
        plane.position.copy(position);
        plane.name = setName(Math.round(position.x), Math.round(position.y));
            
        //console.log(plane.name);
        addToList(plane.name);
        //plane = pp(plane);
        scene.add(plane);
        //console.log(geometry.attributes.position);

        };

        img.src = relleu;

        //return img;
    }
    function hexToBase64(str) {
        str = str.replace(/\r|\n/g, "").replace(/([\da-fA-F]{2}) ?/g, "0x$1 ").replace(/ +$/, "").split(" ");
        //console.log(str);
        str = _arrayBufferToBase64(str);
        //console.log('str ' + str);
        return str;
     }
     function _arrayBufferToBase64( buffer ) {
        var binary = '';
        var bytes = new Uint8Array( buffer );
        var len = bytes.byteLength;
        for (var i = 0; i < len; i++) {
            binary += String.fromCharCode( bytes[ i ] );
        }
        //return window.btoa( binary );
        //console.log(binary);
        return btoa(binary);
      
    }
 
    function getRelleu(x, y, step, v, plane)
    {
        //console.log(x);
        //console.log(y);
        console.log('getrelleu');
        let myPromise =  new Promise(function(myResolve, myReject)
        {
            jQuery.ajax(
                {
                    type: "POST",
                    url: '../php/callServer.php',
                    async: true,
                    //dataType: 'string',
                    // data: {x0:x ,y0:y, step:step},
                    data: "x0="+ x +"& y0="+ y +"& step="+ step +"& v="+ v + "& type=" +1, 
                    success: function(data){  
                        myResolve(data);
                        //console.log('acabat');
                    },
                    error: function(data){
                        console.log('nono');
                        myReject('ERROR');
                    }
                }
            );
        });
        myPromise.then(
            function(value) {loadHeightBinary(plane, value);}
        );
    }

    function loadHeightBinary(plane, relleu)
    {
        console.log('okeey letsgo');
        var rlv = new Image();
        rlv.onload = function()
        {
            var data = getHeightData(rlv);
            var l = plane.geometry.attributes.position.count;
            //set height of vertices
            var j = 2;
            for ( var i = 0; i<l; i++ ) {
                plane.geometry.attributes.position.array[j] = data[i]*0.030;//0.035
                //console.log(data[i]);
                j+=3;
            }
            scene.add(plane);
        }
        rlv.src = "data:image/jfif;base64,"+hexToBase64(relleu);
    }

    import {addToList} from "./memorysaver.js";
    function loadTerrainbinary(imatge, position, x, y, step, xPos, yPos)
    {


        //console.log('loadTerrainBinary');
        //console.log('terrain' + imatge);
         var texture = new THREE.Texture();
        //  var im = imatge;
         var image = new Image();
         //console.log(im);
         image.onload = function() { 
             //console.log('dins');
            texture.image = image; 
            texture.needsUpdate = true; 
            var geometry = new THREE.PlaneGeometry(10,10,499,499);
            var material = new THREE.MeshBasicMaterial( { map: texture } );
            var plane = new THREE.Mesh( geometry, material );
            plane.position.copy(position);
            plane.name = setName(xPos, yPos);
            addToList(plane.name);
            getRelleu(x, y, step, position, plane);
         };
         image.src = "data:image/jfif;base64,"+hexToBase64(imatge);
    }

    function setName(xPos, yPos)
    {
        let nx = xPos.toString();
        if(nx.length == 2)
        {
            nx = '+' + nx;
        }
        if(nx.length == 1)
        {
            nx = '+0' + nx;
        }
        let ny = yPos.toString();
        if(ny.length == 2)
        {
            ny = '+' + ny;
        }
        if(ny.length == 1)
        {
            ny = '+0' + ny;
        }
        return nx + ny
    }


 export {loadTerrain, loadTerrainbinary};
