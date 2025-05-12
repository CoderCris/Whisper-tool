from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Button, Static, TextArea
from textual.containers import Vertical
from services.file_service import process_whisper_file, WhisperProcessingError


class WhisperParserApp(App):
    BINDINGS = [("q", "quit", "Quit")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Vertical(
            Static("Whisper Parser"),
            Static("Ruta al archivo de entrada:"),
            Input(placeholder="Ej: ./mi_audio.txt", id="input_file"),
            Static("Ruta al archivo de salida:"),
            Input(placeholder="Ej: ./output.txt", id="output_file"),
            Button("Procesar", id="process_button"),
            TextArea(id="log", read_only=True),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "process_button":
            input_path = self.query_one("#input_file", Input).value.strip()
            output_path = self.query_one("#output_file", Input).value.strip()
            log = self.query_one("#log", TextArea)

            try:
                result = process_whisper_file(input_path, output_path)
                log.insert("end", f"\n✔ Procesamiento completo. Archivo guardado en {result}")
            except WhisperProcessingError as e:
                log.insert("end", f"\nError: {e}")
