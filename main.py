from PIL import Image, ImageDraw, ImageFont

# Configurações principais
width, height = 400, 500
red_color = (204, 9, 47)
black_color = (0, 0, 0)
background_color = (255, 255, 255)

# Criando a imagem com fundo branco
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Desenhando as faixas diagonais
stripe_width = 60
stripes = [
    ((150, 0), (400, 250)), # Faixa vermelha
    ((90, 0), (340, 250)),  # Faixa preta
    ((30, 0), (280, 250)),  # Faixa vermelha
    ((-30, 0), (220, 250)), # Faixa preta
    ((-90, 0), (160, 250))  # Faixa vermelha
]

for i, stripe in enumerate(stripes):
    color = red_color if i % 2 == 0 else black_color
    draw.polygon([stripe[0], stripe[1], (stripe[1][0] - stripe_width, stripe[1][1] + stripe_width), (stripe[0][0] - stripe_width, stripe[0][1] + stripe_width)], fill=color)

# Desenhando o "CAP" estilizado
try:
    # Se houver uma fonte específica, coloque o caminho aqui
    font = ImageFont.truetype("arial.ttf", 120)
except IOError:
    # Caso a fonte não esteja disponível, use a fonte padrão
    font = ImageFont.load_default()

draw.text((30, 50), "CAP", font=font, fill=black_color)

# Salvando a imagem
image.save("escudo_athletico_paranaense.png")
image.show()
