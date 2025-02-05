import PyPDF2

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
    return text

# Example usage
pdf_path = 'All Service Lines-2.pdf'
extracted_text = extract_text_from_pdf(pdf_path)
print(extracted_text)
