# Comentario de una linea

=begin
  Comentario
  de
  varias
  lineas
=end

# Variables
a = 1
name = "Javier"

# Constantes
A = 1
Age = 21

# Variable global
$x = 42

# Asignacion multiple
a, b, c = 10, 20, 30

# Intercambio de varibales
a, b = b, a

# Imprimir
puts "Hola"
print "Hola" # No agrega salto de linea
puts
puts "Hola #{name}"

# Operaciones aritmeticas
# Orden de las operaciones: ** , * , / , %, +, - 
x = 2
y = 3

puts x + y
puts x - y
puts x * y
puts x / y # Devuelve entero si ambos numeros son tipo entero
puts x % y
puts x ** y # x elevado a y

x += y  # x=x+y
x -= y  # x=x-y
x *= y  # x=x*y
x /= y  # x=x/y
x %= y  # x=x%y
x **= y  # x=x**y

puts "A: #{5-2*3+3}"
puts 'A: #{5-2*3+3}'

# Concatenacion
a = 'Hola'
b = "Javier"
puts a + ' ' + b # no se pueden concatenar strings con numeros

puts a*3 # Imprime 'HolaHolaHola'

# Input
nombre = gets # Devuelve string incluyendo el salto de linea
nombre = gets.chomp # Devuelve el string sin el salto de linea
edad = gets.to_i # Convierte el string en entero. Retorna 0 si no es entero

puts edad

puts nombre.is_a? Integer # False
puts edad.is_a? Integer # True

# Booleanos
# Cuando se pone algo que no es un booleano donde se espera uno. Ruby transforma el objeto pasado a booleano.
# Ej: "Hola" -> true
# Ej: nil -> false
verdadero = true
falso = false

# Comparaciones

a <= b
a >= b
a == b
a < b
a > b
a.eql?(b) # Compara el tipo de dato y el valor. Ej: 3.eql?(3.0) -> false

# Condicionales

if a < b
puts "Chao"
end

if a < b
  puts "Chao"
else
  puts "Algo"
end

if a == b
  puts "Hola"
elsif a >= b
  puts "Aaa"
else
  puts "R"
end

unless a == 1
  puts "Sii"
else
  puts "Nooo"
end

puts "Condicion verdadera" if 10 > 5 # Se imprime si la condicion se cumple
puts "Condicion falsa" unless "a" == "Javier" # Se imprime si la condicion no se cumple

# Operaciones logicas
a && b # and
a || b # or
!a # not

# Switch de ruby

opcion = 1

case opcion
when 1
  puts "Opcion 1"
when 2
  puts "Opcion 2"
when 3
  puts "Opcion 3"
when 4, 5, 6
  puts "Otras opciones"
else
  puts "Opcion no disponible"
end

# Bucle while
a = 0
while a < 10
  puts a
  a += 1
end

a = 0
until a > 10
  puts a
  a += 1
end

# Rangos
rango1 = (1..10) # Numeros de 1 a 10
rango2 = (1...10) # Numeros del 1 al 9

print rango1.to_a
puts
print rango2.to_a
puts

# Bucle for
for i in (1...10)
  puts "Hola #{i}"
end

for i in (1...10)
  break if i == 5 # Termino el bucle for si se cumple la condicion
  puts "Hola #{i}"
end

for i in (1...10)
  next if i.odd? # Me salto a la siguiente iteracion si se cumple la condicion
  puts "Hola #{i}"
end

# Loop do
x = 5
loop do 
  puts "JAJA"
  x -= 1
  break if x < 0
end

# Arrays
items = ["Apple", "Orange", 34.2, true, 10, "Banana"]
items[0] # "Apple"
items[-1] # "Banana"
items << "Javier" # Agrega "Javier" al final del arreglo
items.push("Javier") # Agrega "Javier" al final del arreglo
items.insert(2, "Casa") # Agrega "Casa" en el indice 2
items.pop # Elimina el ultimo elemento
items.delete_at(2) # Elimina el elemento en el indice 2

print items
puts

print items[0..1] # Imprime los elementos del indice 0 al indice 1
puts

a = [1, 2, 3]
b = [4, 5]
res = a + b # Concatena arrays
print res # [1, 2, 3, 4, 5]
puts

a = [1, 2, 3, 4, 5]
b = [2, 4, 5, 6]
res = a - b # Elimina elementos del primer array que estan en el segundo array
print res # [1, 3]
puts

a = [1,2,3]
res = a*2 # Repite elementos en el array
print res # [1, 2, 3, 1, 2, 3]
puts

a = [2, 3, 7, 8]
b = [2, 7, 9]
# & mantiene los elementos comunes de los dos arrays
print a & b # [2, 7]
puts

a = [2, 3, 7, 8]
b = [2, 7, 9]
# | hace una union de los dos arrays
print a | b # [2, 3, 7, 8, 9]
puts

arr = [5, 3, 8]
res = arr.reverse # Revuelve un array con los elementos volteados
print res # [8, 3, 5]
puts

arr = [1, 2, 3]
arr.reverse! # Modifica el array original
print arr # [3, 2, 1]
puts

# Metodos de arrays
array = [1,2,3,4,5]
obj = nil
array.length # Retorna el numero de elementos en el array.
array.size # Retorna el numero de elementos en el array.
array.sort # Retorna un nuevo array con los elementos ordenados.
array.uniq # Retorna un nuevo arreglo sin elementos duplicados.
array.uniq! # Elimina elementos duplicados del arreglo original.
array.freeze # Hace que el arreglo ya no se pueda modificar.
array.include?(obj) # Retorna true si el objeto esta en el array, sino false.
array.min # Retorna el elemnto con el valor mas bajo.
array.max # Retorna el elemnto con el valor mas alto.

