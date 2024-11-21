import tkinter as tk
from tkinter import ttk, messagebox


class CreateSurvey:
    def __init__(self, root, surveys):
        self.surveys = surveys

        # Configurar ventana
        self.window = tk.Toplevel(root)
        self.window.title("Crear Encuesta")
        self.window.geometry("400x350")
        self.window.configure(bg="#f5f5f5")
        self.center_window()

        # Título
        ttk.Label(
            self.window,
            text="Título de la Encuesta:",
            font=("Arial", 9, "bold"),  # Fuente tamaño 9
            background="#f5f5f5",
            foreground="#000000",  # Texto negro
        ).pack(pady=10)

        self.title_entry = ttk.Entry(self.window, font=("Arial", 8))  # Fuente tamaño 8
        self.title_entry.pack(pady=5, fill="x", padx=20)

        # Preguntas
        ttk.Label(
            self.window,
            text="Preguntas (una por línea):",
            font=("Arial", 9, "bold"),  # Fuente tamaño 9
            background="#f5f5f5",
            foreground="#000000",  # Texto negro
        ).pack(pady=10)

        self.questions_text = tk.Text(self.window, font=("Arial", 8), height=10, wrap="word")  # Fuente tamaño 8
        self.questions_text.pack(padx=20, pady=5, fill="both")

        # Botón Guardar
        ttk.Button(
            self.window,
            text="Guardar Encuesta",
            command=self.save_survey,
            style="TButton",
        ).pack(pady=20)

    def center_window(self):
        self.window.update_idletasks()
        width = self.window.winfo_width()
        height = self.window.winfo_height()
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f"{width}x{height}+{x}+{y}")

    def save_survey(self):
        title = self.title_entry.get()
        questions = self.questions_text.get("1.0", "end").strip().split("\n")
        if title and questions:
            self.surveys[title] = {"questions": questions, "responses": []}
            messagebox.showinfo("Éxito", f"Encuesta '{title}' creada correctamente.")
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Debe llenar todos los campos.")

