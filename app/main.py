from fastapi import FastAPI, UploadFile, File, HTTPException
from ultralytics import YOLO
from PIL import Image, UnidentifiedImageError
import io

app = FastAPI()

# Cargar el modelo YOLO
model = YOLO('best.pt')


# Función para preprocesar la imagen
def preprocess_image(image: Image.Image) -> Image.Image:
    """
    Preprocesa la imagen redimensionándola a 640x640.
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
        
        # Hacer predicciones
        results = model.predict(image)
        
        # Extraer las anotaciones de los resultados
        annotations = []
        for result in results:
            for box in result.boxes:
                annotations.append({
                    "label": box.label,
                    "confidence": box.confidence,
                    "coordinates": box.xyxy.tolist()
                })
        
        # Retornar las anotaciones
        return {"annotations": annotations}
    
    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="La imagen subida no es válida o no se puede procesar.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    # Ejecutar el servidor Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

import requests

url = "http://localhost:8000/predict/"
files = {"file": open("11.jpg", "rb")}
response = requests.post(url, files=files)

# Mostrar las anotaciones de la predicción
print(response.json())
