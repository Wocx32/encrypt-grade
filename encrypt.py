from enc import encrypt_file, load_key
import sys

key = load_key()

if len(sys.argv) < 2:
    print('Usage: python encrypt.py <file>')
    exit(1)

file = sys.argv[1]

encrypt_file(file, key)