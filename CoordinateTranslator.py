#!/usr/bin/env python
'''
Created on Apr 18, 2018

@author: pillay
'''

import click
import time

class CoordinateTranslator(object):
    def __init__(self, transcripts_file, query_file):
        self.transcripts_file = transcripts_file
        self.query_file = query_file
    
    
    def process_transcripts_file(self):
        for line in open(self.transcripts_file):
            tr_name, chr_name, start, cigar = line.split('\t')
            print tr_name, chr_name, start, cigar
        
#         with click.progressbar(open(self.transcripts_file)) as bar:
#             for line in bar:
#                 tr_name, chr_name, start, cigar = line.split('\t')
#                 time.sleep(2)
        
    

@click.option('--transcripts_file', required=True, type=click.Path(exists=True),
              help='Transcripts file (4 column tab-separated)')
@click.option('--query_file', required=True, type=click.Path(exists=True),
              help='Query file (2 column tab-separated')
@click.command(context_settings=dict(
    ignore_unknown_options=True,
    help_option_names=[],
))
def cli(transcripts_file, query_file):
    '''
    Command line interface with options
    '''
    ct = CoordinateTranslator(transcripts_file, query_file)
    ct.process_transcripts_file()
    
    
        
if __name__ == '__main__':
    cli()