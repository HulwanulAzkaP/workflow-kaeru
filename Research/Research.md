# Research — Catatan Riset

> Simpan temuan yang mendukung keputusan proyek. Bedakan sumber, fakta yang ditemukan, interpretasi, dan keputusan yang disetujui. Verifikasi informasi versi/keamanan dari sumber resmi dan bertanggal.

## Catatan riset

### Template entri
- **ID/judul riset:**
- **Pertanyaan/tujuan dan cakupan:**
- **Tanggal pemeriksaan:**
- **Agent/penyusun:**
- **Sumber (URL/dokumen dan versi relevan):**
- **Temuan yang didukung bukti:**
- **Interpretasi/asumsi AI (pisahkan dari temuan):**
- **Relevansi, keterbatasan, dan hal yang belum terverifikasi:**
- **Alternatif dan trade-off:**
- **Rekomendasi:**
- **Status keputusan (usulan/disetujui/ditolak/tergantikan):**
- **Alasan, pihak pemberi persetujuan, dan rujukannya:**
- **Dokumen desain/aturan yang menggunakan keputusan:**
- **Tindak lanjut dan kondisi/tanggal pemeriksaan ulang:**

## Aturan penggunaan
- Ini template workflow reusable. Saat membuat proyek baru, pisahkan sumber tentang penyusunan workflow di bawah dari riset produk; jangan menganggap contoh teknologi sebagai pilihan proyek.
- Catat asal bukti dan versi yang relevan; utamakan sumber resmi untuk API, versi, dan advisory keamanan. Jangan mengarang tanggal atau nomor versi jika belum diverifikasi.
- Bedakan fakta dari sumber, interpretasi AI, rekomendasi, dan keputusan yang benar-benar disetujui. Hasil riset bukan otomatis aturan atau izin tindakan.
- Rujuk keputusan yang disetujui dari dokumen desain/aturan terkait; jangan menyalin seluruh riset ke setiap dokumen.
- Tandai keputusan tergantikan dan rujuk keputusan barunya; jangan membuat versi yang berbeda tampak sama-sama berlaku.
- Informasi dinamis seperti dukungan versi/advisory perlu diperiksa kembali saat akan dipakai. Sumber lama tidak membuktikan kondisi keamanan terkini.
- Tidak wajib menambah folder atau mekanisme ADR khusus; gunakan prinsip pencatatan keputusan yang proporsional.

## Referensi kerangka Research
- W3C, PROV Primer (asal-usul informasi): https://www.w3.org/TR/prov-primer/
- AWS, Decision Record Process: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html

## Riset kerangka workflow

### Instruksi agent dan context lintas sesi
- **Temuan:** File instruksi agent berfungsi sebagai entry point; jaga tetap ringkas dan arahkan ke rincian yang terpisah. Context/memory yang dipilih dan dimuat saat diperlukan membantu mengelola perhatian/token.
- **Sumber:** https://learn.chatgpt.com/docs/agent-configuration/agents-md ; https://agents.md/ ; https://www.anthropic.com/research/effective-context-engineering-for-ai-agents

### Desain tingkat tinggi dan fase
- **Temuan:** Pisahkan gambaran tingkat tinggi dari detail komponen; fase punya tujuan, hasil, pemilik, dependensi, serta kriteria transisi yang jelas.
- **Sumber:** https://c4model.com/ ; https://www.atlassian.com/work-management/project-management/phases

### Pelacakan pekerjaan dan memori
- **Temuan:** Status kerja perlu membedakan progres dari review/selesai; pengetahuan jangka panjang, status workflow, instruksi resmi, dan dugaan agent sebaiknya tidak tercampur. Catatan usang perlu diperbarui atau ditandai tergantikan.
- **Sumber:** https://support.atlassian.com/jira-cloud-administration/docs/what-are-issue-statuses-priorities-and-resolutions/ ; https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool ; https://aaif.io/blog/agent-memory-patterns-tradeoffs-open-problems

### Project management dan perubahan
- **Temuan:** PM mengelola tujuan, scope, tugas, sumber daya, hambatan; perubahan scope perlu dianalisis dampaknya dan disetujui; pelajaran dapat dicatat sepanjang proyek.
- **Sumber:** https://www.pmi.org/about/what-is-a-project-manager ; https://www.pmi.org/learning/library/scope-control-projects-you-6972 ; https://www.pmi.org/learning/library/applying-lessons-learned-implement-project-8344

