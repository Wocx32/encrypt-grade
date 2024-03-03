from enc import decrypt_file, load_key
import sys

key = load_key()

if len(sys.argv) < 2:
    print('Usage: python decrypt.py <file>')
    exit(1)

file = sys.argv[1]

decrypt_file(file, key)