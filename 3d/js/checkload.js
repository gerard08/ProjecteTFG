var tamanyImatge = 6.65;
var minXcoord = 42.169, minYcoord = 1.453, maxXcoord = 43.569, maxYcoord = 2.953, step=0.4;
//var minX = -10, minY = -10, maxX = 10, maxY = 10;

function getImage(x, y, step, direction)
{
    jQuery.ajax(
        {
            type: "POST",
            url: '../php/callServer.php',
            // dataType: 'json',
            // data: {x0:x ,y0:y, step:step},
            data: "x0="+ truncate(x) +"& y0="+ truncate(y) +"& step="+ step + "& direction=" +direction, 
            success: function(data){  
                console.log(data);
            }
        }
    );
}


function truncate(number, decimals = 3)
{
    number = number.toString(); //If it's not already a String
    number = number.slice(0, (number.indexOf("."))+decimals+1); //With 3 exposing the hundredths place
    return Number(number); //If you need it back as a Number
}
function callLoad(orientation, end, varEditar)
{
    //vertical
    if(orientation == 1)
    {
        //dreta
        if(end)
        {
            //calculo coordenades fixes
            var x0 = maxXcoord;
            var x1 = maxXcoord + step;

            //calculo valors de y
            for(var y=minYcoord; y + step <= maxYcoord + 0.01; y+=step )
            {
                var y1 = y + step;
                //console.log(x0, x1, truncate(y), truncate(y1));
                getImage(x0, y, step, orientation);
            }

            //actualitzem valors màxims
            maxXcoord = x1;
            varEditar += tamanyImatge;
            console.log('calculs imatges dreta actualitzats');
            return varEditar;
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
        maxX = callLoad(1, true, maxX);
    }
    if(minX - x > -1)
    {
        minX = callLoad(1,false, minX);
    }
    return [minX, minY, maxX, maxY]
}

export {checkload};