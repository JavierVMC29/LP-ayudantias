<?php
session_start();
?>
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
  <title>Usuarios</title>
</head>

<body class="users">
  <?php include_once('./navbar.php') ?>
  <main>
    <?php if(isset($_SESSION['username'])): ?>
    <div class="table_container">
      <h1>Usuarios registrados</h1>
      <table>
        <thead>
          <th>Nombre</th>
          <th>Nombre de usuario</th>
          <th>Email</th>
        </thead>
        <?php 
      $path = './data/usuarios.csv';
      if(file_exists($path)){
        $file = fopen($path,'r');
        while (($row = fgetcsv($file)) !== false) {
          echo "<tr>
          <td>$row[0]</td>
          <td>$row[1]</td>
          <td>$row[2]</td>
          </tr>";
        }
        fclose($file);
      }
      ?>
      </table>
      <?php else: ?>
      <div class="container">
        <h1>Inicia Sesion para ver esta pagina</h1>
        <p><a href="./index.php">Iniciar Sesion</a></p>
      </div>
      <?php endif; ?>
  </main>
</body>

</html>