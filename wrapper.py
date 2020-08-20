def wrap(files):
    import os
    from os import path
    import gzip
    import shutil

    print("Wrapping Project File...")
    print("Found Files: ", files, "\n")

    for file in files:
        with open("./converted/" + file, 'rb') as f:
            with gzip.open("./_output/" + file, 'wb') as t:
                shutil.copyfileobj(f, t)
        if(path.exists("./_output/" + file + ".prproj")):
            os.remove("./_output/" + file + ".prproj")
        os.rename("./_output/" + file, "./_output/" + file + ".prproj")
        os.remove("./converted/" + file)