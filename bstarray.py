# bst from array
# take in a sorted array
# find the middle index
# check if your target value is greater then or less then the index in the array
# pass in the the upperhalf or the lowerhalf recursivly 
# if you found it return
# hieght value 

class BinaryTreeNode:
  def ___init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def inOrder(self):
    print(self.value)
    if self.left != None:
      self.left.inOrder()
    if self.right != None:
      self.right.inOrder()

  def insert(self, arr):
    # find the middle 
    middle = len(arr)//2
    # create a node
    print(arr)
    self.value = arr[middle]
    # on the branches return self.insert
    if len(arr) > 1:
      self.left = self.insert(arr[middle:])
      self.right = self.insert(arr[:middle])
    print(self.value, self.left.value, self.right.value)
    # return Node
    return self






sorted_array = [1, 2, 3, 4, 5, 6, 7]

# find the middle 
bst = BinaryTreeNode()
print(bst.insert(sorted_array))
# bst.inOrder()
