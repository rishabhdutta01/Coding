from LinkedList import LinkedList

if __name__ == '__main__':
    #List1
    list1 = LinkedList()
    list1.add_element(7)
    list1.add_element(8)
    list1.add_element(10)
    list1.add_element(12)

    #list1.print_list()

    #List2
    list2 = LinkedList()
    list2.add_element(2)
    list2.add_element(4)
    list2.add_element(6)
    list2.add_list(list1, 3)

    print(list1.find_intersection(list2))

    #list2.print_list()
