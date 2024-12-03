from fastapi import FastAPI, UploadFile, File, HTTPException
from ultralytics import YOLO
from PIL import Image, UnidentifiedImageError
import io
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.responses import JSONResponse
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

        
        # Preprocesar la imagen (función que debería estar definida previamente)
        image = preprocess_image(image)

        # Hacer predicciones con el modelo YOLO
        print('Antes del predict')
        results = model.predict(image) ### Aqui da el error 500
        print('Predict realizado')
        
        # Asegurarnos de que 'results' contiene lo que esperamos
        annotations = []
        if hasattr(results, 'boxes') and results.boxes:
            for box in results.boxes:
                annotations.append({
                    "label": box.label,
                    "confidence": box.confidence,
                    "coordinates": box.xyxy.tolist()
                })
        else:
            raise ValueError("El modelo no devolvió resultados válidos.")

        # Si no se encuentra ninguna anotación, retornar un mensaje vacío
        if not annotations:
            return JSONResponse(
                status_code=200,
                content={"message": "No se detectaron objetos en la imagen."}
            )

        # Retornar las anotaciones como JSON
        return JSONResponse(
            status_code=200,
            content={"annotations": annotations}
        )

    except UnidentifiedImageError:
        raise HTTPException(status_code=400, detail="La imagen subida no es válida o no se puede procesar.")
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=f"Error en el modelo: {str(ve)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

    except UnidentifiedImageError:
        # Error específico para una imagen inválida
        raise HTTPException(status_code=400, detail="La imagen subida no es válida o no se puede procesar.")
    except Exception as e:
        print(f"Error interno: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
