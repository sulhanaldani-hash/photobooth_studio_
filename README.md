# Photobooth Studio Android — build package

Project ini mempertahankan HTML Photobooth Studio sebagai tampilan utama dan membungkusnya dengan Capacitor untuk Android. Perubahan yang ditambahkan berfokus pada integrasi Android: deklarasi izin kamera, plugin penyimpanan/berbagi foto, dan workflow build APK.

## Build APK melalui GitHub Actions
1. Buat repository GitHub kosong.
2. Upload seluruh isi folder project ini (termasuk `.github` dan `scripts`).
3. Buka tab **Actions** → **Build Photobooth Studio APK**.
4. Pilih **Run workflow**.
5. Setelah proses berhasil, buka hasil workflow dan unduh artifact `photobooth-studio-debug-apk`.
6. Ekstrak artifact dan instal `app-debug.apk` pada perangkat Android.

## Build lokal
Persyaratan: Node.js 20+, Java 21, Android SDK.

```bash
npm install
npx cap add android
python3 scripts/patch-android-manifest.py
npx cap sync android
cd android
./gradlew assembleDebug
```

APK berada di `android/app/build/outputs/apk/debug/app-debug.apk`.

## Perubahan integrasi Android
- Izin kamera dideklarasikan pada AndroidManifest; kamera depan/belakang tidak diwajibkan agar perangkat tanpa kamera tertentu tetap dapat memasang aplikasi.
- Akses live camera menggunakan `getUserMedia` dan `enumerateDevices` dari halaman aplikasi.
- Simpan Strip menggunakan Capacitor Filesystem di Android; dialog berbagi Android dibuka bila tersedia. Di browser biasa, unduhan memakai mekanisme web seperti sebelumnya.
- Workflow mengompilasi APK debug dan mengunggahnya sebagai artifact.

## Pemeriksaan perangkat nyata yang tetap diperlukan
APK belum dinyatakan lulus pengujian pada semua merek/perangkat. Setelah build, uji izin kamera, kamera depan/belakang, pemilihan kamera, hitung mundur, pengambilan foto, simpan/bagikan hasil, orientasi portrait/landscape, tombol Back Android, dan ukuran layar HP/tablet. Perilaku kamera dapat berbeda menurut versi Android, vendor, dan kebijakan izin perangkat.

Catatan: versi ini adalah APK debug untuk pengujian/sideload, bukan APK release bertanda tangan untuk Play Store.
