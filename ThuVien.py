from numbers import Number
from collections.abc import Iterable


def ChieuDai(mang: []):
    """ Trả về chiều dài của mảng

    :param mang: Mảng
    :return: Chiều dài (số lượng phần tử có trong mảng)
    """
    chieu_dai = 0
    for _ in mang:
        chieu_dai += 1
    return chieu_dai


def Dem(mang: [], x):
    """ Trả về số lần xuất hiện của x có trong mảng

    :param mang: Mảng
    :param x: Giá trị cần đếm trong mảng
    :return: Số lần xuất hiện
    """
    so_lan = 0
    for phan_tu in mang:
        if phan_tu == x:
            so_lan += 1
    return so_lan


def Noi(mang_dau, mang_cuoi):
    """Trả về mảng nối mảng cuối vào sau mảng đầu

    :param mang_dau: Mảng đầu
    :param mang_cuoi: Mảng cuối
    :return: Mảng mới bao gồm mảng đầu và mảng cuối
    """
    if not isinstance(mang_dau, Iterable) and isinstance(mang_cuoi, Iterable):
        return [mang_dau] + mang_cuoi
    elif isinstance(mang_dau, Iterable) and not isinstance(mang_cuoi, Iterable):
        return mang_dau + [mang_cuoi]
    return mang_dau + mang_cuoi


def Tong(mang: []):
    """Trả về tổng các giá trị trong mảng số

    :param mang: Mảng số
    :return: Tổng
    """
    tong = 0
    for phan_tu in mang:
        if isinstance(phan_tu, Number):
            tong += phan_tu
        else:
            raise Exception('Phần tử trong mảng phải là số')
    return tong


def DaySo(bat_dau: Number, ket_thuc: Number, buoc_nhay: Number = 1):
    """Tạo một dãy số từ điểm bắt đầu cho tới điểm kết thúc (không bao gồm điểm kết thúc)

    :param bat_dau: Giá trị đầu tiên của dãy số
    :param ket_thuc: Điểm cuối cùng của dãy số (không bao gồm chính nó)
    :param buoc_nhay: Sự thay đổi của giá trị liên tiếp
    :return: Dãy số
    """
    mang = []
    if buoc_nhay == 0:
        raise Exception('Bước nhảy không thể là 0 được')
    elif bat_dau == ket_thuc:
        raise Exception('Điểm bắt đầu và điểm kết thúc không thể bằng nhau')
    elif bat_dau < ket_thuc:
        while bat_dau <= ket_thuc - buoc_nhay:
            mang = Noi(mang, bat_dau)
            bat_dau += buoc_nhay
    else:
        while bat_dau >= ket_thuc - buoc_nhay:
            mang = Noi(mang, bat_dau)
            bat_dau += buoc_nhay
    return mang


def LonNhat(mang: []):
    """Tìm giá trị lớn nhất có trong mảng

    :param mang: Mảng
    :return: Giá trị lớn nhất
    """
    chieu_dai = ChieuDai(mang)
    if chieu_dai == 0:
        raise Exception('Mảng không được bỏ trống')
    else:
        lon_nhat = mang[0]
        for vi_tri in DaySo(1, chieu_dai):
            if lon_nhat < mang[vi_tri]:
                lon_nhat = mang[vi_tri]
        return lon_nhat


def NhoNhat(mang: []):
    """Tìm giá trị nhỏ nhất có trong mảng

    :param mang: Mảng
    :return: Giá trị nhỏ nhất
    """
    chieu_dai = ChieuDai(mang)
    if chieu_dai == 0:
        raise Exception('Mảng không được bỏ trống')
    else:
        nho_nhat = mang[0]
        for vi_tri in DaySo(1, chieu_dai):
            if nho_nhat > mang[vi_tri]:
                nho_nhat = mang[vi_tri]
        return nho_nhat


def DaoNguoc(mang: []):
    chieu_dai = ChieuDai(mang)
    if chieu_dai <= 1:
        return mang
    mang_dao_nguoc = []
    for vi_tri in DaySo(chieu_dai - 1, -1, -1):
        mang_dao_nguoc = Noi(mang_dao_nguoc, mang[vi_tri])
    return mang_dao_nguoc

def SapXep(mang: []):
    def Partition(mang: [], low: int, high: int):
        pivot = mang[high]
        left = low
        right = high - 1
        while True:
            while left <= right and mang[left] < pivot:
                left += 1
            while right >= left and mang[right] > pivot:
                right -= 1
            if left >= right:
                break
            mang[left], mang[right] = mang[right], mang[left]
            left += 1
            right -= 1
        mang[left], mang[high] = mang[high], mang[left]
        return left
    def QuickSort(mang, low, high):
        if low < high:
            so = Partition(mang, low, high)
            QuickSort(mang, low, so - 1)
            QuickSort(mang, so + 1, high)
    QuickSort(mang, 0, ChieuDai(mang) - 1)