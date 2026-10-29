# Todo — Daftar Kerja Aktif

> Catat pekerjaan yang perlu dilakukan agent/AI. Perbarui setelah setiap pekerjaan selesai atau revisi. Jangan tandai selesai sebelum QA lulus.

## Status
- `Akan dikerjakan`
- `Sedang dikerjakan`
- `Menunggu QA`
- `Menunggu review teknis`
- `Perlu revisi` — rujuk temuan QA/Tech Lead dan tugas perbaikannya.
- `Terblokir` — tulis penyebab, dependensi/keputusan yang diperlukan, dan penanggung jawab tindak lanjut.
- `Selesai` — QA lulus dan gerbang persetujuan Tech Lead yang berlaku sudah dipenuhi untuk versi pekerjaan yang sama.
- Temuan `Issue`/`Bug` dicatat pada item terkait beserta tindak lanjut; bukan status selesai.

## Gerbang QA dan Tech Lead
- Untuk implementasi yang sudah lulus QA tetapi belum mendapat persetujuan teknis yang diwajibkan, gunakan `Menunggu review teknis`, bukan `Selesai`.
- Catat keputusan Tech Lead (`Disetujui`, `Perlu revisi`, atau `Terblokir`) beserta rujukan dan identitas versi/artefak yang ditinjau.
- Ikuti gerbang tahap di dokumen fase; persetujuan rencana/desain tidak sama dengan persetujuan implementasi. Jangan menganggap gate teknis tidak berlaku tanpa dasar yang jelas pada aturan/fase proyek.
- Perubahan setelah review perlu penilaian ulang sesuai dampaknya; persetujuan lama bukan bukti untuk versi baru. QA tetap wajib untuk penutupan tugas.

## Pekerjaan
| ID | Tugas / kriteria penerimaan | Penanggung jawab (agent) | Status | Dikerjakan | QA dicek / hasil / bukti versi | Tech Lead / keputusan / rujukan versi | Fase / Revisi terkait | Issue found | Bug found | Catatan |
|---|---|---|---|---|---|---|---|---|---|---|

Rujuk fase melalui path file, serta revisi melalui nomor dan path `Revision/Revision(N).md` yang sudah dinomori. Gunakan `—` bila tidak ada revisi terkait; jangan membuat revisi fiktif atau menyalin status pelaksanaan ke banyak dokumen.

## Issue / bug terbuka
| ID terkait | Temuan | Dampak/prioritas | Penanggung jawab | Tindak lanjut/status |
|---|---|---|---|---|

## Riwayat pembaruan
| Tanggal | Perubahan Todo | Alasan/rujukan |
|---|---|---|