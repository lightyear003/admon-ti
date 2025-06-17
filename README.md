# Autodiagnóstico de Eficiencia en la Administración de Tecnologías

Este proyecto es una aplicación de escritorio desarrollada en Python con Tkinter que permite a empresas realizar un autodiagnóstico de eficiencia en la administración de tecnologías. La evaluación se basa en tres marcos de referencia:

- CMMI (Capability Maturity Model Integration)
- COBIT (Control Objectives for Information and Related Technologies)
- ITIL (Information Technology Infrastructure Library)

## Requisitos

- Python 3.8 o superior
- pip
- Sistema operativo Windows o Linux
- Git (opcional, si se clona desde repositorio)

## Instalación

### 1. Descargar el código fuente

Puedes clonar el repositorio o descargarlo como archivo ZIP:

Clonar con Git:

```
git clone https://github.com/lightyear003/admon-ti.git
cd admon-ti
```

### 2. Crear un entorno virtual

En Linux:

```
python3 -m venv venv
source venv/bin/activate
```

En Windows:

```
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

Dentro del entorno virtual, instalar las siguientes bibliotecas:

```
pip install fpdf matplotlib
```

Estas dependencias son necesarias tanto para la visualización como para la generación de reportes en PDF.

## Ejecución

Una vez instaladas las dependencias, hay dos formas de ejecutar el software:

### Opción 1: Ejecutar el código Python directamente

```
python main.py
```

Esto abrirá una ventana con la interfaz gráfica del sistema.

### Opción 2: Ejecutar el binario precompilado

En la carpeta `dist/` se encuentran dos binarios:

- `main` (para Linux)
- `main.exe` (para Windows)

Además, se incluyen las siguientes carpetas y archivos necesarios para su funcionamiento:

```
dist/
├── main
├── diagnostico-ti.exe
├── preguntas/
│   ├── cmmi.json
│   ├── cobit.json
│   └── itil.json
├── recomendaciones.json
```

Para ejecutar en Linux:

```
cd dist
./main
```

Para ejecutar en Windows:

- Ir a la carpeta `dist`
- Hacer doble clic en `diagnostico-ti.exe`

El sistema abrirá una ventana donde el usuario puede seleccionar el marco a evaluar, responder las preguntas y obtener una evaluación con sugerencias personalizadas.

## Resultados

El sistema genera un archivo `reporte.pdf` con los resultados del diagnóstico. Este archivo se guarda en:

- Linux: `/home/usuario/Documentos/resultados/`
- Windows: `C:\Users\usuario\Documents\resultados\`

## Estructura del proyecto

```
autodiagnostico-ti/
├── main.py
├── evaluador.py
├── report_generator.py
├── recomendaciones.json
├── preguntas/
│   ├── cmmi.json
│   ├── cobit.json
│   └── itil.json
├── dist/
│   ├── main
│   ├── diagnostico-ti.exe
│   ├── preguntas/
│   └── recomendaciones.json
```

## Licencia

Este proyecto se distribuye con fines educativos y de uso interno. No está autorizado para uso comercial sin previa autorización.

