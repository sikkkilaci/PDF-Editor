from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(accept_downloads=True, viewport={'width':1200,'height':900})
    errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///home/claude/LAGZERO-PDF-Editor.html'); pg.set_input_files('#file','test2.pdf'); pg.wait_for_selector('.ln'); pg.wait_for_timeout(500)
    pg.locator('.ln',has_text='Zweite').first.click(); pg.keyboard.press('Control+A'); pg.keyboard.type('Zweite Xylophon'); pg.wait_for_timeout(300)
    print('visible btn:', pg.is_visible('#fontFileBtn'))
    pg.locator('.ed').first.focus()
    pg.set_input_files('#fontFile','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'); pg.wait_for_timeout(500)
    print('CHIP:',pg.inner_text('#fontChip'))
    with pg.expect_download() as d: pg.click('#save')
    d.value.save_as('out3.pdf'); pg.wait_for_timeout(300)
    print('WARN',repr(pg.inner_text('#mWarn')),'ERR',errs)
    b.close()
