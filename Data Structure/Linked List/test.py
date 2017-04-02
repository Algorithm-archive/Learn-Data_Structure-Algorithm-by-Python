from linked_list import LinkedList

new_list = LinkedList()

new_list.add(10)
new_list.show_all_items()
new_list.add(15)
new_list.show_all_items()
new_list.add(5)
new_list.show_all_items()
new_list.remove()
new_list.show_all_items()
new_list.add(2)
new_list.show_all_items()
print(new_list.find(50)) # Testing find with a invalid item
print(new_list.find(10)) # Testing find with a valid item
print(new_list.delete(15)) # Testing delete with a valid item
print(new_list.delete(100)) # Testing delete with a invalid item