# Hashes
ages = { "David" => 28, "Amy"=> 19, "Rob" => 42 }
months = { [1,"jan"] => "January" }
puts ages["Amy"]
puts months[[1,"jan"]]

# Hashes y symbols
# Forma normal
h = {:name=>"Dave", :age=>28, :gender=>"male"}
puts h[:age]
# Forma corta
h = {name:"Dave", age:28, gender:"male"}
puts h[:age]

# Metodos de Hashes
hash = {saludo: "Hola"}
key = :saludo
value = "Hola"
hash.delete(key) # Elimina el elemento con el key pasado como parametro.
hash.key(value) # Retorna el key del valor pasado como parametro. Si no lo encuentra retorna nil.
hash.invert # Crea un nuevo hash con los keys y valores invertidos. Ej: {"name" => "Javier"} -> {"Javier" => "name"}.
hash.keys # Retorna un array con todos los keys del hash.
hash.values #Reotrna un arreglo con todos los valores del hash.
hash.length # Retorna el tamaño del hash.

# Arrays anidados
arr = [ [1, 2, 3], [4, 5, 6] ]
puts arr[1][2]

# Hashes anidados
cars = {
  bmw: { year:2016, color:"red"},
  mercedes: { year:2012, color:"black"},
  porsche: { year:2014, color:"white"}
}
puts cars[:bmw][:color]

# Iterators
arr = [2, 4, 6]
arr.each do |x|
    puts x
end

sizes = {svga:800, hd:1366, uhd:3840}
sizes.each do |key, value|
    puts "#{key}=>#{value}"
end

sizes = {svga:800, hd:1366, uhd:3840}
sizes.each { |key, value| puts "#{key}=>#{value}" }

str = "Hola"
str.each_char {|c| puts c}

10.times {puts "Hi"}

# Metodos
def say
  puts "Hi"
end

def sum(a, b)
  puts a+b
end

def sum(a, b=8)
  puts a+b
end

def myMethod(*c) # c es un arreglo de parametros
  print c
  puts
end
myMethod(1,2,3) # c = [1,2,3]

def squares(a, b, c)
  return a*a, b*b, c*c # Podemos retornar varios valores a la vez, se retorna un arreglo automaticamente
end
arr = squares(2, 3, 6)
print arr
puts
# esta funcion va a retornar 5, porque los metodos siempre retornan la ultima linea de ejecucion
def test
  a = 8
  b = 3
  c = a-b
end
puts test

# POO
class Student
  PI = 3.14 # Constante
  @@variable_de_clase
  @gpa = 0 # variable de instancia
  attr_reader :name # Getter
  attr_accessor :age # Getter y Setter
  attr_writer :gpa # Setter
  attr_reader :carrera
  # Constructor
  def initialize(name, age, carrera)
    @name = name
    @age = age
    @carrera = carrera
  end

  # Metodo de clase
  def self.info
    puts "Esto es un metodo de clase"
  end

  # Metodo de instancia
  def walk
    puts "#{self.name} esta caminando..."
  end

  # toString
  def to_s
    "#{self.name} estudia #{self.carrera}"
  end
  
  # todos los metodos declarados despues de la palabra private son privados, a menos que declaremos otra palabra como protected
  private
  def metodo_privado
    puts "Soy privado"
  end

  protected
  def metodo_protected
    puts "Soy protected"
  end
end

p1 = Student.new("Javier", 21, "Computacion") # Crea un objeto de clase Person
p1.walk

puts p1

Student.info
puts Student::PI # Acceder a constante de clase

# Herencia
# Ruby no soporta herencia multiple
# Las variables de instancia siempre son privadas
# Los metodos son publicos por defecto
class Animal
  def initialize(name, color)
    @name = name
    @color = color
  end
  def speak
    puts "Hola"
  end
end

class Dog < Animal
end

class Cat < Animal
  attr_accessor :age
  def speak
    super
    puts "Meow"
  end
end

d = Dog.new("Bob", "brown")
d.speak

c = Cat.new("Lucy", "white")
c.age = 2
c.speak

class Animal
  def initialize(name)
    @name = name
  end
end

class Cat  < Animal
  def initialize(name, age)
    super(name)
    @age = age
  end
  def to_s
    "#{@name} is #{@age} years old."
  end
end

c = Cat.new("Bob", 3)
puts c

# Operator Overloading
class Shape
  attr_accessor :h, :w
  def initialize(h, w)
      self.h = h
      self.w = w
  end
  def +(other)
      Shape.new(self.h+other.h, self.w+other.w)
  end
end

a = Shape.new(7, 4)
b = Shape.new(9, 18)
c = a + b
puts c.h
puts c.w 


# Archivos
file = File.open("users.txt")
file_data = file.read # Lee todo el archivo, retorna un string
file.close
puts file_data

file = File.open("users.txt")
file_data = file.readlines.map(&:chomp) # Lee cada linea, devuelve un array con las lineas
file.close
print file_data
puts

file = File.open("users.txt")
file_data = file.read.split # Separa por saltos de linea, devuelve un array de las lineas
file.close
print file_data
puts

File.foreach("users.txt") { |line| puts line }


File.open("log.txt", "w") { |f| f.write "#{Time.now} - User logged in\n" }


=begin

Revisar estos links para saber mas
https://www.rubyguides.com/2015/05/working-with-files-ruby/
https://www.sololearn.com/learning/1081

=end