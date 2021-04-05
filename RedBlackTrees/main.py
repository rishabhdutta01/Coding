# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from RedBlackTree import RedBlackTree

if __name__ == '__main__':
    rbt = RedBlackTree()

    f = open("input.txt", "r", encoding="utf-8")
    data = f.readlines()
    f.close()

    for node in data:
        rbt.insert(int(node.strip()))
        print("Height of tree:", rbt.height())

    askmore = True
    while askmore:
        print("1. Insert item")
        print("2. Search item")
        print("3. Sort")
        print("4. Successor of item")
        print("5. Predecessor of item")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Height")
        print("9. Print tree")
        print("10. Exit")
        choice = int(input("Enter choice number:"))
        if choice == 1:
            key = int(input("Enter item key to be inserted:"))
            rbt.insert(key)
            print("New height of tree: ", rbt.height())
        elif choice == 2:
            key = int(input("Enter item key to be searched:"))
            node = rbt.search(key)
            print("Found" if node.value is not None else "Not Found")
        elif choice == 3:
            print(rbt.sort())
        elif choice == 4:
            key = int(input("Enter successor item key:"))
            print(rbt.successor(rbt.search(key)))
        elif choice == 5:
            key = int(input("Enter predecessor item key:"))
            print(rbt.predecessor(rbt.search(key)))
        elif choice == 6:
            print(rbt.minimum())
        elif choice == 7:
            print(rbt.maximum())
        elif choice == 8:
            print(rbt.height())
        elif choice == 9:
            print(rbt.printTree(rbt.root))
        else:
            askmore = False
