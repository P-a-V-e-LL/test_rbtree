from RBTree import *
global first_tree

first_tree = RBTree()


def main():
    first_tree = RBTree()
    print("Menu:")
    print("1. Insert")
    print("2. Search by index (i)")
    print("3. Search by key")
    print("4. Exit")
    print("------------------------------")
    while True:
        i = int(input("Select action: "))
        if i == 1:
            key = int(input("Enter a key: "))
            first_tree.insert(key)
        elif i == 2:
            index = int(input("Enter searching index: "))
            print("Key >> ", first_tree.os_select(first_tree.root, index))
        elif i == 3:
            value = int(input("Enter searching key: "))
            print("Index >> ", first_tree.os_rank(first_tree, value))
        elif i == 4:
            os.abort()
        else:
            print("ERROR! Wrong value.")


main()