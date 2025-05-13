from pathlib import Path
from parser.file_handler import read_file, write_file
from parser.processor import remove_timestamps_and_merge_text


class WhisperProcessingError(Exception):
    """Excepción para errores de procesamiento de archivos Whisper."""
    pass


def validate_paths(input_path: str, output_path: str) -> tuple[Path, Path]:
    if not input_path or not output_path:
        raise WhisperProcessingError("Los paths de entrada y salida no pueden estar vacíos.")

    input_file = Path(input_path)
    output_file = Path(output_path)

    if not input_file.exists():
        raise WhisperProcessingError(f"El archivo de entrada '{input_path}' no existe.")

    return input_file, output_file


def process_text_from_file(input_file: Path) -> str:
    try:
        raw_text = read_file(str(input_file))
        return remove_timestamps_and_merge_text(raw_text)
    except Exception as e:
        raise WhisperProcessingError(f"Error al leer o procesar el archivo: {e}") from e


def save_processed_text(output_file: Path, cleaned_text: str) -> None:
    try:
        write_file(str(output_file), cleaned_text)
    except Exception as e:
        raise WhisperProcessingError(f"Error al escribir el archivo: {e}") from e


def process_whisper_file(input_path: str, output_path: str) -> str:
    """
    Orquesta la lectura, procesamiento y escritura de un archivo Whisper.

    Args:
        input_path (str): Ruta al archivo original con timestamps.
        output_path (str): Ruta donde guardar el archivo limpio.

    Returns:
        str: Ruta del archivo de salida procesado.

    Raises:
        WhisperProcessingError: Si hay errores de validación o de procesamiento.
    """
    input_file, output_file = validate_paths(input_path, output_path)
    cleaned_text = process_text_from_file(input_file)
    save_processed_text(output_file, cleaned_text)
    return str(output_file)
