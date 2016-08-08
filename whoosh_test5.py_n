#!/usr/bin/env python
# -*- coding: utf-8 -*-

from whoosh.index import create_in
from whoosh.fields import *

from whoosh.analysis import CharsetFilter, StemmingAnalyzer
from whoosh.support.charset import accent_map



#use a broader analyser to filter accentuation - use it in title and author fields
my_analyzer = StemmingAnalyzer() | CharsetFilter(accent_map)
#use words with only one character to search for publication field only
min_analyzer = StemmingAnalyzer(minsize=1)

schema = Schema(title=TEXT(analyzer=my_analyzer, stored=True), path=ID(unique=True, stored=True), author=TEXT(analyzer=my_analyzer, stored=True), secondauthor=TEXT(analyzer=my_analyzer), publication=TEXT(stored=True, analyzer=min_analyzer))
ix = create_in("indexdir", schema)
writer = ix.writer()


# PUB1 #
########

writer.add_document(title=u"Pórtico", path=u"/pub1/#page/9", author=u"Dr. António Bartolomeu Gromicho", publication=u"1")
writer.add_document(title=u"Sinfonia de Abertura", path=u"/pub1/#page/11", author=u"The second one is even more interesting!" ,publication=u"1")
writer.add_document(title=u"Urbanisaçao e Turismo", path=u"/pub1/#page/13", author=u"Dr. António Bartolomeu Gromicho" ,publication=u"1")
writer.add_document(title=u"Pedras da minha Terra", path=u"/pub1/#page/18", author=u"António Cordovil" ,publication=u"1")
writer.add_document(title=u"O Convento de Santa Helena do Monte do Calvário", path=u"/pub1/#page/19", author=u"Dr. Celestino David" ,publication=u"1")
writer.add_document(title=u"O quinquagésimo aniversário do Teatro Garcia de Rezende", path=u"/pub1/#page/30", author=u"Joaquim Augusto da Camara Manuel" ,publication=u"1")
writer.add_document(title=u"Glórias da Universidade Henriquina", path=u"/pub1/#page/40", author=u"Dr. Cónego Medeiros" ,publication=u"1")
writer.add_document(title=u"Monumentos de Homenagem", path=u"pub1/#page/47", author=u"Joaquim Augusto da Camara Manuel" ,publication=u"1")
writer.add_document(title=u"Composição da Câmara Municipal de Évora", path=u"/pub1/#page/55", author=u"Da Redacção" ,publication=u"1")
writer.add_document(title=u"Posturas, Editais e Regulamentos", path=u"/pub1/#page/57", author=u"Da Redacção" ,publication=u"1")
writer.add_document(title=u"Actividade Municipal para 1943", path=u"/pub1/#page/59", author=u"Da Redacção" ,publication=u"1")
writer.add_document(title=u"Relatório da proposta para a Municipalização dos Serviços de fornecimento de energia eléctrica à Cidade de Évora", path=u"/pub1/#page/70" , author=u"Da Redacção", publication=u"1")
writer.add_document(title=u"Alterações ao Regulamento Geral de Contrução Urbana para a Cidade de Évora", path=u"/pub1/#page/85", author=u"Da Redacção" ,publication=u"1")
writer.add_document(title=u"Relação de obras realizadas no ano de 1942", path=u"/pub1/#page/89", author=u"Da Redacção" ,publication=u"1")
writer.add_document(title=u"Extractos das Sessões da Comissão Municipal de Turismo", path=u"/pub1/#page/92" , author=u"Da Redacção", publication=u"1")
writer.add_document(title=u"Movimento de visitantes da Repartição de Turismo", path=u"/pub1/#page/99", author=u"Da Redacção" ,publication=u"1")
writer.add_document(title=u"Évora Ilustrada", path=u"/pub1/#page/105", author=u"Padre Manuel Fialho", secondauthor=u"Dr. Armando Nobre de Gusmão" ,publication=u"1")

# PUB2 #
########

writer.add_document(title=u"Os Cursos de Cicerones do Grupo Pro-Évora", path=u"/pub2/#page/6", author=u"Dr. António Bartolomeu Gromicho", publication=u"2")

