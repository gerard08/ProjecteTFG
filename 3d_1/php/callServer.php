<?php  

function sendData($xy0, $step)
{
  error_reporting(E_ALL);  
  $address = gethostbyname('localhost');  
  $service_port = 9000;  
    
  /* Create a TCP/IP socket */  
  $socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);  
    
  if ($socket === false) {  
    echo "socket_create() fails: Reason: " . socket_strerror(socket_last_error()) . "<br/>";  
  } else {  
    echo "Socket created.<br/>";  
  }  
    
  //echo "Trying connect to '$address' in port '$service_port'...";  
  $result = socket_connect($socket, $address, $service_port);  
  if ($result === false) {  
    echo "socket_connect() fails. Reason: $result " . socket_strerror(socket_last_error($socket)) . "\n";  
  } else {  
    //echo "OK.<br/>";  
  }  
    
  $in = $xy0;  
  socket_write($socket, $in, strlen($in));  
  //echo strlen($in);
  $in = $step;
  socket_write($socket, $in, strlen($in));
    
  echo "Receiving...<br/>";  
  //  $all_out = '';  
  //  while ($out = socket_read($socket, 1024)) {  
  //    $all_out .= $out;  
  //  }  
  $out = socket_read($socket, 1024);
  echo "Received: ". $out . "<br/>";  
    
  echo "Closing socket...<br/>";  
  socket_close($socket);  
  echo "Closed.";  
}
   
 ?>  