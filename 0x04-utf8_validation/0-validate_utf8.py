#!/usr/bin/python3
"""
UTF-8 Validation Module
"""

def validUTF8(data):
    """
    Validate if the data set is a valid UTF-8 encoding.

    :param data: List of integers representing bytes of data
    :return: True if data is valid UTF-8 encoding, False otherwise
    """
    num_bytes = 0

    for byte in data:
        if byte < 0 or byte > 255:
            return False
        
        binary_repr = format(byte, '#010b')[-8:]

        if num_bytes == 0:
            if binary_repr.startswith('0'):
                continue
            elif binary_repr.startswith('110'):
                num_bytes = 1
            elif binary_repr.startswith('1110'):
                num_bytes = 2
            elif binary_repr.startswith('11110'):
                num_bytes = 3
            else:
                return False
        else:
            if not binary_repr.startswith('10'):
                return False
            num_bytes -= 1

    return num_bytes == 0