writer.add_document(title=u"Conferência pronunciada no dia 18 de Junho de 1939, no Salão Nobre da Câmara Municipal", path=u"/pub2/#page/10", author=u"Dr. Alberto Mac-Bride", publication=u"2")
writer.add_document(title=u"O dia da Cidade", path=u"/pub2/#page/24", author=u"Joaquim Augusto da Camara Manuel", publication=u"2")
writer.add_document(title=u"O Retábulo Flamengo da antiga capela-mór da Sé de Évora", path=u"/pub2/#page/28", author=u"Túlio Espanca", publication=u"2")
writer.add_document(title=u"Notas à margem de uma Exposição de Fotografias Antigas", path=u"/pub2/#page/41", author=u"Joaquim Augusto da Camara Manuel", publication=u"2")
writer.add_document(title=u"Cruzeiros, Alminhas e Memórias de Évora", path=u"/pub2/#page/50", author=u"Túlio Espanca", publication=u"2")

writer.add_document(title=u"Relatório da gerência Municipal do ano de 1942", path=u"/pub2/#page/55", author=u"Da Redacção", publication=u"2")
writer.add_document(title=u"Serviços Municipalizados - Relatório da gerência de 1942", path=u"/pub2/#page/83", author=u"Da Redacção", publication=u"2")
writer.add_document(title=u"Extractos da sessões de Comissão Municipal de Turismo", path=u"/pub2/#page/123", author=u"Da Redacção", publication=u"2")
writer.add_document(title=u"Movimento de visitantes da Repartição de Turismo", path=u"/pub2/#page/126", author=u"Da Redacção", publication=u"2")
writer.add_document(title=u"Évora Ilustrada", path=u"/pub2/#page/130", author=u"Padre Manuel Fialho", publication=u"2")

# PUB3 #
########

writer.add_document(title=u"A Pintura flamenga em Évora no século XVI - Variedades e estilos na obra atribuída a Frei Carlos", path=u"/pub3/#page/5", author=u"Dr. João Couto", publication=u"3")
writer.add_document(title=u"Évora, Acrópole de Portugal", path=u"/pub3/#page/40", author=u"Dr. Celestino David", publication=u"3")
print "ola"
writer.add_document(title=u"Gabriel Pereira - Notas sôbre os \"Estudos Eborenses\"", path=u"/pub3/#page/84", author=u"Dr. Pedro Lino Bragança Gil", publication=u"3")
writer.add_document(title=u"A Feira de S. João", path=u"/pub3/#page/92", author=u"Joaquim Augusto da Câmara Manuel", publication=u"3")
writer.add_document(title=u"Centro de Informação e Socorro Social", path=u"/pub3/#page/102", author=u"Dr. António Bartolomeu Gromicho", publication=u"3")
writer.add_document(title=u"Património Artístico Municipal - A Ermida de S. Bráz", path=u"/pub3/#page/104", author=u"Túlio Espanca", publication=u"3")
writer.add_document(title=u"Orquestra Sinfónica Eborense", path=u"/pub3/#page/115", author=u"Dr. A. G.", publication=u"3")
writer.add_document(title=u"Monumentos de Évora: Sé - Pórtico dos Apóstolos-, S. Francisco e Espinheiro", path=u"/pub3/#page/109", author=u"Da Redacção", publication=u"3")

writer.add_document(title=u"Posturas, Editais e Regulamentos", path=u"/pub3/#page/135", author=u"Da Redacção", publication=u"3")
writer.add_document(title=u"Extractos das sessões da Comissão Municipal de Turismo", path=u"/pub3/#page/138", author=u"Da Redacção", publication=u"3")
writer.add_document(title=u"Movimento de visitantes da Repartição de Turismo", path=u"/pub3/#page/143", author=u"Da Redacção", publication=u"3")
writer.add_document(title=u"Évora Ilustrada: Apresentação e estudo do Dr. Armando Nobre de Gusmão", path=u"/pub3/#page/145", author=u"Padre Manuel Fialho", publication=u"3")


