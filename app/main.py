from fastapi import FastAPI, UploadFile, File, HTTPException
from ultralytics import YOLO
from PIL import Image, UnidentifiedImageError, ImageDraw
import io
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import StreamingResponse
import logging

app = FastAPI()

# Rutas para los templates
templates = Jinja2Templates(directory="templates")

# Ruta al modelo YOLO
model = YOLO('best81.pt')

# Ruta raíz para evitar el error 404
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Función para preprocesar la imagen
def preprocess_image(image: Image.Image) -> Image.Image:
    """
    Preprocesa la imagen redimensionándola a 640x640.
    Puedes cambiar el tamaño según sea necesario para adaptarse al modelo.
    """
    return image.resize((640, 640))

@app.post("/predict/", summary="Haz una predicción con el modelo YOLO")
async def predict(file: UploadFile = File(...)):
    """
    Endpoint que recibe una imagen y devuelve las anotaciones del modelo YOLO.
    """
    try:
        # Leer la imagen subida
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes))

        # Preprocesar la imagen
        image = preprocess_image(image)

        # Hacer predicciones con el modelo YOLO
        results = model.predict(image)

        # Dibujar las bounding boxes en la imagen
        draw = ImageDraw.Draw(image)
        for result in results[0].boxes.data:  # Asumiendo que YOLO devuelve predicciones de esta forma
            box = result[:4].tolist()  # Coordenadas de la caja (xyxy)
            label = int(result[5])  # Etiqueta del objeto (asumiendo que es el índice de la clase)
            
            # Dibujar la caja
            draw.rectangle([box[0], box[1], box[2], box[3]], outline="red", width=3)
            draw.text((box[0], box[1]), str(label), fill="red")

        # Convertir la imagen a bytes
        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='PNG')
        img_byte_arr.seek(0)

        # Devolver la imagen con las bounding boxes
        return StreamingResponse(img_byte_arr, media_type="image/png")

    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="La imagen subida no es válida o no se puede procesar.")
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Error en el modelo: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
