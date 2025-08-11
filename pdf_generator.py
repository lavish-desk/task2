from fpdf import FPDF
import datetime
import os

class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Data Report", ln=True, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_summary(self, summary):
        self.set_font("Arial", "", 12)
        self.multi_cell(0, 10, summary)
        self.ln(5)

    def add_image(self, image_path):
        if os.path.exists(image_path):
            self.image(image_path, x=10, y=self.get_y(), w=180)
        else:
            self.set_font("Arial", "I", 10)
            self.cell(0, 10, "Visualization image not found.", ln=True)

def generate_pdf(summary_text, image_path, output_path="reports/report.pdf"):
    pdf = PDFReport()
    pdf.add_page()
    pdf.add_summary(summary_text)
    pdf.add_image(image_path)
    pdf.output(output_path)
