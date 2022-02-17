var tamanyImatge = 10;
var thr = 0.15;
var minXcoord, minYcoord, maxXcoord, maxYcoord, step=0.1;
const threshold = 20;
const delTH = 30;
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
                    console.log(data);
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
    //console.log('callLoad');
    //vertical
    if(orientation == 0)
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
                //console.log('????????');
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
    //console.log('socdins');
    if(orientation == 1)
    {
        //amunt
        if(end)
        {
            //la x és fixa
            const x = maxXcoord;
            const yPos = var1 + tamanyImatge;// maxY + tamanyImatge
            var xPos = var2;//minX
            for(let y = minYcoord; y <= maxYcoord-0.01; y += step)
            {
                //console.log('amuntdins');
                //let th = 0;
                //yPos<0 ? th=10 : th=-10;
                const v = new THREE.Vector3(xPos,yPos,0);
                getImage(x, y, step, v, xPos, yPos);
                xPos += tamanyImatge;
            }
            
             maxXcoord += step;
            return yPos;
        }
        else
        {
            console.log('aqui aqui');
            //la x és fixa
            const x = minXcoord - step;
            const yPos = var1 - tamanyImatge;// maxY + tamanyImatge
            var xPos = var2;//minX
            for(let y = minYcoord; y <= maxYcoord-0.01; y += step)
            {
                //console.log('avalldins');
                //let th = 0;
                //yPos<0 ? th=10 : th=-10;
                const v = new THREE.Vector3(xPos,yPos,0);
                getImage(x, y, step, v, xPos, yPos);
                xPos += tamanyImatge;
            }
            
             minXcoord -= step;
            return yPos;
        }
    }
}
//var xyz;
function checkload(x,y,minX,minY,maxX,maxY)
{

    if(x > maxX - threshold)
    {
        maxX = callLoad(0, true, maxX, minY);
        //[minX, maxX, minY, maxY, minXcoord, maxXcoord, minYcoord, maxYcoord] = checkDistance(x, y, delTH, minX, maxX, minY, maxY, tamanyImatge, minXcoord, maxXcoord, minYcoord, maxYcoord, step);
        //console.log('maxX: ', maxX);
    }
    if(x < minX+threshold)
    {
        minX = callLoad(0,false, minX, minY);
        //[minX, maxX, minY, maxY, minXcoord, maxXcoord, minYcoord, maxYcoord] = checkDistance(x, y, delTH, minX, maxX, minY, maxY, tamanyImatge, minXcoord, maxXcoord, minYcoord, maxYcoord, step);
        //console.log('minX: ',minX);
    }
    //console.log(y, maxY - threshold);
    
    if(y > maxY - threshold)
    {
        //console.log('amuntfora');
        maxY = callLoad(1, true, maxY, minX);
    }
    if(y < minY + threshold)
    {
        minY = callLoad(1, false, minY, minX);
        //console.log('avall');
    }
    //[minX, maxX, minY, maxY, minXcoord, maxXcoord, minYcoord, maxYcoord] = checkDistance(x, y, threshold, minX, maxX, minY, maxY, tamanyImatge, minXcoord, maxXcoord, minYcoord, maxYcoord, step);
    return [minX, minY, maxX, maxY]
}

function getCoords()
{
    return [minXcoord, maxXcoord, minYcoord, maxYcoord];
}

export {checkload, getImage, getCoords, setCoords};