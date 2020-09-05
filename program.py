# *****************************Welcome To Conversion Program ********************************
print('+-----------------------------------------+')
print('|                                         |')
print('|For Binary use 0b in front of number     |')
print('|For Decimal use 0o in front of number    |')
print('|For Octal use 0d in front of number      |')
print('|For Hexadecimal use 0x in front of number|')
print('|                                         |')
print('+-----------------------------------------+\n')

print('|*******************Caution**********************|')
print(' No Exception handling is done so give good input')
print('|************************************************|\n')

def binary(number): 
    value = int(number) 
    print(value, " in Binary : ", bin(value)) 
      
def octal(number): 
    value = int(number) 
    print(value, " in Octal : ", oct(value)) 

def decimal(number): 
    value = int(number) 
    print(value, " in Decimal : ", int(value)) 
  
def hexadecimal(number): 
    value = int(number) 
    print(value, " in Hexadecimal : ", hex(value)) 
  

number = input('Enter The Number ')
result = 0

if(number[:2]=='0b'):
    num_update = number[2:]
    print(num_update)
    result = sum([int(num_update[len(num_update)-i-1])*(2**i) for i in range(len(num_update))])

elif(number[:2]=='0o'):
    num_update = number[2:]
    print(num_update)
    result = sum([int(num_update[len(num_update)-i-1])*(8**i) for i in range(len(num_update))])

elif(number[:2]=='0x'):
    num_update = number[2:]
    print(num_update)
    result = sum(int(num_update[len(num_update)-i-1])*(16**i) for i in range(len(num_update)))

else:
    result = int(number)

print('_____________Result____________')
print('Binary Value     : ',bin(result))
print('Octal Value      : ',oct(result))
print('Decimal Value    : ',result)
print('HexDecimal Value : ',hex(result))

print(result)
