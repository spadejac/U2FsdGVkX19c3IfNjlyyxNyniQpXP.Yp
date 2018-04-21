'''
Created on Apr 20, 2018

@author: pillay
'''

from collections import OrderedDict

class Cigar(object):
    def __init__(self, cigar=[]):
        self.cigar = cigar
        self.cigar_dict = OrderedDict()

    def __repr__(self):
        return '{}'.format([''.join(str(op[0])+op[1] for op in self.cigar)])
    
    @classmethod
    def fromString(klass, cigar_as_str):
        '''
        Converts a CIGAR string into its corresponding 
        CIGAR list of tuples representation
        :rtype: List[ tuple[ int ]]
        '''
        cigar_list = []
        buf = ''
        for c in cigar_as_str:
            if c  in ['M', 'I', 'D']:
                cigar_list.append((int(buf), c))
                buf = ''
            else:
                buf += c

        return klass(cigar_list) 
    
        
    def build_map(self, pos):
        '''
        :type pos: int
        :rtype: Dict
        Returns an ordered dictionary data structure representing 
        the map between 0-centric values and `pos`-centric values.
        The returned object is a lean minimal dictionary which
        limits its contents to pivotal values.
        '''
        if self.cigar_dict:
            # Truncate if already exists
            self.cigar_dict = OrderedDict()
        
        self.cigar_dict[0] = pos

        for offset, op in self.cigar:

            last_key = next(reversed(self.cigar_dict))
            last_val = self.cigar_dict[last_key]
            
            if op == 'M':
                self.cigar_dict [ last_key+offset-1 ] = last_val + offset - 1
            if op == 'D':
                self.cigar_dict [ last_key +1 ] = last_val + offset + 1
            if op == 'I':
                for i in range(offset):
                    self.cigar_dict [ last_key + i + 1] = -1
                self.cigar_dict [last_key + offset + 1] = last_val + 1
        
        print self.cigar_dict
        return self.cigar_dict
                    
    
    def map(self, zero_based_pos):
        if not self.cigar_dict:
            raise ValueError('Need to call build_map() to initialize first')
        if zero_based_pos < 0:
            raise KeyError('Invalid query coordinate')
        
        x = zero_based_pos
        while x not in self.cigar_dict:
            x -= 1
        return self.cigar_dict[x] + zero_based_pos - x        
