# Documentación de la API

## **Descripción General**
Esta API permite cargar una imagen, procesarla con un modelo YOLO preentrenado (`best81.pt`) y devolver la imagen con las detecciones (bounding boxes) superpuestas.

---

## **Endpoints**

### **1. GET `/`**
**Descripción:**  
Devuelve la página de inicio basada en un template HTML.  
Es útil para implementar una interfaz visual básica para cargar imágenes y mostrar resultados.

**Parámetros:**  
- **Query Params:** Ninguno.

**Respuesta Exitosa (200):**  
- **Contenido:** Renderización del archivo `index.html`.

---

### **2. POST `/predict/`**
**Descripción:**  
Recibe una imagen, realiza una predicción utilizando un modelo YOLO y devuelve la imagen con las bounding boxes generadas por el modelo.

**Parámetros:**
- **Body:**
  - **file (UploadFile):** Archivo de imagen que se desea analizar.

**Detalles del Proceso:**  
1. La imagen cargada es preprocesada (redimensionada a 640x640 píxeles).  
2. El modelo YOLO realiza la predicción sobre la imagen.  
3. Se dibujan las bounding boxes y etiquetas de las detecciones sobre la imagen.  
4. La imagen procesada se devuelve como una respuesta en formato PNG.

**Ejemplo de Uso con `curl`:**
```bash
curl -X POST "http://127.0.0.1:8000/predict/" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@ruta_de_tu_imagen.jpg"
```

**Respuesta Exitosa (200):**  
- **Formato:** `image/png`  
- **Contenido:** Imagen con las bounding boxes superpuestas.

**Errores Posibles:**
- **400 Bad Request:** 
  - La imagen subida no es válida o no se puede procesar.
  - Error en el modelo durante la predicción.
- **500 Internal Server Error:** Error interno en el servidor.

---

## **Detalles Técnicos**

### **Modelos y Librerías Utilizadas**
1. **YOLO (Ultralytics):** Modelo preentrenado para detección de objetos.  
   Archivo del modelo: `best81.pt`.  
2. **PIL (Pillow):** Procesamiento de imágenes.
3. **FastAPI:** Framework para construir la API.
4. **Jinja2 Templates:** Para renderizar la página HTML inicial.

### **Preprocesamiento de Imágenes**
Todas las imágenes son redimensionadas a `640x640` píxeles antes de ser procesadas por el modelo.

### **Errores Manejados**
- **`UnidentifiedImageError`:** Para imágenes no válidas.
- **`ValueError`:** En caso de errores durante la predicción.
- **Cualquier excepción genérica:** Manejo como error interno.

---

## **Ejecución de la API**
Para ejecutar la API localmente:
1. Asegúrate de tener instaladas todas las dependencias necesarias:
   ```bash
   pip install fastapi uvicorn ultralytics pillow jinja2
   ```
2. Inicia el servidor con:
   ```bash
   uvicorn main:app --reload
   ```
   Esto ejecutará la API en `http://127.0.0.1:8000`.

---

## **Plantillas HTML**
El archivo `index.html` debe estar ubicado en el directorio `templates` y proporcionar una interfaz para cargar imágenes al endpoint `/predict/`.

---

## **Notas Adicionales**
- Verifica que el modelo YOLO (`best81.pt`) esté correctamente ubicado en el directorio correspondiente.
- El tamaño de las imágenes (640x640) puede ajustarse dependiendo del modelo y los requerimientos.
