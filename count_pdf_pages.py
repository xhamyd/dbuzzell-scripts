from pathlib import Path
from pypdf import PdfReader


def get_pdf_page_count(pdf_file_path):
    """
    Counts the number of pages in a PDF file.

    Args:
        pdf_file_path (Path): Path to the PDF file.

    Returns:
        int: Number of pages in the PDF file.
    """
    try:
        reader = PdfReader(pdf_file_path)
        return len(reader.pages)
    except Exception as e:
        print(f"Error processing {pdf_file_path}: {e}")
        return 0


def count_pages_in_directory(directory_path):
    """
    Counts the number of pages in all PDF files within a directory.

    Args:
        directory_path (Path): Path to the directory containing PDF files.

    Returns:
        dict: A dictionary where keys are PDF file paths and values are page counts.
    """
    pdf_files = directory_path.glob("*.pdf")
    return {
        pdf_file: get_pdf_page_count(pdf_file) for pdf_file in pdf_files
    }


if __name__ == "__main__":
    directory_path = Path(r"C:\Users\xhamy\Desktop\Kellogg\Clubs & Social\Kellogg Bands\Sheet Music")  # Replace with your directory path

    if not directory_path.is_dir():
        print(f"Error: Directory '{directory_path}' not found.")
    else:
        pdf_page_counts = count_pages_in_directory(directory_path)

        if pdf_page_counts:
            for pdf_file, page_count in pdf_page_counts.items():
                print(f"{pdf_file}: {page_count} pages")
            total_pages = sum(pdf_page_counts.values())
            print(f"Total pages in all PDFs: {total_pages}")
        else:
            print("No PDF files found in the directory.")
