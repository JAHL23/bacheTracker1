# **bacheTracker1**
[Video Demo](https://drive.google.com/file/d/1yFKRYdtsBxjHf9F1rEJHg3mw0oOz0mVI/view?usp=drive_link)

# ![Logo Facultad de Ciencias](images/logoFC85.png) Proyecto - Detección de Baches en imagenes de camino.

[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3100/)


[![Ultralytics Version](https://img.shields.io/badge/ultralytics-8.0.56-green.svg)](https://pypi.org/project/ultralytics/8.0.56/)



**Integrantes**: Jorge Alberto Herrera León / Isaac Daniel Pérez


## Entegrables:

1. [Memoria Técnica](dev_model/MEMORIA-TECNICA.md)
1. [Documentación API](app/api-documentation.md)


## **Índice**
- [**bacheTracker1**](#bachetracker1)
- [ Proyecto - Detección de Baches en imagenes de caminos](#-proyecto---Detección-de-Baches-en-imagenes-de-caminos)
  - [Entegrables:](#entegrables)
  - [**Índice**](#índice)
  - [**Introducción**](#introducción)
  - [**Planteamiento del Problema**](#planteamiento-del-problema)
  - [**Objetivos**](#objetivos)
    - [**Objetivo General**](#objetivo-general)
    - [**Objetivos Específicos**](#objetivos-específicos)
  - [**Metodología**](#metodología)
  - [**Tecnología Utilizada**](#tecnología-utilizada)
  - [**Impacto del Proyecto**](#impacto-del-proyecto)
  - [**Conclusiones**](#conclusiones)
  - [**Referencias**](#referencias)

---

## **Introducción**
Los baches en las carreteras representan un problema significativo para la seguridad vial y el mantenimiento de las infraestructuras urbanas. Este proyecto tiene como objetivo desarrollar un modelo para la detección automática de baches utilizando la tecnología YOLOv8.

---

## **Planteamiento del Problema**
La detección manual de baches es un proceso ineficiente y propenso a errores. Se requiere una solución automatizada que permita identificar baches en tiempo real para mejorar las condiciones de las carreteras y reducir riesgos.

---

## **Objetivos**

### **Objetivo General**
Desarrollar un modelo de detección automática de baches utilizando YOLOv8 para mejorar la seguridad vial y apoyar en el mantenimiento de infraestructuras.

### **Objetivos Específicos**
1. Implementar un modelo de detección previamente entrenado en un conjunto de datos específico.
2. Evaluar el rendimiento del modelo utilizando métricas de precisión y exhaustividad.
3. Generar visualizaciones y estadísticas del rendimiento del modelo.
4. Documentar el proceso de desarrollo y los resultados obtenidos.

---

## **Metodología**
1. **Recolección de Datos:** Obtención de imágenes de carreteras con baches.
2. **Implementación del Modelo:** Utilización de YOLOv8 para entrenar el modelo con el conjunto de datos.
3. **Entrenamiento y Validación:** Configuración de parámetros y entrenamiento del modelo en un entorno de Notebook.
4. **Análisis de Resultados:** Evaluación del modelo mediante métricas y visualizaciones como la matriz de confusión y curvas de precisión-recall.

---

## **Tecnología Utilizada**
- **Lenguaje de Programación:** Python.
- **Notebook de Jupyter:** Google Colab para el desarrollo y entrenamiento del modelo.
- **Bibliotecas y Herramientas:**
  - **YOLOv8:** Framework de detección de objetos utilizado para entrenar el modelo.
  - **Ultralytics:** Librería para implementar YOLOv8.
  - **Google Colab:** Plataforma para ejecutar notebooks y aprovechar recursos de GPU.
  - **Roboflow:** Herramienta para gestionar y descargar conjuntos de datos.
- **Otros:** Librerías estándar de Python y dependencias requeridas por YOLOv8.

---

  El modelo alcanzó un mAP promedio de 0.756, indicando una buena capacidad para detectar baches con precisión aceptable. Las visualizaciones generadas permiten entender mejor el rendimiento y áreas de mejora.

**Resultados y Análisis**



---

## **Impacto del Proyecto**
La implementación de este modelo permite:
- **Mejorar la Seguridad Vial:** Detección temprana de baches para evitar accidentes.
- **Optimizar Recursos:** Ayudar a las autoridades a priorizar reparaciones y mantenimiento.
- **Contribuir a la Automatización:** Reducir la dependencia de procesos manuales en la detección de daños en carreteras.

---

## **Conclusiones**
El proyecto demostró la viabilidad de utilizar YOLOv8 para la detección automática de baches con resultados prometedores. La metodología aplicada y las herramientas utilizadas permitieron desarrollar un modelo efectivo que puede ser mejorado con más datos y ajustes adicionales.

---

## **Referencias**
1. Ultralytics YOLOv8 Documentation: https://docs.ultralytics.com/
2. Roboflow: https://roboflow.com/
3. Google Colab: https://colab.research.google.com/
