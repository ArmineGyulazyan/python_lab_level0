def xor_cipher(file, key):
    res = ""
    with open(file, 'r') as file, open('xor_decode', 'w') as new_file:
        text = file.read()
        for i in range(len(text)):
            res += chr(ord(text[i]) ^ ord(key[i % len(key)]))

        new_file.write(res)

xor_cipher('xor_encode','encode')