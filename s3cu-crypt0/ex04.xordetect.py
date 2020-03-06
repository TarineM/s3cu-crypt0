def single_char_xor(input_bytes, char_value):
    output_bytes = b''
    for byte in input_bytes:
        output_bytes += bytes([byte ^ char_value])
    return output_bytes


def bruteforce_single_char_xor(ciphertext):
    potential_messages = []
    for key_value in range(256):
        message = single_char_xor(ciphertext, key_value)
        data = {
            'message': message,
            'key': key_value
            }
        potential_messages.append(data)
    return potential_messages


def main():
    ciphers = open('h014.txt').read().splitlines()
    potential_plaintext = []
    for hexstring in ciphers:
        ciphertext = bytes.fromhex(hexstring)
        potential_plaintext.append(bruteforce_single_char_xor(ciphertext))
    i=1
    for item in potential_plaintext:
      if i==171:
        print("Line ", i, " ", item)
      i+=1



# Answer: {'message': b'Now that the party is jumping\n', 'key': 53} for line 171