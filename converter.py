def convert(files):
    import os
    import lxml.etree as ET
    import opencc
    import json
    import __base64 as b64
    CC = opencc.OpenCC('t2s.json')

    print("Converting Texts to Simplified Chinese...", "\n")
    
    for file in files:
        with open("./decompressed/" + file, 'rb') as f:
            root = ET.fromstring(f.read())
        tree = ET.ElementTree(root)
        
        for node in root.iter("ArbVideoComponentParam"):
            if(node[1].tag == "Name" and node[1].text == "Source Text"):
                if(node[5].text != None):
                    parsed, temp = b64.decode(node[5].text)
                    parsed["mTextParam"]["mStyleSheet"]["mText"] = CC.convert(parsed["mTextParam"]["mStyleSheet"]["mText"])
                    node[5].text = b64.encode(parsed, temp)
        tree.write("./converted/" + file, encoding='utf-8', xml_declaration=True)
        os.remove("./decompressed/" + file)