# Bubble sort va Merge sort
# Bubble sort
# Eng sodda tartiblash algoritmi
# Qo'shni elementlarni solishtirish va o'rnini almashtirish orqali ishlaydi.

def bubbleSort(array: list) -> list:
    for i in range(len(array)):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                print(array) 