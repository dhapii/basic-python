from Crypto.Util.number import long_to_bytes

# Given large integer
number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the integer to bytes
byte_data = long_to_bytes(number)

# Convert bytes to a readable string
message = byte_data.decode('utf-8')
print("Decoded message:", message)

def xor_with_13(label):
    xor_result = ''.join(chr(ord(char) ^ 13) for char in label)
    return f'crypto{{{xor_result}}}'

# Example usage
label = "1100"
flag = xor_with_13(label)
print(flag)
