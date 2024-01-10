enum Color { negro, blanco, gris }

abstract class Animal {
  void hablar();
}

class Gato extends Animal {
  String nombre = '';
  Color? color;

  // constructor normal
  Gato(String nombre, {this.color = Color.blanco}) {
    this.nombre = nombre;
    this.color = color;
  }

  @override
  void hablar() {
    print('miau');
  }

  @override
  String toString() {
    return "{ Nombre: ${this.nombre} | Color: ${this.color?.name} }";
  }
}

class Perro extends Animal {
  String nombre = '';
  Color? color;

  Perro(this.nombre, {this.color = Color.blanco}); // constructor simplificado

  @override
  void hablar() {
    print('guau');
  }

  @override
  String toString() {
    return "{ Nombre: ${this.nombre} | Color: ${this.color?.name} }";
  }
}

void main() {
  Gato gato = new Gato('Oreo');
  Perro perro = new Perro('Lu', color: Color.negro);

  gato.hablar();
  perro.hablar();

  print(gato);
  print(perro);

  var data = {perro: 'David', gato: 'Javier'};

  print(data);
}
