'''
generate all the strings of length n drawn from 0...........k-1
'''

def range_to_list(k):
    return [ str(i) for i in range(k) ]

print(range_to_list(4))

def base_k_strings(n,k):
    if n == 0 : return []
    if n == 1: return range_to_list(k)
    return [ digit + bit_string for digit in base_k_strings(1,k) for bit_string in base_k_strings(n-1,k)]

print(base_k_strings(4,3))