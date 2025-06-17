import os
import json
from fpdf import FPDF
from pathlib import Path

def generar_reporte_pdf(resultados):
    carpeta_resultados = Path.home() / "Documentos" / "resultados"
    carpeta_resultados.mkdir(parents=True, exist_ok=True)

    ruta_pdf = carpeta_resultados / "reporte.pdf"
    ruta_reco = Path("recomendaciones.json")

    recomendaciones = {}
    if ruta_reco.exists():
        with open(ruta_reco, encoding="utf-8") as f:
            recomendaciones = json.load(f)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Reporte de Autodiagnóstico de TI", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.ln(10)

    for marco, data in resultados.items():
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, f"{marco}", ln=True)

        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f"Evaluación: {data['evaluacion']}", ln=True)
        pdf.cell(0, 10, f"Promedio obtenido: {data['promedio']}", ln=True)

        recomendacion = recomendaciones.get(marco, {}).get(data['evaluacion'], "No hay recomendaciones disponibles.")
        pdf.multi_cell(0, 10, f"Recomendación: {recomendacion}")
        pdf.ln(5)

    pdf.output(str(ruta_pdf))
    print(f"[✓] PDF generado: {ruta_pdf}")

