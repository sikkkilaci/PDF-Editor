// LAGZERO PDF Editor – Windows-App (Electron)
const { app, BrowserWindow, shell, session, Menu } = require('electron');
const path = require('path');
const fs = require('fs');

let win = null;
const pdfArg = argv => argv.slice(1).find(a => /\.pdf$/i.test(a) && fs.existsSync(a));

function openPdf(file){
  if (!win || !file) return;
  try {
    const b64 = fs.readFileSync(file).toString('base64');
    win.webContents.executeJavaScript(`window.__lzOpenBytes(${JSON.stringify(path.basename(file))}, ${JSON.stringify(b64)})`);
  } catch (e) { console.error(e); }
}

function create(){
  Menu.setApplicationMenu(null);
  win = new BrowserWindow({
    width: 1400, height: 950, minWidth: 900, minHeight: 600,
    title: 'LAGZERO PDF Editor', backgroundColor: '#050609',
    icon: path.join(__dirname, 'build', 'icon.png'),
    webPreferences: { contextIsolation: true, nodeIntegration: false, sandbox: true, spellcheck: false }
  });
  // Installierte Schriften (Local Font Access) und Kopieren in die Zwischenablage (Fehlerbericht) erlauben, alles andere nicht
  const ses = session.defaultSession;
  const allowed = new Set(['local-fonts', 'clipboard-sanitized-write']);
  ses.setPermissionRequestHandler((wc, perm, cb) => cb(allowed.has(perm)));
  ses.setPermissionCheckHandler((wc, perm) => allowed.has(perm));
  // Speichern: Windows-Dialog „Speichern unter“ (Electron zeigt ihn automatisch)
  ses.on('will-download', (e, item) => {
    const zip = /\.zip$/i.test(item.getFilename());
    item.setSaveDialogOptions(zip
      ? { title: 'Fehlerbericht speichern', filters: [{ name: 'ZIP-Archiv', extensions: ['zip'] }] }
      : { title: 'Bearbeitetes PDF speichern', filters: [{ name: 'PDF', extensions: ['pdf'] }] });
  });
  // Links (Discord) im normalen Browser öffnen, nie in der App
  win.webContents.setWindowOpenHandler(({ url }) => { if (/^https?:/.test(url)) shell.openExternal(url); return { action: 'deny' }; });
  win.webContents.on('will-navigate', (e, url) => { if (!url.startsWith('file:')) { e.preventDefault(); if (/^https?:/.test(url)) shell.openExternal(url); } });
  win.loadFile(path.join(__dirname, 'app', 'editor.html'));
  win.webContents.once('did-finish-load', () => openPdf(pdfArg(process.argv)));
}

if (!app.requestSingleInstanceLock()) app.quit();
else {
  app.on('second-instance', (e, argv) => { if (win){ if (win.isMinimized()) win.restore(); win.focus(); openPdf(pdfArg(argv)); } });
  app.whenReady().then(create);
  app.on('window-all-closed', () => app.quit());
}
