# Insertion Sort — O(n²)
# Ide: seperti menyusun kartu di tangan. Ambil satu elemen,
# geser elemen di kirinya yang lebih besar, lalu sisipkan di tempat yang pas.


def insertion_sort(arr, tampilkan=True):
    a = arr.copy()
    n = len(a)
    perbandingan = 0

    if tampilkan:
        print(f"Awal        : {a}\n")

    for i in range(1, n):
        kunci = a[i]                       # elemen yang mau disisipkan
        j = i - 1
        if tampilkan:
            print(f"   ambil {kunci}, sisipkan ke {a[:i]}")
        while j >= 0:
            perbandingan += 1
            if a[j] > kunci:
                a[j + 1] = a[j]            # geser ke kanan
                j -= 1
            else:
                break
        a[j + 1] = kunci
        if tampilkan:
            print(f"Langkah {i}   : {a}   (bagian urut: {a[:i + 1]})\n")

    return a, perbandingan


if __name__ == "__main__":
    data = [5, 2, 9, 1, 7, 3]
    hasil, jumlah = insertion_sort(data)
    n = len(data)
    print(f"Hasil akhir : {hasil}")
    print(f"Jumlah perbandingan: {jumlah}")
    print(f"Terburuk n(n-1)/2 = {n * (n - 1) // 2} -> O(n²); kalau data sudah urut cuma n-1 = {n - 1} -> O(n)")
