
For Text and other data types.
This program requires user input as a python file name, 
an input text file name and bit length through command line.
The files maybe taken as bytearray and then converted to string and 
then encoded.While decoding the string is decoded and then converted to
byte array and then store as the file.

Set the current directory to the location where the file is present.

TEXT-run python LZW_text.py <filename> <number of Bits>
Compression varies with the value of the number. 
 
Encoding:
The input data is encoded using the encoder.py file,
the dictionary of size 256 is built and initialized,
using the python dictionary data structure
in the dictionary, key are characters and values are the ascii values
the lzw compression algorithm is applied and we get the compressed data,
the program outputs the compressed data and stores it to an 
output file named inputFileName.lzw


Decoding:
The compressed data is decompressed using the decoder.py file,
the dictionary of size 256 is built and initialized,
using the python dictionary data structure
in the dictionary, key are characters and values are the ascii values
the lzw decompression algorithm is applied and we get the decompressed data,
the program outputs the decompressed data and stores it to an 
output file named inputFileName_decoded.txt


	

The program works well with both the examples provided on canvas, 
for other data the efficiency depends on the the repeating data values
and the size of data.
The Image conversion  to it's RGB values is of the internet.

For images-
Put the images in the folder images and
we can see the compressed file in teh compressed files folder,
 and the decompressed images in the decompressedfiles folder.
TO RUN-type LZW_image.py and then enter the imagefile name.(Make sure its the right format).  