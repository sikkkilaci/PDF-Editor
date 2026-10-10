const { _electron } = require('playwright-core'); const fs = require('fs');
(async () => {
  const app = await _electron.launch({ executablePath: '/root/app/node_modules/electron/dist/electron', args: ['--no-sandbox', '/root/app', '/root/t/lo.pdf'] });
  const win = await app.firstWindow(); await win.waitForSelector('.ln', { timeout: 30000 }); await win.waitForTimeout(800);
  console.log('Titel:', await win.title(), '| Geladen per Öffnen-mit:', await win.innerText('#status'));
  await app.evaluate(({ session }) => session.defaultSession.on('will-download', (e, item) => item.setSavePath('/root/t/app_out.pdf')));
  await win.locator('.ln:visible', { hasText: 'Bescheinigung' }).first().click(); await win.keyboard.press('Control+A'); await win.keyboard.type('App-Test Bescheinigung'); await win.waitForTimeout(300);
  console.log('Schrift:', await win.innerText('#fontChip'));
  await win.click('#save'); await win.waitForTimeout(2500);
  console.log('Gespeichert:', fs.existsSync('/root/t/app_out.pdf'), '| Pop-up:', await win.isVisible('#modal'), '|', await win.innerText('#mFile'));
  await win.screenshot({ path: '/root/t/app_popup.png' });
  const n0 = app.windows().length; await win.click('#modal a.discord'); await win.waitForTimeout(800);
  console.log('Discord öffnet kein App-Fenster:', app.windows().length === n0, '| URL bleibt:', win.url().startsWith('file:'));
  await win.click('#mClose');
  console.log(await win.evaluate(async () => { try { const l = await window.queryLocalFonts(); return 'PC-Schriften-Zugriff: OK (' + l.length + ' Schriften)'; } catch (e) { return 'PC-Schriften Fehler: ' + e.message; } }));
  await win.screenshot({ path: '/root/t/app_main.png' });
  await app.close();
})().catch(e => { console.error('FEHLER', e.message); process.exit(1); });
