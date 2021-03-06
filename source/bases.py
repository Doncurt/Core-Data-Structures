#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace
'''
Notes about how to think about numbers.
numbers are a representation of exactly how many items are present in terms of singlular units EX (2 is 2 intances of one unit).My concept of the base ten( and other systems) are that the ticking point basically is the end of a box that can store a set number of units. For base ten we decide that every box can only contain 10 units.

Zero as a concept:
zero acts as a placeholder or a signal for "this box is initializ with one number, but is otherwise empty, also there are the this many boxes of(in our case 10) units before me"

 So our first box would be 0:{1-9}, 1:{1-9}, 2:{1-9} so 11 would be in the second box in the first position, while 29 would be in the second box in the last position.

'''

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    '''
    1. Comes in as a string
    2. Base if compared first, if it meets the conditions, both digits and number
    are passed into int for conversions

    JUST FOUND OUT THAT I CANT USE THE INT FUNCTION
    '''

    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2) //DONE

    # TODO: Decode digits from hexadecimal (base 16)//DONE

    # TODO: Decode digits from any base (2 up to 36)//DONE
    # ...
    if base == 2:
        return int(digits, 2)
    elif base == 16:
        return int(digits,16)
    else:
        return int(digits,base)


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    '''
    # TODO: Encode number in binary (base 2)// TESTS
    if base == 2:
        nums = {'0':'000','1':'001','2':'010','3':'011',
                 '4':'100','5':'101','6':'110','7':'111'}
        #octal converstion
        octal = "%o" % number
        #empty string for output
        binary_Str = ''
        # convert octal to its binary equivalent
        for c in octal: binary_Str += nums[c]
        return binary_Str

'''

    #sets up the alpahbet incase of hex
    alphabet='0123456789abcdefghijklmnopqrstuvwxyz'
    #if the given base isnt base two( and there for more than base two but nees account for higher types
    # then go to the next loop)
    if base<2 or base>len(alphabet):
        #due to base 64 having more charactors, the alphabet has to be assigned to something using all of them
        if base==64: # assume base64 rather than raise error
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
        else:
            #raises an error that screams that the base you put in is out of range..basically that its higher than what can be handled for this loop
            raise AssertionError(" All about that base...and its out of range")
    if isinstance(number,complex): # return a tuple
        return ( int2base(number.real,base,alphabet) , int2base(number.imag,base,alphabet) )
    if number<=0:
        if x==0:
            return alphabet[0]
        else:
            return  '-' + int2base(-number,base,alphabet)
    # else x is non-negative real
    rets=''
    while number>0:
        number,idx = divmod(number,base)
        rets = alphabet[idx] + rets
    return rets

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...
    return encode(decode(digits, base1), base2)
'''
STRETCH CHALLENGES!!!


'''
def fractToBinary(fraction):

    int_to_left,fractional = fraction.split('.')
    #print(int_to_left)
    #print(fractional)
    # turn from binary to int now
    int_to_left =int(int_to_left, 2)
    fractional = int(fractional,2)
    #turn into string so that they can be joined together
    int_to_left_str = str(int_to_left)
    fractional_str = str(fractional)
    # convert to a single string
    converted =[int_to_left_str,fractional_str]
    #join on .
    converted = '.'.join(converted)

    return converted


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
