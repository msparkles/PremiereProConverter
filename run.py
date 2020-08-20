import os

import decompress
import converter
import wrapper

decompress.decompress(os.listdir("_prproj"))
converter.convert(os.listdir("decompressed"))
wrapper.wrap(os.listdir("converted"))

input("\nPress Enter to continue...")