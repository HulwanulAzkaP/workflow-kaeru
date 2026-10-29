# Design — Backend

> **Status: kerangka spesifikasi backend reusable yang disetujui.** Framework, protokol, struktur, dan target operasional ditentukan sesuai kebutuhan proyek. Template tidak mewajibkan REST/GraphQL/event, monolith/microservices, queue, atau cache.

## Peran dokumen
Simpan spesifikasi hasil desain backend di sini, bukan instruksi peran agent. Ikuti `Design/Design.md` dan keputusan Architect. Placeholder bukan keputusan implementasi.

## Modul dan aturan bisnis
- Tanggung jawab dan batas tiap modul: [belum ditentukan]
- Aturan bisnis dan kondisi valid/tidak valid: [belum ditentukan]

## Kontrak API dan integrasi
- Protokol dan sumber utama kontrak yang dirujuk frontend: [belum ditentukan]
- Request–response, validasi, format error: [belum ditentukan]
- Pagination dan kompatibilitas perubahan bila relevan: [belum ditentukan]
- Integrasi eksternal serta batas tanggung jawab: [belum ditentukan]

## Keamanan
- Autentikasi dan otorisasi per operasi/resource: [belum ditentukan]
- Pengelolaan rahasia, proteksi data sensitif, dan batas request: [belum ditentukan]
- Respons error tidak boleh membocorkan rahasia atau detail internal sensitif.

## Konsistensi data
- Batas transaksi dan perilaku saat sebagian operasi gagal: [belum ditentukan]
- Rujukan skema dan keputusan data: `Design/database.md`; jangan menduplikasi rincian skema.

## Kegagalan dan pemulihan
- Timeout panggilan dan batas retry: [belum ditentukan]
- Kebijakan backoff/jitter bila diperlukan: [belum ditentukan]
- Pencegahan efek ganda/idempotensi untuk operasi yang relevan: [belum ditentukan]
- Timeout tidak membuktikan operasi belum terjadi; retry harus mempertimbangkan efek samping dan beban layanan.

## Batas resource dan biaya (bila relevan)
- Batas ukuran payload/upload, jumlah hasil pagination, operasi batch, dan konkurensi: [belum ditentukan sesuai workload]
- Batas penggunaan layanan berbayar dan respons saat kuota tercapai: [belum ditentukan]
- Rate limit jumlah request saja bukan pengganti pembatasan biaya/resource per operasi.

## Keamanan request keluar (bila backend mengakses URL dari input)
- Tujuan, protokol, dan batas jaringan yang diizinkan: [belum ditentukan]
- Validasi tujuan dan redirect serta perlindungan akses jaringan internal/metadata cloud dari input tak tepercaya: [belum ditentukan sesuai kebutuhan]
- Rancang perlindungan SSRF sesuai konteks; jangan menganggap URL valid secara sintaks berarti tujuan aman.

## Webhook dan event (bila digunakan)
- Sumber kontrak provider serta mekanisme verifikasi keaslian: [belum ditentukan]
- Penanganan duplikasi dan pencegahan efek ganda: [belum ditentukan]
- Perilaku untuk event terlambat atau tidak berurutan: [belum ditentukan]
- Kebijakan delivery/retry mengikuti provider yang dipilih; jangan mengasumsikan urutan atau pengiriman tepat sekali tanpa jaminan yang terverifikasi.

## Operasional dan observability
- Konfigurasi lingkungan dan pemisahan rahasia: [belum ditentukan]
- Logging tanpa rahasia, health check, dan metrik kegagalan sesuai kebutuhan: [belum ditentukan]
- Target performa dan cara mengukurnya: [belum ditentukan]

## Validasi penerimaan
- Skenario integrasi, keamanan, serta performa yang wajib diverifikasi QA: [belum ditentukan]
- Rujukan bukti/hasil QA: [belum tersedia]

## Referensi kerangka
- OWASP, API Resource Consumption: https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/
- OWASP, SSRF Prevention: https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html
- Stripe, Webhooks (contoh perilaku provider, bukan kewajiban memakai Stripe): https://docs.stripe.com/webhooks
- Microsoft, API Design: https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design
- OWASP, REST Security: https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html
- AWS, Timeouts and Retries: https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/

## Teknologi, dependensi, dan keputusan
- Pilihan teknologi/dependensi beserta versi, alasan, dan rujukan keputusan Architect: [belum ditentukan sesuai proyek]
- Rujukan riset dan persetujuan: [belum tersedia]