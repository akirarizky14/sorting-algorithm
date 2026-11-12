# Quick Sort — rata-rata O(n log n), terburuk O(n²)
# Ide (divide and conquer):
#   1. Pilih satu pivot (di sini: elemen paling kanan).
#   2. Partisi: yang lebih kecil dari pivot ke kiri, yang lebih besar ke kanan.
#   3. Ulangi untuk bagian kiri dan bagian kanan.

import math

perbandingan = 0


def partisi(a, rendah, tinggi, tampilkan, jarak):
    global perbandingan
    pivot = a[tinggi]
    i = rendah - 1
    for j in range(rendah, tinggi):
        perbandingan += 1
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[tinggi] = a[tinggi], a[i + 1]   # pivot ke posisi akhirnya
    p = i + 1
    if tampilkan:
        print(f"{jarak}   -> {a[rendah:p]} [{a[p]}] {a[p + 1:tinggi + 1]}   array: {a}")
    return p


def quick_sort(a, rendah, tinggi, tampilkan=True, level=0):
    if rendah < tinggi:
        jarak = "    " * level
        if tampilkan:
            print(f"{jarak}pivot {a[tinggi]} untuk {a[rendah:tinggi + 1]}")
        p = partisi(a, rendah, tinggi, tampilkan, jarak)
        quick_sort(a, rendah, p - 1, tampilkan, level + 1)
        quick_sort(a, p + 1, tinggi, tampilkan, level + 1)


def jalankan(arr, tampilkan=True):
    global perbandingan
    perbandingan = 0
    a = arr.copy()
    quick_sort(a, 0, len(a) - 1, tampilkan)
    return a, perbandingan


if __name__ == "__main__":
    data = [5, 2, 9, 1, 7, 3]
    print(f"Awal        : {data}\n")
    hasil, jumlah = jalankan(data)
    n = len(data)
    print(f"\nHasil akhir : {hasil}")
    print(f"Jumlah perbandingan: {jumlah}")
    print(f"Perkiraan n × log₂ n ≈ {n * math.log2(n):.0f}  -> O(n log n) rata-rata")

    print("\n--- Kasus terburuk: data yang SUDAH urut, pivot selalu yang terbesar ---\n")
    hasil, jumlah = jalankan([1, 2, 3, 5, 7, 9])
    print(f"\nJumlah perbandingan: {jumlah} = n(n-1)/2  -> O(n²)")
