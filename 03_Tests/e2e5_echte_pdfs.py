# Test mit echten PDFs (Word, Firmen-PDFs). Aufruf:
#   python e2e5_echte_pdfs.py eingabe.pdf ausgabe.pdf '[["#mLine","Suchtext","Neuer Text"],["#mPara","Absatzanfang","Neuer Absatz"]]'
import sys, json, os, pathlib
from playwright.sync_api import sync_playwright
EDITOR = pathlib.Path(__file__).resolve().parent.parent / '01_Programm' / 'LAGZERO-PDF-Editor.html'
f, out = sys.argv[1], sys.argv[2]; jobs = json.loads(sys.argv[3])
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={'width':1300,'height':1000}, accept_downloads=True)
    logs = []; pg.on('pageerror', lambda e: logs.append('PAGEERR ' + str(e)))
    pg.goto(EDITOR.as_uri()); pg.set_input_files('#file', f)
    pg.wait_for_selector('.ln', timeout=60000); pg.wait_for_timeout(1500)
    for mode, find, new in jobs:
        pg.click(mode); el = pg.locator('.ln', has_text=find).first; el.scroll_into_view_if_needed(); el.click()
        pg.keyboard.press('Control+A'); pg.keyboard.type(new); pg.wait_for_timeout(300)
        print('SCHRIFT', find, '->', pg.inner_text('#fontChip'))
    with pg.expect_download() as d: pg.click('#save')
    d.value.save_as(out); pg.wait_for_timeout(500)
    print('STATUS', pg.inner_text('#status')); print('WARNUNG', pg.inner_text('#mWarn'))
    print('\n'.join(logs)); b.close()
