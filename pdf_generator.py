from fpdf import FPDF

def generate_certificate(name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Certificate of Completion", ln=True, align='C')
    pdf.ln(20)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"This is to certify that {name} has completed the Python Project.", ln=True, align='C')
    pdf.output("certificate.pdf")
    print("Certificate created!")

# Example usage
generate_certificate("Ishita Rajesh Suradkar")
