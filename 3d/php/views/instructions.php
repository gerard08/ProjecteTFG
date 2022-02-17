<div class='instructions'>
    <div id="barradalt" style="order:1; flex-grow:1;">
        <h1 id='titol',style="order: 1; flex-grow: 1">INSTRUCCIONS</h1>
        <a onclick="closeInstructions()" class="close"> </a>
    </div>
    <div class='controls', style="order: 1; flex-grow: 1">
        <div class='teclat', style="order: 1; flex-grow: 1">
            <img id="tecles", src='img/controlKeys.png', style="order: 1; flex-grow: 1"/>
            <ul id="explicacio1">
                <li><b id="wasd">W/A/S/D : </b>Moviment de la càmera en els eixos X i Z</li>
                <li><b id="qe">Q/E : </b>Rotació de la càmera</li>
                <li><b id="rf">R/F : </b>Elevació de la càmera en l'eix Y</li>
            </ul>
        </div>
        <div class="mouse", style="order: 1; flex-grow: 1">
            <img id="mouse", src='img/mouse.png', style="order: 1; flex-grow: 1"/>
            <ul id="explicacio2">
                <li> <b id="mantenir"> Click esquerra i mantenir apretat </b>per moure la direcció de la càmera
            </ul>
        </div>
    </div>
</div>

<script>
    function closeInstructions()
    {
        document.getElementById('instructions').style.display = 'none';
    }
</script>