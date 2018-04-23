# Explanation and Critique

## Code Organization
Primarily, all relevant code has been organized into two different modules.
- CoordinateTranslator.py
- Cigar.py

    ### Cigar.py
    Contains the Cigar class that can be initialized with either a CIGAR signature
    or the list of operations that such a signature describes. In theory, it 
    supports the extended CIGAR format although most testing has been limited 
    to the standard CIGAR format. 
    
    The Cigar() class defines two important methods. 
    1. `build_map(pos)` takes in a position attribute and builds a lean minimal 
    OrderedDictionary() whose contents are limited to key-value pairs that 
    represent the mapping between critical zero-based transcript coordinates and 
    corresponding reference coordinates. In this version, the map is maintained 
    in memory and has been tested against datasets with up until a million lines
    of data. Scalability beyond this is discussed below.The map building 
    operation is completed in O(n) time where n is the length of the CIGAR 
    string.
    2. `map(zero_based_pos)` takes in a zero based position on the transcript
    coordinate and returns the corresponding reference genome coordinate. In the
    event that an invalid input is provided, the program silently ignores it.
    However, if a coordinate that points to an insertion within the reference
    coordinate is provided, `-1` is returned indicating that there is not a unique
    counterpart. A number of other approaches are possible to address this
    case, however, in maintaining the expected format of the output file by 
    providing an integer value but at the same time attempting to distinguish such
    and alignment from a MATCH, `-1` was chosen. The map() function has a 
    theoretical upperbound of O(n), however is much faster in practice. If 
    greater efficiency is desired, for superior performance, binary search or 
    another search algorithm may be easily adapted since working on a sorted 
    dataset. It will however result is code complexity and decreased readability.
    
    ### CoordinateTranslator.py
    Contains the CoordinateTranslator() class that accepts input files described
    in the problem description. This module presents the wrapper specific to the 
    problem at hand as opposed to CIGAR.py which is generic to CIGAR strings.
    Two instance methods are defined.
    1. `process_transcripts_file()` operates on the transcripts input file and 
    iterates through it to build a custom data structure defined by `CoordinateTranslator.transcripts`.
    Essentially, it is a dictionary with the names of all transcripts defined in
    the transcripts file as keys. The value for any given key(transcript_id) in 
    `CoordinateTranslator.transcripts` is another dictionary with keys, one each
    for each reference sequence that it maps to. The value of this dictionary is
    a list of CIGAR objects from CIGAR.py, with each member in the list representing
    alignment at a distinct position of the transcript to the reference.
    2. `translate()` operates on the query file and calls out to `Cigar.map()`
    for actual reference mapping.

## Scalability
This solution requires maintaining the `CoordinateTranslator.transcripts` data
structure in memory. While it is built space-efficiently, this can quite easily
be a bottleneck when working with large files. To scale-up this data-structure
could either be stored on disk using a framework such as pytables while only
retrieving essential elements during query or alternatively employ a divide-and-conquer
approach by using a hashing scheme to direct data for any given transcript to a
bin identified by `hash(transcript_id)%number_of_bins`.

## Strengths
- Solution is object-oriented and representative of real-world operations.
- Separation of concerns between Cigar and CoordinateTranslator classes enables cleaner reusable code.
- The transcript file is effectively pre-processed. It can directly support a query API instead of a query file quite easily.
- One single data structure keeps track of all operations. This results in faster query response time.
- Use of collections data structures keep the code simple.
- Each line in each input file is not read more than once resulting in minimal I/O blockage.

## Weaknesses
 - The current implementation has high space-complexity. While the goal of the design is to enable fast query response and avoid repetitive work, storage on disk as discussed in the scalability section would be essential to support large files.
 - Mapping to an insertion area in the reference returns -1. While the reasoning for this choice has been explained above, there may be better alternatives to depict this.


## Other
- build_map() can be quickly adapted to support 5' to 3' alignments
- genomic_coordinate to transcript_coordinate mapping can also be supported by altering the data structure to invert both inner and outer key-value pairs.
- I tested with real-world data from 1000genomes project where by extracting CIGAR strings out of BAM files.

    