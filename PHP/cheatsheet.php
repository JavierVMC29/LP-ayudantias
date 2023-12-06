<?php

// Variables
$name = 'Javier';
$name2 = 'Javavega';
$email_address = 'javavega@espol.edu.ec';
$age = 21;
$gpa = 4;

// Impresion en pantalla
echo "Hola $name\n";
echo 'Hola ' . $name . "\n"; // concatenacion de strings con variables
echo 'Hola $name\n';
echo "\n";

// Contantes
define('universidad', 'ESPOL');
echo universidad . "\n";

// Tipos de dato - (String, Integer, Float, Boolean, Array, Object, NULL, Resource.)
$string = 'Esto es un string';
$int = 10;
$float = 0.2;
$bool = true;
$array = array("David", "Amy", "John");
$array2[0] = 'Calamardo';
$array2[1] = 'Bob esponja';
$people = array("David"=>"27", "Amy"=>"21", "John"=>"42");

// operacion de strings con numeros (los strings se convierten a numeros automaticamente)
$str = '10';
$int = 20;
echo $str + $int ."\n";

// variable de variable
$a = 'hola';
$hola = 'Hello';
echo $$a . "\n"; // $$a es igual a "Hello"

// Arrays
$array = array("David", "Amy", "John");

// Arrays asociativos
$array = array("David"=>"27", "Amy"=>"21", "John"=>"42");

// Arrays 2D
$array = array(
  'online'=>array('David', 'Amy'),
  'offline'=>array('John', 'Rob', 'Jack'),
  'away'=>array('Arthur', 'Daniel')
);

// Condicionales
$a = 1;
$b = 2;

// ==, <=, >-, !=, !==, ===
if($a == $b){
  echo 'True'."\n";
}elseif($a < $b){
  echo 'True 2'."\n";
}else{
  echo 'False'."\n";
}

// while loop
// or , and, &&, ||, not, !
while($a > $b or $a < 1){
  echo "Si\n";
}

// do while loop
do {
  echo "Hola\n";
}while($a == $b);

// for loop
for($i = 0; $i < 10; $i++){
  echo "For #$i\n";
}

// for each loop
$array = array(1,2,3,4,5);
foreach($array as $element){
  echo "$element\n";
}
foreach($array as $key => $value){
  echo "($key: $value)\n";
}

$array = array('nombre' => 'Javier', 'carrera' => 'Computacion');
foreach($array as $element){
  echo "$element\n";
}
foreach($array as $key => $value){
  echo "($key: $value)\n";
}

// switch
$a = 0;
switch($a){
  case 1:
    echo 'a = 1';
    break;
  case 2:
    echo 'a = 2';
    break;
  default:
    echo "No match\n";
}

// Funciones

function myFuntion(){
  echo "Funcion sin argumentos\n";
}

function myFuntion2($a, $b){
  echo "Funcion con argumentos\n";
}

function myFuntion3($a, $b, $c=0, $d=1){
  echo "Funcion con argumentos por defecto: (c=$c, d=$d)\n";
}

function myFuntion4($a, $b){
  return "a * b = ".$a*$b."\n";
}

myFuntion();
myFuntion2(1, 2);
myFuntion3(0, 2);
myFuntion4(2,2);

// Archivos
$path = './data/demo.txt';
if(file_exists($path)){ // Comprobamos que existe el archivo a leer
  $file = fopen($path, 'r'); // Abro el archivo en modo lectura.
  while(!feof($file)){
    $line = fgets($file); // Obtengo una linea del archivo.
    echo $line;
  }
  fclose($file); // Cierro el archivo.
}

$file = fopen($path, 'a'); // Abro el archivo en modo append (para agregar al final del archivo manteniendo lo que habia antes).
$line = 'Hola, como estas?';
fputs($file, $line); // Agrego una linea al archivo.
fclose($file);

$file = fopen($path, 'w'); // Abro el archivo en modo escritura (se borrara lo que habia antes al escribir).
$lines_array = array('Hola, como estas?', 'No muy bien :(');
$lines = join("\n", $lines_array);
fputs($file, $lines);
fclose($file);

// Archivos csv
$path = './data/ejemplo.csv';

if(file_exists($path)){
  $file = fopen($path, 'r'); 
  while(($row = fgetcsv($file)) !== false){
    print_r($row); // fgetcsv retorna un array, no un string como fgets.
  }
  fclose($file);
}

$file = fopen($path, 'a'); 
$row = array("Carro", "$1000"); // Creo un nuevo registro para agregarlo al csv.
fputcsv($file, $row); // fputcsv espera un array, no un string como fputs.
fclose($file);

$file = fopen($path, 'w');
$reg1 = array('Pedro', '22');
$reg2 = array('Juan', '100');
$registros = array($reg1, $reg2);
foreach($registros as $reg){
  fputcsv($file, $reg);
}
fclose($file);

// Variables predefinidas

/*
PHP's superglobal variables are 
$_SERVER
$GLOBALS
$_REQUEST
$_POST
$_GET
$_FILES
$_ENV
$_COOKIE
$_SESSION
*/

// Para saber mas lean esto de aqui
// https://jobtensor.com/Tutorial/PHP/en/Introduction

?>