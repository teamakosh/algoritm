# Bloom Filters

# google kuniga millionlab saytlarni indeksasiya qiladi.
# Har kuni yana millionlab yangi sahifalar yaratiladi
# Bitta sahifani qayta indeksasiya qilmaslik uchun indeksasiya qilingan saytlar ro'yxatini saqlab borish kerak
# Oson yo'li indeksasiya qilingan saytlarni hash jadvali ko'rinishida saqlash
# Hash jadvalidan o'qish vaqti O(1) ga teng.
# Muammo: Milliardlab saytlar haqidagi jadvalni saqlash uchun terabaytlab jot kerak.
# Yechim: Bloom filter

# Bloom filter bu ehtimoliy (probabilistic) ma'lumotlar tuzilmasi

# hash jadvali o'rniga Bloom filterga sayt manzilini berish va bu sayt indeksasiya qilinganligi ehtimolligini bilish mumkin. 
# Misol: 87% ehtimollik bilan indeksasiya qilingan.

# Bloom filterlari 100% aniqlik bermaydi, lekin juda kam joy egallaydi.

# HyperLogLog
# Amazon e-bozori foydalanuvchi ko'rgan (izlagan) mahsulotlar ro'yxatini saqlab borishi kerak
# Millionlab foydalanuvchilar milliardlab mahsulotlar qidiradi.
# Har bir foydalanuvchi haqida bu ma'lumotlarni saqlab borish (logging) xotirada juda katta joy talab qiladi
# Yechim: HyperLogLog
# Bu yechim ham Bloom filter kabi ehtimollar nazariyasiga asoslangan va tahminiy yechim qaytaradi.

# Secure Hash Algorithm (SHA)
# Ishlatilishi: Mualliflik huquqini himoya qilish
# Kuchli hash funksiya o'xshash matnlar uchun ham mutlaqo tasodifiy hash qiymatlarni qaytaradi
# Lekin ba'zida bizga o'xshash narsalarni solishtirish talab qilinadi
# bunday holatda Sinhash Funksiyasi yordam beradi
# Yotube - yuklangan videolarni solishtirish uchun
# Truli platformalar o'g'rilangan kitob/dasturlar yuklanganini tekkshirish