# PUB4 #
########
writer.add_document(title=u"Henrique Pousão - Pintor Alentejano", path=u"/pub4/#page/6", author=u"Dr. Celestino David", publication=u"4")
writer.add_document(title=u"O Primeiro Centenário do Liceu de Évora", path=u"/pub4/#page/71", author=u"Dr. António Bartolomeu Gromicho", publication=u"4")
writer.add_document(title=u"Há quarenta anos...", path=u"/pub4/#page/93", author=u"João Rosa", publication=u"4")
writer.add_document(title=u"Mestre André de Resende", path=u"/pub4/#page/98", author=u"Joaquim Augusto da Câmara Manuel", publication=u"4")
writer.add_document(title=u"Património Artístico Municipal: Ermida de N.ª S.ª de Guadalupe", path=u"/pub4/#page/104", author=u"Da Redacção", publication=u"4")
writer.add_document(title=u"A Escola do Magistério Primário de Évora", path=u"/pub4/#page/111", author=u"Da Redacção", publication=u"4")
writer.add_document(title=u"As festas da Cidade pela Feira de S. João", path=u"/pub4/#page/113", author=u"Da Redacção", publication=u"4")
writer.add_document(title=u"Jogos Florais Bocageanos. Quadras Populares Alentejanas: 1.ª Francisco Duarte Ferreira 2.ª Frederico Carapeta - Monte Alentejano 3.ª Armando Neves Sonetos: Fernando Tavares dias - Seára em Fogo Pde José Maria Sardo - O Céu do Alentejo Armando Neves - Legenda", path=u"/pub4/#page/117", author=u"Da Redacção", publication=u"4")

writer.add_document(title=u"Extractos das sessões da Comissão Municipal de Turismo", path=u"/pub4/#page/123", author=u"Da Redacção", publication=u"4")
writer.add_document(title=u"Movimento de visitantes da Repartição de Turismo", path=u"/pub4/#page/127", author=u"Da Redacção", publication=u"4")

writer.add_document(title=u"Évora Ilustrada: Apresentação e estudo do Dr. António Nobre de Gusmão", path=u"/pub4/#page/129", author=u"Padre Manuel Fialho", publication=u"4")


# PUB5 #
########

writer.add_document(title=u"Alguns azulejos de Évora", path=u"/pub5/#page/5", author=u"João Miguel Santos Simões", publication=u"5")
writer.add_document(title=u"A Estação Meteorológica de Évora", path=u"/pub5/#page/22", author=u"Dr. Henrique Amorim Ferreira", publication=u"5")
writer.add_document(title=u"O Cálice barroco da Sé de Évora", path=u"/pub5/#page/28", author=u"Cónego Dr. José Filipe Mendeiros", publication=u"5")
writer.add_document(title=u"Évora, rainha da arte e do Turismo", path=u"/pub5/#page/45", author=u"Dr. António Bartolomeu Gromicho", publication=u"5")
writer.add_document(title=u"Um subsídio importante para a história do \"Templo de Diana\"", path=u"/pub5/#page/51", author=u"Cónego Dr. José Filipe Mendeiros", publication=u"5")
writer.add_document(title=u"As Fontes de Inspiração da Catedral de Évora", path=u"/pub5/#page/59", author=u"Dr. Mário Tavares Chicó", publication=u"5")
writer.add_document(title=u"Subsídios para o estudo do Jornalismo Eborense", path=u"/pub5/#page/85", author=u"Joaquim Augusto da Câmara Manuel", publication=u"5")
writer.add_document(title=u"Convento de N.ª Sr.ª dos Remédios / Monumento de Évora: Igreja da Misericórdia-, Mosteiro de St.ª Clara e Claustro da Sé", path=u"/pub5/#page/103", author=u"Túlio Espanca", publication=u"5")
writer.add_document(title=u"Catálogo dos Monumentos Nacionais", path=u"/pub5/#page/118", author=u"Da Redacção", publication=u"5")
writer.add_document(title=u"Três Exposições", path=u"/pub5/#page/121", author=u"Dr. Armando Gusmão", publication=u"5")
writer.add_document(title=u"Catálogo da Exposição de Arte Ornamental do Liceu", path=u"/pub5/#page/135", author=u"Da Redacção", publication=u"5")

writer.add_document(title=u"Posturas, Editais e Regulamentos", path=u"/pub5/#page/145", author=u"Da Redacção", publication=u"5")
writer.add_document(title=u"Relatório de Actividade e Bases do Orçamento para 1944", path=u"/pub5/#page/148", author=u"Dr. Miguel Rodrigues Bastos", publication=u"5")
writer.add_document(title=u"Mapa-Resumo das contas das Festas da Cidade", path=u"/pub5/#page/159", author=u"Da Redacção", publication=u"5")
writer.add_document(title=u"Extractos das Sessões da Comissão Municipal de Turismo", path=u"/pub5/#page/160", author=u"Da Redacção", publication=u"5")
writer.add_document(title=u"Movimento de visitantes da zona de Turismo", path=u"/pub5/#page/164", author=u"Da Redacção", publication=u"5")
writer.add_document(title=u"Évora Ilustrada - Apresentação e estudo do Dr. Armando Nobre de Gusmão", path=u"/pub5/#page/167", author=u"Padre Manuel Fialho", publication=u"5")



