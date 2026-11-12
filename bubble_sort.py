# Bubble Sort — O(n²)
# Ide: bandingkan dua elemen bertetangga, tukar kalau urutannya salah.
# Setiap putaran, elemen terbesar "menggelembung" ke ujung kanan.


def bubble_sort(arr, tampilkan=True):
    a = arr.copy()
    n = len(a)
    perbandingan = 0

    if tampilkan:
        print(f"Awal        : {a}\n")

    for i in range(n - 1):                 # putaran ke-1 .. ke-(n-1)
        ada_tukar = False
        for j in range(n - 1 - i):         # bagian kanan yang sudah benar tidak dicek lagi
            perbandingan += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                ada_tukar = True
                if tampilkan:
                    print(f"   tukar {a[j + 1]} dan {a[j]}  -> {a}")
        if tampilkan:
            print(f"Putaran {i + 1}   : {a}   ({a[n - 1 - i]} sudah di posisi akhir)\n")
        if not ada_tukar:                  # tidak ada tukar = sudah urut, berhenti lebih awal
            break

    return a, perbandingan


if __name__ == "__main__":
    data = [5, 2, 9, 1, 7, 3]
    hasil, jumlah = bubble_sort(data)
    n = len(data)
    print(f"Hasil akhir : {hasil}")
    print(f"Jumlah perbandingan: {jumlah}")
    print(f"Rumus terburuk n(n-1)/2 = {n}×{n - 1}/2 = {n * (n - 1) // 2}  -> O(n²)")
