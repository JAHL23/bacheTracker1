from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import uvicorn
from PIL import Image
import io

# Cargar el modelo
modelo = YOLO("model/best.pt")

# Crear la aplicación FastAPI
app = FastAPI()

# Definir el endpoint para predicción
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Leer el contenido del archivo
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # Realizar la predicción
    results = modelo(image)

    # Procesar los resultados según tus necesidades
    detections = results.pandas().xyxy[0].to_dict(orient="records")

    return {"detections": detections}

# Ejecutar la aplicación
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)