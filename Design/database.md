# Design — Database

> **Status: kerangka spesifikasi data reusable yang disetujui.** Pilihan penyimpanan, teknologi, versi, dan target mengikuti kebutuhan proyek. Tidak mewajibkan SQL, PostgreSQL, ORM, atau database server. Tandai bagian tidak relevan beserta alasannya; placeholder bukan keputusan teknis.

## Peran dokumen
Simpan hasil rancangan data di sini; instruksi peran ada di `Agents/database.md`. Ikuti tujuan `Design/Design.md` dan keputusan Architect. Backend merujuk detail data di dokumen ini, bukan membuat salinan skema yang berbeda.

## 1. Pilihan penyimpanan
- DBMS/versi atau mekanisme penyimpanan: [belum ditentukan]
- Alasan pemilihan, batasan, dan rujukan riset/keputusan: [belum ditentukan]

## 2. Model dan kamus data
- Entitas dan hubungan (diagram bila membantu): [belum ditentukan]

| Entitas/field | Makna | Tipe | Satuan | Boleh kosong/default | Sensitivitas |
|---|---|---|---|---|---|

## 3. Integritas data
- Keunikan, referensi, validasi, dan mekanisme penjaganya: [belum ditentukan]
- Perilaku saat update/hapus dan dampaknya pada data terkait: [belum ditentukan]
- Tipe data saja belum tentu menjaga seluruh aturan bisnis; tentukan constraint atau mekanisme setara sesuai teknologi.

## 4. Pola akses dan performa
- Query/pola akses utama dan perkiraan volume: [belum ditentukan]
- Indeks/optimasi beserta alasan bila diperlukan: [belum ditentukan]
- Target, kondisi, dan cara pengukuran performa: [belum ditentukan]

## 5. Konsistensi dan akses
- Batas transaksi, konkurensi, dan konsistensi: [belum ditentukan]
- Hak akses dan pemisahan data pengguna/tenant bila relevan: [belum ditentukan]
- Rujukan aturan akses operasional: `Rules/Rules.md`; jangan menyimpan kredensial di sini.

## 6. Siklus hidup dan pemulihan
- Retensi, penghapusan, dan perlindungan data sensitif: [belum ditentukan]
- Sumber skema/migrasi berversi dan kompatibilitas aplikasi: [belum ditentukan]
- Strategi pemulihan perubahan/migrasi: [belum ditentukan]
- Backup dan pemeriksaan restore sesuai kebutuhan: [belum ditentukan]
- Skema/migrasi harus dapat dilacak, direview, dan diuji sebelum diterapkan sesuai izin proyek.

## 7. Kriteria penerimaan
- Pemeriksaan integritas, hak akses, migrasi, dan pemulihan yang wajib diverifikasi QA: [belum ditentukan]
- Rujukan hasil/bukti QA: [belum tersedia]

## Referensi kerangka
- PostgreSQL, Constraints (contoh DBMS, bukan pilihan wajib): https://www.postgresql.org/docs/current/ddl-constraints.html
- PostgreSQL, Data Types: https://www.postgresql.org/docs/current/datatype.html
- AWS, Codify Data Operations: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.3-codify-data-operations.html