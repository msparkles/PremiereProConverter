def decompress(files):
    print("Found Files: ", files, "\n")
    
    import os
    import gzip
    import shutil
    
    print("Copying XML Files...", "\n")

    for file in files:
        with gzip.open("./_prproj/" + file, 'rb') as f:
            with open(os.path.splitext("./decompressed/" + file)[0], 'wb') as t:
                shutil.copyfileobj(f, t)