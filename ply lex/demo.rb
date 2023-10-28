# Archivo de pruebas

# Asignaciones validas
a = 100
b = 0.01
c = true
d = "Hola"
e = a - b * 2 / 34.3 ** 2
f = a > b
g = a and b
a,b,c = 1,2,3

# Operaciones validas
x = 1
y = 10

x + y
x - y
x * y
x / y
x ** y
x % y

x + y - x * y / 2 ** 2 % 2

x > y
x < y
x >= y
x <= y
x == y
x <=> y

# Condicionales validos
if (x > y)
end

if (x > y)
  print "Hola mundo"
end

if (x > y) then
  print "Hola mundo"
end

if x > y
  print "Hola mundo"
end

if x > y then
  print "Hola mundo"
end

if (x > y)
  print "Hola mundo"
  if (true)
    print "Hola mundo"
  end
end

if (x > y)
  print "Hola mundo"
elsif (x < y)
  print "Hola mundo"
end

if (x > y) then
  print "Hola mundo"
elsif (x < y) then
  print "Hola mundo"
end

if x > y then
  print "Hola mundo"
elsif x < y then
  print "Hola mundo"
end

if x > y
  print "Hola mundo"
elsif x < y
  print "Hola mundo"
end

# Estructuras de datos

# Arrays
a = [ 45, 3, 19, 8 ]
b = [ "sam", "max", 56, 98.9, 3, 10, "jill" ]

a.clear()
b.delete("max")

# Hash
z = { "mike" => 75, "bill" => 18, "alice" => 32 }

z.delete("mike")
z.fetch("bill", 18)

# Funciones

def miFuncion
  print("Hola")
end

def miFuncion()
  print("Hola")
end

def miFuncion(mensaje)
  print(mensaje)
end

def miFuncion(mensaje1, mensaje2)
  puts(mensaje1)
  print(mensaje2)
end

# Clases validas
class Fred
  @@age
  @@name = "Javier"
  def initialize(v)
    @val = v
  end

  def set(v)
    @val = v
  end

  def get
    return @val
  end
end



# Impresiones validas

print "Hello, World!\n"
print("Hola Mundo\n")
puts "Hello, World!"
puts("Hello, World!")
print ("Hola Mundo")
puts ("Hello, World!")