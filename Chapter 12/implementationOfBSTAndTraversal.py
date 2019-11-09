#Linked List implementation of a binary tree and traversal of binary tree along with search, delete operations

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def enqueue(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(val)

    def dequeue(self):
        temp = self.head
        self.head = temp.next
        return temp.val

    def display(self):
        temp = self.head
        result = list()
        while temp:
            result.append(temp.val)
            temp = temp.next
        return result

    def isEmpty(self):
        if not self.head:
            return True
        return False


class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(val)

    def pop(self):
        temp = self.head
        if temp.next == None:
            self.head = None
        prev = temp
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None
        return temp.val

    def display(self):
        temp = self.head
        result = list()
        while temp:
            result.append(temp.val.val)
            temp = temp.next
        return result

    def isEmpty(self):
        if not self.head:
            return True
        return False


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree():
    def __init__(self):
        self.root = None

    def addNode(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            temp = self.root
            if val != temp.val:
                while True:
                    if val < temp.val:
                        prev = temp
                        temp = temp.left

                        if not temp:
                            prev.left = TreeNode(val)
                            break

                    elif val > temp.val:
                        prev = temp
                        temp = temp.right
                        if not temp:
                            prev.right = TreeNode(val)
                            break

    def searchNode(self, val):
        temp = self.root
        while temp:
            if val == temp.val:
                return True
            elif val < temp.val:
                temp = temp.left
            elif val > temp.val:
                temp = temp.right
        return False

    def deleteNode(self, node):
        if not self.root:
            print('No Tree exist')
        else:
            temp = self.root
            prev = temp
            right = False
            left = False
            while temp.val != node:
                prev = temp
                if temp.val > node:
                    right = False
                    left = True
                    temp = temp.left
                elif temp.val < node:
                    left = False
                    right = True
                    temp = temp.right
                if not temp:
                    break
            if not temp.right and not temp.left:
                if left:
                    prev.left = None
                elif right:
                    prev.right = None
            elif temp.right and not temp.left:
                if left:
                    prev.left = temp.right
                elif right:
                    prev.right = temp.right
            elif not temp.right and temp.left:
                if left:
                    prev.left = temp.left
                elif right:
                    prev.right = temp.left
            elif temp.right and temp.left:
                nextNode = temp.right
                prevNode = None
                while nextNode.left:
                    prevNode = nextNode
                    nextNode = nextNode.left
                value = nextNode.val
                if prevNode:
                    if nextNode.right:
                        prevNode.left = nextNode.right
                    else:
                        prevNode.left = None
                    temp.val = value
                else:
                    temp.val = value
                    temp.right = nextNode.right

    def displayBFS(self):
        temp = self.root
        queue = Queue()
        queue.enqueue(temp)
        result = list()
        while not queue.isEmpty():
            curr = queue.dequeue()
            result.append(curr.val)
            if curr.left:
                queue.enqueue(curr.left)
            if curr.right:
                queue.enqueue(curr.right)
        return result

    def displayDFSInOrder(self):
        print('******************')
        temp = self.root
        result = list()
        stck = Stack()
        while True:
            while temp:
                stck.push(temp)
                temp = temp.left
            if not temp and not stck.isEmpty():
                temp = stck.pop()
                result.append(temp.val)
                temp = temp.right
            if not temp and stck.isEmpty():
                break
        return result


def main():
    tree = BinaryTree()
    arr = [10, 5, 15, 7, 4, 12, 17, 22, 32, 2, 9]
    for each in arr:
        tree.addNode(each)

    print(tree.searchNode(5))
    print(tree.searchNode(25))
    print(tree.displayBFS())
    print(tree.displayDFSInOrder())
    print(tree.deleteNode(15))
    print(tree.displayBFS())


main()


