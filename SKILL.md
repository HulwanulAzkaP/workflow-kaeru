---
name: workflow-kaeru
description: Use when initializing, resuming, revising, or handing off an AI-assisted project with Workflow Kaeru. Apply the bundled project templates, role instructions, QA and technical-review gates without assuming a framework or agent harness.
---

# Workflow Kaeru

## Tujuan dan pemicu
Gunakan untuk membuat kerangka proyek baru dari nol, melanjutkan pekerjaan lintas sesi, mengelola revisi, atau menyiapkan penyerahan hasil. Ini instruksi workflow dan template, bukan plugin orkestrasi atau installer tools.

## Lokasi dan keselamatan
- **Paket sumber** adalah direktori yang berisi `SKILL.md` ini beserta seluruh sumber dayanya. Referensi Markdown di sini relatif terhadap paket sumber.
- **Target proyek** adalah lokasi yang dipilih user. Jangan menyamakan paket sumber dengan proyek produk tanpa arahan eksplisit.
- Pastikan mode dan target dari permintaan/konteks. Tanyakan bila belum jelas; jangan membuat proyek dengan nama atau scope karangan.
- Jangan menimpa file yang sudah ada. Jika target berisi file, inventarisasi konflik dan minta keputusan sebelum menimpa/merge; periksa file tersembunyi dan symlink agar tidak menulis di luar target yang diizinkan.
- Jangan mengubah profil global, memasang plugin/skill/tools, memilih layanan berbayar, mengaktifkan telemetry, mengganti model, atau mengubah izin tanpa persetujuan sesuai scope.
- Placeholder bukan fakta atau izin. Pilihan teknologi, versi, angka target, dan aturan proyek harus berdasarkan kebutuhan dan konfirmasi.

## Dokumen bersama dan sumber daya
Baca detail hanya saat relevan; jangan memuat semua dokumen setiap giliran.

| Sumber daya paket | Digunakan untuk |
|---|---|
| [AGENTS.md](AGENTS.md) | Instruksi bersama dan konteks lintas sesi |
| [Rules/Rules.md](Rules/Rules.md) | Cakupan, standar, keamanan, dan matriks izin |
| [Rules/user.md](Rules/user.md) | Preferensi user yang dikonfirmasi untuk proyek |
| [Design/Design.md](Design/Design.md) | Tujuan dan desain tingkat tinggi |
| [Design/frontend.md](Design/frontend.md) | Spesifikasi frontend bila relevan |
| [Design/backend.md](Design/backend.md) | Spesifikasi backend bila relevan |
| [Design/database.md](Design/database.md) | Spesifikasi penyimpanan/data bila relevan |
| [Plan/Todo.md](Plan/Todo.md) | Status aktif, pemilik, bukti QA/review, dan rujukan revisi |
| `Plan/Phases/Phases(N).md` | Template tujuan/deliverable/gate fase |
| [Memory/Memory.md](Memory/Memory.md) | Keputusan dan pengetahuan tahan lintas sesi |
| [Memory/CodeMap.md](Memory/CodeMap.md) | Navigasi codebase, bukan pengganti sumber aktual |
| [Research/Research.md](Research/Research.md) | Bukti riset, alternatif, dan keputusan |
| `Revision/Revision(N).md` | Template perubahan, dampak, persetujuan, dan pemulihan |
| [Dist/README.md](Dist/README.md) | Kerangka penyerahan output terverifikasi |

## Mode init — proyek baru
1. Tetapkan paket sumber dan target terpisah; periksa target dan konflik sebelum menulis.
2. Salin **hanya** `AGENTS.md` dan direktori `Agents/`, `Design/`, `Plan/`, `Memory/`, `Rules/`, `Research/`, `Revision/`, serta `Dist/` dari paket ke target. Jangan salin `.git`, README paket, `SKILL.md`, validator, cache, atau data pribadi sebagai isi produk secara otomatis.
3. Pada salinan target, ubah status/template `AGENTS.md` menjadi konteks proyek baru yang sesuai. Isi tujuan dan keputusan yang telah dikonfirmasi; jangan mengubah paket sumber.
4. Pahami pengguna, scope, batasan, cara kolaborasi, dan izin. Isi dokumen Rules serta desain tingkat tinggi secukupnya sebelum mengimplementasikan produk. Bila user ingin brainstorming bertahap, ikuti satu poin setiap kali.
5. Buat bagian riset produk yang bersih. Pisahkan sumber penyusunan workflow yang sudah tersedia dari riset/keputusan produk. Jangan membawa progres, Memory, preferensi pribadi, atau output dari proyek lain.
6. Gunakan template fase/revisi hanya saat diperlukan: ganti `N` dengan nomor yang jelas, rujuk tugas di Todo, dan jangan mengarang pencapaian atau hasil QA. Placeholder template boleh tetap ada sebagai contoh yang ditandai.
7. Lakukan preflight agent, skills/tools tambahan, izin, dan harness melalui prosedur Architect. Dokumentasikan gap sebelum tugas bergantung pada kemampuan tersebut.
8. Periksa struktur dan rujukan pada target; jika Python tersedia, jalankan validator paket dengan `--root <target> --mode project`. Laporkan yang sudah dibuat, keputusan terbuka, serta blocker. Inisialisasi bukan izin langsung mengimplementasikan semua fitur.

