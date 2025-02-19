from PIL import Image, ImageDraw

# Crear una imagen de 50x50 píxeles
size = 50
image = Image.new('RGB', (size, size), 'white')
draw = ImageDraw.Draw(image)

# Dibujar un círculo rojo
draw.ellipse([0, 0, size-1, size-1], fill='red')

# Guardar la imagen
image.save('images/ball.png')