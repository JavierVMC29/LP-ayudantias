/*

Tipos de dato:
1. Numbers (Integer, Double)
2. Strings
3. Booleans
4. Lists
5. Maps

*/

void main(List<String> args) {
  // Las variables guardan una referencia al valor asignado.
  // Formas de declarar variables
  var a = 1;
  int b = 12;
  var c; // null por defecto
  dynamic x = 1; // puede cambiar su tipo de dato
  const y = 1; // no se puede modificar
  final z = 1; // no se puede modificar

  // Operadores aritmeticos
  a + b - x * a / z;
  a % b; // Modulo
  int r = a ~/ b; // Division truncada

  print("a: ${a} | b: ${b} | c: ${c} | x: ${x} | y: ${y} | z: ${z} | r: ${r}");

  // Operadores logicos
  bool condition1 = true;
  bool condition2 = false;

  condition1 && condition2; // false
  condition1 || condition2; // true
  !condition1; // false

  // condicionales
  // ==, <=, >=, <, >, is
  var num = 2;
  if (num > 0) {
    print("${num} is positive");
  } else if (num < 0) {
    print("${num} is negative");
  } else {
    print("${num} is neither positive nor negative");
  }

  // condicionales de una linea
  var cond3 = null;
  condition1 ? 'se cumplio la condicion 1' : 'no se cumplio condicion 1';
  cond3 ?? 'Cond3 es null';

  // labels para controlar el flujo con break y continue
  outerloop: // nombre del label
  for (var i = 0; i < 5; i++) {
    // print("Outerloop: ${i}");
    innerloop: // nombre del label
    for (var j = 0; j < 5; j++) {
      if (j > 3) break; // Quit the innerloop loop
      if (i == 2) break innerloop; // Quit the innerloop loop
      if (i == 4) break outerloop; // Quit the outerloop loop
      // print("Innerloop: ${j}");
    }
  }

  outerloop:
  for (var i = 0; i < 3; i++) {
    // print("Outerloop:${i}");

    for (var j = 0; j < 5; j++) {
      if (j == 3) {
        continue outerloop;
      }
      // print("Innerloop:${j}");
    }
  }

  // switch
  int opt = 1;
  switch (opt) {
    case 0:
      {
        print('Opt 0');
      }
      break;

    case 1:
      {
        print('Opt 1');
      }
      break;

    default:
      {
        print('Default');
      }
      break;
  }

  // listas
  var listNull = null;
  var list = [1, 2, 3];
  list.add(10); // list = [1, 2, 3, 10]
  var list2 = [0, ...list]; // [0, 1, 2, 3]
  var list3 = [0, ...?listNull]; // [0] , no causa exception

  var promoActive = false;
  var nav = ['Home', 'Furniture', 'Plants', if (promoActive) 'Outlet'];

  var listOfInts = [1, 2, 3];
  var listOfStrings = ['0', for (var i in listOfInts) '$i']; // [0, 1, 2, 3]

  var l = [
    1,
    'Hola',
    [1, 2, 3]
  ];

  print(l);
  print(list);
  print(list2);
  print(list3);
  print(nav);
  print(listOfStrings);

  // maps
  var gifts = {
    // Key:    Value
    'first': 'partridge',
    'second': 'turtledoves',
    'fifth': 'golden rings'
  };

  var nobleGases = {
    2: 'helium',
    10: 'neon',
    18: 'argon',
  };

  var gifts2 = Map<String, String>();
  gifts2['first'] = 'partridge';
  gifts2['second'] = 'turtledoves';
  gifts2['fifth'] = 'golden rings';

  print(gifts);
  print(nobleGases);
  print(gifts2);

  // sets
  var halogens = {'fluorine', 'chlorine', 'bromine', 'iodine', 'astatine'};
  var names = <String>{};

  var elements = <String>{};
  elements.add('fluorine');
  elements.addAll(halogens);

  print(halogens);
  print(names);

  // funciones
  bool isEven(int number) {
    return number % 2 == 0;
  }

  bool isEvenOneLine(int number) => number % 2 == 0;

// Ej. uso: enableFlags(bold: true, hidden: false);
  void enableFlags({bool? bold, bool? hidden}) {
    print('Funcion con parametros con nombre');
  }

// valores por defecto en los parametros
// Ej. uso: enableFlags2(bold: true); // hidden toma el valor por defecto
  void enableFlags2({bool bold = false, bool hidden = false}) {
    print('Funcion con parametros con valores predeterminados');
  }

// parametros obligatorios
// Ej. uso: enableFlags2(hidden: true); // bold toma el valor por defecto
  void enableFlags3({bool bold = false, required bool hidden}) {
    print('Funcion con parametros obligatorios');
  }

  // funciones anonimas
  const lista = ['apples', 'bananas', 'oranges'];
  lista.map((item) {
    return item.toUpperCase();
  }).forEach((item) {
    print('$item: ${item.length}');
  });

  // try catch
  try {
    // algunaFuncion();
  } catch (e) {
    print('Error: $e'); // Handle the exception first.
  } finally {
    // algunaOtraFuncion();
  }

  // tipo de dato
  print('The type of a is ${a.runtimeType}');
}

// scope de variables
// bool topLevel = true;

// void main() {
//   var insideMain = true;

//   void myFunction() {
//     var insideFunction = true;

//     void nestedFunction() {
//       var insideNestedFunction = true;

//       assert(topLevel);
//       assert(insideMain);
//       assert(insideFunction);
//       assert(insideNestedFunction);
//     }
//   }
// }


// Revisar estos links para saber mas
// https://dart.dev/guides/language/language-tour
// https://stackoverflow.com/questions/50431055/what-is-the-difference-between-the-const-and-final-keywords-in-dart

// Flutter
// https://docs.flutter.dev/get-started/install/windows