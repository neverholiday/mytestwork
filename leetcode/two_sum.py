#!/usr/bin/env python
#   Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__( self ):
        isNone = False
        nextNode = self
        strOutput = ""
        while isNone is False:
            val = nextNode.val
            strOutput = strOutput + " {} ".format( val )
            nextNode = nextNode.next
            if nextNode is None:
                isNone = True
            else:
                strOutput = strOutput + " -> "
        
        return strOutput

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        #   get value        
        firstValue = self.getValueFromLinkList( l1 )
        secondValue = self.getValueFromLinkList( l2 )

        #   adddition operation
        answerValue = firstValue + secondValue

        #   change to link list

        return answerValue

    def getValueFromLinkList( self, linkList ):
        """
        get value from link list
        """
        
        #   initial value
        value = 0
        currentValue = 0
        multiplyFactor = 1
        isNodeNone = False

        while isNodeNone is False:

            #   get current value
            currentValue = linkList.val

            #   get next node
            linkList = linkList.next
            
            #   terminate loop when node is None
            if linkList == None:
                isNodeNone = True

            #   construct decimal value
            value = ( currentValue * multiplyFactor ) + value

            #   scale up ten times
            multiplyFactor *= 10
        
        return value

if __name__ == '__main__':

    #   (2 -> 4 -> 3)
    parent1 = ListNode( 2 )
    node2 = ListNode( 4 )
    node3 = ListNode( 3 )
    parent1.next = node2
    node2.next = node3

    #   (5 -> 6 -> 4)
    parent2 = ListNode( 5 )
    node5 = ListNode( 6 )
    node6 = ListNode( 4 )
    parent2.next = node5
    node5.next = node6

    #   define solution
    solv = Solution()
    val1 = solv.getValueFromLinkList( parent1 )
    val2 = solv.getValueFromLinkList( parent2 )

    result = solv.addTwoNumbers( parent1, parent2 )

    print "{} : Value 1 = {}".format( parent1, val1 )
    print "{} : Value 2 = {}".format( parent2, val2 )
    print "{} + {} = {}".format( parent1, parent2, result )
    

