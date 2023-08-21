"""
Cryptopals Challenge 1 Set 1
    Convert hex to base64
"""

import base64

def hex_to_base64(hex_str: str) -> str:
    # convert str to bytes object then convert bytes to b64
    # .decode() used to remove b'' wrapping
    return base64.b64encode(bytes.fromhex(hex_str)).decode()
        
# input hex string
hex_str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

print(hex_to_base64(hex_str))
# SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t