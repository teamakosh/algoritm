# Quicksort
# Quicksort ham ma'lumotlarni tartiblash algoritmi
# Selection sortga nisbatan bir necha barobar tezroq
# Divide and conquer yordamida ishlaydi.
# Tasavvur qiling biz biror array elementlarini tartibga keltirmoqchimiz.
# Birinchi qiladigan ishimiz to'xtash sharti (base case) topish 
# To'xtash sharti ikki hil bo'lishi mumkin:
# Bo'sh array [9]
# Bir elementdan iborat array [9]
# Yuqoridagi ikki holatda array tartibli bo'ladi.

# Agar array 2 elementdan iborat bo'lda, tartiblash oson:
# Birinchi elementni 2-element bilan solishtiramiz va kerak bo'lsa o'rnini almashtiramiz: [12, 10] -> [10, 12]

# Agar array 3 ta elementdan iborat bo'lsa,
# Quicksort quyidagicha ishlaydi:
# 1. Ixtiyoriy elementni tayanch nuqtasi (pivot) qilib olamiz.
# 2. Tayanch nuqtasidan kichkina elementlarni nuqtadan chapga, katta elementlarni nuqtadan o'ngga ajratamiz.
# 3. Toki to'xtash shartiga yetguniga qadar chapdagi va o'ngdagi elementlar uchun yuoridagi qadamalarni takrorlaysiz(rekursiya)
 
