=begin
Comandos para instalar las librerias
gem install 'pry' 
gem install 'nokogiri'
=end


require 'open-uri'
require 'net/http'
require 'nokogiri'

class Scraper
  def getRazasDeGatos
    html = URI.open("https://es.wikipedia.org/wiki/Anexo:Razas_de_gatos")
    doc = Nokogiri::HTML(html)
    links = doc.css('.mw-parser-output > ul > li > a') # especies[0] = <a href="/wiki/Abisinio_(gato)" title="Abisinio (gato)">Abisinio</a>
    razas = []
    i = 0
    links.each do |link|
      razas[i] = link.text
      i += 1
    end
    return razas[0, razas.length() - 2] # No devuelvo los ultimos 2 links porque no son de gatos
  end

  def getInfoBox(raza_gato)
    html = URI.open("https://es.wikipedia.org/wiki/Anexo:Razas_de_gatos")
    doc = Nokogiri::HTML(html)
    links = doc.css('.mw-parser-output > ul > li > a') # especies[0] = <a href="/wiki/Abisinio_(gato)" title="Abisinio (gato)">Abisinio</a>
    link_data = links.select do |link| 
      link.text.eql?(raza_gato)
    end

    title_attribute = ""
    if link_data.any?
      title_attribute = link_data.first['title']
      puts "Title attribute for #{raza_gato}: #{title_attribute}"
    else
      puts "#{raza_gato} not found in the links"
    end

    html = URI.open("https://es.wikipedia.org/wiki/" + title_attribute.split(' ').join('_'))
    doc = Nokogiri::HTML(html)
    
    infobox = doc.css('.infobox')
    
    datos = infobox.css('tr th + td')
    cabeceras = infobox.css('tr th[scope="row"]')

    text_cabeceras = []
    text_datos = []
    i = 0
    datos.each do |dato|
      text_datos[i] = dato.text
      i += 1
    end
    i = 0
    cabeceras.each do |cabecera|
      text_cabeceras[i] = cabecera.text
      i += 1
    end

    info = {}
    info.default = 0

    for i in (1...cabeceras.size)
      info[text_cabeceras[i]] = text_datos[i]
    end
    return info
  end
end

scrape = Scraper.new
razas = scrape.getRazasDeGatos
print razas
puts

infobox = scrape.getInfoBox("Bosque de Noruega")
print infobox
puts

infobox = scrape.getInfoBox("Mau egipcio")
print infobox
puts

infobox = scrape.getInfoBox("Cymric")
print infobox
puts