import tkinter as tk
from tkinter import messagebox
import json
import os
from evaluador import evaluar_respuestas
from report_generator import generar_reporte_pdf

def cargar_preguntas():
    base = "preguntas"
    marcos = {}
    for archivo in os.listdir(base):
        if archivo.endswith(".json"):
            nombre = archivo.split(".")[0].upper()
            with open(os.path.join(base, archivo), encoding="utf-8") as f:
                marcos[nombre] = json.load(f)
    return marcos

class DiagnosticoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Autodiagnóstico de Tecnologías - CMMI, COBIT e ITIL")
        self.marcos = cargar_preguntas()
        self.respuestas = {marco: [] for marco in self.marcos}
        self.preguntas_actuales = []
        self.indice_pregunta = 0
        self.marco_actual = None
        self.frame_inicio()

    def frame_inicio(self):
        self.clear_frame()
        label = tk.Label(self.root, text="Selecciona un marco de referencia", font=("Arial", 14))
        label.pack(pady=10)

        for marco in self.marcos:
            btn = tk.Button(self.root, text=marco, width=20,
                            command=lambda m=marco: self.iniciar_diagnostico(m))
            btn.pack(pady=5)

    def iniciar_diagnostico(self, marco):
        self.marco_actual = marco
        self.preguntas_actuales = self.marcos[marco]
        self.indice_pregunta = 0

        messagebox.showinfo(
            "Instrucciones",
            f"Contesta las siguientes {len(self.preguntas_actuales)} preguntas usando una escala del 1 al 5:\n\n"
            "1 = Nunca / No existe\n"
            "3 = Parcialmente implementado\n"
            "5 = Completamente implementado"
        )

        self.mostrar_pregunta()

    def mostrar_pregunta(self):
        self.clear_frame()
        pregunta = self.preguntas_actuales[self.indice_pregunta]

        lbl_num = tk.Label(
            self.root,
            text=f"Pregunta {self.indice_pregunta + 1} de {len(self.preguntas_actuales)}",
            font=("Arial", 10),
            fg="gray"
        )
        lbl_num.pack(pady=5)

        lbl = tk.Label(self.root, text=f"{pregunta['id']}: {pregunta['question']}", wraplength=400, font=("Arial", 12))
        lbl.pack(pady=10)

        self.valor = tk.IntVar()
        opciones = {
            1: "1 - Nunca",
            2: "2 - Rara vez",
            3: "3 - A veces",
            4: "4 - Frecuentemente",
            5: "5 - Siempre"
        }

        for val, texto in opciones.items():
            tk.Radiobutton(self.root, text=texto, variable=self.valor, value=val).pack(anchor="w")

        btn = tk.Button(self.root, text="Siguiente", command=self.guardar_respuesta)
        btn.pack(pady=10)

    def guardar_respuesta(self):
        val = self.valor.get()
        if val == 0:
            messagebox.showwarning("Advertencia", "Por favor selecciona una respuesta.")
            return
        self.respuestas[self.marco_actual].append(val)
        self.indice_pregunta += 1
        if self.indice_pregunta < len(self.preguntas_actuales):
            self.mostrar_pregunta()
        else:
            self.frame_inicio()

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        if any(len(r) > 0 for r in self.respuestas.values()):
            tk.Button(self.root, text="Ver Resultados", command=self.mostrar_resultados).pack(side="bottom", pady=10)

    def mostrar_resultados(self):
        self.clear_frame()
        resultados = evaluar_respuestas(self.respuestas)

        tk.Label(self.root, text="Resultados del Diagnóstico", font=("Arial", 14)).pack(pady=10)
        for marco, data in resultados.items():
            tk.Label(
                self.root,
                text=f"{marco}: {data['evaluacion']} (Promedio: {data['promedio']})",
                font=("Arial", 12)
            ).pack(pady=5)

        tk.Button(self.root, text="Exportar PDF", command=lambda: self.exportar(resultados)).pack(pady=5)
        tk.Button(self.root, text="Reiniciar", command=self.reiniciar).pack(pady=10)

    def exportar(self, resultados):
        generar_reporte_pdf(resultados)
        messagebox.showinfo("Exportación exitosa", "El archivo 'reporte.pdf' fue generado exitosamente.")

    def reiniciar(self):
        self.respuestas = {marco: [] for marco in self.marcos}
        self.frame_inicio()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x450")
    app = DiagnosticoApp(root)
    root.mainloop()

