from heapq import heapify, heappop, heappush

class MedianFinder:

    """

    maintain a maxheap o every element to the left
    min heap of every elem to the right

    1

    1 3

    we add to heaps and push/pop based on the heap lengths
    that is the basic idea anyway

    the rule we need to enforce is this: 

    if we ever encounter
    
    """

    def __init__(self):

        self.num_elems = 0
        self.leftheap = []
        self.rightheap = []

        return None
        

    def addNum(self, num: int) -> None:

        if len(self.leftheap) < len(self.rightheap):

            heappush(self.leftheap, -num)
            leftmax = heappop(self.leftheap)

            leftmax = -leftmax

            heappush(self.rightheap, leftmax)

            rightmin = heappop(self.rightheap)

            heappush(self.leftheap, -rightmin)

        elif len(self.leftheap) == len(self.rightheap):

            heappush(self.leftheap, -num)
            leftmax = heappop(self.leftheap)

            leftmax = -leftmax

            # In this way, rightheap always has one more element.
            heappush(self.rightheap, leftmax)

        self.num_elems += 1

        return None
        

    def findMedian(self) -> float:

        if len(self.rightheap) > len(self.leftheap):
            return self.rightheap[0]

        else:
            r = self.rightheap[0]
            l = self.leftheap[0]

            left = -l

            return (r + left)/2

        return 0
        
        