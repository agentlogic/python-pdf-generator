# Python PDF generator POC

## Setup

- Install dependencies: `pdfkit` and `jinja2`
- Install `wkhtmltopdf` library:
    - On MacOS, do `brew install wkhtmltopdf`
		- On Ubuntu, do `sudo apt-get install wkhtmltopdf`
		- On Windows, download from [here](https://wkhtmltopdf.org/downloads.html)
- Run the app: `python html_to_pdf.py`

## Change PDF template

To change the PDF template and styles, just update the `template.html` file.

**NOTE**: The `wkhtmltopdf` library is a pain in the ass when trying to use modern-day CSS rules, and needs
some Google-fu skills to solve a few annoying problems.
