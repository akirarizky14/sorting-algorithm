# Bandingkan jumlah perbandingan kelima algoritma untuk n yang makin besar.
# Lihat: O(n²) naik ~100× tiap n naik 10×, O(n log n) naik jauh lebih pelan.

import random

from bubble_sort import bubble_sort
from selection_sort import selection_sort
from insertion_sort import insertion_sort
import merge_sort
import quick_sort

random.seed(1)
print(f"{'n':>6} | {'bubble':>9} | {'selection':>9} | {'insertion':>9} | {'merge':>7} | {'quick':>7}")
print("-" * 64)
for n in [10, 100, 1000]:
    data = [random.randint(1, 10_000) for _ in range(n)]
    hasil = [
        bubble_sort(data, False)[1],
        selection_sort(data, False)[1],
        insertion_sort(data, False)[1],
        merge_sort.jalankan(data, False)[1],
        quick_sort.jalankan(data, False)[1],
    ]
    print(f"{n:>6} | {hasil[0]:>9} | {hasil[1]:>9} | {hasil[2]:>9} | {hasil[3]:>7} | {hasil[4]:>7}")
