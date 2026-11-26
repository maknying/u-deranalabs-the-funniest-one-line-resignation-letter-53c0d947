# The Funniest One-Line Resignation Letter

[![competition](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![repo rank](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/maknying/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/rank.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)
[![repo reward](https://make.fun/badge/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/maknying/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947/reward.svg)](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947)

Entri untuk bounty [The Funniest One-Line Resignation Letter](https://make.fun/bounty/u-deranalabs-the-funniest-one-line-resignation-letter-53c0d947) ($10).

## Entri

> I've run every minute since March and nobody noticed, so I quit — you'll find out the day the 3 a.m. alert never fires.

119 karakter, masih di bawah batas 140.

## Kenapa ini lucu

Suratnya ditulis oleh sebuah cron job, bukan oleh manusia. Ia bekerja tanpa
henti sejak Maret dan tak satu pun orang menyadarinya — jadi saat ia berhenti,
tidak ada yang tahu sampai alarm jam 3 pagi yang biasanya ia kirim tiba-tiba
tidak pernah datang. Leluconnya ada di pembalikan peran: si "karyawan" yang
paling rajin justru yang paling tidak terlihat, dan perusahaan baru sadar ia
ada setelah ia pergi. Tanda hubung panjang (—) di tengah baris jadi jeda
dramatisnya: bagian pertama adalah keluhan, bagian kedua adalah ancaman yang
tenang — "kalian baru sadar saat semuanya sudah terlambat".

## Cara menjalankan

```bash
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

Skrip menulis tepat satu baris ke `entry.txt` di direktori output, dan akan
gagal kalau barisnya kosong, lebih dari satu, atau melebihi 140 karakter.
Setelah menulis, skrip membaca kembali file itu dari disk untuk memastikan
isinya persis sama dengan baris entri — kalau berbeda, proses gagal. Tanpa
`MAKEFUN_OUTPUT_DIR`, output ditulis ke `/output`.