#PUB6#
writer.add_document(title=u"Da Universidade de Évora", path=u"/pub6/#page/5", author=u"Dr. António Bartolomeu Gromicho", publication=u"6")
writer.add_document(title=u"O grupo Pro-Évora e os Monumentos Nacionais", path=u"/pub6/#page/27", author=u"Joaquim Augusto Câmara Manuel", publication=u"6")
writer.add_document(title=u"A música em Évora no século XVI", path=u"/pub6/#page/33", author=u"Padre José Augusto Alegria", publication=u"6")
writer.add_document(title=u"A Sé de Évora do século XII ao fim do século XVII", path=u"/pub6/#page/52", author=u"Cónego dr. Jerónimo de Alcântara Guerreiro", publication=u"6")
writer.add_document(title=u"As Pinturas da Catedral de Évora em 1537 e o Retábulo Flamengo da Capela do Esporão", path=u"/pub6/#page/65", author=u"Da Redacção", publication=u"6")
writer.add_document(title=u"Alguns Azulejos de Évora - séc. XVII", path=u"/pub6/#page/102", author=u"João M. Santos Simões", publication=u"6")
writer.add_document(title=u"Templum Dianae Sacrum", path=u"/pub6/#page/119", author=u"Túlio Espanca", publication=u"6")
writer.add_document(title=u"Música da Idade Média e da Renascença", path=u"/pub6/#page/123", author=u"Da Redacção", publication=u"6")
writer.add_document(title=u"A Orquestra Sinfónica Eborense em Beja", path=u"/pub6/#page/125", author=u"Cândido Marrecas", publication=u"6")
writer.add_document(title=u"Ferros Artísticos de Évora", path=u"/pub6/#page/129", author=u"Dr. Mário Tavares Chicó", publication=u"6")
writer.add_document(title=u"Catálogo da Exposição de Arte Ornamental do Liceu", path=u"/pub6/#page/137", author=u"Da Redacção", publication=u"6")
writer.add_document(title=u"Relatório da Actividade Municipal de 1943", path=u"/pub6/#page/153", author=u"Dr. Miguel Rodrigues Bastos", publication=u"6")
writer.add_document(title=u'''O Boletim "A Cidade de Évora" e a acção da Comissão Municipal de Turismo''', path=u"/pub6/#page/185", author=u"Dr. António Bartolomeu Gromicho", publication=u"6")
writer.add_document(title=u"Extractos das reuniões da Comissão Municipal de Turismo", path=u"/pub6/#page/198", author=u"Da Redacção", publication=u"6")
writer.add_document(title=u"Movimento de visitantes da zona de Turismo", path=u"/pub6/#page/200", author=u"Da Redacção", publication=u"6")
writer.add_document(title=u"Évora Ilustrada: Apresentação e estudo do Dr. Armando Nobre de Gusmão, Padre Manuel Fialho", path=u"/pub6/#page/207", author=u"Padre Manuel Fialho", publication=u"6")
writer.add_document(title=u"Estatutos da Universidade de Évora - Manuscrito Quinhentista", path=u"/pub6/#page/225", author=u"Da Redacção", publication=u"6")

#PUB7-8#

