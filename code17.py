import jpg2pdf as jp

with jp.create('imagem/teste.pdf') as pdf:
    pdf.add('imagem/foto1.jpg')
    pdf.add('imagem/foto3.jpg')