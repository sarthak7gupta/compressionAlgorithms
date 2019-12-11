import re
# RLE(run-length encoding) decoder 
def decode(string):
    if string == '':
        return ''
    multiplier = 1
    count = 0
    rle_decoding = []
                          
    rle_encoding = []     
    
    rle_encoding = re.findall(r'[A-Za-z]|-?\d+\.\d+|\d+|[\w\s]', string) 
    for item in rle_encoding:
        if item.isdigit():
            multiplier = int(item)
        elif item.isalpha() or item.isspace():
            while count < multiplier:
                rle_decoding.append('{0}'.format(item))
                count += 1
            multiplier = 1
            count = 0 
    return(''.join(rle_decoding))

#RLE(run-length encoding) encoder
def encode(string):
    if string == '':
        return ''
    i = 0
    count = 0
    letter = string[i]
    rle = []
    while i <= len(string) - 1:        
        while string[i] == letter:
            i+= 1
            count +=1
            #catch the loop on last character so it doesn't got to top and access out of bounds
            if i > len(string) - 1:
                break
        if count == 1:
            rle.append('{0}'.format(letter))
        else:
            rle.append('{0}{1}'.format(count, letter))
        if i > len(string) - 1: #ugly that I have to do it twice
            break
        letter = string[i]
        count = 0
    #join list of strings together to create one string to return
    final = ''.join(rle)
    return final

f1=open("alice29.txt","r")
f2=open("b.txt","w")
content=f1.read()        
f2.write(encode(content))
#print(encode('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB'))