string = list(input())
oneToZero = 0
zeroToOne = 0

if string[0] == '1':
    zeroToOne += 1
else:
    oneToZero += 1
    
for i in range(len(string)-1):
    if string[i] == '1' and string[i+1] != '1':
        oneToZero += 1

    elif string[i] == '0' and string[i+1] != '0':
        zeroToOne += 1

print(min(oneToZero, zeroToOne))
