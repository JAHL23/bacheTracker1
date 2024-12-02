from fastapi import FastAPI, UploadFile, File, HTTPException
from ultralytics import YOLO
from PIL import Image, UnidentifiedImageError
import io

app = FastAPI()

# Ruta al modelo YOLO
model = YOLO('best81.pt')

# Ruta raíz para evitar el error 404
@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la API de predicción YOLO. Usa '/predict/' para realizar predicciones."}

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

        # Si no se encuentra ninguna anotación, se retorna un mensaje vacío
        if not annotations:
            return {"message": "No se detectaron objetos en la imagen."}

        # Retornar las anotaciones
        return {"annotations": annotations}

    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="La imagen subida no es válida o no se puede procesar.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
