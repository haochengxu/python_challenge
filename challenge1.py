a = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. 
    rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb
    gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq 
    qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj'''

def translate(character, step):
    if(ord(character) >= ord('a') and ord(character) <= ord('z')):
        if (ord(character) + step > ord('z')):
            return chr(ord('a') + ord(character) + step - ord('z') - 1)
        else:
            return chr(ord(character) + step)
    else:
        print character + '2'
        return character

b= ''

for i in a:
    b = b + translate(i, 2)

print b