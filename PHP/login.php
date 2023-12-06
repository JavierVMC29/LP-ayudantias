<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="./css/style.css">
  <title>Login</title>
</head>

<body>
  <main>
    <div class="container">
      <h1>Inicia Sesion</h1>
      <?php
            if(isset($errorLogin)){
                echo $errorLogin;
            }
            /** 
             * Cuando se haga el submit del formulario la variable $_POST sera asi:
             * $_POST = array(
             *  "username" => value del input
             *  "password" => value del input
             *  "loginSubmit" => value del input
             * )
             * el action es la pagina a la que seremos redirigidos cuando se haga el submit del formulario.
            */
        ?>
      <form action="./index.php" method="POST">
        <div>
          <label for="username">Nombre de usuario</label>
          <input type="text" id="username" name="username">
        </div>
        <div>
          <label for="password">Contrasena</label>
          <input type="password" id="password" name="password">
        </div>
        <button type="submit" name="loginSubmit">Iniciar Sesion</button>
      </form>
      <p>No tienes una cuenta? <a href="./register.php">Registrate</a></p>
    </div>
  </main>
</body>

</html>