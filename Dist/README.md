# Dist — Output Penyerahan

> **Status: kerangka workflow reusable yang disetujui.** Format artefak, versi, struktur subfolder, dan metode distribusi ditentukan saat proyek baru dimulai. Saat ini belum ada output produk yang dibuat atau dinyatakan siap pakai.

## Fungsi dan batas folder
- Simpan hanya output penyerahan yang benar-benar dihasilkan: aplikasi, paket, laporan, model, dataset, atau format lain sesuai proyek.
- Jangan gunakan folder ini sebagai source kerja, log sementara, atau catatan progres. Progres tetap di `Plan/Todo.md`.
- `Dist/` adalah lokasi paket penyerahan dalam kerangka workflow, bukan kewajiban mengubah folder build bawaan framework. Bedakan secara konseptual dari output build tool seperti `dist/`; hindari bergantung pada perbedaan huruf besar/kecil di filesystem yang tidak membedakannya. Lokasi build dan pengemasan ditetapkan sesuai proyek.

## 1. Artefak hasil
- Daftar artefak dan formatnya: [belum tersedia]
- Struktur subfolder bila diperlukan: [belum ditentukan sesuai proyek]
- Simpan artefak aktual, bukan placeholder yang diklaim sebagai hasil build/output.

## 2. Panduan penggunaan
- Cara membuka, menjalankan, atau menggunakan artefak: [belum tersedia]
- Prasyarat dan platform yang didukung: [belum ditentukan]
- Konfigurasi yang dibutuhkan: [belum ditentukan; jangan memasukkan kredensial atau rahasia]

## 3. Identitas versi
- Versi/identitas output: [belum tersedia]
- Rujukan source/commit atau identitas lain asal output: [belum tersedia]
- Rujukan proses build/pembuatan: [belum tersedia]

## 4. Status verifikasi
- Rujukan bukti QA untuk versi/artefak yang diserahkan: [belum diuji]
- Rujukan persetujuan Tech Lead sesuai gate proyek: [belum ditinjau]
- Cocokkan bukti dengan output aktual. Jangan memberi label siap pakai jika pemeriksaan wajib belum lulus; output yang diubah atau dibangun ulang perlu dinilai ulang sesuai dampaknya.
- Penyerahan atau persetujuan teknis tidak otomatis memberi izin publish/deploy; ikuti `Rules/Rules.md`.

## 5. Catatan penyerahan
- Ringkasan perubahan: [belum tersedia]
- Keterbatasan dan masalah yang masih diketahui: [belum dinilai]
- Rujukan revisi, dokumentasi, atau tindak lanjut terkait: [belum tersedia]

## 6. Integritas dan keaslian (bila diperlukan)
- Metode verifikasi sesuai risiko distribusi (checksum/provenance/signature): [belum ditentukan]
- Bukti/nilai verifikasi dan cara memeriksanya: [belum tersedia]
- Nilai checksum harus dihitung dari artefak aktual, bukan dikarang. Checksum saja bukan jaminan keaslian; verifikasi sumber bukti dan identitas pembuat bila dibutuhkan.

## Referensi kerangka
- GitHub, Releases: https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases
- SLSA, Artifact Verification: https://slsa.dev/spec/v1.2/verifying-artifacts

Referensi tersebut mendukung prinsip pengemasan dan verifikasi; template tidak mewajibkan GitHub, SLSA penuh, atau format rilis tertentu.
