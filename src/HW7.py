# TASK 1
# Create a class that implements a binary search tree and can perform basic operations such as insertion,
# deletion, and searching.

class BinarySearchTree:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def insert(self, key):
        if self.key is None:
            self.key = key
            return
        if self.key == key:
            return
        if key < self.key:
            if self.left is None:
                self.left = BinarySearchTree(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = BinarySearchTree(key)
            else:
                self.right.insert(key)

    def search(self, key):
        if key < self.key:
            if self.left is None:
                return False
            return self.left.search(key)
        elif key > self.key:
            if self.right is None:
                return False
            return self.right.search(key)
        else:
            return True

    def delete(self, key):
        if self is None:
            return self
        if key < self.key:
            if self.left:
                self.left = self.left.delete(key)
            return self
        if key > self.key:
            if self.right:
                self.right = self.right.delete(key)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_right = self.right
        while min_right.left:
            min_right = min_right.left
        self.key = min_right.key
        self.right = self.right.delete(min_right.key)
        return self

    def print(self):
        if self.left:
            self.left.print()
        print(self.key)
        if self.right:
            self.right.print()


# bst = BinarySearchTree(10)
# print("Insert")
# bst.insert(5)
# bst.insert(4)
# bst.insert(6)
# bst.print()
# print(bst.search(10))
# print("Delete")
# bst.delete(5)
# bst.print()

# TASK 2
# Create a class that implements a red black tree and can perform basic operations such as insertion,
# deletion, and searching.


class RedBlackTree:

    class Node:
        def __init__(self, key = None, color = 'RED'):
            self.right = None
            self.left = None
            self.p = None
            self.key = key
            self.color = color

    def __init__(self):
        self.NIL = self.Node(key = None, color='BLACK')
        self.root = self.NIL
        self.ordered = []
        pass

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.p = x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.p = x
        y.p = x.p
        if x.p == self.NIL:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x
        x.p = y

    def insert(self, z):
        new_node = self.Node(key = z)
        y = self.NIL
        x = self.root
        while x != self.NIL:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right
        new_node.p = y
        if y == self.NIL:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node
        new_node.left = self.NIL
        new_node.right = self.NIL
        new_node.color = "RED"
        self.rb_insert_fixup(new_node)

    def rb_insert_fixup(self, z):
        while z.p.color == "RED":
            if z.p == z.p.p.left:
                y = z.p.p.right
                if y.color == 'RED':
                    z.p.color = "BLACK"
                    y.color = "BLACK"
                    z.p.p.color = "RED"
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.left_rotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.right_rotate(z.p.p)
            else:
                y = z.p.p.left
                if y.color == 'RED':
                    z.p.color = "BLACK"
                    y.color = "BLACK"
                    z.p.p.color = "RED"
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.right_rotate(z)
                    z.p.color = 'BLACK'
                    z.p.p.color = 'RED'
                    self.left_rotate(z.p.p)
        self.root.color = 'BLACK'

    def remove(self, z):
        node = self.search(z)
        y = node
        initial_color = y.color
        if node.left == self.NIL:
            x = node.right
            if node.p == self.NIL:
                self.root = node.right
            elif node == node.p.left:
                node.p.left = node.right
            else:
                node.p.right = node.right
            node.right.p = node.p
        elif node.right == self.NIL:
            x = node.left
            if node.p == self.NIL:
                self.root = node.right
            elif node == node.p.left:
                node.p.left = node.right
            else:
                node.p.right = node.right
            node.right.p = node.p
        else:
            temp = node.right
            while temp.left != self.NIL:
                temp = temp.left
            y = temp
            initial_color = y.color
            x = y.right
            if y.p == node:
                x.p = y
            else:
                if y.p == self.NIL:
                    self.root = y.right
                elif y == y.p.left:
                    y.p.left = y.right
                else:
                    y.p.right = y.right
                y.right.p = y.p

                y.right = node.right
                y.right.p = y
            if node.p == self.NIL:
                self.root = y
            elif node == node.p.left:
                node.p.left = y
            else:
                node.p.right = y
            y.p = node.p
            y.left = node.left
            y.left.p = y
            y.color = node.color
        if initial_color == 'BLACK':
            self.rb_delete_fixup(x)

    def rb_delete_fixup(self, x):
        while x != self.root and x.color == 'BLACK':
            if x == x.p.left:
                w = x.p.right
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.p.color = 'RED'
                    self.left_rotate(x.p)
                    w = x.p.right
                if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                    w.color = 'RED'
                    x = x.p
                else:
                    if w.right.color == 'BLACK':
                        w.left.color = 'BLACK'
                        w.color = 'RED'
                        self.right_rotate(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.p.color = 'RED'
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.right.color == 'BLACK' and w.left.color == 'BLACK':
                    w.color = 'RED'
                    x = x.p
                else:
                    if w.left.color == 'BLACK':
                        w.right.color = 'BLACK'
                        w.color = 'RED'
                        self.left_rotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = 'BLACK'
                    w.left.color = 'BLACK'
                    self.right_rotate(x.p)
                    x = self.root
        x.color = 'BLACK'

    def search(self, x):
        return self.__search(self.root, x)

    def __search(self, node, x):
        if node == self.NIL:
            return None
        elif x == node.key:
            return node
        elif x < node.key:
            return self.__search(node.left, x)
        else:
            return self.__search(node.right, x)


# TASK 3
# Write a function that implements a merge sort algorithm.

def merge(arr, l, m, r):
    i = l
    j = m + 1
    while i <= m + 2 and j <= r:
        if arr[i] < arr[j]:
            i += 1
        else:
            temp = arr[j]
            k = j - 1
            while k >= i:
                arr[k + 1] = arr[k]
                k -= 1
            arr[i] = temp
            j += 1


def mergeSort(arr, l, r):
    if l < r:
        m = l + (r - l) // 2

        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)


def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i], end = ' ')


arr = [7, 2, 9, 3, 1, 5]
# print("Before Merge Sort")
# print_arr(arr)
# mergeSort(arr, 0, len(arr) - 1)
# print()
# print('After Merge Sort')
# print_arr(arr)

# TASK 4
# Write a function that implements an insertion sort algorithm.


def insertionSort(arr):
    if (len(arr)) <= 1:
        return
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# print()
# print('Before Insertion Sort')
# print_arr(arr)
# insertionSort(arr)
# print()
# print('After Insertion Sort')
# print_arr(arr)
# print()

# TASK 5
# Write a function that implements a sorting algorithm in linear time.


def countingSort(arr):
    maximum = int(max(arr))
    minimum = int(min(arr))
    length = maximum - minimum + 1

    count_arr = [0 for _ in range(length)]
    output_arr = [0 for _ in range(len(arr))]

    for i in range(0, len(arr)):
        count_arr[arr[i] - minimum] += 1

    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - minimum] - 1] = arr[i]
        count_arr[arr[i] - minimum] -= 1

    for i in range(0, len(arr)):
        arr[i] = output_arr[i]


# arr = [-1, 3, 3, 8, -5, -3, 1]
# print("Before Counting Sort")
# print(arr)
# countingSort(arr)
# print("After Counting Sort")
# print(arr)