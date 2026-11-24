from pathlib import Path
import sys
p = Path('android/app/src/main/AndroidManifest.xml')
if not p.exists():
    raise SystemExit('AndroidManifest.xml tidak ditemukan')
s = p.read_text()
permissions = '''    <uses-permission android:name="android.permission.CAMERA" />\n    <uses-feature android:name="android.hardware.camera" android:required="false" />\n    <uses-feature android:name="android.hardware.camera.front" android:required="false" />\n'''
if 'android.permission.CAMERA' not in s:
    s = s.replace('<application', permissions + '    <application', 1)
if 'android:usesCleartextTraffic' not in s:
    s = s.replace('<application', '<application android:usesCleartextTraffic="false"', 1)
p.write_text(s)
