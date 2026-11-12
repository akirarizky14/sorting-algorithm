# Merge Sort — O(n log n)
# Ide (divide and conquer):
#   1. Bagi array jadi dua sampai tiap bagian tinggal 1 elemen.
#   2. Gabungkan (merge) dua bagian yang sudah urut jadi satu bagian urut.

import math

perbandingan = 0


def merge(kiri, kanan):
    global perbandingan
    hasil = []
    i = j = 0
    while i < len(kiri) and j < len(kanan):
        perbandingan += 1
        if kiri[i] <= kanan[j]:
            hasil.append(kiri[i])
            i += 1
        else:
            hasil.append(kanan[j])
            j += 1
    hasil.extend(kiri[i:])                 # sisa yang belum masuk
    hasil.extend(kanan[j:])
    return hasil


def merge_sort(a, tampilkan=True, level=0):
    jarak = "    " * level
    if len(a) <= 1:                        # kasus dasar rekursi
        return a

    tengah = len(a) // 2
    if tampilkan:
        print(f"{jarak}bagi  {a} -> {a[:tengah]} | {a[tengah:]}")

    kiri = merge_sort(a[:tengah], tampilkan, level + 1)
    kanan = merge_sort(a[tengah:], tampilkan, level + 1)
    hasil = merge(kiri, kanan)

    if tampilkan:
        print(f"{jarak}gabung {kiri} + {kanan} -> {hasil}")
    return hasil


def jalankan(arr, tampilkan=True):
    global perbandingan
    perbandingan = 0
    hasil = merge_sort(arr.copy(), tampilkan)
    return hasil, perbandingan


if __name__ == "__main__":
    data = [5, 2, 9, 1, 7, 3]
    print(f"Awal        : {data}\n")
    hasil, jumlah = jalankan(data)
    n = len(data)
    print(f"\nHasil akhir : {hasil}")
    print(f"Jumlah perbandingan: {jumlah}")
    print(f"Perkiraan n × log₂ n = {n} × {math.log2(n):.2f} ≈ {n * math.log2(n):.0f}  -> O(n log n)")