### Design, architecture, dan engineering
- **Temuan:** Design handoff menyebut perilaku/appearance dan aksesibilitas; arsitektur mendokumentasikan trade-off serta dapat memakai guardrail yang bisa diperiksa; dependency perlu dipantau keamanan dan dikunci agar build reproducible; secure coding dan tes sesuai risiko perlu dijaga.
- **Sumber:** https://www.nngroup.com/articles/creating-design-specs-for-development/ ; https://www.nngroup.com/articles/usability-testing-101/ ; https://software-architecture-guild.com/guide/role/role-overview/ ; https://www.infoq.com/articles/fitness-functions-architecture/ ; https://docs.github.com/en/code-security/concepts/supply-chain-security/best-practices-for-maintaining-dependencies ; https://cloud.google.com/blog/topics/developers-practitioners/best-practices-dependency-management ; https://google.github.io/eng-practices/review/ ; https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/stable-en/02-checklist/05-checklist

### Ponytail-inspired coding style
- **Temuan:** Pahami dan telusuri alur terlebih dahulu, kemudian pilih implementasi minimum dengan urutan reuse → standard library → native → dependency tersedia → kode baru. Jangan mengorbankan security, validasi, error handling, accessibility, atau pemeriksaan logika nontrivial.
- **Sumber:** https://github.com/dietrichgebert/ponytail/blob/main/AGENTS.md ; https://github.com/dietrichgebert/ponytail/blob/main/skills/ponytail/SKILL.md

### Caveman-inspired communication dan konteks
- **Keputusan workflow:** Adaptasi prinsip komunikasi ringkas, payload literal, konteks terarah, dan akses kembali ke bukti lengkap ditulis di `AGENTS.md`; Ponytail tetap di `Agents/engineer.md`. Tidak perlu mengambil skill eksternal untuk mengikuti prinsip yang sudah tertulis.
- **Batas:** Adaptasi instruksi bukan instalasi CLI/proxy dan tidak menyediakan kompresi otomatis atau Auto routing. Keamanan, approval, detail yang diminta, serta bukti QA tidak boleh hilang demi token. Fitur runtime tambahan perlu evaluasi dan persetujuan terpisah; CLI/cloud memiliki implikasi telemetry dan aliran data yang berbeda dari instruksi lokal.
- **Sumber:** https://github.com/JuliusBrussee/caveman ; https://github.com/JuliusBrussee/caveman/blob/main/SECURITY.md
- **Status:** Disetujui untuk adaptasi, bukan penyalinan mentah; bukan klaim penghematan yang sudah diuji pada workflow ini.

### AI harness readiness
- **Temuan:** Harness menentukan ketersediaan dan konfigurasi tools, skills, memory, approval, dan delegasi; verifikasi kapabilitas serta status dukungannya pada runtime aktual.
- **Sumber:** https://learn.microsoft.com/en-us/agent-framework/concepts/harness

### Desain data dan keamanan database
- **Temuan:** Gunakan constraint untuk integritas; indeks harus didasarkan pada pola query dan ditimbang terhadap biaya; akses database perlu least privilege dan query terparameterisasi. Pertimbangkan klasifikasi/minimisasi/retensi data, kompatibilitas migrasi berversi, konkurensi/transaksi, serta verifikasi restore sesuai kebutuhan.
- **Sumber:** https://www.postgresql.org/docs/current/ddl-constraints.html ; https://www.postgresql.org/docs/current/indexes.html ; https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html ; https://www.postgresql.org/docs/current/ddl-rowsecurity.html ; https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.eac.3-codify-data-operations.html ; https://www.postgresql.org/docs/current/transaction-iso.html ; https://www.postgresql.org/docs/current/backup.html ; https://privsec.harvard.edu/data-lifecycle

### QA — kerangka yang disetujui
- **Tambahan disetujui:** Catat tes flaky dan riwayat retry tanpa menyembunyikan kegagalan awal; keputusan kelulusan mengikuti kebijakan proyek. Jangan menganggap scanner otomatis membuktikan kepatuhan aksesibilitas penuh; periksa interaksi yang relevan dan ungkap kebutuhan evaluasi manusia yang belum terpenuhi.
- **Sumber tambahan:** https://playwright.dev/docs/test-retries ; https://www.w3.org/WAI/test-evaluate/
- **Keputusan:** QA memeriksa penerimaan secara independen, menyusun skenario berbasis kebutuhan/risiko, melaporkan bug yang dapat direproduksi, melakukan retest/regresi, dan memberi keputusan berbukti. Tes wajib yang belum berjalan tidak boleh dianggap lulus; kelulusan terkait versi pekerjaan yang diperiksa. Pengujian sistem nyata harus sesuai izin dan scope.
- **Sumber:** https://istqb.org/certifications/certified-tester-foundation-level-ctfl-v4-0/ ; https://playwright.dev/docs/best-practices ; https://owasp.org/www-project-web-security-testing-guide/

