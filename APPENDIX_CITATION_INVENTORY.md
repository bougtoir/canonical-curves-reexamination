# Appendix citation inventory (JCPA)

| Cited identifier | Manuscript location (text_jcpa.py) | Variant used | Item exists | Source | First citation | Order |
| --- | --- | --- | --- | --- | --- | --- |
| Appendix Table A1 | Case 1 design ("exclusions ... reported in Appendix Table A1") | "Appendix Table A1" | YES (tab_a1) | fukushima/results/dropped_units.csv → build_manuscript.table_data | Case 1, data/design | 1st appendix citation |
| Appendix Table A2 | Case 1, SC robustness ("synthetic-control results are reported in Appendix Table A2") | "Appendix Table A2" | YES (tab_a2) | fukushima/results/sc_unit_summary.csv | Case 1, robustness | 2nd |
| Appendix Figure A1 | Case 2, robustness ("neighboring-state event studies assess sensitivity (Appendix Figure A1)") | "Appendix Figure A1" | YES (fig_a1) | kansas neighboring-state event-study outputs → figures/figure_A1.png | Case 2 | 3rd |

- No other Appendix/Supplementary variants ("Supplementary Figure/Table",
  "Fig. A1", "Table A3"…) occur anywhere in the manuscript (grep over
  rendered text).
- Citation order A1 → A2 → A1(fig) matches Appendix presentation order
  Table A1, Table A2, Figure A1.
- All cited items now physically embedded in the main manuscript DOCX
  (Appendix section after References).
