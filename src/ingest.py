import os
import pdfplumber

RAW_DIR = "data/raw"
OUT_DIR = "data/processed"

os.makedirs(OUT_DIR, exist_ok=True)

def extract_text_from_pdf(pdf_path):
    text_pages = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                text_pages.append(text)
    return "\n\n".join(text_pages)

def main():
    files = os.listdir(RAW_DIR)
    pdf_files = [f for f in files if f.endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in data/raw")
        return

    pdf_name = pdf_files[0]
    pdf_path = os.path.join(RAW_DIR, pdf_name)

    print(f"Reading: {pdf_path}")
    text = extract_text_from_pdf(pdf_path)

    output_file = pdf_name.replace(".pdf", ".txt")
    output_path = os.path.join(OUT_DIR, output_file)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Text saved to: {output_path}")

if __name__ == "__main__":
    main()
