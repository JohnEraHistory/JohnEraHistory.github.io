from pathlib import Path

def list_pdf_files(directory):
    # Create a Path object for the specified directory
    dir_path = Path(directory)
    
    # Use the rglob method to recursively find all PDF files
    pdf_files = dir_path.rglob('*.pdf')
    
    # Iterate over the generator and print each file path
    for pdf in pdf_files:
        print(pdf)

# Example usage:
directory_path = 'source\\articles\\pdfs'
list_pdf_files(directory_path)
