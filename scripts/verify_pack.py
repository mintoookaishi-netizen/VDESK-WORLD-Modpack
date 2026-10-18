#!/usr/bin/env python3
"""Offline check: pack SHA256 and exactly 28 official-CDN URL/hash entries.
Does not execute mods, access network, or establish absence of malware.
"""
from pathlib import Path
from urllib.parse import urlparse
import hashlib,json,zipfile

root=Path(__file__).resolve().parent.parent
manifest=json.loads((root/'manifest.json').read_text(encoding='utf8'))
archive=root/manifest['pack']
assert hashlib.sha256(archive.read_bytes()).hexdigest()==manifest['sha256'], 'pack SHA256 mismatch'
with zipfile.ZipFile(archive) as z:
    index=json.loads(z.read('modrinth.index.json'))
assert index==json.loads((root/'modrinth.index.json').read_text(encoding='utf8')), 'index mismatch'
assert len(index['files'])==28==len(manifest['files'])
refs={x['filename']:x for x in manifest['files']}
for x in index['files']:
    path=Path(x['path'])
    assert str(path).replace('\\','/').startswith('mods/') and '..' not in path.parts
    row=refs.pop(path.name)
    assert x['hashes']['sha1']==row['sha1']
    assert x['hashes']['sha512']==row['sha512']
    assert x['downloads']==[row['download']]
    assert all(urlparse(u).scheme=='https' and urlparse(u).hostname=='cdn.modrinth.com' for u in x['downloads'])
assert not refs
print('PASS: .mrpack SHA256 / 28 entries / source URLs / hashes match.')
print('Not a malware scan. The VDESK pack is not published or reviewed within Modrinth.')
