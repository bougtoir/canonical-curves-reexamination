# Reference audit — FINAL (Evidence & Policy)

## Format compliance (Bristol University Press Harvard)

All 29 entries follow: `Author, A, year, Title, Journal vol, issue,
pages, https://doi.org/…` — no `&` in lists (and in text citations),
no access dates, DOI/URL last. Spot-verified in rendered PDF (page 18
of manuscript PDF): entries for Cairney 2016, Cartwright and Hardie
2012, Cook 1977, Draper 1995, ICRP 2007, Lempert and Collins 2007 etc.
all conform.

## Citedness

`check_manuscript.py` `reference_citation_notes`: all references have a
matching in-text author–year token (Harvard-style `, year,` fallback
added for paren-less format). Zero uncited references after removal of
Weimer and Vining (2017), which the retargeted text no longer cited.

## Link verification (from check report)

- Crossref 200: 10.1257/jel.20191450; 10.1198/jasa.2009.ap08746;
  10.1111/ajps.12116; 10.1162/003355304772839588; 10.1177/0049124104268644;
  10.1057/978-1-137-51781-4; 10.1080/00401706.1977.10489493;
  10.1111/j.2517-6161.1995.tb02015.x; 10.1016/j.icrp.2007.10.003;
  10.1111/j.1539-6924.2007.00940.x; 10.1186/1472-6963-14-2;
  10.1007/s11077-016-9263-z; 10.3982/ECTA19402; 10.1039/C2EE22019A;
  10.3390/su5030955; 10.1332/174426409X463811.
- URL 200: pref.fukushima report; kslegislature HB2117; e-stat (2);
  ljworld Laffer article; UNSCEAR 2013 report; reconstruction.go.jp.
- URL 403 (bot-blocked, resolve fine in browser): heritage.org Laffer
  report; iris.who.int WHO 2013 — retained, both canonical documents.

## New vs removed (vs JCPA package)

- Added (evidence-use literature): Nutley, Walter and Davies (2007);
  Oliver et al. (2014); Cartwright and Hardie (2012); Ward, House and
  Hamer (2009, Evidence & Policy).
- Removed (comparative-methods apparatus): Bennett and Howlett (1992);
  Dolowitz and Marsh (2000); Freeman (2006); George and Bennett (2005);
  Hall (1993); Przeworski and Teune (1970); Rose (1991); Weimer and
  Vining (2017).
- Net list length: 29 references.

## Verdict

PASS. Format conforms to BUP Harvard; every reference cited; all
resolvable links verified.
