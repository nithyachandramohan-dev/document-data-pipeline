# Document Data Pipeline

An end-to-end Python data pipeline that ingests document files (PDFs), extracts and cleans text, transforms it into structured data, and stores it in a relational database for querying and analysis.

This project demonstrates core data engineering concepts including data ingestion, transformation, loading (ETL), and version control using Git and GitHub.

---

## Project Overview

The pipeline performs the following steps:

1. **Ingest**
   - Reads PDF documents from a raw data directory
   - Extracts textual content using Python

2. **Transform**
   - Cleans extracted text (removes empty lines and noise)
   - Converts text into structured tabular format using Pandas

3. **Load**
   - Loads structured data into an SQLite database
   - Enables SQL-based querying

---

## Tech Stack

- **Programming Language:** Python 3  
- **Libraries:** Pandas, pdfplumber, SQLAlchemy  
- **Database:** SQLite  
- **Tools:** Git, GitHub  
- **Environment:** Python Virtual Environment (venv)

---

## Project Structure
document-data-pipeline/
│
├── src/
│   ├── ingest.py        # Extracts text from PDF documents
│   ├── transform.py     # Cleans and structures extracted text
│   └── load_to_db.py    # Loads structured data into SQLite
│
├── data/
│   ├── raw/             # Input PDFs (ignored by git)
│   └── processed/       # Generated files (ignored by git)
│
├── requirements.txt
├── .gitignore
└── README.md


---

## How to Run the Pipeline

## How to Run the Pipeline

Follow the steps below to run the complete document data pipeline.

---

### Step 1: Set up the environment

Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

data/raw/

data/raw/sample_document.pdf

##Run pipeline

python src/ingest.py
python src/transform.py
python src/load_to_db.py

## Verify the output

data/processed/

##squlite db created

data/document_pipeline.db

##You can query the database using SQLite

sqlite3 data/document_pipeline.db
SELECT COUNT(*) FROM document_lines;



## Key Learnings

- Built a complete ETL pipeline from scratch
- Processed unstructured document data
- Performed data cleaning and transformation using Pandas
- Loaded structured data into a relational database
- Used Git and GitHub for version control


## Future Enhancements

- Add OCR support for scanned PDFs
- Support multiple document formats
- Automate pipeline execution
- Deploy using cloud storage services


## Author

Nithya Chandra Mohan  
MSCS Student, California State University Long Beach  
GitHub: https://github.com/nithyachandramohan-dev
