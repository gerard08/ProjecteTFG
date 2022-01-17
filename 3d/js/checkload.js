var tamanyImatge = 10;
var thr = 0.15;
var minXcoord = 41.79500149991982, minYcoord = 1.73451324838962, maxXcoord = 42.29500149991983, maxYcoord = 2.23451324838962, step=0.1;
//var minX = -10, minY = -10, maxX = 10, maxY = 10;
import {loadTerrainbinary} from './terrain.js';
// Using 'superagent' which will return a promise.

function getImage(x, y, step, v)
{
    //console.log('getimage');
    let myPromise =  new Promise(function(myResolve, myReject)
    {
        console.log('cridada');
        console.log(truncate(y, 15));
        jQuery.ajax(
            {
                type: "POST",
                url: '../php/callServer.php',
                async: true,
                //dataType: 'string',
                // data: {x0:x ,y0:y, step:step},
                
                data: "x0="+ truncate(x) +"& y0="+ truncate(y, 15) +"& step="+ step +"& v="+ v + "& type=" +0, 
                success: function(data){  
                    myResolve(data);
                    //console.log(data);
                    //document.getElementById("si").innerHTML = "<?php ob_start();include 'php/callServer.php';$result = ob_get_clean();echo $result?>";
                },
                error: function(data){
                    myReject('ERROR');
                }
            }
        );
    });

    myPromise.then(
        function(value) {loadTerrainbinary(value, v, truncate(x), truncate(y, 15), step);}
    );
    //var result;

    //loadTerrainbinary(result, 0, v);
    //console.log(result);
    //return result;
}

function truncate(number, decimals = 14)
{
    number = number.toString(); //If it's not already a String
    number = number.slice(0, (number.indexOf("."))+decimals+1); //With 3 exposing the hundredths place
    return Number(number); //If you need it back as a Number
}
function callLoad(orientation, end, var1, var2)
{
    //vertical
    if(orientation == 1)
    {
        //dreta
        if(end)
        {
            //la y és fixa
            const y = maxYcoord;
            var yPos = var2;// + tamanyImatge;
            const xPos = var1 + tamanyImatge;
            var x;
            for(x = maxXcoord; x >= minXcoord +0.1; x -= step)
            {
                 const v = new THREE.Vector3(xPos-thr*2,yPos-thr,0);
                 getImage(x, y, step, v);
                 yPos -= tamanyImatge;
            }
            
             maxYcoord += step;
            return xPos;
        }
        //esquerra
        else
        {
            //la y és fixa
            const y = minYcoord;
            var yPos = var2;// + tamanyImatge;
            const xPos = var1 - tamanyImatge;
            var x;
            for(x = maxXcoord; x >= minXcoord +0.1; x -= step)
            {
                    const v = new THREE.Vector3(xPos-thr*2,yPos-thr,0);
                    getImage(x, y, step, v);
                    yPos -= tamanyImatge;
            }
            
                minYcoord -= step;
            return xPos;
        }
    }
    //horitzontal
    else
    {

    }
}

function checkload(x,y,minX,minY,maxX,maxY)
{
    //console.log(maxX - x);
    if((maxX - x) < 45)
    {
        maxX = callLoad(1, true, maxX, maxY);
    }
    if(minX - x > -45)
    {
        minX = callLoad(1,false, minX, maxY);
    }
    return [minX, minY, maxX, maxY]
}


export {checkload, getImage};