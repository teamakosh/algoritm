# Qidirish Algoritmlar

# Qidirish Algoritmlarning eng soddasi Linear Search hisoblanadi

# Linear Search - Masalan, ro'yhatni ichidan qandaydir ma'lumot topmoqchisiz, Shunda siz uni topguncha qidirasiz, qidirish Linear Search deb ataladi.

# Binary Search Linear Searchga qaraganda tezrq ishlaydi.

# N ta elementdan iborat A ro'yxati berilgan: [a, b, c, ...]
# T biz ro'xyat ichidan qidirayotgan qiymat.
# Bizga T ning indeksi kerak.
    
# 1. pastki chegarani L=0, tepa chegarani H=N-1 deb belgilaymiz
# 2. Agar L>H bo'lsa qidirmaymiz.
# 3. O'rta qiymatning indeksini topamiz m= (L+H)/2
# 4. Agar A=T bo'lsa m ni qaytaramiz.   
# 5. Agar A<T bo'lsa, L = m+1 qilamiz va 2-qadamga qaytamiz.
# 6. Agar A>T bo'lsa, H = m-1 qilamiz va 2-qadamga qaytamiz.

# Algoritm qadamlari

# Linear search
# N ta elementdan iborat ro'yxat uchun:
# Maksimum qadamlar soni N ga teng.

# Binear Search
# N ta elementdan iborat ro'yxat uchun:
# Maksimum qadamlar soni log2(N) ga teng.

def linear_search(list, item):
    for n in range(len(list)):
        if list[n]==item:
            return n
    return None

def binary_search(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = (low +high)//2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
    
    myList1 = [1,3,4,6,7,8,10,12,23]
    print(linear_search(myList1,7))
    print(binary_search(myList1,7))
     

