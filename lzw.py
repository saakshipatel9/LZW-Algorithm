# Saakshi Patel (801361041)

import os
from utils import has_extension

class LZW:
    def __init__(self, bit_length: int):
        self.bit_length = bit_length

    def print_lzw_bytes(self, file_path: str):
        """Print bytes for a lwz file."""
        # Check file extension
        if not has_extension(file_path, ".lzw"):
            raise "Only .lzw files allowed for printing binary."

        # Read file
        with open(file_path, "rb") as file:
            encoded_data = file.read()

        # Print
        for byte in encoded_data:
            print(format(byte, '08b'), end=' ')

    def encode(self, file_path: str):
        """Encode the text in a file."""
        # Check file extension
        if not has_extension(file_path, ".txt"):
            raise Exception("Only .txt files allowed for encoding.")

        # Read from .txt file
        with open(file_path, "r") as file:
            input_symbols = file.read()

        # Encode data
        MAX_TABLE_SIZE = 2 ** self.bit_length
        table = {chr(i): i for i in range(256)}
        current_code = 256
        string = ""
        encoded_data = bytearray()

        for symbol in input_symbols:
            current_symbol = string + symbol
            if current_symbol in table:
                string = current_symbol
            else:
                encoded_data.extend(
                    [(table[string] >> 8) & 0xFF, table[string] & 0xFF])
                if current_code < MAX_TABLE_SIZE:
                    table[current_symbol] = current_code
                    current_code += 1
                string = symbol

        if string:
            encoded_data.extend(
                [(table[string] >> 8) & 0xFF, table[string] & 0xFF])

        base_path, _ = os.path.splitext(file_path)
        new_file_path = f"{base_path}.lzw"

        with open(new_file_path, "wb") as file:
            file.write(encoded_data)

        return new_file_path

    def decode(self, file_path: str):
        """Decode a .lzw file"""
        # Check file extension
        if not has_extension(file_path, ".lzw"):
            raise Exception("Only .lzw files allowed for decoding.")

        # Read binary data
        with open(file_path, "rb") as file:
            encoded_data = file.read()

        # Decode data
        MAX_TABLE_SIZE = 2 ** self.bit_length
        table = {i: chr(i) for i in range(256)}
        current_code = 256
        decoded_data = []
        prev_code = (encoded_data[0] << 8) + encoded_data[1]
        output_string = table[prev_code]
        decoded_data.append(output_string)

        for i in range(2, len(encoded_data), 2):
            code = (encoded_data[i] << 8) + encoded_data[i + 1]

            if code in table:
                current_string = table[code]
            else:
                current_string = table[prev_code] + table[prev_code][0]

            decoded_data.append(current_string)

            if current_code < MAX_TABLE_SIZE:
                table[current_code] = table[prev_code] + current_string[0]
                current_code += 1

            prev_code = code

        decoded_string = ''.join(decoded_data)

        base_path, _ = os.path.splitext(file_path)
        new_file_path = f"{base_path}_decoded.txt"

        with open(new_file_path, "w+") as file:
            file.write(decoded_string)

        return new_file_path
