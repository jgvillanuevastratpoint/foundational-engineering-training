import argparse
import os
from pathlib import Path

from docx import Document
from docx.document import Document as _Document
from docx.oxml.table import CT_Tbl
from docx.oxml.text.paragraph import CT_P
from docx.table import Table
from docx.text.paragraph import Paragraph

W_NS = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def iter_block_items(doc):
    """Yield Paragraph and Table objects in document (or cell) order."""
    parent = doc.element.body
    for child in parent.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, doc)
        elif isinstance(child, CT_Tbl):
            yield Table(child, doc)


def _indent_level(p):
    """Return list indentation depth for a paragraph based on its ind attribute."""
    pPr = p._p.pPr
    if pPr is None:
        return 0
    ind = pPr.find(f"{W_NS}ind")
    if ind is None:
        return 0
    left = ind.get(f"{W_NS}left")
    if left is None:
        return 0
    try:
        return int(left) // 360
    except ValueError:
        return 0


def render_runs(p):
    """Render a paragraph's text with inline bold/italic markers."""
    parts = []
    for run in p.runs:
        text = run.text
        if not text:
            continue
        if run.bold and run.italic:
            parts.append(f"***{text}***")
        elif run.bold:
            parts.append(f"**{text}**")
        elif run.italic:
            parts.append(f"*{text}*")
        else:
            parts.append(text)
    return "".join(parts)


def render_paragraph(p):
    """Render a paragraph to one or more markdown lines, or None if empty."""
    style = p.style.name if p.style else ""

    if style.startswith("Heading") or style in ("Title", "Subtitle"):
        if style == "Title":
            return "# " + p.text.strip()
        if style == "Subtitle":
            return "## " + p.text.strip()
        try:
            level = int(style.split()[-1])
        except ValueError:
            level = 2
        return "#" * min(level, 6) + " " + p.text.strip()

    if not p.text.strip():
        return ""

    pPr = p._p.pPr
    if pPr is not None and pPr.numPr is not None:
        indent = _indent_level(p)
        return "  " * indent + "- " + p.text.strip()

    return render_runs(p)


def _cell_text(cell):
    return cell.text.strip().replace("|", "\\|").replace("\n", "<br>")


def render_table(table):
    """Render a table to markdown pipe lines."""
    if not table.rows:
        return []
    header = [_cell_text(c) for c in table.rows[0].cells]
    width = len(header)
    lines = ["| " + " | ".join(header) + " |"]
    lines.append("|" + "|".join("---" for _ in range(width)) + "|")
    for row in table.rows[1:]:
        cells = [_cell_text(c) for c in row.cells]
        while len(cells) < width:
            cells.append("")
        lines.append("| " + " | ".join(cells) + " |")
    return lines


def convert_docx_to_md(docx_path, out_dir=None):
    """Convert a .docx file to markdown.

    Returns the path of the written .md file.
    """
    docx_path = Path(docx_path)
    doc = Document(docx_path)

    lines = []
    for block in iter_block_items(doc):
        if isinstance(block, Table):
            lines.extend(render_table(block))
            lines.append("")
            continue

        rendered = render_paragraph(block)
        if rendered == "":
            lines.append("")
        elif rendered is not None:
            lines.append(rendered)
            lines.append("")

    text = "\n".join(lines).strip() + "\n"

    out_dir = Path(out_dir) if out_dir else docx_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    base = docx_path.stem
    if base.endswith(".md"):
        base = base[:-3]
    out_path = out_dir / (base + ".md")
    out_path.write_text(text, encoding="utf-8")
    return out_path


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Convert a .docx file to markdown."
    )
    parser.add_argument("file", help="Path to the .docx file")
    parser.add_argument(
        "--out-dir",
        help="Directory for the output .md file (defaults to the docx's directory)",
    )
    args = parser.parse_args(argv)

    if not args.file.lower().endswith(".docx"):
        parser.error("input file must be a .docx file")

    out_path = convert_docx_to_md(args.file, args.out_dir)
    print(f"Converted: {args.file} -> {out_path}")


if __name__ == "__main__":
    main()
