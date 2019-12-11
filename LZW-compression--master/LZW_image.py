from LZW import LZW
import base64
import os
import io

from array import array
from PIL import Image

import sys
from sys import argv
import struct
from struct import *
from LZW import LZW
import os

print("Enter File name")
input_file = input()
compressor = LZW(os.path.join("Images",input_file+".tif"))
compressor.compress()

decompressor = LZW(os.path.join("CompressedFiles",input_file+"Compressed.lzw"))
decompressor.decompress()