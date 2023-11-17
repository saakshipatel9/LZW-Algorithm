####  <b><i>Saakshi Patel (801361041)</b></i>

# ITCS 6112 Programming Project 1: Lempel-Ziv-Welch (LZW) Compression

## PROGRAM DESIGN

Here's an overview of the design:

### OVERALL STRUCTURE
#### <b>Module Imports</b>:

* `os`: Imported for interacting with the operating system.

* `utils`: Contains helper functions, specifically has_extension, used for checking file extensions.

#### <b>LZW Class</b>:

* `__init__(self, bit_length: int)`: Constructor initializing the LZW object with a specified bit length.

* `print_lzw_bytes(self, file_path: str)`: Method to print bytes of an .lzw file in binary format.

* `encode(self, file_path: str)`: Method to encode text from a .txt file using LZW compression.

* `decode(self, file_path: str)`: Method to decode a .lzw file back to its original text.

### DESIGN ELEMENTS

#### <b>File Extension Checking</b>:

* The `has_extension` function from the `utils` module is used to ensure correct file extensions for encoding, decoding, and printing binary data.

#### <b>Error Handling</b>:

*   It raises exceptions when encountering invalid file extensions or other potential errors during encoding or decoding operations.

#### <b>LZW Algorithm Implementation</b>:

* It utilizes a dictionary (`table`) to store mappings of symbols (characters or sequences) to their respective codes during encoding and decoding.

* It implements the LZW compression algorithm for encoding and the reverse process for decoding, using dictionary lookups to replace sequences with codes and vice versa.

#### <b>File I/O Operations</b>:

* It reads the input text or binary data from files and writes encoded/decoded data to new files with appropriate extensions (`lzw` for encoded data and `_decoded.txt` for decoded text).

### FLOW OF OPERATIONS:

#### <b>Argument Parsing</b>:

* The program takes command-line arguments using `argparse` to specify encoding, decoding, or printing binary data.

#### <b>LZW Class Usage</b>:

* Based on the command-line arguments, appropriate methods of the `LZW` class are invoked (`encode`, `decode`, or `print_lzw_bytes`).

#### <b>File Processing</b>:

* Read input data from `.txt` files, perform encoding, decoding, or printing of binary data, and write the results to new files.

### EXTENSIBILITY AND REUSABILITY:

* The LZW class design allows for easy extension by incorporating different functionalities related to LZW compression and decompression.

* The use of separate methods for encoding, decoding, and printing binary data enhances code readability and maintainability.

## DATA STRUCTURE DESIGN

Here's an outline of the data structures utilized in the provided code:

### DATA STRUCTURES USED:

#### <b> Dictionary (`table`)</b>:

* <b>Purpose</b>: To store mappings of symbols to their respective codes during encoding and decoding.
* <b>Structure</b>: It's a key-value pair data structure.
* <b>Implementation</b>: Initially populated with ASCII characters (256 entries), and it dynamically grows during encoding.
* <b>Operations</b>:
  * <b>During Encoding</b>: Adds new entries for encountered sequences that are not present in the dictionary.
  * <b>During Decoding</b>: Reconstructs the dictionary based on encoded data to decode symbols.

### ADDITIONAL STRUCTURES AND DATA HANDLING:

#### <b>Bytearray (`encoded_data`)</b>:

* <b>Purpose</b>: Stores the encoded data as a sequence of bytes during the encoding process.

* <b>Structure</b>: Linear sequence of bytes.

* <b>Implementation</b>: Appends bytes or byte pairs representing encoded symbols.

#### <b>Lists (`decoded_data`, `output_string`)</b>:

* <b>Purpose</b>: Temporary storage during the decoding process.

* <b>Structure</b>: Linear sequences.

* <b>Implementation</b>: Used to accumulate decoded symbols or sequences before constructing the final decoded text.

### DESIGN CONSIDERATION:

#### <b>Efficient Lookup and Update</b>:

* The dictionary (table) structure is crucial for efficient lookup and update operations during both encoding and decoding.

* Encoding relies on quickly accessing and updating entries for encountered sequences, while decoding reconstructs the dictionary based on the encoded data.

