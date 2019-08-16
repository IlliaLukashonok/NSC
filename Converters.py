def converter_from_dec(num, to):
    """Convert to 2 and to 16"""
    out = ''
    out1 = ''
    while num:
        dic = {
            "10":"a",
            "11":"b",
            "12":"c",
            "13":"d",
            "14":"e",
            "15":"f"}
        bal = int(num) % to
        num_1 = str(bal)
        if num_1 in dic:
            num_1 = dic[num_1]
        out = out + num_1
        num = int(num) // to
    if to == 2:
        outl = [out[i:i+4] for i in range(0, len(out), 4)]
        i = len(outl[len(outl)-1])
        out1 = str(''.join(outl))
        if len(outl[len(outl)-1]) != 4:
            while i in range(4):
                if i == 0:
                    i = len(outl[len(outl) - 1])
                outl[len(outl) - 1] = outl[len(outl) - 1] + '0'
                i += 1
        out = str(' '.join(outl))     
        out = '){}( {}'.format(out1, out)
    return out[::-1]

def converter_to_dec(num, fr):
    conv = 0
    splited = []
    num = num[::-1]
    for i in range(len(num)):
        splited.append(num[i])
    dic = {
        "a":"10",
        "b":"11",
        "c":"12",
        "d":"13",
        "e":"14",
        "f":"15"}
    if fr == 16:
        for i in range(len(num)):
            if splited[i] in dic:
                splited[i] = dic[splited[i]]
    for i in range(len(num)):
        conv += int(splited[i]) * (fr**i)
    return conv

def converter_bin_to_hex(num):
    """Convert hex to bin"""
    splited = [num[i:i+4] for i in range(0, len(num), 4)]
    table = {"0000":"0", "0001":"1", "0010":"2", "0011":"3",
             "0100":"4", "0101":"5", "0110":"6", "0111":"7",
             "1000":"8", "1001":"9", "1010":"a", "1011":"b",
             "1100":"c", "1101":"d", "1110":"e", "1111":"f"}
    for i in range(int(len(num)/4)):
        splited[i] = table[splited[i]]
    return ''.join(splited)

def converter_hex_bin(num):
    """Convert hex to bin"""
    return converter_from_dec(converter_to_dec(num, 16), 2)
