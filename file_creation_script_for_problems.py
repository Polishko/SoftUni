import os
import re
from docx import Document
# docx: Python library (python-docx) for working with Microsoft Word documents (.docx).
# Document: a class inside the docx library, used to read, modify, and create Word documents.

def extract_titles_from_docx(docx_path):
    """
    Extracts numbered problem titles from a Word document.
    Assumes titles follow a format like '1. Problem Title', '2. Another Title'.
    """
    titles = []
    try:
        doc = Document(docx_path)
        for para in doc.paragraphs:
            match = re.match(r"^\d+\.\s*(.+)$", para.text)  # Matches "1. Problem Title"
            if match:
                title = match.group(1).strip()
                titles.append(title)
    except Exception as e:
        print(f"Error reading document: {e}")
    return titles

def create_files_from_titles(directory, titles, extension="py"):
    """
    Creates empty files using extracted titles.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    for index, title in enumerate(titles, start=1):
        safe_title = re.sub(r"[^\w\d]+", "_", title)  # Replace special characters (non-word chars not allowed in file names)
        file_name = f"problem_{index}_{safe_title}.{extension}"
        file_path = os.path.join(directory, file_name)
        
        with open(file_path, "w") as f:
            f.write(f"# {title}\n")  # Adds title as a comment in the file
        
        print(f"Created: {file_path}")

# --- User Input ---
docx_path = input("Enter the path to the Word document: ")
output_dir = input("Enter the output directory for the files: ")
file_extension = input("Enter the file extension (e.g., py, txt, md): ")

# --- Processing ---
titles = extract_titles_from_docx(docx_path)

if titles:
    create_files_from_titles(output_dir, titles, file_extension)
    print("\nFile creation complete!")
else:
    print("\nNo problem titles found in the document.")
