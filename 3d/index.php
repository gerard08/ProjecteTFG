<!DOCTYPE html>

<html>
	<head>
		<meta charset="utf-8">
		<title>VisualitzaciĆ³, creaciĆ³ i millora de terrenys 3D</title>
		<link rel="shortcut icon" type="image/x-icon" href="./img/logo.ico">
		<link rel="stylesheet" href="/css/estil.css">
		<script src="js/threejs/build/three.js"></script>
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js">
		<script type="module" src="js/movement.js"></script>
		<script type="module" src="js/terrain.js"></script>
		<script type="module" src="js/scene.js"></script>
		<script type="module" src="js/memorysaver.js"></script>
		<script type="module" src="js/automate.js"></script>

		<style>
			body { margin: -10; }
		</style>
	</head>
	<body>
		<div id="loading"><?php include_once "php/views/loadingScreen.php" ?></div>
		<div id="contingut">
			<div id="instructions"><?php include_once "php/views/instructions.php" ?></div>
		</div>
	</body>
</html>
