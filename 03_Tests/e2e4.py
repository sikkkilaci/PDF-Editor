from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(accept_downloads=True, viewport={'width':1200,'height':900})
    errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('file:///home/claude/LAGZERO-PDF-Editor.html'); pg.set_input_files('#file','test.pdf'); pg.wait_for_selector('.ln'); pg.wait_for_timeout(500)
    pg.locator('.ln',has_text='Kunde').first.click(); pg.keyboard.type(' X')            # edit then undo
    pg.click('#undo'); print('after undo eds:', pg.locator('.ed').count(), 'hidden lines:', pg.locator('.ln[hidden]').count())
    pg.click('#mAdd'); box=pg.locator('.page').first.bounding_box()
    pg.mouse.click(box['x']+300, box['y']+620); pg.keyboard.type('Neu: Unterschrift Müller'); pg.wait_for_timeout(200)
    print('CHIP:',pg.inner_text('#fontChip'))
    print(pg.evaluate("()=>__lz.edits.map(e=>({t:e.type,txt:e.el.innerText,x:e.x,y:e.y,info:e.info&&e.info.raw,res:e.res&&e.res.kind}))"))
    with pg.expect_download() as d: pg.click('#save')
    d.value.save_as('out4.pdf'); pg.wait_for_timeout(300); pg.screenshot(path='hdr.png',clip={'x':900,'y':0,'width':300,'height':100})
    print('ERR',errs)
    b.close()
