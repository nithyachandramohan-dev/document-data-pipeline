import os
import pandas as pd

INPUT_DIR = "data/processed"
OUTPUT_DIR = "data/processed"

def clean_text_lines(text):
    lines = text.split("\n")
    cleaned = [line.strip() for line in lines if line.strip()]
    return cleaned

def main():
    files = [f for f in os.listdir(INPUT_DIR) if f.endswith(".txt")]

    if not files:
        print("No text files found")
        return

    txt_file = files[0]
    txt_path = os.path.join(INPUT_DIR, txt_file)

    with open(txt_path, "r", encoding="utf-8") as f:
        text = f.read()

    cleaned_lines = clean_text_lines(text)

    df = pd.DataFrame({
        "line_number": range(1, len(cleaned_lines) + 1),
        "content": cleaned_lines
    })

    csv_path = os.path.join(OUTPUT_DIR, txt_file.replace(".txt", ".csv"))
    df.to_csv(csv_path, index=False)

    print(f"Structured data saved to {csv_path}")
    print(df.head())

if __name__ == "__main__":
    main()