writer.add_document(title=u"O Grupo Pro-Évora", path=u"/pub07-08/#page/5", author=u"Dr. Celestino David", publication=u"07-08")
writer.add_document(title=u"Alguns Azulejos de Évora - Séc. XVIII", path=u"/pub07-08/#page/53", author=u"João M. Santos Simões", publication=u"07-08")
writer.add_document(title=u"Os mais antigos Documentos do Arquivo da Sé de Évora", path=u"/pub07-08/#page/69", author=u"Pde dr. Carlos da Silva Tarouca", publication=u"07-08")
writer.add_document(title=u"O Aqueduto da Água da Prata / Monumento de Évora", path=u"/pub07-08/#page/106", author=u"Túlio Espanca", publication=u"07-08")
writer.add_document(title=u"Magia de Évora", path=u"/pub07-08/#page/144", author=u"Joaquim Augusto da Câmara Manuel", publication=u"07-08")
writer.add_document(title=u"A Música em Évora no séc. XVI", path=u"/pub07-08/#page/149", author=u"Pde José Augusto Alegria", publication=u"07-08")
writer.add_document(title=u"A Sé de Évora no séc. XII ao fim do séc. XVII", path=u"/pub07-08/#page/165", author=u"Cónego dr. Jerónimo de Alcântara Guerreiro", publication=u"07-08")
writer.add_document(title=u"Jogos Florais da Emissora Nacional", path=u"/pub07-08/#page/176", author=u"Da Redacção", publication=u"07-08")
writer.add_document(title=u"Évora - Poêma", path=u"/pub07-08/#page/180", author=u"João da Silva Tavares", publication=u"07-08")
writer.add_document(title=u"Évora Ilustrada - Apresentação e estudo do Dr. Armando Nobre de Gusmão", path=u"/pub07-08/#page/187", author=u"Padre Manuel Fialho", publication=u"07-08")
writer.add_document(title=u"Estatutos da Universidade de Évora - Manuscrito quinhentista", path=u"/pub07-08/#page/205", author=u"Da Redacção", publication=u"07-08")
writer.add_document(title=u"Homenagem da Câmara Municipal de Évora à memória do Eng.º Duarte Pachêco", path=u"/pub07-08/#page/233", author=u"Dr. Miguel Rodrigues Bastos", publication=u"07-08")
writer.add_document(title=u"Relatório da Actividade Municipal para 1945", path=u"/pub07-08/#page/233", author=u"Dr. Miguel Rodrigues Bastos", publication=u"07-08")
writer.add_document(title=u"Extractos das Sessões da Comissão Municipal de Turismo", path=u"/pub07-08/#page/238", author=u"Da Redacção", publication=u"07-08")
writer.add_document(title=u"Movimentos de visitantes da zona de Turismo", path=u"/pub07-08/#page/243", author=u"Da Redacção", publication=u"07-08")

#PUB9-10#
writer.add_document(title=u"Desenhos antigos da Biblioteca de Évora", path=u"/pub09-10/#page/5", author=u"Dr. Luís Silveira", publication=u"09-10")
writer.add_document(title=u"A Virgem da Glória", path=u"/pub09-10/#page/22", author=u"Mário de Sampayo Ribeiro", publication=u"09-10")
writer.add_document(title=u"Fortificações e Alcaidarias de Évora", path=u"/pub09-10/#page/53", author=u"Túlio Espanca", publication=u"09-10")
writer.add_document(title=u"Dois Pintores eborenses do século XVI", path=u"/pub09-10/#page/148", author=u"Túlio Espanca", publication=u"09-10")
writer.add_document(title=u"Alguns Azulejos de Évora", path=u"/pub09-10/#page/119", author=u"Eng.º João M. Santos Simões", publication=u"09-10")
writer.add_document(title=u"Alguns Quadros da Igreja do Espírito Santo em Évora", path=u"/pub09-10/#page/137", author=u"Eng.º Henrique da Fonseca Chaves", publication=u"09-10")
writer.add_document(title=u"A Igreja dos Lóios de Évora", path=u"/pub09-10/#page/156", author=u"Pde Dr. Carlos da Silva Tarouca e Dr. Mário Tavares Chicó", publication=u"09-10")
writer.add_document(title=u"Posturas, Editais e Regulamentos", path=u"/pub09-10/#page/191", author=u"Da Redacção", publication=u"09-10")
writer.add_document(title=u"Relatório da Activade Minicipal em 1944", path=u"/pub09-10/#page/193", author=u"Dr. Miguel Rodrigues Bastos", publication=u"09-10")
writer.add_document(title=u"Extractos das Sessões da Comissão Municipal de Turismo", path=u"/pub09-10/#page/207", author=u"Da Redacção", publication=u"09-10")
writer.add_document(title=u"Movimento de visitantes da zona de Turismo", path=u"/pub09-10/#page/222", author=u"Da Redacção", publication=u"09-10")