#### <b>Dynamic Data Handling</b>:

* The dictionary grows dynamically during encoding as new sequences are encountered and need to be assigned codes.

* Decoding involves dynamically reconstructing the dictionary from the encoded data.

### CONCLUSION:

The primary data structure, the dictionary (`table`), serves as the backbone for the LZW compression and decompression processes. Its dynamic nature allows for efficient storage and retrieval of encoded symbols and sequences. Additionally, supporting structures like byte arrays and lists aid in temporarily storing encoded or decoded data during the respective processes.

## FILE BREAKDOWN
The program is divided into three main files. 

* The first file, `lzw.py`, defines a Python class LZW that implements Lempel-Ziv-Welch compression and decompression algorithms.

* The second file, `main.py` contains the implementation of the command-line tool for encoding and decoding text importing the LZW algorithm from the first file, i.e. `lzw.py`.

* The third file, `utils.py` takes a file path and a target extension as inputs, checks if the file's extension matches the given target extension, and returns a boolean value indicating whether they match or not.

Also, the `data` folder includes the input `in.txt` file and will also contain the generated output `in_decoded.txt` file and `in.lzw` file.

## SUMMARY 

The program seems robust in many aspects, but there are areas where improvements or potential issues might arise.

### WORKS WELL:

#### <b>Functionality Implementation</b>:

* The program successfully implements LZW compression and decompression functionality.

* Encoding and decoding operations seem to work as intended, generating compressed .lzw files and decoding them back to the original text.

#### <b>Modular Design</b>:

* The code is structured using a class (`LZW`) that encapsulates related methods for encoding, decoding, and printing binary data. This supports code organization and reusability.

#### <b>Error Handling</b>:

* The program incorporates error handling by raising exceptions when encountering invalid file extensions or potential issues during encoding or decoding.

### POTENTIAL IMPROVEMENTS OR FAILURES:

#### <b>Testing and Edge Cases</b>:

* Ensuring robustness by testing with various input file sizes, edge cases (empty files, large files), and different file formats (besides `.txt` and `.lzw`) could strengthen the program's reliability.

#### <b>Efficiency and Optimization</b>:

* Depending on the scale of the input, optimizing the algorithm for memory usage or speed might be beneficial. Considerations for large files or optimizing dictionary operations could be explored.

#### <b>Extension Handling</b>:

* Currently, the program only handles `.txt` and `.lzw` extensions. Handling other file extensions or generic binary files could enhance its usability.

### SUMMARY:

The program works well in performing LZW compression and decompression tasks. Overall, it has a solid foundation but could benefit from refinement in certain areas for increased robustness and usability.

## PROGRAMMING LANGUAGE AND COMPILER VERSION

The project is coded in `Python` using version `Python 3.11.6`

## HOW TO RUN THE PROGRAM

It is a simple command line tool. You can see all options by running:

### SHOW HELP

```
$ python main.py --help

usage: main.py [-h] (-e ENCODE | -d DECODE | --print_lzw PRINT_LZW) [--bit_length BIT_LENGTH]

A simple LZW Encoder Decoder

options:
  -h, --help            show this help message and exit
  -e ENCODE, --encode ENCODE
                        Encode the input text
  -d DECODE, --decode DECODE
                        Decode the input text
  --print_lzw PRINT_LZW
                        Print out the .lwz file in 16 bit format.
  --bit_length BIT_LENGTH
                        Specify the bit length (default: 12)
```


### ENCODE A FILE
Only `.txt` files are accepted.

```
$ python main.py --encode data/in.txt --bit_length 12

Encoded Data saved at data/in.lzw
```

### DECODING A FILE
Only `.lzw` files are accepted.

```
$ python main.py --decode data/in.lzw --bit_length 12

Decoded data saved at data/in_decoded.txt
```

### PRINTING A LZW FILE
LZW files can be printed. The encoded output is saved in `16 bit format`.

```
$ python main.py --print_lzw data/in.lzw --bit_length 12

00000000 01100001 00000000 01100010 00000001 00000001 00000001 00000000 None
```

