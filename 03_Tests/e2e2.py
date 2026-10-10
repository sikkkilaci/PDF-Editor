from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(accept_downloads=True)
    errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///home/claude/LAGZERO-PDF-Editor.html'); pg.set_input_files('#file','test2.pdf'); pg.wait_for_selector('.ln'); pg.wait_for_timeout(500)
    for src,new in [('Hallo','Wolle Hall'),('Zweite','Zweite Xylophon')]:
        pg.locator('.ln',has_text=src).first.click(); pg.keyboard.press('Control+A'); pg.keyboard.type(new); pg.wait_for_timeout(300)
        print('CHIP:',pg.inner_text('#fontChip'))
    with pg.expect_download() as d: pg.click('#save')
    d.value.save_as('out2.pdf'); pg.wait_for_timeout(300)
    print('WARN',pg.inner_text('#mWarn'), 'ERR',errs)
    pg.screenshot(path='modal.png')
    b.close()
