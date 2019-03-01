Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

    O(n) -- it makes two recursive calls in each step, but only if the corresponding child nodes exist. Thus, it should only run once for each node. (This is assuming that the given cb function is O(1). If the callback function itself has a higher order, it will slow down the depth-first search too.)

2. What is the space complexity of your `depth_first_for_each` function?

    O(n) -- because that's the space complexity of the binary search tree in the first place. With my recursive method, no additional data structure is needed to store anything.

3. What is the runtime complexity of your `breadth_first_for_each` method?

    O(n) -- again, it only runs once for each node, and checks whether nodes exist before trying to run anything for them.

4. What is the space complexity of your `breadth_first_for_each` method?

    O(n) -- in addition to the original binary search tree, my method uses a queue data structure. This queue will hold references to nodes in it, up to approximately half of n at a time, so this adds to the space complexity but doesn't move it to a higher-than-linear order.


5. What is the runtime complexity of the provided code in `names.py`?

    O(n**2) -- it has nested for loops that each traverse the entire names lists.

6. What is the space complexity of the provided code in `names.py`?

    O(n) -- it just has to hold the two names 

7. What is the runtime complexity of your optimized code in `names.py`?

    O(n log n) -- the expensive part of my optimized code is running two timsorts.

8. What is the space complexity of your optimized code in `names.py`?

    O(n) -- my (faster) solution doesn't have any data structures other than the given arrays, sorted. And timsort's space complexity is O(n), according to a Google search.