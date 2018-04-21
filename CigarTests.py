'''
Created on Apr 20, 2018

@author: pillay
'''

import unittest

from Cigar import Cigar

class CigarTests(unittest.TestCase):
    def setUp(self):
        self.cg = Cigar.fromString('8M7D6M2I2M11D7M')
    
    def testInit(self):
        assert self.cg.cigar[0][0] == 8
        assert self.cg.cigar[5][0] == 11
        assert self.cg.cigar[6][0] == 7
        assert self.cg.cigar[0][1] == 'M'
        assert self.cg.cigar[5][1] == 'D'
        
    def test_build_map(self):
        assert len(self.cg.build_map(3)) == 10        
    
    def test_map(self):
        self.cg.build_map(3)
        assert self.cg.map(1)  == 4
        assert self.cg.map(4)  == 7
        assert self.cg.map(10)  == 20
        assert self.cg.map(13) == 23
        assert self.cg.map(14) == -1
        assert self.cg.map(16) == 24
        assert self.cg.map(24) == 43
            
if __name__ == '__main__':
    unittest.main()        