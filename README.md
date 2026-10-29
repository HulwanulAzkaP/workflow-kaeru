# Workflow Kaeru

**Kerangka proyek berbasis dokumen untuk AI Agents: dari perencanaan, implementasi, dan revisi hingga penyerahan hasil yang terverifikasi.**

Workflow Kaeru menyediakan template dan instruksi peran yang dapat digunakan ulang untuk proyek baru. Framework, bahasa, database, model AI, dan harness tidak ditentukan oleh template.

> **Status:** draf workflow yang dapat digunakan sebagai baseline. Struktur dan paket dapat diperiksa dengan validator lokal; orkestrasi agent dan alur proyek penuh belum diuji end-to-end pada semua harness. Ini bukan aplikasi, plugin runtime, atau installer agent.

## Mulai di sini

| Kebutuhan | Dokumen |
|---|---|
| Memahami dan menyiapkan workflow | README ini |
| Meminta AI menginisialisasi, melanjutkan, atau merevisi proyek | [SKILL.md](SKILL.md) |
| Instruksi utama saat agent bekerja | [AGENTS.md](AGENTS.md) |
| Aturan operasional dan izin proyek | [Rules/Rules.md](Rules/Rules.md) |
| Rencana dan progres pekerjaan | [Plan/Todo.md](Plan/Todo.md) |

`SKILL.md` menjelaskan prosedur; dokumen lain tetap menjadi sumber detail. Tidak perlu mengunduh skill Ponytail atau Caveman untuk mengikuti prinsip yang sudah diadaptasi di sini.

## Quick start untuk manusia

