import tkinter as tk
from tkinter import ttk, messagebox


class ViewResults:
    def __init__(self, root, surveys):
        if not surveys:
            messagebox.showerror("Error", "No hay encuestas disponibles.")
            return

        self.surveys = surveys
        self.window = tk.Toplevel(root)
        self.window.title("Resultados de Encuestas")

        ttk.Label(self.window, text="Seleccione una Encuesta:").grid(row=0, column=0, pady=5, padx=5)
        self.survey_list = ttk.Combobox(self.window, values=list(surveys.keys()), state="readonly")
        self.survey_list.grid(row=0, column=1, pady=5, padx=5)

        ttk.Button(self.window, text="Ver Resultados", command=self.show_results).grid(row=1, column=0, columnspan=2, pady=10)
        self.results_text = tk.Text(self.window, width=50, height=20)
        self.results_text.grid(row=2, column=0, columnspan=2, pady=10)

    def show_results(self):
        survey_title = self.survey_list.get()
        if survey_title:
            self.results_text.delete("1.0", "end")
            survey = self.surveys[survey_title]
            self.results_text.insert("end", f"Resultados de la encuesta '{survey_title}':\n\n")
            for i, response in enumerate(survey["responses"], start=1):
                self.results_text.insert("end", f"Respuesta {i}:\n")
                for j, answer in enumerate(response, start=1):
                    self.results_text.insert("end", f"  Pregunta {j}: {answer}\n")
                self.results_text.insert("end", "\n")
        else:
            messagebox.showerror("Error", "Seleccione una encuesta.")
