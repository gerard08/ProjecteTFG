var tamanyImatge = 10;
var minXcoord = 41.169, minYcoord = 1.053, maxXcoord = 42.173, maxYcoord = 2.057, step=0.2;
//var minX = -10, minY = -10, maxX = 10, maxY = 10;
import {loadTerrainbinary} from './terrain.js';
function getImage(x, y, step, v)
{
    var result;
    jQuery.ajax(
        {
            type: "POST",
            url: '../php/callServer.php',
            async: false,
            //dataType: 'string',
            // data: {x0:x ,y0:y, step:step},
            data: "x0="+ truncate(x) +"& y0="+ truncate(y) +"& step="+ step +"& v="+ v,// + "& direction=" +direction, 
            success: function(data){  
                //console.log(data);
                result = data;
            }
        }
    );
    //loadTerrainbinary(result, 0, v);
    //console.log(result);
    return result;
}


function truncate(number, decimals = 3)
{
    number = number.toString(); //If it's not already a String
    number = number.slice(0, (number.indexOf("."))+decimals+1); //With 3 exposing the hundredths place
    return Number(number); //If you need it back as a Number
}
function callLoad(orientation, end, varEditar, var2)
{
    //vertical
    if(orientation == 1)
    {
        //dreta
        if(end)
        {
            var maxX = varEditar;
            var minY = var2;
            //calculo coordenades fixes
            var x0 = maxXcoord;
            var x1 = maxXcoord + step;
            var noux = maxX + 10;
            var nouy = minY;
            //calculo valors de y
            // var img = getImage(x0, nouy, step, orientation);
            // loadTerrainbinary(img, 0, new THREE.Vector3(0,0,0));//new THREE.Vector3(-noux,nouy,1));

            for(var y=minYcoord; y + step <= maxYcoord + 0.01; y+=step )
            {
                //var y1 = y + step;
                //console.log(x0, x1, truncate(y), truncate(y1));
                var v = new THREE.Vector3(noux, nouy, 0);
                // var worker = new Worker('/js/workerJob.js');
                // worker.postMessage({ "args": [x0, y, step, v] });
                var img = getImage(x0, y, step, orientation, v);
                //console.log('imatge ' + img);
                loadTerrainbinary(img, 0, new THREE.Vector3(noux,nouy,0));
                nouy += 10;
            }
            //actualitzem valors màxims
            maxXcoord = x1;
            maxX += tamanyImatge;
            console.log('calculs imatges dreta actualitzats');
            return maxX;
        }
        //esquerra
        else
        {
            //calculo coordenades fixes
            var x0 = minXcoord - step;
            var x1 = minXcoord;

            //calculo valors de y
            for(var y=minYcoord; y+step <= maxYcoord+0.01; y+=step )
            {
                var y1 = y+step;
                //console.log(x0,x1,truncate(y),truncate(y1));
                getImage(x0, y, step, orientation);
                console.log('aquest no');

            }

            //actualitzem valors mínims
            minXcoord = x0;
            varEditar -= tamanyImatge;
            console.log('càlcul imatges esquerra actualitzat');
            return varEditar;
        }
    }
    //horitzontal
    else
    {

    }
}

function checkload(x,y,minX,minY,maxX,maxY)
{
    //si canvio els 1 depenent del zoom de la camera podre carregar les files o columnes
    //correctament
    if(maxX - x < 1)
    {
        maxX = callLoad(1, true, maxX, minY);
    }
    if(minX - x > -1)
    {
        //minX = callLoad(1,false, minX);
    }
    return [minX, minY, maxX, maxY]
}


export {checkload, getImage};