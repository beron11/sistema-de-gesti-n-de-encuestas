import tkinter as tk
from tkinter import ttk, messagebox


class AnswerSurvey:
    def __init__(self, root, surveys):
        if not surveys:
            messagebox.showerror("Error", "No hay encuestas disponibles.")
            return

        self.surveys = surveys
        self.window = tk.Toplevel(root)
        self.window.title("Responder Encuesta")

        ttk.Label(self.window, text="Seleccione una Encuesta:").grid(row=0, column=0, pady=5, padx=5)
        self.survey_list = ttk.Combobox(self.window, values=list(surveys.keys()), state="readonly")
        self.survey_list.grid(row=0, column=1, pady=5, padx=5)

        self.answer_frame = ttk.Frame(self.window)
        self.answer_frame.grid(row=2, column=0, columnspan=2)

        ttk.Button(self.window, text="Cargar Encuesta", command=self.load_questions).grid(row=1, column=0, columnspan=2, pady=10)

    def load_questions(self):
        survey_title = self.survey_list.get()
        if survey_title:
            for widget in self.answer_frame.winfo_children():
                widget.destroy()

            questions = self.surveys[survey_title]["questions"]
            self.entries = []

            for i, question in enumerate(questions, start=1):
                ttk.Label(self.answer_frame, text=f"{i}. {question}").grid(row=i-1, column=0, pady=5, padx=5)
                entry = ttk.Entry(self.answer_frame, width=30)
                entry.grid(row=i-1, column=1, pady=5, padx=5)
                self.entries.append(entry)

            ttk.Button(self.answer_frame, text="Enviar Respuestas", command=lambda: self.submit_answers(survey_title)).grid(
                row=len(questions), column=0, columnspan=2, pady=10
            )

    def submit_answers(self, survey_title):
        responses = [entry.get() for entry in self.entries]
        if all(responses):
            self.surveys[survey_title]["responses"].append(responses)
            messagebox.showinfo("Éxito", f"Respuestas registradas para '{survey_title}'.")
            self.window.destroy()
        else:
            messagebox.showerror("Error", "Debe responder todas las preguntas.")
