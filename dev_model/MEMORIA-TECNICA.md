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
    - [Funcionamiento del modelo YOLO](#funcionamiento-del-modelo-yolo)
  - [Arquitectura de YOLO](#arquitectura-de-yolo)
    - [Resultados modelo](#resultados-modelo)
  - [Pruebas sobre el modelo](#pruebas-sobre-el-modelo)
    - [Matriz de confusión.](#matriz-de-confusión)
    - [Conclusiones](#conclusiones)
  - [Anexos](#anexos)

## Portada
- **Nombre del Proyecto**: Clasificador baches
- **Fecha**: noviembre de 2024.  
- **Integrantes**: Jorge Alberto Herrera León / Isaac Daniel Pérez

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

### Funcionamiento del modelo YOLO

YOLO ("You Only Look Once") es una familia de algoritmos de visión por computadora diseñados para la detección de objetos en imágenes y videos en tiempo real. A diferencia de otros métodos de detección, YOLO procesa la imagen completa en una sola pasada por la red neuronal, logrando alta precisión y velocidad. Esta capacidad la hace ideal para aplicaciones como vigilancia, robótica, conducción autónoma y más.


## Arquitectura de YOLO

YOLO utiliza una red neuronal convolucional (CNN) optimizada para realizar detección de objetos. Aquí están los componentes clave:

1. Backbone

El wwwbackbone es una CNN preentrenada, como Darknet, que extrae características importantes de la imagen. En las versiones más recientes, como YOLOv5 y YOLOv8, se han adoptado arquitecturas más ligeras y rápidas.

2. Cabeza de Predicción

Se encarga de generar las predicciones finales basadas en las características extraídas. Incluye:

Coordenadas de las bounding boxes.

Confianza para cada predicción.

Distribuciones de probabilidad para cada clase.

La salida del modelo, son coordenadas de bounding boxes, etiquetas de clase y puntajes de confianza.

### Resultados modelo
Documenta los resultados obtenidos del modelo.

## Pruebas sobre el modelo

### Matriz de confusión.

![Matriz de confusión](https://github.com/usuario/repositorio/raw/rama/images/confusion_matrix.png)

![Precision Recall Curve](\images\PR_curve.png)

El modelo tiene un buen balance entre precisión y exhaustividad, con un mAP promedio de 0.756, lo cual indica que el modelo realiza predicciones razonablemente confiables y es capaz de identificar una proporción adecuada de baches.

![Precision-Confidence](\images\P_curve.png)

"all classes 1.00 at 0.821": Sugiere que, al considerar todas las clases, el modelo alcanza una precisión máxima de 1.0 a un nivel de confianza de 0.821.

Ahora veamos la curva F1

![Precision-Confidence](\iages\F1_curve.png)

En general, esta curva sugiere que el modelo tiene un rendimiento aceptable y que el umbral óptimo de confianza está bien definido.

### Conclusiones

El desarrollo del modelo basado en YOLOv8 para la detección de baches ha demostrado ser una solución efectiva en la identificación de irregularidades en superficies viales. A través del entrenamiento y validación, el modelo alcanzó una precisión máxima de 1.0 a un nivel de confianza de 0.821, lo que indica un alto grado de exactitud en las predicciones realizadas.

Las curvas de precisión y F1 obtenidas sugieren que el modelo mantiene un rendimiento consistente y que el umbral de confianza seleccionado es óptimo para el balance entre precisión y recall. Sin embargo, se reconoce la importancia de continuar ajustando hiperparámetros y ampliando el conjunto de datos para mejorar aún más la capacidad de generalización del modelo.

## Anexos
- [Repositorio Github](https://github.com/JAHL23/bacheTracker1)
- [Conjunto de Datos para la Detección de baches en Roboflow](https://universe.roboflow.com/projects-hjaax/pothole-detection-using-yolov5/dataset/1)
- [Documentación ultralytics](https://docs.ultralytics.com/guides/)
