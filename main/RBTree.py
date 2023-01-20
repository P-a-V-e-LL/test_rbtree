from Node import *
from termcolor import colored


class RBTree:
    def __init__(self):
        self.root = None

    def fix_size(self, node):
        while node != self.root:
            node.fix()
            node = node.parent
            self.fix_size(node)
        else:
            node.fix()

    def print_root(self):
        print(self.root.key, self.root.size, self.root.red)

    def left_rotate(self, node):
        print("LEFT ROTATE ", node.key)
        y = node.right
        node.right = y.left
        if y.left != None:
            y.left.parent = node
        p = node.parent
        y.parent = p
        if node == self.root:
            self.root = y
            print("New root >> {0}".format(y.key))
        elif node == p.left:
            p.left = y
        elif node == p.right:
            p.right = y

        y.left = node
        node.parent = y
        # size
        y.size = node.size
        if node.right != None and node.left != None:
            node.size = node.right.size + node.left.size + 1
        elif node.right == None and node.left != None:
            node.size = node.left.size + 1
        elif node.right != None and node.left == None:
            node.size = node.right.size + 1
        else:
            node.size = 1

    def right_rotate(self, node):
        print("RIGHT ROTATE ", node.key)
        y = node.left
        node.left = y.right
        if y.right != None:
            y.right.parent = node
        p = node.parent
        y.parent = p
        if node == self.root:
            self.root = y
            print("New root >> {0}".format(y.key))
        elif node == p.left:
            p.left = y
        elif node == p.right:
            p.right = y

        y.right = node
        node.parent = y
        # size
        y.size = node.size
        if node.right != None and node.left != None:
            node.size = node.right.size + node.left.size + 1
        elif node.right == None and node.left != None:
            node.size = node.left.size + 1
        elif node.right != None and node.left == None:
            node.size = node.right.size + 1
        else:
            node.size = 1

    def search(self, key):
        current_node = self.root
        while current_node is not None and key != current_node.key:
            if key < current_node.key:
                current_node = current_node.left
            else:
                current_node = current_node.right
        # print('Parent {} is {}'.format(current_node.key, current_node.parent.key))
        #print(colored(current_node.key, 'red'))
        return current_node

    def insert(self, key):  
        node = Node(key)                                #1
        # Base Case - Nothing in the tree
        if self.root is None:                           #2
            node.red = False                            #3
            self.root = node                            #3
            print('ROOT IS - {0}'.format(self.root.key))#3
            return                                      #15
        last_node = self.root                           #4
        while last_node is not None:                    #5
            potential_parent = last_node                #6
            if node.key < last_node.key:                #7
                last_node = last_node.left              #8
            else:                                       #9
                last_node = last_node.right             #9
        # Assign parents and siblings to the new node
        node.parent = potential_parent                  #10
        print('NODE KEY- {0} NODE PARENT - {1} '.format(node.key,
                                                      node.parent.key))#10
        if node.key < node.parent.key:                  #11
            node.parent.left = node                     #12
            print('GO LEFT < NODE PARENT PARENT LEFT KEY - ',
                  node.parent.key)                      #12
        else:                                           #13
            node.parent.right = node                    #13
            print('GO RIGHT > NODE PARENT PARENT RIGHT KEY - ',
                  node.parent.key)                      #13
        node.left = None                                #14
        node.right = None                               #14
        f = node.parent                                 #14
        self.fix_size(f)                                #14
        self.fix_tree(node)                             #14

    def fix_tree(self, node):
        print('NODE PARENT RED - {}'.format(node.parent.red))
        try:
            while node is not self.root and node.parent.red is True:
                print('FIX>> NODE KEY - {} '
                      'NODE PARENT KEY - {} '.format(node.key, node.parent.key))
                if node.parent == node.parent.parent.left: # если отец является левым сыном
                   try:
                       uncle = node.parent.parent.right  # то дядя - правый сын деда
                       print('[LEFT] UNCLE RED - {} '
                             'UNCLE KEY - {} PARENT PARENT KEY - {}'.format(uncle.red, uncle.key, node.parent.parent.key))
                       if uncle.red:  # case 1 красный дядя
                           node.parent.red = False
                           uncle.red = False
                           node.parent.parent.red = True
                           node = node.parent.parent
                           if node != self.root:
                               print('NODE RED - {} UNCLE RED - {} PARENT RED - '
                                     '{}'.format(
                                   colored(node.red, 'red',
                                           attrs=['reverse', 'blink']),
                                   colored(uncle.red, 'yellow',
                                           attrs=['reverse', 'blink']),
                                   colored(node.parent.red, 'yellow',
                                           attrs=['reverse', 'blink'])))
                           else:
                               print('NODE IS ROOT')
                       else:
                           if node == node.parent.right:
                               # This is Case 2
                               print('in TEST>>>>', node.key)
                               node = node.parent
                               print('AFTER TEST>>>>', node.key)
                               self.left_rotate(node)
                           # This is Case 3
                           node.parent.red = False
                           node.parent.parent.red = True
                           self.right_rotate(node.parent.parent)

                   except AttributeError:
                       print("No uncle")
                       if node == node.parent.right:
                           # This is Case 2
                           print('in TEST>>>>', node.key)
                           node = node.parent
                           print('AFTER TEST>>>>', node.key)
                           self.left_rotate(node)
                       # This is Case 3
                       node.parent.red = False
                       node.parent.parent.red = True
                       self.right_rotate(node.parent.parent)
                       continue

                else:
                    try:
                        uncle = node.parent.parent.left
                        print('[RIGHT] UNCLE RED - {} '
                              'UNCLE KEY - {}'.format(uncle.red, uncle.key))
                        if uncle.red:
                            #  Case 1
                            node.parent.red = False
                            uncle.red = False
                            node.parent.parent.red = True
                            node = node.parent.parent
                            if node != self.root:
                                print('NODE RED - {} UNCLE RED - {} PARENT RED - '
                                      '{}'.format(
                                    colored(node.red, 'red',
                                            attrs=['reverse', 'blink']),
                                    colored(uncle.red, 'yellow',
                                            attrs=['reverse', 'blink']),
                                    colored(node.parent.red, 'yellow',
                                            attrs=['reverse', 'blink'])))
                            else:
                                print('NODE IS ROOT')
                        else:
                            if node == node.parent.left:
                                # This is Case 2
                                print('in TEST>>>>', node.key)
                                node = node.parent
                                print('AFTER TEST>>>>', node.key)
                                self.right_rotate(node)
                            # This is Case 3
                            node.parent.red = False
                            node.parent.parent.red = True
                            self.left_rotate(node.parent.parent)

                    except AttributeError:
                        print("No Uncle")
                        if node == node.parent.left:
                            # This is Case 2
                            print('in TEST>>>>', node.key)
                            node = node.parent
                            print('AFTER TEST>>>>', node.key)
                            self.right_rotate(node)
                        # This is Case 3
                        node.parent.red = False
                        node.parent.parent.red = True
                        self.left_rotate(node.parent.parent)
                        continue

            #self.root.red = False
        except AttributeError:
            print("\n\nTree BUILT")
        self.root.red = False

    def os_select(self, root, i):
        try:
            if root.left != None:                       #2
                r = root.left.size + 1                  #3
            else:                                       #4
                r = 1                                   #4
            if i == r:                                  #5
                return root.key                         #6
            elif i < r:                                 #7
                return self.os_select(root.left, i)     #8
            else:                                       #9
                return self.os_select(root.right, i - r)#9
        except AttributeError:                          #10
            print("ERROR! OUT OF RANGE!")               #10

    def os_rank(self, tree, x):
        node = tree.search(x)                        # 1
        if node.left != None:                        # 2
            r = node.left.size + 1                   # 3
        else:                                        # 4
            r = 1                                    # 4
        y = node                                     # 5
        while y != tree.root:                        # 6
            if y == y.parent.right:                  # 7
                if y.parent.left != None:            # 8
                    r = r + y.parent.left.size + 1   # 9
                else:                                # 10
                    r = r + 1                        # 10
            y = y.parent                             # 11
        return r                                     # 12