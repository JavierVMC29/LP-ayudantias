<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="./css/style.css">
  <title>Home</title>
</head>

<body>
  <?php include_once('./navbar.php') ?>
  <main>
    <?php if(isset($_SESSION['username'])): ?>
    <div class="container">
      <h1>Bienvenido <?php echo $_SESSION['username'];  ?></h1>
    </div>
    <?php else: ?>
    <div class="container">
      <h1>Inicia Sesion para ver esta pagina</h1>
      <p><a href="./index.php">Iniciar Sesion</a></p>
    </div>
    <?php endif; ?>
  </main>
</body>

</html>