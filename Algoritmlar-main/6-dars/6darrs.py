# Ma'lumotlar tuzilmasi algoritmlar
# Linked Lists
# Muallif: Shaxzodjon Zoirov

from linkedlistfuncs import Node, LinkedList

# Linked list yaratamiz
llist = LinkedList()

# Uchta node (tugun) yaratamiz
llist.head = Node('Dushanba')
Tuesday = Node('Seshanba')
Wednesday = Node('Chorshanba')

# Tugunlarni bog'laymiz
llist.head.next = Tuesday
Tuesday.next = Wednesday