#PUB11#
writer.add_document(title=u"Duas Esculturas", path=u"/pub11/#page/7", author=u"Henrique da Fonseca Chaves", publication=u"11")
writer.add_document(title=u"Pintores dos Séculos XVIII e XIX no Alentejo", path=u"/pub11/#page/19", author=u"João Rosa", publication=u"11")
writer.add_document(title=u"Palácios Reais de Évora", path=u"/pub11/#page/31", author=u"Túlio Espanca", publication=u"11")
writer.add_document(title=u"Foros e Próprios do Concelho (Tombo Municipal de 1651)", path=u"/pub11/#page/101", author=u"Da Redacção", publication=u"11")
writer.add_document(title=u"Posturas, Editais e Regulamentos", path=u"/pub11/#page/123", author=u"Da Redacção", publication=u"11")
writer.add_document(title=u"Movimento de Visitantes da Zona de Turismo", path=u"/pub11/#page/129", author=u"Da Redacção", publication=u"11")


#PUB12#
writer.add_document(title=u"Justificação", path=u"/pub12/#page/7", author=u"António de Jesus Silveira", publication=u"12")
writer.add_document(title=u"Uma Carta Inédita", path=u"/pub12/#page/9", author=u"Gabriel Pereira", publication=u"12")
writer.add_document(title=u"Gabriel Pereira e a sua querida terra natal", path=u"/pub12/#page/7", author=u"António Ferrão", publication=u"12")
writer.add_document(title=u"Gabriel Pereira - O competente e bondoso inspector das Bibliotecas e Arquivos", path=u"/pub12/#page/17", author=u"António Baião", publication=u"12")
writer.add_document(title=u"Mestre Gabriel Pereira", path=u"/pub12/#page/23", author=u"João Barreira", publication=u"12")
writer.add_document(title=u"Gabriel Pereira - A autenticidade da sua cultura", path=u"/pub12/#page/23", author=u"Hernâni Cidade", publication=u"12")
writer.add_document(title=u"No Centenário de Gabriel Pereira", path=u"/pub12/#page/27", author=u"Luís Chaves", publication=u"12")
writer.add_document(title=u"Em lembrança de Gabriel Pereira", path=u"/pub12/#page/37", author=u"A. G. da Rocha Madahil", publication=u"12")
writer.add_document(title=u"Gabriel Pereira", path=u"/pub12/#page/49", author=u"Carlos Lima Pires da Fonseca", publication=u"12")
writer.add_document(title=u"Évora na comemoração centenária do nascimento de Mestre Gabriel Pereira", path=u"/pub12/#page/55", author=u"João Rosa", publication=u"12")
writer.add_document(title=u"Gabriel Pereira - A obra admirável deste escritor renasce com o aparecimento e animação do espírito pró-Évora", path=u"/pub12/#page/55", author=u"Celestino David", publication=u"12")
writer.add_document(title=u"Gabriel Pereira, precursor do espírito Pró-Évora", path=u"/pub12/#page/65", author=u"Joaquim Augusto Câmara Manuel", publication=u"12")
writer.add_document(title=u"Um incunábulo colombino da Biblioteca de Évora", path=u"/pub12/#page/91", author=u"Manuel C. Baptista de Lima", publication=u"12")
writer.add_document(title=u"O Grupo Pró-Évora", path=u"/pub12/#page/117", author=u"Dr. Celestino David", publication=u"12")
writer.add_document(title=u"Evolução dos Paços do Concelho", path=u"/pub12/#page/129", author=u"Túlio Espanca", publication=u"12")
writer.add_document(title=u"Um filho de D. Pedro II na Universidade de Évora", path=u"/pub12/#page/191", author=u"Manuel C. Baptista de Lima", publication=u"12")
writer.add_document(title=u"Foros e Próprios do Concelho (Tombo Municipal de 1651)", path=u"/pub12/#page/213", author=u"Manuel C. Baptista de Lima", publication=u"12")

