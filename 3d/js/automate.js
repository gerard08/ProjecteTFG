import {getImage} from './checkload.js';

function loadInitialImages(x0, y0, step, nrowcols = 5)
{
    var xmin = x0;
    var ymin = y0;
    var xmax;
    var ymax;
    let xPos = -20;
    let yPos = -20;
    let x = x0
    let y = y0
    console.log('imatges demanades');
    for(let i = 0; i < nrowcols; i++)
    {
        for(let j = 0; j < nrowcols; j++)
        {console.log(i*10 + j);
            // let thx;
            // let thy;
            // yPos<0 ? thy=0.01 : thy=-0.01;
            // xPos<0 ? thx=0.01 : thx=-0.01;

            //aixo fa una recta vertical
            const v = new THREE.Vector3(xPos, yPos, 0);
            getImage(x, y, step, v, xPos, yPos);
            yPos +=10;
            x += step;
        }
        xmax = x;
        yPos = -20;
        y += step;
        x = x0;
        xPos += 10;
        ymax = y;
    }
    console.log(xmin, ymin, xmax, ymax);
    return [xmin, ymin, xmax, ymax];
}

export {loadInitialImages};