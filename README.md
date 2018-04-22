# Coordinate Translator

This software was developed as a solution to the programming assignment described
[here](https://github.com/spadejac/U2FsdGVkX19c3IfNjlyyxNyniQpXP.Yp/blob/master/Exercise.pdf).
The general objective is to translate transcript coordinates to corresponding
reference coordinates given a CIGAR string and the position at which alignment
occurs.

## Installation

To install locally on your computer

```bash
git clone https://github.com/spadejac/U2FsdGVkX19c3IfNjlyyxNyniQpXP.Yp CoordinateTranslator
cd CoordinateTranslator
python2.7 setup.py install
```

*Note: Taking this approach to installation ensures appropriate installation of
prerequisites.*

## Running tests
From within the directory where package was installed (**CoordinateTranslator** 
if following installation instructions), run:
```bash
python2.7 CigarTests.py
```
The tests are intended to test against various CIGAR string formats and common
use of methods available. All tests should pass.

## Running
CoordinateTranslator is the executable and is expected to run from any location 
if properly installed. To see a help screen with options and arguments, run:

```CoordinateTranslator --help```

Example:
```
$ CoordinateTranslator --help
Usage: CoordinateTranslator [OPTIONS]

  A translator for zero-based transcript coordinates to reference
  coordinates

Options:
  --output_file FILENAME   Name for file to write results into  [required]
  --query_file PATH        Query file (2 column tab-separated  [required]
  --transcripts_file PATH  Transcripts file (4 column tab-separated)
                           [required]
  -h, --help               Show this message and exit.
```

### Sample data
Sample data is included within and can be located under the sample_data directory.
To run with included sample data, one could:
```CoordinateTranslator --transcripts_file sample_data/transcripts.example --query_file sample_data/query.example --output_file <output_file_name>```

Example:
```
$ CoordinateTranslator --transcripts_file sample_data/transcripts.example --query_file sample_data/query.example --output_file output.example
Reading transcripts file sample_data/transcripts.example
Analyzing transcripts file  [####################################]  100%
4 translation instances have been written into output.example
```

File Contents:
```
$ cat sample_data/transcripts.example 
TR1	CHR1	3	8M7D6M2I2M11D7M
TR2	CHR2	10	20M
$ cat sample_data/query.example 
TR1	4
TR2	0
TR1	13
TR2	10
$ cat output.example 
TR1	4	CHR1	7
TR2	0	CHR2	10
TR1	13	CHR1	23
TR2	10	CHR2	20
```

## Critique
[Explanation and Critique](https://github.com/spadejac/U2FsdGVkX19c3IfNjlyyxNyniQpXP.Yp/blob/master/Authors_Critique.md)



## Author

 - [Manoj Pillay](https://www.linkedin.com/in/manojpillay)

## License

This project is licensed under the MIT License. Please see [LICENSE](https://github.com/spadejac/U2FsdGVkX19c3IfNjlyyxNyniQpXP.Yp/blob/master/LICENSE) 
for details.

## Acknowledgments

- [StackOverflow](https://stackoverflow.com)
- [Click developers](https://github.com/pallets/click/graphs/contributors)