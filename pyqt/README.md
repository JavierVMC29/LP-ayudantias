# Analizador léxico y sintáctico con PyQt 5 y PLY

- [Documentación oficial de PLY](https://ply.readthedocs.io/en/latest/ply.html)
- [Repositorio oficial de PLY](https://github.com/dabeaz/ply)
- [Documentación oficial de PyQt 5](https://www.riverbankcomputing.com/static/Docs/PyQt5/)


## Proyecto demo

Para probar el proyecto sigue los siguientes pasos:


1. Crea un entorno virtual de Python

```shell
py -m venv .venv
```

2. Activa el entorno virtual de Python

```shell
.venv\Scripts\activate
```

3. Instala las dependencias

```shell
py -m pip install -r requirements.txt
```

4. Ejecútalo

```shell
python main.py
```

## Qt Designer

Qt Designer te permite crear interfaces de usuario con PyQt a través de una interfaz gráfica fácil de usar.

>**Nota:** Antes de empezar asegurate de tener activado el entorno virtual de Python.

Para instalar Qt Designer usa el siguiente comando:

```shell
pip install qt6-tools
```

Para abrir la interfaz de Qt Designer usa el siguiente comando:

```shell
qt6-tools designer
```


>**Nota:** Para crear el archivo requirements usa el siguiente comando
```shell
py -m pip freeze > requirements.txt
```