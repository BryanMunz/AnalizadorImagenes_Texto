import pytesseract
from PIL import Image
from langdetect import detect
import translate
import cv2

# Configuración de la ruta a Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# Ruta a la imagen
imagen = cv2.imread('imagen.png')

# Mostrar la imagen en una ventana utilizando OpenCV
cv2.imshow('Imagen Original', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Convertir la imagen a formato RGB (PIL)
imagen_pil = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))

# Reconocimiento de texto
texto_reconocido = pytesseract.image_to_string(imagen_pil)

# Verificar si se ha detectado texto
if texto_reconocido.strip():
    # Imprimir el texto reconocido
    print("Texto reconocido:")
    print(texto_reconocido)

    # Detectar el idioma del texto reconocido
    idioma_detectado = detect(texto_reconocido)

    if idioma_detectado != 'es':
        # Traducción de texto usando la biblioteca translate
        translator = translate.Translator(to_lang="es")
        texto_espanol = translator.translate(texto_reconocido)

        # Imprimir el texto reconocido en español
        print("\nTexto en español:")
        print(texto_espanol)
else:
    print("No se ha detectado texto en la imagen.")