### Tech Lead — gerbang persetujuan teknis
- **Keputusan disetujui:** Tech Lead meninjau spesifikasi, arsitektur, integrasi, keamanan, maintainability, dan bukti QA; memberi keputusan disetujui/perlu revisi/terblokir beserta alasan serta syarat revisi. Persetujuan terkait versi yang diperiksa dan hasilnya disampaikan ke Project Manager. Tidak menggantikan QA, mengambil alih Architect/PM, atau memberi izin deploy/tindakan destruktif secara otomatis.
- **Sumber:** https://google.github.io/eng-practices/review/reviewer/standard.html ; https://docs.github.com/en/pull-requests/how-tos/review-pull-requests/approving-a-pull-request-with-required-reviews ; https://handbook.gitlab.com/handbook/engineering/careers/ic-leadership/tech-lead/
- **Tambahan disetujui:** Tinjau validitas assertion/tes, nyatakan cakupan dan batas kompetensi review, cocokkan bukti dengan versi perubahan, periksa tes wajib yang mungkin dilewati CI, konsolidasikan revisi dan eskalasikan konflik berulang, serta tinjau rollout/pemulihan dan deteksi kegagalan untuk perubahan rilis berisiko.
- **Sumber tambahan:** https://google.github.io/eng-practices/review/reviewer/looking-for.html ; https://google.github.io/eng-practices/review/reviewer/speed.html ; https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/troubleshooting-required-status-checks ; https://sre.google/workbook/canarying-releases/
- **Batas penerapan:** Mekanisme enforcement teknis dan tooling belum ditetapkan; referensi GitHub tidak berarti workflow wajib memakai GitHub atau pull request. Canary tidak wajib untuk semua proyek; readiness review bukan izin deploy.

### Revision — kerangka yang disetujui
- **Keputusan:** Catatan revisi memuat identitas/sumber, alasan dan perubahan, dampak, keputusan permintaan, pelaksanaan melalui ID Todo/fase, serta versi hasil dan bukti QA/Tech Lead untuk penutupan. Persetujuan permintaan tidak berarti implementasi selesai atau izin deploy; status pekerjaan aktif tetap di Todo.
- **Sumber:** https://google.github.io/eng-practices/review/developer/cl-descriptions.html ; https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager.html

### Tambahan Revision dan perbaikan lintas dokumen — disetujui dan diterapkan
- **Rencana pemulihan revisi berisiko:** Template Revision memuat versi awal/baseline, kondisi penghentian, rollback atau fix-forward, dampak pada data, penanggung jawab/izin, dan verifikasi pemulihan. Pengembalian kode tidak otomatis mengembalikan data; prosedur rinci cukup dirujuk.
- **Pembagian revisi besar:** Pisahkan perubahan yang tidak berkaitan, termasuk refactor dan fitur bila memungkinkan; nyatakan dependensi tanpa mewajibkan setiap commit menjadi file revisi baru.
- **Gate Todo/fase:** Todo membedakan menunggu QA, menunggu review teknis, perlu revisi, terblokir, dan selesai. Penutupan memerlukan QA lulus serta gate Tech Lead yang berlaku terpenuhi pada versi hasil yang sesuai; fase merujuk gate dan keputusan teknis tanpa menyalin progres.
- **Penamaan peran:** Handoff dan koordinasi frontend di `Agents/design.md` secara eksplisit menuju Engineer yang menangani frontend, bukan peran Frontend terpisah.
- **Ketertelusuran:** Todo memuat rujukan fase/revisi dan template fase memuat ID/path revisi serta rujukan keputusan. File Revision merujuk ID tugas dan fase; status pekerjaan aktif tetap satu sumber di Todo.
- **Sumber riset lanjutan:** https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_mit_deploy_risks_plan_for_unsucessful_changes.html ; https://google.github.io/eng-practices/review/developer/small-cls.html

### Dist — penyerahan hasil yang disetujui
- **Keputusan:** `Dist/README.md` memuat kerangka artefak aktual, panduan penggunaan, identitas versi/asal output, rujukan QA/Tech Lead yang sesuai versi, catatan penyerahan, serta integritas/keaslian bila diperlukan. Tidak boleh mengklaim output siap pakai tanpa pemeriksaan wajib; publish/deploy tetap mengikuti izin proyek.
- **Batas:** Format output dan lokasi build mengikuti proyek/framework; template tidak mewajibkan GitHub atau implementasi SLSA penuh. Checksum saja bukan jaminan keaslian.
- **Sumber:** https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases ; https://slsa.dev/spec/v1.2/verifying-artifacts

Catatan ini merangkum riset untuk rancangan workflow, bukan rekomendasi teknologi bagi proyek produk tertentu. Catatan riset proyek riil dan keputusan spesifik ditambahkan saat proyek dimulai.