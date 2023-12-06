<?php

session_start();

include_once('./includes/encrypt.php');
function userAuth($username, $password)
  {
    $path = './data/usuarios.csv';
    $auth = false;
    if (file_exists($path)) {
      $file = fopen($path, 'r');
      while (($row = fgetcsv($file)) !== false) {
        if ($row[1] == $username) {
          $auth = Password::verify($password, $row[3]);
        }
      }
      fclose($file);
      return $auth;
    }
  }

if (isset($_SESSION['username'])) {
    header("location: .//home.php");
} elseif (isset($_POST['loginSubmit'])) {

    $username = $_POST['username'];
    $password = $_POST['password'];
    
    if (userAuth($username, $password)) {
        /**
         * $_SESSION = array(
         *  "username" => $username
         * )
         */
        $_SESSION['username'] = $username;

        header("location: ./home.php");
    } else {
        $errorLogin = "Nombre de usuario y/o password incorrecto";
        include_once './login.php';
    }
} elseif (isset($_POST['registerSubmit'])) {
    $name = $_POST['name'];
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];
    $pass_hash = Password::hash($password);

    $path = './data/usuarios.csv';
    $disponible = true;
    if (file_exists($path)) {
        $file = fopen($path, 'r');
        while (($row = fgetcsv($file)) !== false) {
            if ($row[1] == $username) {
                $disponible = false;
                break;
            }
        }
        fclose($file);
    }
    if ($disponible) {
        $file = fopen($path, 'a');
        fputcsv($file, array($name, $username, $email, $pass_hash));
        fclose($file);
        $todo_file = fopen('./data/todos_' . $username . '.csv', 'w');
        fclose($todo_file);
        include_once './login.php';
    }else{
        $errorRegister = "Nombre de usuario no disponible";
        include_once './register.php';
    }

} else {
    include_once './login.php';
}
?>