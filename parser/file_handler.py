from pathlib import Path


def read_file(path: str) -> str:
    """
    Lee el contenido de un archivo de texto.

    Args:
        path (str): Ruta al archivo.

    Returns:
        str: Contenido del archivo como cadena.
    """
    return Path(path).read_text(encoding="utf-8")


def write_file(path: str, content: str) -> None:
    """
    Escribe contenido de texto en un archivo.

    Args:
        path (str): Ruta al archivo.
        content (str): Texto a escribir.
    """
    Path(path).write_text(content, encoding="utf-8")
