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
  <title>Todos</title>
</head>

<body class="users">
  <?php include_once("./navbar.php") ?>
  <main>
    <?php if(isset($_SESSION['username'])): ?>
    <div class="table_container">
      <h1>Actividades</h1>
      <form action="./todos.php" method="post" class="todo_form">
        <div>
          <label for="todo_name">Nombre</label>
          <input type="text" id="todo_name" name="todo_name">
        </div>
        <div>
          <label for="todo_date">Fecha</label>
          <input type="date" id="todo_date" name="todo_date">
        </div>
        <div>
          <label for="" class="invisible">a</label>
          <button type="submit" name="add_todo_submit">Agregar</button>
        </div>
      </form>
      <table>
        <thead>
          <th>Nombre</th>
          <th>Fecha</th>
        </thead>
        <?php 
      $path = './data/todos_'.$_SESSION['username'].'.csv';
      if(file_exists($path)){
        $file = fopen($path,'r');
        $i = 0;
        while (($row = fgetcsv($file)) !== false) {
          echo "<tr>
          <td>$row[0]</td>
          <td>$row[1]</td>
          <td>
            <form action='./todos.php' method='post'>
              <input type='text' name='todo_id' value='$i' class='invisible_none'>
              <button type='submit' name='delete_todo_submit'>Borrar</button>
            </form>
          </td>
          </tr>";
          $i++;
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