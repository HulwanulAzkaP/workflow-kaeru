# Rules — Aturan Proyek

> **Status: kerangka workflow reusable yang disetujui.** Nilai dan aturan khusus proyek diisi saat proyek baru dimulai. Placeholder kosong bukan izin atau persetujuan operasional.

## Cara menggunakan
Tulis aturan singkat, spesifik, dan dapat diperiksa. Rujuk dokumen otoritatif daripada menduplikasi isinya. Kemampuan teknis mengakses suatu target tidak otomatis memberi izin untuk bertindak.

## 1. Cakupan kerja
- Folder/komponen yang termasuk cakupan: [belum ditentukan]
- Lingkungan/target yang boleh diakses: [belum ditentukan]
- Batas perubahan dan area di luar cakupan: [belum ditentukan]

## 2. Standar implementasi
- Konvensi kode dan pemeriksaan otomatis: [belum ditentukan]
- Rujukan struktur/desain: `Design/Design.md` dan dokumen rinci terkait.
- Kebijakan pemilihan/perubahan dependency: [belum ditentukan]
- Prinsip implementasi: ikuti `Agents/engineer.md`; keputusan arsitektur mengikuti rancangan proyek.

## 3. Keamanan dan data
- Klasifikasi serta penanganan data sensitif: [belum ditentukan]
- Penyimpanan dan penggunaan rahasia: [belum ditentukan; jangan menaruh nilainya di dokumen proyek]
- Hak akses minimum sesuai tugas: [belum ditentukan]
- Jangan mengakali pembatasan akses atau memperluas kewenangan hanya karena secara teknis memungkinkan.

## 4. Matriks izin
Isi target dan batas tindakan secara eksplisit. Jika izin belum jelas, minta keputusan sebelum tindakan terkait; jangan menafsirkan kolom kosong sebagai approval.

| Tindakan | Target/lingkungan/path | Izin (boleh / review teknis / approval user) | Pemberi persetujuan | Pemeriksaan/bukti wajib |
|---|---|---|---|---|

Persetujuan teknis tidak otomatis berarti persetujuan user untuk deploy atau tindakan destruktif; ikuti matriks yang disepakati.

## 5. Validasi dan penerimaan
- Pemeriksaan wajib dan cara menjalankannya: [belum ditentukan]
- Cakupan/platform/lingkungan uji: [belum ditentukan]
- Standar pengujian dan keputusan QA: `Agents/qa.md`.
- Gerbang review teknis: `Agents/tech_lead.md`.
- Status tugas dan bukti terkait: `Plan/Todo.md`; tugas selesai hanya setelah QA lulus.

## 6. Perubahan aturan
- Pihak yang berwenang menyetujui perubahan aturan: [belum ditentukan]
- Catat alasan, persetujuan, kapan mulai berlaku, dan aturan lama yang digantikan.
- Jika aturan bertentangan atau kewenangan belum jelas, minta keputusan main window/user; jangan mengubah aturan untuk membenarkan tindakan sendiri.

| Aturan/perubahan | Alasan | Disetujui oleh/rujukan | Mulai berlaku | Menggantikan |
|---|---|---|---|---|

## Referensi kerangka
- GitHub, Custom Instructions: https://docs.github.com/enterprise-cloud@latest/copilot/concepts/prompting-and-context/custom-instructions
- OWASP, Authorization: https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html