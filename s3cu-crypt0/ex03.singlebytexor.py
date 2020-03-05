
def single_char_xor(input_bytes, char_value):
    """Returns the result of each byte being XOR'd with a single value.
    """
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
    return output_bytes


def main():
    hexstring = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
    ciphertext = bytes.fromhex(hexstring)
    for key_value in range(256):
        message = single_char_xor(ciphertext, key_value)
        print('key: ', key_value, ", message: ", message)

if __name__ == '__main__':
    main()

# Response
# key:  88 , message:  b"Cooking MC's like a pound of bacon"