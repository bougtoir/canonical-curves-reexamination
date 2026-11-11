"""
Generate a separate, editable .docx containing the manuscript tables:
  - Table 1: Summary of re-examination results (all analyzed curves)
  - Appendix A: Source metadata table

Provided as a separate editable file in addition to the inline tables in the
main manuscript. All content is read from results/ and data/ (no hard-coded
values).

Onishi T. 2026.
"""

import os
import json

import pandas as pd
from docx import Document
from docx.shared import Pt
from docx.enum.table import WD_TABLE_ALIGNMENT

from generate_manuscript_hdsr import EXCLUDED_CURVES

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(BASE_DIR, 'results')
DATA_DIR = os.path.join(BASE_DIR, 'data')


def _n_by_name():
    with open(os.path.join(RESULTS_DIR, 'full_results.json'), 'r') as f:
        return {r['name']: r['n'] for r in json.load(f)}


def create_tables():
    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(10)

    df = pd.read_csv(os.path.join(RESULTS_DIR, 'summary_table.csv'))
    total = len(df)

    doc.add_heading('Table 1. Summary of re-examination results', level=1)
    p = doc.add_paragraph(
        f"Complete results for all {total} analyzed curves. p (full) = nested "
        f"F-test with all data; p (clean) = after removing the top three Cook's "
        f"distance points.")
    p.paragraph_format.space_after = Pt(6)

    table = doc.add_table(rows=1, cols=7)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(
            ['#', 'Curve', 'N', 'p (full)', 'p (clean)', 'BIC best', 'Verdict']):
        cell = table.rows[0].cells[i]
        cell.text = h
        cell.paragraphs[0].runs[0].bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(9)
    for idx, row in df.iterrows():
        rc = table.add_row().cells
        rc[0].text = str(idx + 1)
        rc[1].text = str(row['Curve'])
        rc[2].text = str(row['N'])
        pf = row['p (full)']
        rc[3].text = f"{pf:.4f}" if pd.notna(pf) and pf > 0.0001 else (
            f"{pf:.1e}" if pd.notna(pf) else "n/a")
        pc = row['p (clean)']
        rc[4].text = f"{pc:.4f}" if pd.notna(pc) and pc > 0.0001 else (
            f"{pc:.1e}" if pd.notna(pc) else "n/a")
        rc[5].text = str(row['BIC best'])
        rc[6].text = str(row['Verdict']).replace('_', ' ')
        for cell in rc:
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.size = Pt(9)

    doc.add_page_break()
    doc.add_heading('Appendix A. Source metadata table', level=1)
    n_excluded = len(EXCLUDED_CURVES)
    inventory = total + n_excluded
    p = doc.add_paragraph(
        f"Source information for all {inventory} inventoried curves. The "
        f"{n_excluded} curves that could not be backed by a traceable dataset "
        f"(the Yerkes-Dodson and Weber-Fechner laws) are shown with a dash for "
        f"sample size and marked 'Excluded'; the remaining {total} are the "
        f"analyzed set.")
    p.paragraph_format.space_after = Pt(6)

    source_meta_path = os.path.join(DATA_DIR, 'source_metadata.json')
    with open(source_meta_path, 'r', encoding='utf-8') as f:
        sources = json.load(f)
    n_by_name = _n_by_name()
    combined = list(sources) + [dict(c, excluded=True) for c in EXCLUDED_CURVES]

    table = doc.add_table(rows=1, cols=6)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(
            ['#', 'Curve', 'Original paper', 'Data source', 'N',
             'Claimed form']):
        cell = table.rows[0].cells[i]
        cell.text = h
        cell.paragraphs[0].runs[0].bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(8)
    for src in sorted(combined, key=lambda s: s['id']):
        rc = table.add_row().cells
        rc[0].text = str(src['id'])
        rc[1].text = src['name']
        rc[2].text = src['original_paper']
        if src.get('excluded'):
            rc[3].text = 'Excluded \u2014 no traceable dataset'
            rc[4].text = '\u2014'
        else:
            rc[3].text = src['data_source']
            n_val = n_by_name.get(src['name']) or src.get('current_n')
            rc[4].text = str(n_val) if n_val else 'WB API'
        rc[5].text = src['claimed_form']
        for cell in rc:
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.size = Pt(8)

    output_path = os.path.join(BASE_DIR, 'tables_canonical_curves_hdsr.docx')
    doc.save(output_path)
    print(f"Tables saved to: {output_path}")
    return output_path


if __name__ == "__main__":
    create_tables()
