Here is the `README.md` file in markdown format:

```markdown
# Auto-CheatSheet

Automate the creation of high-resolution, customizable cheatsheets from multiple PDFs. This tool processes PDF documents, dynamically arranges pages into a cheatsheet format, and allows users to customize the cheatsheet settings. Ideal for students creating compact study aids or professionals summarizing key documents.

---

## Features
- **Dynamic Page Arrangement:** Automatically adjusts page size and layout to fit the entire cheatsheet.
- **Customizable Settings:** Specify paper size, margins, image resolution (DPI), and more.
- **High Resolution:** Extracts and processes PDF pages at high DPI for clear, readable content.
- **Supports Multiple PDFs:** Merge pages from multiple documents into a single cheatsheet.

---

## Requirements
- Python 3.8 or higher
- Install the necessary libraries:
  - `pymupdf` (PyMuPDF)
  - `Pillow`
  - `tqdm`

You can install all required dependencies using:
```bash
pip install -r requirements.txt
```

---

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/auto-cheatsheet.git
   cd auto-cheatsheet
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure your input PDFs are placed in the `input` directory.

4. The generated cheatsheet will be saved in the `output` directory.

---

## Steps to Run the Code

1. **Basic Usage:**
   Run the script with default settings:
   ```bash
   python main.py
   ```
   - Default paper size: A4
   - Default DPI: 600
   - Default image size: 200x200 pixels
   - Default output file: `output/cheatsheet.pdf`

2. **Customize Paper Size:**
   Specify a standard paper size (e.g., A3):
   ```bash
   python main.py --paper_size A3
   ```

   Use a custom paper size by specifying width and height in pixels:
   ```bash
   python main.py --paper_size custom --custom_paper_size 5000 7000
   ```

3. **Change Image Size:**
   Specify the size of each page in the cheatsheet:
   ```bash
   python main.py --image_size 300 300
   ```

4. **Adjust DPI for Higher Resolution:**
   Increase DPI to enhance the clarity of text and images:
   ```bash
   python main.py --dpi 1200
   ```

5. **Add Margins Between Pages:**
   Adjust the margin between pages in pixels:
   ```bash
   python main.py --margin 20
   ```

6. **Combine Multiple Customizations:**
   Combine multiple options to create a highly customized cheatsheet:
   ```bash
   python main.py --paper_size custom --custom_paper_size 4000 6000 --image_size 250 250 --dpi 1200 --margin 15
   ```

---

## Example Workflow
1. Place your PDF files in the `input` directory.
2. Run the script with desired settings:
   ```bash
   python main.py --paper_size A3 --dpi 1200 --margin 10
   ```
3. Check the `output` directory for the generated cheatsheet:
   ```bash
   output/cheatsheet.pdf
   ```

---

## Troubleshooting
- **Blurry Images:**
  Increase the DPI using the `--dpi` option (e.g., `--dpi 1200` or `--dpi 2000`).
- **Too Many Pages:**
  If all pages don’t fit on one cheatsheet, consider using a larger paper size (e.g., A3 or custom).
- **Memory Errors:**
  High DPI can consume significant memory. Lower the DPI (e.g., `--dpi 600`) or process fewer PDFs at a time.

---

## Contributing
Contributions are welcome! Please open an issue or submit a pull request to suggest improvements.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
```

Copy and paste this content into your `README.md` file. Let me know if you need further adjustments!
