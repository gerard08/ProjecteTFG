<?php  
function hex2float($strHex) {
  $hex = sscanf($strHex, "%02x%02x%02x%02x%02x%02x%02x%02x");
  $bin = implode('', array_map('chr', $hex));
  $array = unpack("Gnum", $bin);
  return $array['num'];
}

//echo 'importat';



if(isset($_POST['v']))
{
  //echo 'importat2';
  //header("Refresh:0", url=);
  sendData();
}

function sendData()
{
  //echo 'jeje';
  $x0 = strval($_POST['x0']);
  $y0 = strval($_POST['y0']);
  $step = strval($_POST['step']);
  $v = strval($_POST['v']);

  //echo $x0,' ',$y0,' ',$step,'\n';
  if(strlen($x0)<6) $x0 = '0'.$x0;
  if(strlen($y0)<6) $y0 = '0' .$y0;
  //echo $x0,' ',$y0,' ',$step,'\n';

  error_reporting(E_ALL);  
  $address = gethostbyname('localhost');  
  $service_port = 9000;  
    
  /* Create a TCP/IP socket */  
  $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);  
    
  if ($socket === false) {  
    echo "socket_create() fails: Reason: " . socket_strerror(socket_last_error()) . "<br/>";  
  } else {  
    //echo "Socket created.<br/>";  
  }  
    
  //echo "Trying connect to '$address' in port '$service_port'...";  
  $result = socket_connect($socket, $address, $service_port);  
  if ($result === false) {  
    echo "socket_connect() fails. Reason: $result " . socket_strerror(socket_last_error($socket)) . "\n";  
  } else {  
    //echo "OK.<br/>";  
  }  
    
  $in = $x0; 
  socket_write($socket, $in, strlen($in));  
  $in = $y0;  
  socket_write($socket, $in, strlen($in));  
  $in = $step;
  socket_write($socket, $in, strlen($in));
    
  //echo "Receiving...<br/>";  
  //  $all_out = '';  
  //  while ($out = socket_read($socket, 1024)) {  
  //    $all_out .= $out;  
  //  }  
  $out = socket_read($socket, 4000000);
  //echo "Received: ". $out . "<br/>";  
  //echo "Closing socket...<br/>";  
  socket_close($socket);  
  //echo "Closed.";  
  $out = bin2hex($out);
  //echo substr($out, 0, 4); // returns FF00
  //$out = strip_tags($out);
  //echo base64_decode($out); 
  file_put_contents('foto.jfif', $out);
  echo $out;
}
 ?>  


     