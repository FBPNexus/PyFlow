from numpy import sign

from PyFlow.Core import(
    FunctionLibraryBase,
    IMPLEMENT_NODE
)
from PyFlow.Core.AGraphCommon import *

class IntLib(FunctionLibraryBase):
    '''doc string for IntLib'''
    def __init__(self,packageName):
        super(IntLib, self).__init__(packageName)

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={'Category': 'Math|Int', 'Keywords': ['+', 'append']})
    ## Sum of two ints
    def add(a=('IntPin', 0), b=('IntPin', 0)):
        '''
        Sum of two ints
        '''
        return a + b

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={'Category': 'Math|Bits manipulation', 'Keywords': []})
    def bitwiseAnd(a=('IntPin', 0), b=('IntPin', 0)):
        '''
        Bitwise AND (A & B)
        '''
        return a & b

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={'Category': 'Math|Bits manipulation', 'Keywords': []})
    def bitwiseNot(a=('IntPin', 0)):
        '''
        Bitwise NOT (~A)
        '''
        return ~a

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={'Category': 'Math|Bits manipulation', 'Keywords': []})
    def bitwiseOr(a=('IntPin', 0), b=('IntPin', 0)):
        '''
        Bitwise OR (A | B)
        '''
        return a | b

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={'Category': 'Math|Bits manipulation', 'Keywords': []})
    def bitwiseXor(a=('IntPin', 0), b=('IntPin', 0)):
        '''
        Bitwise XOR (A ^ B)
        '''
        return a ^ b

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={'Category': 'Math|Bits manipulation', 'Keywords': []})
    def binaryLeftShift(a=('IntPin', 0), b=('IntPin', 0)):
        '''
        Binary left shift a << b
        '''
        return a << b

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={'Category': 'Math|Bits manipulation', 'Keywords': []})
    def binaryRightShift(a=('IntPin', 0), b=('IntPin', 0)):
        '''
        Binary right shift a << b
        '''
        return a >> b

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={'Category': 'Math|Bits manipulation', 'Keywords': []})
    def testBit(intType=('IntPin', 0), offset=('IntPin', 0)):
        '''
        Returns a nonzero result, 2**offset, if the bit at 'offset' is one
        '''
        mask = 1 << offset
        return(intType & mask)

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={'Category': 'Math|Bits manipulation', 'Keywords': []})
    def setBit(intType=('IntPin', 0), offset=('IntPin', 0)):
        '''
        Returns an integer with the bit at 'offset' set to 1'
        '''
        mask = 1 << offset
        return(intType | mask)

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={'Category': 'Math|Bits manipulation', 'Keywords': []})
    def clearBit(intType=('IntPin', 0), offset=('IntPin', 0)):
        '''
        Returns an integer with the bit at 'offset' cleared.
        '''
        mask = ~(1 << offset)
        return(intType & mask)

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={'Category': 'Math|Bits manipulation', 'Keywords': []})
    def toggleBit(intType=('IntPin', 0), offset=('IntPin', 0)):
        '''
        Returns an integer with the bit at 'offset' inverted, 0 -> 1 and 1 -> 0.
        '''
        mask = 1 << offset
        return(intType ^ mask)

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={'Category': 'Math|Int', 'Keywords': []})
    def selectInt(A=('IntPin', 0), B=('IntPin', 0), PickA=('BoolPin', False)):
        '''
        If bPickA is true, A is returned, otherwise B is
        '''
        return A if PickA else B

    @staticmethod
    @IMPLEMENT_NODE(returns=('IntPin', 0), meta={'Category': 'Math|Int', 'Keywords': []})
    def sign(a=('IntPin', 0)):
        '''
        Sign (integer, returns -1 if A &lt; 0, 0 if A is zero, and +1 if A &gt; 0)
        '''
        return sign(a)
