# Memoria Técnica

## Índice
- [Memoria Técnica](#memoria-técnica)
  - [Índice](#índice)
  - [Portada](#portada)
  - [Alcance del proyecto](#alcance-del-proyecto)
    - [Objetivo](#objetivo)
    - [Introducción](#introducción)
  - [Fuentes de información y procedimientos aplicados](#fuentes-de-información-y-procedimientos-aplicados)
    - [Construcción del modelo](#construcción-del-modelo)
    - [Sobre el dataset](#sobre-el-dataset)
    - [Entrenamiento del modelo](#entrenamiento-del-modelo)
    - [Funcionamiento del modelo YOLO8](#funcionamiento-del-modelo-yolo8)
    - [Resultados modelo](#resultados-modelo)
    - [Pruebas sobre el modelo](#pruebas-sobre-el-modelo)
    - [Conclusiones](#conclusiones)
  - [Conclusiones generales](#conclusiones-generales)
  - [Anexos](#anexos)

## Portada
- **Nombre del Proyecto**: Clasificador baches
- **Fecha**: noviembre de 2024.  

## Alcance del proyecto
Implementar un sistema que pueda detectar baches en tiempo real a partir de imágenes o videos capturados por cámaras, sistema consumible via una API.

### Objetivo
Este proyecto tiene como objetivo desarrollar un modelo de clasificación de baches en tiempo real utilizando la tecnología YOLO (You Only Look Once). YOLO es una técnica avanzada de detección de objetos que permite identificar y clasificar objetos en imágenes y videos con alta precisión y velocidad. Al implementar este modelo, buscamos proporcionar una herramienta eficaz para la detección automática de baches.

### Introducción

 YOLO es una técnica avanzada de detección de objetos que permite identificar y clasificar objetos en imágenes y videos con alta precisión y velocidad.

Dado que no se disponía de una gran cantidad de imágenes de baches, se optó por utilizar técnicas de aprendizaje por transferencia, específicamente fine-tuning, para adaptar un modelo preentrenado YOLOv8 (**CNN**)a la tarea de clasificación de baches. Esta técnica permite aprovechar el conocimiento adquirido por el modelo en otras tareas de detección de objetos y aplicarlo a la detección de baches, mejorando así la precisión y eficiencia del modelo con un conjunto de datos limitado.

## Fuentes de información y procedimientos aplicados


### Construcción del modelo
Para la construcción del modelo, se utilizó el dataset de detección de baches proporcionado por Roboflow, disponible en [este enlace](https://universe.roboflow.com/projects-hjaax/pothole-detection-using-yolov5/dataset/1). Aunque el dataset fue originalmente utilizado para entrenar un modelo YOLOv5, en este proyecto se empleó el mismo dataset para entrenar un modelo YOLOv8.

Para el fine-tuning del modelo YOLOv8, se siguieron las guías y procedimientos detallados en la documentación de Ultralytics, disponible [aquí](https://docs.ultralytics.com/guides/). Estas guías proporcionaron instrucciones claras sobre cómo ajustar un modelo preentrenado para la tarea específica de detección de baches, mejorando así la precisión y eficiencia del modelo con un conjunto de datos limitado.

### Sobre el dataset

Una de las ventajas de usar un dataset de Roboflow, es que al momento de descargar los datos se particionan en 3 conjuntos.

**test** con 465 imagenes.

**train** con 133 imagenes.

**valid** con 67 imagenes.

tenemos un total de 665 imagenes, no se realizo data augmentation.


Solo tenemos un tipo de clase(**bache**).

Para preprocesar los datos, escalamos a 640*640 pixeles.

### Entrenamiento del modelo

Se utilizó un modelo preentrenado YOLOv8 (yolov8l.pt) y se realizó fine-tuning con un conjunto de datos específico de baches. El entrenamiento se llevó a cabo durante 45 épocas con imágenes de tamaño 640x640.

### Funcionamiento del modelo YOLO8


### Resultados modelo
Documenta los resultados obtenidos del modelo.

### Pruebas sobre el modelo
Describe las pruebas realizadas sobre el modelo.

### Conclusiones
Conclusiones específicas de cada modelo probado.

## Conclusiones generales
Presenta las conclusiones globales del proyecto.

## Anexos
- Referencias al código realizado.
- Repositorio en GitHub del proyecto.
