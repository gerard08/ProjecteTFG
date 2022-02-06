
function showLoad()
{
    console.log('hehehe');
    document.getElementById('instructions').style.display = 'none';
    document.getElementById('loading').style.display = 'block';
}

function showInstructions()
{
    console.log('instructions');
    document.getElementById('instructions').style.display = 'block';
    document.getElementById('loading').style.display = 'none';
}


export {showInstructions , showLoad};