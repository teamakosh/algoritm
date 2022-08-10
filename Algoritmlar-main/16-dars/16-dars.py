# Pythonda graphlarni dictionary (lug'at, hash jadvali) yordamida yaratish mumkin:
graph = {} # bo'sh graph
graph['siz'] = ['ali', 'vali', 'tohir']
graph['ali'] = ['aziza', 'olim']
graph['vali'] =['botir', 'ziyoda']


# Qidirish algoritmi
# 1-qadam: Queue yaratamiz
# 2-qadam: Queue boshidagi odamni ajratamiz.
# 3-qadam: Ajratilgan odam kimligini aniqlaymiz.
# 4-qadam: Natijaga qarab ish ko'ramiz.
# 5-qadam: Loop
# 6-qadam: Agar usha shaxsni topa olmasa, demak unga bog'lanib bo'lmaydi.

from collections import deque

def search(start_node, target='elon musk'):
    search_queue = deque()
    search_queue += graph[start_node]
    searched = set()

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == target:
                print(f'{target}ni topdik!')
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False