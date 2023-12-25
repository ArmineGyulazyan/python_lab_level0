def caesar_cipher(test,test2,s):
    res = ""
    with open(test,'r') as current, open(test2,'w') as changed:
        text = current.read()
        for char in text:
            if char.isalpha():
                if char.isupper():
                    res += chr(((ord(char)+s-65)%26)+65)
                else:
                    res += chr(((ord(char)+s-97)%26)+97)
            else:
                res += char
        return changed.write(res)

print(caesar_cipher('current','changed',4))