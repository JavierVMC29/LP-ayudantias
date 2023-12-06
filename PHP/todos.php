<?php
session_start();
function delete_todo($todo_id){
  $file = fopen('./data/todos_' . $_SESSION['username'] . '.csv', 'r');
  $copy = array();
  $i = 0;
  
  while(($row = fgetcsv($file)) !== false){
    $copy[$i] = $row;
    $i++;
  }
  fclose($file);

  $file = fopen('./data/todos_' . $_SESSION['username'] . '.csv', 'w');
  foreach($copy as $index=>$row){
    if($index != $todo_id){
      fputcsv($file, $row);
    }
  }
  fclose($file);
}

function add_todo($todo){
  $file = fopen('./data/todos_' . $_SESSION['username'] . '.csv', 'a');
  fputcsv($file, $todo);
  fclose($file);
}

if(isset($_POST['add_todo_submit'])){
  $todo = array($_POST['todo_name'], $_POST['todo_date']);
  add_todo($todo);
}elseif(isset($_POST['delete_todo_submit'])){
  $id = $_POST['todo_id'];
  delete_todo($id);
}

include_once('./actividades.php');


?>