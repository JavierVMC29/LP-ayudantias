# Ejercicio 1
# Contar cuantas veces aparece una letra en un texto

texto = "Hola, como estas? espero que todo este bien. Veamonos este fin de semana!"
texto.downcase! # Vuelve todo minusculas
frequencias = {} # Inicializa el hash
frequencias.default = 0 # Valor inicial de cualquier elemento igual a 0. Ej: {"a" => 0}

texto.each_char { |char| frequencias[char] += 1}

frequencias.each {|letra, frecuencia| puts "#{letra} : #{frecuencia}" }