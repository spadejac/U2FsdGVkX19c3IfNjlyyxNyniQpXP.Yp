#!/usr/bin/env python
'''
Created on Apr 18, 2018

@author: pillay
'''

import click
import time
from collections import defaultdict


from pprint import pprint

from Cigar import Cigar

class CoordinateTranslator(object):
    def __init__(self, transcripts_file, query_file):
        self.transcripts_file = transcripts_file
        self.query_file = query_file
        self.transcripts = defaultdict(lambda : defaultdict(list))
    
    def process_transcripts_file(self):
#         for line in open(self.transcripts_file):
#             tr_name, chr_name, start, cigar_str = line.strip().split('\t')
#             try: 
#                 cigar = Cigar.fromString(cigar_str)
#                 cigar.build_map(int(start))
#                 self.transcripts[tr_name][chr_name].append(cigar)
#             except IndexError:
#                 continue
        
        
        with open(self.transcripts_file) as data:
            with click.progressbar(data, 
                                   label='Processing',
                                   ) as bar:
                for line in bar:
                    tr_name, chr_name, start, cigar_str = line.strip().split('\t')
                    try: 
                        cigar = Cigar.fromString(cigar_str)
                        cigar.build_map(int(start))
                        self.transcripts[tr_name][chr_name].append(cigar)
                    except IndexError:
                        continue
        #pprint(self.transcripts)
        
    def translate(self, outfile):
        for line in open(self.query_file):
            tr_name, zero_pos = line.strip().split()
            for ref in self.transcripts[tr_name]:
                cigars = self.transcripts[tr_name][ref]
                for cigar in cigars:
                    outfile.write( '\t'.join([tr_name, zero_pos, ref, 
                                              str(cigar.map(int(zero_pos)))
                                              ]) + '\n' )
                    
            

@click.option('--transcripts_file', required=True, type=click.Path(exists=True),
              help='Transcripts file (4 column tab-separated)')
@click.option('--query_file', required=True, type=click.Path(exists=True),
              help='Query file (2 column tab-separated')
@click.option('--output_file', required=True, type=click.File(mode='w'))
@click.command(context_settings=dict(
    ignore_unknown_options=True,
    help_option_names=[],
))
def cli(transcripts_file, query_file, output_file):
    '''
    Command line interface with options
    '''
    ct = CoordinateTranslator(transcripts_file, query_file)
    ct.process_transcripts_file()
    ct.translate(output_file)

if __name__ == '__main__':
    cli()