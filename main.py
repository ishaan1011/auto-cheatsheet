import os
import argparse
from utils import process_pdfs, generate_cheatsheet

# Predefined paper sizes
PAPER_SIZES = {
    "A4": (2480, 3508),  # 8.3 x 11.7 inches at 300 DPI
    "A3": (3508, 4961),  # 11.7 x 16.5 inches at 300 DPI
}

def parse_args():
    """Parse command-line arguments for customization."""
    parser = argparse.ArgumentParser(description="Generate a cheatsheet from PDF files.")
    parser.add_argument("--input_dir", type=str, default="input", help="Directory containing input PDF files.")
    parser.add_argument("--output_file", type=str, default="output/cheatsheet.pdf", help="Path to save the cheatsheet.")
    parser.add_argument("--paper_size", type=str, choices=list(PAPER_SIZES.keys()) + ["custom"], default="A4",
                        help="Paper size for the cheatsheet.")
    parser.add_argument("--custom_paper_size", type=int, nargs=2, metavar=("WIDTH", "HEIGHT"),
                        help="Custom paper size in pixels (width height).")
    parser.add_argument("--dpi", type=int, default=600, help="Resolution of extracted images in DPI.")
    parser.add_argument("--margin", type=int, default=10, help="Margin between images on the cheatsheet.")
    return parser.parse_args()

def main():
    args = parse_args()

    # Resolve paper size
    if args.paper_size == "custom":
        if args.custom_paper_size:
            paper_size = tuple(args.custom_paper_size)
        else:
            raise ValueError("Custom paper size must be specified with --custom_paper_size.")
    else:
        paper_size = PAPER_SIZES[args.paper_size]

    # Ensure output directory exists
    os.makedirs(os.path.dirname(args.output_file), exist_ok=True)

    # List all PDFs in the input directory
    pdf_files = [os.path.join(args.input_dir, f) for f in os.listdir(args.input_dir) if f.endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in the input directory.")
        return

    # Process the PDFs
    processed_pages = process_pdfs(pdf_files, dpi=args.dpi)

    # Generate the cheatsheet
    generate_cheatsheet(processed_pages, args.output_file, paper_size, margin=args.margin)
    print(f"Cheatsheet created: {args.output_file}")

if __name__ == "__main__":
    main()