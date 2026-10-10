// Setzt Symbol und Versionsinfo der .exe ohne Wine (resedit, reines JavaScript)
const fs = require('fs'), path = require('path');
const ResEdit = require('resedit');
exports.default = async ctx => {
  if (ctx.electronPlatformName !== 'win32') return;
  const exe = path.join(ctx.appOutDir, ctx.packager.appInfo.productFilename + '.exe');
  const PE = ResEdit.NtExecutable.from(fs.readFileSync(exe), { ignoreCert: true });
  const res = ResEdit.NtExecutableResource.from(PE);
  const ico = ResEdit.Data.IconFile.from(fs.readFileSync(path.join(__dirname, 'build', 'icon.ico')));
  ResEdit.Resource.IconGroupEntry.replaceIconsForResource(res.entries, 1, 1033, ico.icons.map(i => i.data));
  const vi = ResEdit.Resource.VersionInfo.fromEntries(res.entries)[0];
  vi.setStringValues({ lang: 1033, codepage: 1200 }, {
    ProductName: 'LAGZERO PDF Editor', FileDescription: 'LAGZERO PDF Editor', CompanyName: 'LAG|ZERØ – Adem Tasdemir',
    LegalCopyright: '© 2026 Adem Tasdemir', OriginalFilename: 'LAGZERO PDF Editor.exe', InternalName: 'LAGZERO PDF Editor' });
  const v = ctx.packager.appInfo.version.split('.').map(Number);
  vi.setFileVersion(v[0], v[1], v[2], 0); vi.setProductVersion(v[0], v[1], v[2], 0);
  vi.outputToResourceEntries(res.entries);
  res.outputResource(PE);
  fs.writeFileSync(exe, Buffer.from(PE.generate()));
  console.log('  • Symbol + Versionsinfo gesetzt:', exe);
};
