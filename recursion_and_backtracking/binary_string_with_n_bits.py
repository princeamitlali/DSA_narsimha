'''
generate all the binary string with n bits. assume A[0.......... n-1]
'''

def append_in_fron(x,L):
    return [x+element for element in L]

def bit_strings(n):
    if n == 0: return []
    if n == 1: return ['0','1']
    else:
        return (append_in_fron('0',bit_strings(n-1)) + append_in_fron("1",bit_strings(n-1)))
    
    
def bit_strings2(n):
    if n == 0: return []
    if n == 1: return ['0','1']
    return [digit + bit_string for digit in bit_strings2(1) for bit_string in bit_strings2(n-1)]

print(bit_strings2(4))
    
    
print(bit_strings(4))