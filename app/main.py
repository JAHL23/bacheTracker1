from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
from PIL import Image
import io

app = FastAPI()

# Cargar el modelo YOLO
model = YOLO('best81.pt')

# Función para preprocesar la imagen
def preprocess_image(image: Image.Image) -> Image.Image:
    return image.resize((640, 640))

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
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
    
    return {"annotations": annotations}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)