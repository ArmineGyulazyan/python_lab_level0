def rle_encode(file):
    with open(file, 'r') as file, open('rle_decode', 'w') as new_file:
        text = file.read()
        res = ''
        i = 0
        while i < len(text):
            count = 0
            key = text[i]
            for j in range(i, len(text)):
                if text[j] == key:
                    count += 1
                    i += 1
                else:
                    break
            res += key + str(count) if count > 1 else key
        new_file.write(res)


rle_encode('rle_encode')