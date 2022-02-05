var tamanyImatge = 10;
var thr = 0.15;
var minXcoord, minYcoord, maxXcoord, maxYcoord, step=0.1;
const threshold = 50;
import {loadTerrainbinary} from './terrain.js';
import { checkDistance} from "./memorysaver.js";

function setCoords(minXc, minYc, maxXc, maxYc)
{
    minXcoord = minXc;
    minYcoord = minYc;
    maxXcoord = maxXc;
    maxYcoord = maxYc;
}

function getImage(x, y, step, v, xPos, yPos)
{
    //console.log('getimage');
    let myPromise =  new Promise(function(myResolve, myReject)
    {
        //console.log('cridada');
        //console.log(truncate(y, 15));
        jQuery.ajax(
            {
                type: "POST",
                url: '../php/callServer.php',
                async: true,                
                data: "x0="+ truncate(x) +"& y0="+ truncate(y, 15) +"& step="+ step +"& v="+ v + "& type=" +0, 
                success: function(data){ 
                    myResolve(data);
                },
                error: function(data){
                    myReject('ERROR');
                }
            }
        );
    });

    myPromise.then(
        function(value) {loadTerrainbinary(value, v, truncate(x), truncate(y, 15), step, xPos, yPos);}
    );
}

function truncate(number, decimals = 14)
{
    number = number.toString(); //If it's not already a String
    number = number.slice(0, (number.indexOf("."))+decimals+1); //With 3 exposing the hundredths place
    return Number(number); //If you need it back as a Number
}
function callLoad(orientation, end, var1, var2)
{
    console.log('callLoad');
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
            for(let x = minXcoord; x <= maxXcoord-0.01; x += step)
            {
                console.log('????????');
                let th = 0;
                //yPos<0 ? th=10 : th=-10;
                const v = new THREE.Vector3(xPos,yPos,0);
                getImage(x, y, step, v, xPos, yPos);
                yPos += tamanyImatge;
            }
            
             maxYcoord += step;
            return xPos;
        }
        //esquerra
        else
        {
            //la y és fixa
            const y = minYcoord - step;
            var yPos = var2;// + tamanyImatge;
            const xPos = var1 - tamanyImatge;
            var x;
            for(let x = minXcoord; x <= maxXcoord+0.01; x += step)
            {
                    const v = new THREE.Vector3(xPos,yPos,0);
                    getImage(x, y, step, v, xPos, yPos);
                    yPos += tamanyImatge;
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
    // console.log('________________________');
    // console.log(x, -threshold+maxX);
    // console.log(x, minX+threshold);
    //console.log(maxX - x);
    if(x > maxX - threshold)
    {
        //console.log(maxX - x);
        //console.log(threshold);
        //console.log('maxX');
        maxX = callLoad(1, true, maxX, minY);
        //[minX, maxX, minY, maxY, minXcoord, maxXcoord, minYcoord, maxYcoord] = checkDistance(x, y, 50, minX, maxX, minY, maxY, minXcoord, maxXcoord, minYcoord, maxYcoord, step);
        // [minX, maxX, minY, maxY, minXcoord, maxXcoord, minYcoord, maxYcoord] = checkDistance(x, y, threshold, minX, maxX, minY, maxY, tamanyImatge, minXcoord, maxXcoord, minYcoord, maxYcoord, step);
        console.log('maxX: ', maxX);
    }
    if(x < minX+threshold)
    {
        //console.log(mixX+x);
        //console.log(-threshold);
        //console.log('minX');
        minX = callLoad(1,false, minX, minY);
        // [minX, maxX, minY, maxY, minXcoord, maxXcoord, minYcoord, maxYcoord] = checkDistance(x, y, threshold, minX, maxX, minY, maxY, tamanyImatge, minXcoord, maxXcoord, minYcoord, maxYcoord, step);
        console.log('minX: ',minX);
    }
    //[minX, maxX, minY, maxY, minXcoord, maxXcoord, minYcoord, maxYcoord] = checkDistance(x, y, threshold, minX, maxX, minY, maxY, tamanyImatge, minXcoord, maxXcoord, minYcoord, maxYcoord, step);
    return [minX, minY, maxX, maxY]
}

function getCoords()
{
    return [minXcoord, maxXcoord, minYcoord, maxYcoord];
}

export {checkload, getImage, getCoords, setCoords};