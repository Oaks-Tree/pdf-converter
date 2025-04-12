from flask import Flask, request, send_file
from PyPDF2 import PdfReader, PdfWriter
import io

app = Flask(__name__)
app.secret_key = b'oakstree'

@app.route("/")
def hello():
    return "Hello, I love Flask!"


@app.route('/convert-pdf', methods=['POST'])
def convert_pdf():
    # Get the PDF file from the request
    pdf_file = request.files['pdf_file']

    # Read the PDF file
    reader = PdfReader(pdf_file)

    # Create a new PDF writer
    writer = PdfWriter()

    # Iterate over the pages and add them to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Set the PDF version to 1.6
    writer._header_version = (1, 6)

    # Create a new PDF file
    new_pdf_file = io.BytesIO()
    writer.write(new_pdf_file)

    # Send the new PDF file as a response
    new_pdf_file.seek(0)
    return send_file(new_pdf_file, as_attachment=True, download_name='converted_pdf.pdf')


if __name__ == '__main__':
    app.run(debug=True)
