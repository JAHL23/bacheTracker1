from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import uvicorn
from PIL import Image
import io
import os

# Cargar el modelo
model_path = os.path.join("model", "best.pt")

modelo = YOLO(model_path)
