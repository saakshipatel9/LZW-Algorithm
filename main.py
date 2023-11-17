# Saakshi Patel (801361041)

from lzw import LZW
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A simple LZW Encoder Decoder")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-e", "--encode", help="Encode the input text")
    group.add_argument("-d", "--decode", help="Decode the input text")
    group.add_argument("--print_lzw", help="Print out the .lwz file in 16 bit format.")

    parser.add_argument("--bit_length", type=int, default=12, help="Specify the bit length (default: 12)")

    args = parser.parse_args()

    compressor = LZW(bit_length=args.bit_length)

    try:
        if args.encode:
            file_path = args.encode
            output_file = compressor.encode(file_path)
            print(f"Encoded Data saved at {output_file}")
        elif args.decode:
            file_path = args.decode
            output_file = compressor.decode(file_path)
            print(f"Decoded data saved at {output_file}")
        elif args.print_lzw:
            file_path = args.print_lzw
            print(compressor.print_lzw_bytes(file_path))
        else:
            print("Wrong input!")
    except Exception as e:
        print(f"Error Occured: {e}")
