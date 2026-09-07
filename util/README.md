# docx2md

Convert a `.docx` file to Markdown.

## Usage

Convert a single file, output written next to the source `.docx`:

```bash
python util/docx2md.py path/to/example.docx
```

Specify a different output directory:

```bash
python util/docx2md.py path/to/example.docx --out-dir out/
```

Use as a library:

```python
from docx2md import convert_docx_to_md

out_path = convert_docx_to_md("example.docx", out_dir="out/")
```

## Install

```bash
pip install -r util/requirements.txt
```

## Features

- Headings (Title, Heading 1–6)
- Bold / italic / bold-italic inline text
- Bulleted and numbered lists (with indentation)
- Tables (rendered as GitHub-flavored Markdown pipe tables)
