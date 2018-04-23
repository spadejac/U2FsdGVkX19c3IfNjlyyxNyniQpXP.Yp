#!/usr/bin/env python
'''
Created on Apr 18, 2018

@author: pillay
'''

import click
from collections import defaultdict

from Cigar import Cigar

class CoordinateTranslator(object):
    def __init__(self, transcripts_file, query_file):
        self.transcripts_file = transcripts_file
        self.query_file = query_file
        self.transcripts = defaultdict(lambda : defaultdict(list))
    
    def process_transcripts_file(self):
        lineCount = (sum(1 for line in open(self.transcripts_file)))
        with open(self.transcripts_file, 'rb') as data:
            click.echo("Reading transcripts file {}".format(self.transcripts_file))
            with click.progressbar(data, 
                                   label='Analyzing transcripts file',
                                   length=lineCount) as bar:
                for line in bar:
                    tr_name, chr_name, start, cigar_str = line.strip().split('\t')
                    try: 
                        cigar = Cigar.fromString(cigar_str)
                        cigar.build_map(int(start))
                        self.transcripts[tr_name][chr_name].append(cigar)
                    except IndexError:
                        continue
        
    def translate(self, outfile):
        mapCount = 0
        for line in open(self.query_file):
            tr_name, zero_pos = line.strip().split()
            for ref in self.transcripts[tr_name]:
                cigars = self.transcripts[tr_name][ref]
                for cigar in cigars:
                    ref_coord = cigar.map(int(zero_pos))
                    if ref_coord:
                        outfile.write( '\t'.join([tr_name, zero_pos, ref, 
                                                  str(ref_coord)
                                                  ]) + '\n' )
                        mapCount += 1
                        
                    
        if mapCount:
            print ("{} translation instances have been written into {}".format(mapCount, outfile.name))
        else:
            print ("No mappings found - output file {} not written".format(outfile.name))


@click.option('--transcripts_file', required=True, type=click.Path(exists=True),
              help='Transcripts file (4 column tab-separated)')
@click.option('--query_file', required=True, type=click.Path(exists=True),
              help='Query file (2 column tab-separated')
@click.option('--output_file', required=True, type=click.File(mode='w'),
              help='Name for file to write results into')
@click.command(context_settings=dict(
    ignore_unknown_options=True,
    help_option_names=[ '-h', '--help'],
))
def cli(transcripts_file, query_file, output_file):
    '''
    A translator for zero-based transcript coordinates to reference coordinates
    '''
    
    ct = CoordinateTranslator(transcripts_file, query_file)
    ct.process_transcripts_file()
    ct.translate(output_file)

if __name__ == '__main__':
    cli()
