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
  <title>Registro</title>
</head>

<body>
  <main>
    <div class="container">
      <h1>Registro</h1>
      <?php
            if(isset($errorRegister)){
                echo $errorRegister;
            }
        ?>
      <form action="./index.php" method="POST">
        <div>
          <label for="name">Nombre</label>
          <input type="text" id="name" name="name" required>
        </div>
        <div>
          <label for="username">Nombre de usuario</label>
          <input type="text" id="username" name="username" required>
        </div>
        <div>
          <label for="email">Correo electronico</label>
          <input type="email" id="email" name="email" required>
        </div>
        <div>
          <label for="password">Contrasena</label>
          <input type="password" id="password" name="password" required>
        </div>
        <button type="submit" name="registerSubmit">Registrarse</button>
      </form>
      <p>Ya tienes una cuenta? <a href="./login.php">Inicia Sesion</a></p>
    </div>
  </main>
</body>

</html>