#PUB13-14#
writer.add_document(title=u"O Testamento de Garcia de Rèsende", path=u"/pub13-14/#page/5", author=u"António Bartolomeu Gromicho", publication=u"13-14")
writer.add_document(title=u"As origens da Ordem dos Cavaleiros de Évora (Avis) segundo as Cartas do Arquivo do Cabido da Sé de Évora", path=u"/pub13-14/#page/31", author=u"Pde Carlos da Silva Tarouca", publication=u"13-14")
writer.add_document(title=u"O Bispo D. Frei Manuel do Cenáculo e as Inscrições Tirsenas do Alentejo", path=u"/pub13-14/#page/49", author=u"F. Russel Cortez", publication=u"13-14")
writer.add_document(title=u"Um filho de D. Pedro II na Universidade de Évora", path=u"/pub13-14/#page/59", author=u"Manuel C. Baptista de Lima", publication=u"13-14")
writer.add_document(title=u"Um treslado original do ano 1257 do Foral de Évora", path=u"/pub13-14/#page/111", author=u"Pde Carlos da Silva Tarouca", publication=u"13-14")
writer.add_document(title=u"Notas sobre pintores em Évora nos Séculos XVI e VII", path=u"/pub13-14/#page/125", author=u"Túlio Espanca", publication=u"13-14")
writer.add_document(title=u"Relação XXXI  do Chantre Manuel Severim de Faria anotada pelo Pde Ruela Pombo", path=u"/pub13-14/#page/257", author=u"Da Redacção", publication=u"13-14")
writer.add_document(title=u"O grupo Pró-Évora", path=u"/pub13-14/#page/271", author=u"Celestino David", publication=u"13-14")
writer.add_document(title=u"Évora Restaurada em 1663 anotada por Túlio Espanca", path=u"/pub13-14/#page/299", author=u"Da Redacção", publication=u"13-14")
writer.add_document(title=u"Foros e Próprios do Concelho (Tombo Municipal de 1651)", path=u"/pub13-14/#page/307", author=u"Celestino David", publication=u"13-14")

#PUB15-16#
writer.add_document(title=u"Antas dos Arredores de Évora", path=u"/pub15-16/#page/5", author=u"Greog Leisner", publication=u"15-16")
writer.add_document(title=u"O Romance de Florbela Espanca", path=u"/pub15-16/#page/57", author=u"Celestino David", publication=u"15-16")
writer.add_document(title=u"Francisco de Mendanha e a sua descendência", path=u"/pub15-16/#page/133", author=u"José de Lima", publication=u"15-16")
writer.add_document(title=u"Relação XXVIII  de Manuel Severim de Faria anotada pelo Pde Manuel Ruela Pombo", path=u"/pub15-16/#page/155", author=u"Da Redacção", publication=u"15-16")
writer.add_document(title=u"Alguns Artistas de Évora nos Séculos XVI-XVII", path=u"/pub15-16/#page/167", author=u"Túlio Espanca", publication=u"15-16")
writer.add_document(title=u"Música e músicos em Évora no último quartel do século XIX", path=u"/pub15-16/#page/337", author=u"João Rosa", publication=u"15-16")
writer.add_document(title=u"Foros e Próprios do Concelho de Évora (Tombo Municipal de 1651)", path=u"/pub15-16/#page/355", author=u"João Rosa", publication=u"15-16")

#PUB17-18#
writer.add_document(title=u"As obras do Palácio de D. Manuel", path=u"/pub17-18/#page/5", author=u"Henrique da Fonseca Chaves", publication=u"17-18")
writer.add_document(title=u"Évora Muçulmana", path=u"/pub17-18/#page/33", author=u"José Pedro Machado", publication=u"17-18")
writer.add_document(title=u"A Vida de S. Bernardo em azulejos", path=u"/pub17-18/#page/39", author=u"A. Rocha Brito", publication=u"17-18")
writer.add_document(title=u"O Romance de Florbela Espanca", path=u"/pub17-18/#page/65", author=u"Celestino David", publication=u"17-18")
writer.add_document(title=u"André Falcão de Resende", path=u"/pub17-18/#page/157", author=u"Flório José de Oliveira", publication=u"17-18")
writer.add_document(title=u"As colecções de Pintura da Livraria de D. Frei Manuel do Cenáculo e dos Extintos Conventos de Évora", path=u"/pub17-18/#page/163", author=u"Túlio Espanca", publication=u"17-18")
writer.add_document(title=u"Antas nos Arredores de Évora", path=u"/pub17-18/#page/233", author=u"Greog Leisner", publication=u"17-18")
writer.add_document(title=u"Lembranças eborenses", path=u"/pub17-18/#page/279", author=u"P. Manuel Severim de Faria e Manuel Ruela Pombo", publication=u"17-18")
writer.add_document(title=u"Artes e Artistas de Évora", path=u"/pub17-18/#page/299", author=u"Túlio Espanca", publication=u"17-18")
writer.add_document(title=u"Foros e Próprios do Concelho (Tombo Municipal de 1651)", path=u"/pub17-18/#page/309", author=u"Túlio Espanca", publication=u"17-18")

