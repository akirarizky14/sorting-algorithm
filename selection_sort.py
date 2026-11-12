# Selection Sort — O(n²)
# Ide: cari elemen terkecil di bagian yang belum urut,
# lalu taruh di depan bagian itu. Ulangi.


def selection_sort(arr, tampilkan=True):
    a = arr.copy()
    n = len(a)
    perbandingan = 0

    if tampilkan:
        print(f"Awal        : {a}\n")

    for i in range(n - 1):
        idx_min = i
        for j in range(i + 1, n):          # cari yang terkecil di a[i..n-1]
            perbandingan += 1
            if a[j] < a[idx_min]:
                idx_min = j
        if tampilkan:
            print(f"   terkecil di sisa {a[i:]} adalah {a[idx_min]}")
        a[i], a[idx_min] = a[idx_min], a[i]
        if tampilkan:
            print(f"Putaran {i + 1}   : {a}   (bagian urut: {a[:i + 1]})\n")

    return a, perbandingan


if __name__ == "__main__":
    data = [5, 2, 9, 1, 7, 3]
    hasil, jumlah = selection_sort(data)
    n = len(data)
    print(f"Hasil akhir : {hasil}")
    print(f"Jumlah perbandingan: {jumlah}")
    print(f"Rumus n(n-1)/2 = {n}×{n - 1}/2 = {n * (n - 1) // 2}  -> O(n²), selalu, walau data sudah urut")
