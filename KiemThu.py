from ThuVien import *
from random import *
from time import *

mang_so_1 = list(range(10))
mang_so_2 = DaySo(0, 10)
mang_so_3 = [randint(-10, 10) for n in range(10)]
ds_so_1 = set(range(10))
mang_chu_1 = ['a', 'b', 'c', 'd', 'e']
so_1 = 1
chu_1 = 'a'

def DoThoiGian(ham, ket_qua):
    bat_dau = time()
    ham()
    ket_thuc = time()
    return (ket_thuc - bat_dau) * 1000