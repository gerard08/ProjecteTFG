import { scene } from "./scene.js";
var planes = [];

function addToList(nom)
{
    planes.push(nom);
}

function rmFromList(index)
{
    //console.log(planes);
    //console.log(index + 'borrat');
    console.log(planes[index] + ' borrat');
    var selectedObject = scene.getObjectByName(planes[index]);
    scene.remove( selectedObject );
    planes.splice(index, 1)
    //console.log(planes);
}

var borrat = null;
function checkDistance(xcam, ycam, range, xmin, xmax, ymin, ymax,tamanyImatge, xcoordmin, xcoordmax, ycoordmin, ycoordmax, step)
{
    //let borrat = null;
    planes.forEach(function(elemento, indice, array) {

        //obtenim les coordenades del pla del seu nom
        let x = parseInt(elemento.substring(0,3));
        let y = parseInt(elemento.substring(4,6));

        //comprobem l'eix X
        if(xcam < 0 && xcam + range < x)
        {
            //console.log('xcam+range ',xcam + range, ' <x ', x);
            console.log('%c Borrat dreta ', 'background: #ffff; color: #f00');
            rmFromList(indice);
            if(borrat != x)
            {
                //decrementem valor de Xmax
                xmax = xmax - tamanyImatge;
                xcoordmax = xcoordmax - step;
                console.log('nou xmax = ', xmax);
                borrat = x;
            }
        }
        else if(xcam >=0 && (xcam - range) > x)
        {
            //console.log('xcam-range ',(xcam - range), ' >x ', x);
            console.log('%c Borrat esquerra ', 'background: #ffff; color: #00b');
            rmFromList(indice);
            if(borrat != x)
            {
                //incrementem valor Xmin
                xmin = xmin + tamanyImatge;
                xcoordmin = xcoordmin + step;
                console.log('nou xmin = ', xmin);
                borrat = x;
            }
        }
    });


    return [xmin, xmax, ymin, ymax, xcoordmin, xcoordmax, ycoordmin, ycoordmax];
}

export {checkDistance, addToList, planes};