## Mode resume — sesi/agent berganti
1. Baca `AGENTS.md` target dan Rules yang berlaku. Selanjutnya periksa Todo, fase aktif, Memory, dan CodeMap yang relevan.
2. Verifikasi catatan terhadap file/sumber aktual. Jangan menyatakan hasil lama masih valid jika versi berubah atau buktinya tidak tersedia.
3. Tentukan tugas berikutnya dari prioritas/dependensi aktual; angkat tugas perlu revisi, terblokir, atau menunggu keputusan sebelum melanjutkan gate terkait.
4. Baca instruksi peran dan file yang dibutuhkan, bukan seluruh codebase tanpa seleksi. Perbarui Todo setelah pekerjaan atau revisi; perbarui Memory/CodeMap bila pengetahuan atau struktur berubah.

## Delegasi dan peran
Main window tetap penghubung ke user dan peluncur child sesuai kemampuan harness. PM mengoordinasikan tugas dan menerima keputusan Tech Lead; sub-agent tetap setara sebagai child main window.

- [Project Manager](Agents/project_manager.md): rencana, tugas, dependensi, dampak revisi, dan koordinasi.
- [Design](Agents/design.md): spesifikasi UI/UX untuk Engineer yang menangani frontend.
- [Architect](Agents/architect.md): struktur teknis, dependency/keamanan, dan kesiapan lingkungan AI.
- [Engineer](Agents/engineer.md): implementasi minimum yang benar dan aman; prinsip Ponytail sudah diadaptasi di file tersebut.
- [Database](Agents/database.md): desain/integritas data sesuai kebutuhan.
- [QA](Agents/qa.md): verifikasi penerimaan independen.
- [Tech Lead](Agents/tech_lead.md): keputusan teknis dan syarat revisi.

Pastikan child menerima instruksi bersama, peran, tugas, batas scope/izin, dan hasil yang diharapkan. Jangan mengasumsikan konteks diwariskan, delegasi rekursif, pesan antar-child, atau background agents tersedia. Main window dapat merelay tugas/hasil jika didukung; tanpa delegasi, nyatakan batas dan sepakati pendekatan berurutan. Jangan mengklaim independensi review yang tidak terjadi.

Prinsip Caveman di `AGENTS.md` berlaku pada komunikasi semua peran; jangan memangkas bukti, risiko, atau detail yang diminta demi token. Tidak perlu mengambil skill eksternal hanya untuk prinsip yang sudah tertulis.

## Mode revision — perubahan di tengah proyek
1. Catat arahan dan perubahan yang diminta di salinan bernomor template `Revision/Revision(N).md` pada target.
2. PM menilai dampak pada scope, desain, data, dependency, biaya, Todo/fase, keamanan, dan QA. Keputusan scope/izin mengikuti Rules dan main window, bukan persetujuan teknis semata.
3. Untuk perubahan berisiko, rujuk baseline, kondisi penghentian, serta pemulihan yang benar-benar layak. Rollback kode tidak otomatis memulihkan data.
4. Pecah perubahan besar bila membantu review; catat dependensi, bukan membuat file revisi per commit secara wajib.
5. Tautkan revisi ke Todo/fase. Lakukan implementasi, QA/retest/regresi, dan review Tech Lead sesuai gate serta dampaknya.
6. Simpan status pekerjaan di Todo. Keputusan atas permintaan bukan bukti implementasi selesai; penutupan harus merujuk versi dan bukti yang sesuai.

## Gate selesai dan penyerahan
- Engineer menguji pekerjaannya; pemeriksaan itu tidak menggantikan QA independen.
- Tugas hanya selesai setelah QA lulus dan gate teknis yang berlaku dipenuhi pada versi yang sesuai. Status menunggu review/perlu revisi/terblokir bukan selesai.
- Jika pemeriksaan wajib belum berjalan, tool tidak tersedia, atau bukti tidak cukup, ungkap keterbatasan; jangan mengubahnya menjadi lulus atau menyembunyikan flaky/retry.
- Ikuti [Dist/README.md](Dist/README.md): artefak aktual, panduan penggunaan, identitas asal/versi, bukti QA/Tech Lead, serta keterbatasan. Integritas/provenance diperiksa bila diperlukan.
- Persetujuan teknis atau penyerahan lokal bukan izin publish, merge, deploy, atau operasi destruktif.

## Distribusi dan verifikasi
Untuk memakai sebagai skill terpasang, bawa seluruh paket dan letakkan dalam direktori `workflow-kaeru` agar nama folder sesuai metadata. Folder clone dengan nama lain tetap dapat dibaca manual; auto-discovery mengikuti harness.

Jangan menyalin `SKILL.md` sendirian karena referensi/template akan hilang. Jangan mengarang URL instalasi atau mengklaim dukungan otomatis yang belum diuji.

Jika Python 3.9+ tersedia, jalankan `python scripts/validate_workflow.py` dari paket. Pemeriksaan struktur bukan bukti produk bekerja atau seluruh spesifikasi/harness kompatibel; lakukan pengujian produk pada target sesuai Rules.

## Hasil akhir yang dilaporkan
Ringkas perubahan/hasil, lokasi target/artefak, pemeriksaan yang benar-benar dijalankan, dan hal yang belum diverifikasi atau membutuhkan keputusan. Jangan menampilkan placeholder sebagai hasil nyata.
