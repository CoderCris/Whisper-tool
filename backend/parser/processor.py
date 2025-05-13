import re

def remove_timestamps_and_merge_text(text: str) -> str:
    """
    Elimina marcas de tiempo del formato Whisper y combina las líneas en un solo párrafo.

    Args:
        text (str): Texto original con timestamps.

    Returns:
        str: Texto limpio y unificado.
    """
    cleaned_text = re.sub(r'\[\d{2}:\d{2}\.\d{3} --> \d{2}:\d{2}\.\d{3}\]\s*', '', text)
    return ' '.join(cleaned_text.splitlines())
