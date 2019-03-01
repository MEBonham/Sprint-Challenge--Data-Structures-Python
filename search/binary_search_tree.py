class Queue:
  def __init__(self):
    self.storage = []

  def enqueue(self, val):
    self.storage.append(val)

  def dequeue(self):
    if len(self.storage) == 0:
      return None
    return self.storage.pop(0)

  def size(self):
    return len(self.storage)


class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.depth_first_for_each(cb)
    if self.right:
      self.right.depth_first_for_each(cb)

  def breadth_first_for_each(self, cb, q=Queue()):
    cb(self.value)
    if self.left:
      q.enqueue(self.left)
    if self.right:
      q.enqueue(self.right)
    if q.size() > 0:
      q.dequeue().breadth_first_for_each(cb, q)


  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
