# Merge Sort
# divide and Conquer ususli yordamida ishlaydigan tartiblash algoritmi
# Ro'yxatni ikkiga bo'lib, ikki tarafni alohida tartiblab jamlash asosida ishlaydi.

from colorama import Fore, Back, Style

def mergeSort(arr):
    if len(arr) > 1:
        med = len(arr)//2
        L = arr[:mid]
        print(Back.GREEN + str(L))