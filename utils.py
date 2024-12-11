import fitz  # PyMuPDF
from PIL import Image, ImageChops

def process_pdfs(pdf_files, dpi=600):
    """Extract and process pages from the given PDF files."""
    processed_pages = []
    for pdf in pdf_files:
        doc = fitz.open(pdf)
        for page_num in range(len(doc)):
            pix = doc[page_num].get_pixmap(dpi=dpi)  # Extract at high DPI
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            cropped_img = crop_white_borders(img)
            processed_pages.append(cropped_img)
    return processed_pages

def crop_white_borders(image):
    """Remove excess white borders from an image."""
    grayscale = image.convert("L")
    bbox = grayscale.getbbox()
    return image.crop(bbox)

def generate_cheatsheet(images, output_file, paper_size, margin=10):
    """
    Arrange images into a cheatsheet dynamically based on the number of pages
    while keeping margins constant and adjusting page size.
    """
    if not images:
        print("No images to arrange.")
        return

    # Unpack paper size dimensions
    sheet_width, sheet_height = paper_size

    total_pages = len(images)

    # Determine the optimal grid size (rows x cols)
    cols = int((total_pages ** 0.5) * (sheet_width / sheet_height) ** 0.5)
    rows = (total_pages + cols - 1) // cols  # Round up to fit all pages

    # Calculate available space for images after accounting for margins
    available_width = sheet_width - margin * (cols + 1)
    available_height = sheet_height - margin * (rows + 1)

    # Compute dynamic image size
    image_width = available_width // cols
    image_height = available_height // rows

    # Create a blank canvas for the cheatsheet
    cheatsheet = Image.new("RGB", (sheet_width, sheet_height), "white")

    # Arrange images dynamically on the cheatsheet
    for i, img in enumerate(images):
        x = (i % cols) * (image_width + margin) + margin
        y = (i // cols) * (image_height + margin) + margin
        resized_img = img.resize((image_width, image_height), Image.LANCZOS)
        cheatsheet.paste(resized_img, (x, y))

    # Save to PDF
    cheatsheet.save(output_file, "PDF")
    print(f"Cheatsheet saved to {output_file}")