1. Clone repository publik ini, atau unduh paketnya melalui [GitHub](https://github.com/HulwanulAzkaP/workflow-kaeru):

   ```bash
   git clone https://github.com/HulwanulAzkaP/workflow-kaeru.git workflow-kaeru
   cd workflow-kaeru
   ```
2. Buka folder hasil clone bersama AI agent. Minta agent membaca `SKILL.md` dan tentukan target proyek baru secara eksplisit.
3. Berikan tujuan, pengguna, kebutuhan awal, dan batasan yang sudah diketahui. Yang belum diketahui tetap ditanyakan atau ditandai, bukan diisi dengan asumsi.
4. Review konteks, scope, izin, desain, Todo, dan fase sebelum implementasi dimulai.
5. Lanjutkan pekerjaan melalui QA dan review teknis sesuai gerbang yang disepakati. Simpan output penyerahan di lokasi yang sesuai proyek.

Contoh prompt, dengan placeholder yang harus diganti:

```text
Baca SKILL.md dari paket Workflow Kaeru ini.
Inisialisasi kerangka untuk proyek baru di <PATH_PROYEK_BARU>.
Tujuan proyek: <TUJUAN>.
Jangan ubah paket sumber atau konfigurasi global agent.
Tanyakan keputusan yang belum jelas sebelum implementasi produk.
```

Untuk melanjutkan proyek:

```text
Gunakan prosedur resume di SKILL.md untuk <PATH_PROYEK>.
Baca AGENTS.md, Todo, fase aktif, Memory, dan CodeMap yang relevan.
Laporkan tugas berikutnya dan blocker berdasarkan bukti sebelum melanjutkan.
```

Perintah dalam contoh di atas adalah instruksi bahasa alami, bukan command CLI yang otomatis terpasang.

## Quick start untuk AI Agents

1. Tetapkan dua lokasi berbeda: **paket sumber** dan **target proyek**. Jangan menganggap clone template sebagai permintaan membangun produk di folder yang sama.
2. Pilih prosedur `init`, `resume`, `revision`, atau `handoff` di [SKILL.md](SKILL.md).
3. Saat `init`, salin hanya `AGENTS.md` dan direktori template yang disebut dalam skill. Jangan menimpa file target atau mengimpor histori/preferences proyek lain.
4. Isi konteks dan keputusan yang dikonfirmasi user. Ubah penanda template pada salinan `AGENTS.md` agar sesuai proyek baru; jangan mengubah paket sumber.
5. Muat instruksi bersama dan instruksi peran sesuai kebutuhan. Verifikasi agent/tools/izin yang nyata; Markdown tidak menciptakan kapabilitas runtime.
6. Perbarui Todo berdasarkan progres aktual. QA, persetujuan teknis, dan izin deploy adalah hal berbeda.

Semua path di backtick dalam dokumen proyek ditafsirkan dari **root proyek**, kecuali dinyatakan lain. Tautan Markdown biasa mengikuti lokasi file yang memuatnya. Path sumber daya di `SKILL.md` mengikuti **root paket skill**.

## Struktur paket

```text
workflow_kaeru/
├── README.md                         # Panduan pengguna dan distribusi
├── SKILL.md                          # Prosedur masuk AI
├── AGENTS.md                         # Instruksi bersama / template proyek
├── Agents/
│   ├── project_manager.md
│   ├── design.md
│   ├── architect.md
│   ├── engineer.md
│   ├── database.md
│   ├── qa.md
│   └── tech_lead.md
├── Design/
│   ├── Design.md                     # Tujuan dan gambaran tingkat tinggi
│   ├── frontend.md
│   ├── backend.md
│   └── database.md
├── Plan/
│   ├── Todo.md                       # Sumber utama status pekerjaan
│   └── Phases/Phases(N).md            # Template fase bernomor
├── Memory/
│   ├── Memory.md                     # Pengetahuan proyek lintas sesi
│   └── CodeMap.md                    # Indeks ringan codebase
├── Rules/
│   ├── Rules.md                      # Aturan operasional / matriks izin
│   └── user.md                       # Preferensi user yang dikonfirmasi
├── Research/Research.md               # Bukti riset dan status keputusan
├── Revision/Revision(N).md             # Template catatan revisi
├── Dist/README.md                     # Kerangka penyerahan output
└── scripts/validate_workflow.py        # Pemeriksaan struktur tanpa dependency
```

Nama `Phases(N).md` dan `Revision(N).md` adalah template; ganti `N` dengan nomor ketika membuat fase atau revisi nyata. Jangan membuat fase/revisi fiktif agar folder tampak terisi.

## Peran dan alur kerja

| Peran | Tanggung jawab utama |
|---|---|
| Main window | Menerima arahan user, meluncurkan/menghubungkan sub-agent sesuai runtime, dan menangani keputusan yang dieskalasikan. |
| Project Manager | Merencanakan, membagi tugas, menilai dampak revisi, melacak blocker, dan menerima keputusan Tech Lead. |
| Design | Spesifikasi UI/UX, interaksi, responsivitas, dan aksesibilitas. |
| Architect | Struktur teknis, pilihan dependency/versi, keamanan terkini, serta preflight kesiapan lingkungan AI. |
| Engineer | Implementasi minimum yang benar dan aman, pemeriksaan mandiri, serta perbaikan akar masalah. |
| Database | Desain/integritas data, akses, migrasi, konkurensi, dan pemulihan sesuai kebutuhan. |
| QA | Verifikasi penerimaan independen dan bukti hasil uji. |
| Tech Lead | Gerbang keputusan teknis: disetujui, perlu revisi, atau terblokir. |

Semua sub-agent adalah child dari main window. PM mengoordinasikan tugas di antara mereka; jangan mengasumsikan child dapat meluncurkan atau mengirim pesan ke child lain. Jika harness tidak mendukungnya, main window dapat merelay instruksi/hasil; bila tidak ada delegasi, ungkap keterbatasannya dan sepakati pelaksanaan berurutan. Jangan mengklaim review independen oleh sub-agent jika tidak benar-benar terjadi.

Alur umumnya:

**Kebutuhan → riset/desain → Todo/fase → implementasi → QA → keputusan teknis sesuai tahap → penyerahan.**

- QA gagal atau Tech Lead meminta revisi: perbaiki dan uji/review ulang sesuai dampaknya.
- Gate belum terpenuhi: pekerjaan tidak dianggap siap melewati tahap tersebut.
- Bukti harus sesuai versi/artefak yang diperiksa; hasil lama tidak otomatis berlaku untuk perubahan baru.
- Persetujuan teknis bukan izin publikasi, merge, deploy, atau operasi destruktif.

## Distribusi sebagai skill

Paket menggunakan format `SKILL.md` dengan nama skill **`workflow-kaeru`**. Loader dan lokasi instalasi mengikuti harness masing-masing; clone saja tidak menjamin skill terdeteksi otomatis.

Untuk instalasi mandiri, tempatkan **seluruh paket** di direktori bernama `workflow-kaeru`, bukan menyalin `SKILL.md` sendirian. Nama direktori ber-hyphen ini mengikuti spesifikasi Agent Skills; folder kerja lokal `workflow_kaeru` tidak perlu diganti untuk pembacaan manual.

Bawa `AGENTS.md`, seluruh direktori template, README, dan validator. Jangan menyertakan `.git`, cache, kredensial, atau data proyek pribadi ke paket distribusi. Jangan mengaktifkan hooks, plugin, telemetry, proxy, atau mengganti model secara implisit.

Lisensi proyek ini belum ditetapkan. Sebelum publikasi/distribusi, pemilik perlu menentukan lisensi dan memeriksa kewajiban atribusi materi yang digunakan. Dokumentasi ini tidak memberi lisensi atas karya pihak ketiga.

## Validasi lokal

Membutuhkan Python 3.9+; tidak memerlukan instalasi dependency atau koneksi jaringan.

Dari root paket:

```bash
python scripts/validate_workflow.py
```

Untuk memeriksa struktur salinan proyek hasil inisialisasi:

```bash
python <PATH_PAKET>/scripts/validate_workflow.py --root <PATH_PROYEK> --mode project
```

Validator memeriksa file wajib, metadata dasar skill, referensi/tautan lokal yang relevan, nama entry point, dan konsistensi kolom tabel. Pemeriksaan ini **bukan** QA produk, audit keamanan, validasi resmi seluruh spesifikasi Agent Skills, atau bukti kemampuan harness. Mode proyek hanya memeriksa kerangka; placeholder harus ditinjau secara terpisah sebelum implementasi.

## Kompatibilitas dan batas kemampuan

- Dokumen dapat dibaca secara manual oleh agent yang memiliki akses file. Auto-discovery `AGENTS.md` dan skill berbeda antarharness.
- Model, skill tambahan, tools, MCP, LSP, sandbox, dan delegasi harus diperiksa pada lingkungan nyata.
- Tidak ada jaminan parallel agents, komunikasi antar-child, enforcer Todo, atau kompresi otomatis hanya dari dokumen ini.
- Pilihan teknologi dan izin operasional diisi per proyek; placeholder bukan persetujuan.
- Root template tidak mengandung output produk. `Dist/` bukan alasan mengubah folder build bawaan framework atau menyebarkan data sensitif.

## Sumber prinsip dan dokumentasi

- [Ponytail](https://github.com/dietrichgebert/ponytail): inspirasi pemilihan implementasi minimum setelah memahami masalah; telah diadaptasi, bukan keharusan memasang skill aslinya.
- [Caveman](https://github.com/JuliusBrussee/caveman): inspirasi komunikasi ringkas dan konteks terarah, tanpa mengaktifkan komponen runtime atau layanan cloud.
- [Agent Skills specification](https://agentskills.io/specification): format dan pengemasan skill.
- [Hermes — Creating Skills](https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills): referensi integrasi pada Hermes, bukan jaminan keseragaman semua harness.
- [Research/Research.md](Research/Research.md): sumber teknis dan keputusan penyusunan workflow.

Bagian riset workflow yang sudah terisi adalah dokumentasi asal kerangka, bukan riset produk baru. Saat inisialisasi, buat bagian riset produk bersih dan jangan membawa histori proyek sebelumnya.
