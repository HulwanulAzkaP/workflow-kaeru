# Revision N — [Judul Revisi]

> **Status: kerangka revisi reusable yang disetujui.** Salin file ini saat proyek membutuhkan catatan revisi dan ganti `N` dengan nomor revisi. Ini bukan revisi produk yang sudah berjalan.

## 1. Identitas dan sumber
- Nomor/judul revisi: [belum diisi]
- Tanggal permintaan: [belum diisi]
- Peminta dan rujukan arahan: [belum diisi]

## 2. Alasan dan perubahan
- Kondisi sebelumnya: [belum diisi]
- Alasan/latar belakang: [belum diisi]
- Perubahan yang diminta: [belum diisi]
- Hasil yang diharapkan/kriteria penerimaan: [belum diisi]

## 3. Analisis dampak
- Tujuan dan scope: [belum dinilai]
- Desain/komponen/integrasi: [belum dinilai]
- Data dan migrasi: [belum dinilai]
- Dependency: [belum dinilai]
- Fase dan Todo terkait: [belum diisi]
- Biaya/sumber daya: [belum dinilai]
- Keamanan/risiko dan kebutuhan pengujian ulang: [belum dinilai]

## 4. Keputusan atas permintaan
- Status permintaan (menunggu keputusan / disetujui / perlu revisi / ditolak): [belum ditentukan]
- Alasan dan syarat keputusan: [belum diisi]
- Pihak pemberi persetujuan dan rujukan bukti: [belum diisi]
- Rujukan izin tindakan khusus: `Rules/Rules.md`.

Persetujuan permintaan revisi bukan bukti bahwa implementasi selesai, QA lulus, atau tindakan deploy/destruktif telah diizinkan. Bedakan keputusan permintaan dari hasil review implementasi di bagian penutupan.

## 5. Pelaksanaan
- Agent penanggung jawab: [belum ditentukan]
- Rujukan ID tugas di `Plan/Todo.md`: [belum tersedia]
- Rujukan fase di `Plan/Phases/`: [belum tersedia]
- Status pekerjaan terkini tetap bersumber dari Todo; jangan membuat status paralel yang bertentangan di file revisi.

### Pembagian revisi besar
- Pecah perubahan yang tidak berkaitan menjadi bagian terarah; pisahkan refactor dari fitur bila memungkinkan.
- Catat urutan/dependensi dan rujukan ID tugas atau revisi terkait: [belum ditentukan]
- Pembagian harus menjaga integrasi tetap valid. Tidak wajib membuat satu file revisi baru untuk setiap commit.

### Rencana pemulihan revisi berisiko
- Versi awal/baseline dan kondisi yang diketahui baik: [belum diisi]
- Kondisi penghentian atau pemicu pemulihan: [belum ditentukan]
- Strategi rollback atau fix-forward beserta rujukan prosedur yang relevan: [belum ditentukan]
- Dampak pemulihan terhadap data/migrasi/integrasi: [belum dinilai]
- Agent penanggung jawab, izin, dan cara memverifikasi pemulihan: [belum ditentukan]
- Jika tidak relevan, catat alasannya. Mengembalikan kode tidak otomatis memulihkan data; jangan menjanjikan rollback tanpa menilai perubahan data.
- Rujuk rencana teknis di `Design/backend.md`, `Design/database.md`, atau dokumen relevan; tidak perlu menyalin seluruh prosedur. Pelaksanaan tetap mengikuti izin `Rules/Rules.md`.

## 6. Verifikasi dan penutupan
- Identitas versi/artefak yang diperiksa: [belum tersedia]
- Hasil dan rujukan bukti QA: [belum diuji]
- Keputusan Tech Lead dan rujukannya: [belum ditinjau]
- Dokumen yang diperbarui (desain/aturan/Memory/CodeMap/riset bila terdampak): [belum tersedia]
- Risiko tersisa dan hal yang belum diverifikasi: [belum dinilai]
- Ringkasan hasil penutupan: [belum tersedia]

## Referensi kerangka
- AWS, Plan for Unsuccessful Changes: https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_mit_deploy_risks_plan_for_unsucessful_changes.html
- Google, Small Changes: https://google.github.io/eng-practices/review/developer/small-cls.html
- Google, Change Descriptions: https://google.github.io/eng-practices/review/developer/cl-descriptions.html
- AWS, Change Manager (referensi proses, bukan rekomendasi layanan): https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager.html
