'''
Created on Apr 20, 2018

@author: pillay
'''

import unittest
from Cigar import Cigar

class CigarTests(unittest.TestCase):
    
    def testBasic(self):
        # TTACG--GATACATC
        #   ACGGGGAT   
        self.cg = Cigar([(3, 'M'), (2,'I'), (3,'M')])
        assert len(self.cg.build_map(2)) == 6
        self.cg.build_map(2)
        assert self.cg.map(2)  == 4
        assert self.cg.map(4)  == -1
        assert self.cg.map(6)  == 6
        
    def testStockExample(self):
        # ACTGTCATGTACGTTTAGCTAGCC--TAGCTAGGGACCTAGATAATTTAGCTAG
        #    GTCATGTA-------CTAGCCGGTA-----------AGATAAT

        self.cg = Cigar.fromString('8M7D6M2I2M11D7M')
        assert self.cg.cigar[0][0] == 8
        assert self.cg.cigar[5][0] == 11
        assert self.cg.cigar[6][0] == 7
        assert self.cg.cigar[0][1] == 'M'
        assert self.cg.cigar[5][1] == 'D'        
        assert len(self.cg.build_map(3)) == 10

        self.cg.build_map(3)
        assert self.cg.map(1)  == 4
        assert self.cg.map(4)  == 7
        assert self.cg.map(10)  == 20
        assert self.cg.map(13) == 23
        assert self.cg.map(14) == -1
        assert self.cg.map(16) == 24
        assert self.cg.map(24) == 43

    def test_padded_alignment(self):
        # CACGATCA**GACCGATACGTCCGA
        #     ATCA*AGACCGATAC
        self.cg = Cigar.fromString('4M1P1I9M')
        self.cg.build_map(4)
        assert self.cg.map(4) == -1
        assert self.cg.map(5) == 8
        assert self.cg.map(13) == 16
  
    def test_begin_with_soft_clipped(self):
        # A--AGCTAAA
        #  ccAG
        self.cg = Cigar.fromString('2S')
        self.cg.build_map(1)
        assert self.cg.map(0) == -1
        assert self.cg.map(1) == -1
        assert self.cg.map(2) == 1

    
    def test_quick(self):
        self.cg = Cigar.fromString('2D4M')
        self.cg.build_map(1)
        try:
            for i in range(14):
                print "{}:{}".format(i,self.cg.map(i))
        except KeyError:
            pass
        
            
if __name__ == '__main__':
    unittest.main()