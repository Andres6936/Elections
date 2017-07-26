# Bienvenido a la documentación

Visite el repositorio en [GitHub](https://github.com/Andres6936/N1-Elecciones-Python).

## Comandos

* `mkdocs new [dir-name]` - Crea un nuevo proyecto.
* `mkdocs serve` - Comienza a recargar la pagina de documentación.
* `mkdocs build` - Contruye el sitio de documentación.
* `mkdocs help` - Imprime los mensaje de ayuda.

## Diseño del Proyecto


    Data/                           # Imagenes del Candidato 1, 2 y 3.
    Docs/                           # Contiene los archivos de documentación.
    Docs/Img/                       # Contiene las imagenes de la documentación.
            Interfaz.png            # Imagen de muestra de la interfaz de la App.
    Docs/Modulos/
                Interfaz/           # Documentación del modulo Interfaz.
                    ...
                Mundo/              # Documentación del modulo Mundo.
                    ...
        index.md                    # La página principal de la documentación.
        descripcion.md              # Describe el objetivo del proyecto.
        requerimientos.md           # Describe los requerimientos del proyecto.
    Source/                         # Contiene todos los modulos de la App.
        Interfaz/                   # Modulo Interfaz.
            InterfazElecciones.py
            PanelCandidato.py
            PanelExtension.py
            PanelImagen.py
            PanelUrna.py
        Mundo/                      # Modulo Mundo.
            Candidato.py
            Urna.py
    .gitattributes
    .gitignore                      # Archivos ignorados por Git
    __main__.py                     # Ejecuta la App.
    App.py
    mkdocs.yml                      # El archivo de configuración.
