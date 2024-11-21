import tkinter as tk
from tkinter import ttk
from create_survey import CreateSurvey
from answer_survey import AnswerSurvey
from view_results import ViewResults


class SurveySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Encuestas")
        self.root.geometry("400x300")  # Tamaño reducido de la ventana
        self.root.configure(bg="#f5f5f5")
        self.root.resizable(True, True)

        self.surveys = {}

        # Título
        title_label = tk.Label(
            root,
            text="Sistema de Encuestas",
            font=("Arial", 12, "bold"),  # Ajustamos el tamaño de la fuente
            fg="#000000",  # Color negro para texto
            bg="#f5f5f5",  # Fondo claro
        )
        title_label.pack(pady=10)

        # Botones
        button_frame = ttk.Frame(root, padding=15)
        button_frame.pack(expand=True)

        # Crear estilo para los botones
        style = ttk.Style()
        style.configure(
            "TButton",
            font=("Arial", 10, "bold"),  # Ajustamos el tamaño de la fuente en botones
            padding=5,
            background="#007BFF",  # Azul estándar
            foreground="#000000",  # Texto negro
            relief="raised",
            width=18,  # Ancho fijo para los botones
        )
        style.map(
            "TButton",
            background=[("active", "#0056b3")],  # Color más oscuro al presionar
        )

        # Crear botones con el mismo tamaño
        self.create_button(button_frame, "Crear Encuesta", self.create_survey)
        self.create_button(button_frame, "Responder Encuesta", self.answer_survey)
        self.create_button(button_frame, "Ver Resultados", self.view_results)
        self.create_button(button_frame, "Salir", root.quit)

    def create_button(self, frame, text, command):
        button = ttk.Button(frame, text=text, command=command, style="TButton")
        button.pack(pady=3)  # Reducimos aún más el espaciado entre botones

    def create_survey(self):
        CreateSurvey(self.root, self.surveys)

    def answer_survey(self):
        AnswerSurvey(self.root, self.surveys)

    def view_results(self):
        ViewResults(self.root, self.surveys)


if __name__ == "__main__":
    root = tk.Tk()
    app = SurveySystem(root)
    root.mainloop()
