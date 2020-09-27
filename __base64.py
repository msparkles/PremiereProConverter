def decode(code):
    import base64
    import json
    
    decoded = base64.b64decode(code)
    temp = b''
    while(decoded[0] != 123): # 123 = '{'
        temp += decoded[:1]
        decoded = decoded[1:]
    decoded = decoded.decode("utf-16-le")

    parsed = json.loads(decoded)
    return parsed, temp

def encode(parsed, temp):
    import base64
    import json
    
    encoded = temp
    encoded += json.dumps(parsed, separators=(',', ':'), ensure_ascii=False).encode('utf-16-le')
    encoded = base64.b64encode(encoded)
    
    return encoded