# SDET_Test_Lumu
prueba tecnica vacante Lumu

## 1. Tecnologías y Herramientas
    Lenguaje: Python 3.12+  
    Framework BDD: Behave (Gherkin)  
    Automatización Web: Selenium WebDriver  
    Librería de Aserciones: PyHamcrest  
    Patrón de Arquitectura: POM  

## 2. instalacion y configuracion
    a. clona el repositorio https://github.com/barrera1994/SDET_Test_Lumu
    b. crea y activa entorno virtual      
        -En windows  
            python -m venv .venv  
            .\.venv\Scripts\Activate.ps1  
        -En mac  
            python3 -m venv .venv  
            source .venv/bin/activate  
    c. instala dependencias   
        pip install -r requirements.txt  

## 3. ejecucion de casos  
    a. para ejecutar todo utiliza el comando "behave"  
    b. para ejecutar un escenario en especifico utiliza tags "behave --tags=@punto1"  

## 4. reporte html
    al finalizar cada ejecución, se genera automáticamente un reporte con los resultados de los casos probados dentro de la carpeta reports/
