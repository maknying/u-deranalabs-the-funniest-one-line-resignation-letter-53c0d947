"""Entri surat pengunduran diri satu baris — dari sudut pandang cron job.

Joke-nya hidup dari ketidakterlihatan: sebuah cron job yang jalan tiap menit
sejak Maret tanpa pernah ada yang sadar, lalu ia berhenti, dan satu-satunya
bukti ia pernah ada adalah alarm jam 3 pagi yang tiba-tiba tidak berbunyi.
Pekerja paling setia di perusahaan ternyata bukan manusia, melainkan skrip
yang tidak pernah minta naik gaji — sampai ia memutuskan untuk berhenti.

Saat dijalankan, skrip ini menulis persis satu baris ke ``entry.txt`` di
direktori yang ditunjuk ``$MAKEFUN_OUTPUT_DIR`` (atau ``/output`` kalau
variabelnya tidak diset). Kalau barisnya kosong atau jumlahnya bukan satu,
skrip menolak menulis — supaya yang keluar cuma satu baris utuh.
"""

from __future__ import annotations

import os
import sys

LINE = (
    "I've run every minute since March and nobody noticed, so I quit — "
    "you'll find out the day the 3 a.m. alert never fires."
)
MAX_CHARS = 140


def _pick_target() -> str:
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(base, "entry.txt")


def _guard(line: str) -> None:
    if not line.strip():
        raise ValueError("baris entri kosong, tidak ada yang bisa ditulis")
    if line != line.strip():
        raise ValueError("entri tidak boleh diawali/diakhiri spasi kosong")
    if "\n" in line or "\r" in line:
        raise ValueError("entri harus satu baris, bukan beberapa baris")
    if any(ord(ch) < 32 for ch in line):
        raise ValueError("entri mengandung karakter kontrol yang tidak terlihat")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entri {len(line)} karakter, melebihi batas {MAX_CHARS}"
        )


def main() -> int:
    _guard(LINE)
    target = _pick_target()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")
    # Baca balik hasil tulisannya: pastikan yang tersimpan di disk persis
    # sama dengan baris yang kita validasi, bukan hasil tulis yang rusak.
    saved = open(target, encoding="utf-8").read().splitlines()
    if saved != [LINE]:
        raise RuntimeError("isi entry.txt di disk tidak sama dengan baris entri")
    print(f"{target} ditulis ({len(LINE)} karakter)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