#PUB19-20#
writer.add_document(title=u"Miguel de Arruda e a Igreja de Santo Antão de Évora", path=u"/pub19-20/#page/5", author=u"Da Redacção", publication=u"19-20")
writer.add_document(title=u"Três Pintores Alentejanos", path=u"/pub19-20/#page/11", author=u"Diogo de Macedo", publication=u"19-20")
writer.add_document(title=u"A Catedral de Évora", path=u"/pub19-20/#page/23", author=u"Élie Lambert", publication=u"19-20")
writer.add_document(title=u"Inventário dos antigos Arquivos da Câmara e do Real Celeiro Comum de Évora", path=u"/pub19-20/#page/35", author=u"Túlio Espanca", publication=u"19-20")
writer.add_document(title=u"Os Lóios de Évora", path=u"/pub19-20/#page/143", author=u"João Rosa", publication=u"19-20")
writer.add_document(title=u"O Bairrismo Eborense", path=u"/pub19-20/#page/151", author=u"Joaquim Augusto Câmara Manoel", publication=u"19-20")
writer.add_document(title=u"Microcosmografia e Descrição do Mundo pequeno que é o Homem (Reedição anotada por Flório José de Oliveira)", path=u"/pub19-20/#page/177", author=u"André Falcão de Resende", publication=u"19-20")
writer.add_document(title=u"Miscelânea Histórico-Arqueológica", path=u"/pub19-20/#page/197", author=u"Da Redacção", publication=u"19-20")
writer.add_document(title=u"Foros e Próprios do Concelho (Tombo Municipal de 1651)", path=u"/pub19-20/#page/269", author=u"Da Redacção", publication=u"19-20")


#PUB21-22#
writer.add_document(title=u"Pedro Nunes, Meste do Cardeal Infante D. Henrique", path=u"/pub21-22/#page/5", author=u"Joaquim de Carvalho", publication=u"21-22")
writer.add_document(title=u"Painéis dos Mestres de Ferreirim de Igrejas e Conventos de Évora", path=u"/pub21-22/#page/17", author=u"Luís Reis Santos", publication=u"21-22")
writer.add_document(title=u"Manuel Mendes e o Mestrado-de-Capela da Sé de Évora", path=u"/pub21-22/#page/53", author=u"Mário de Sampaio Ribeiro", publication=u"21-22")
writer.add_document(title=u"A Sala dos Actos da Antiga Universidade de Évora", path=u"/pub21-22/#page/61", author=u"António Bartolomeu Gromicho", publication=u"21-22")
writer.add_document(title=u"A vida de S. Bernardo em azulejos eborenses", path=u"/pub21-22/#page/85", author=u"A. Rocha Brito", publication=u"21-22")
writer.add_document(title=u"Notas arqueológicas de Estremoz e Vila Viçosa", path=u"/pub21-22/#page/97", author=u"Octávio da Veiga Ferreira", publication=u"21-22")
writer.add_document(title=u"Artes e Artistas em Évora do Século XVIII", path=u"/pub21-22/#page/111", author=u"Túlio Espanca", publication=u"21-22")
writer.add_document(title=u"Inventário do primitivo Cartulário da Câmara de Évora", path=u"/pub21-22/#page/209", author=u"Túlio Espanca", publication=u"21-22")
writer.add_document(title=u"Microcosmografia e Descrição do Mundo pequeno que é o Homem", path=u"/pub21-22/#page/187", author=u"André Falcão de Resende e Flório José de Oliveira", publication=u"21-22")
writer.add_document(title=u"Foros e Próprios do Concelho (Tombo Municipal de 1651)", path=u"/pub21-22/#page/229", author=u"Da Redacção", publication=u"21-22")



writer.commit()
from whoosh.qparser import MultifieldParser
with ix.searcher() as searcher:
    query = MultifieldParser(["title","author","secondauthor","publication"], ix.schema).parse("evora")
    results = searcher.search(query)
    for result in results:
        print result
        print result["title"]
        print result["path"]
        print result["author"]
