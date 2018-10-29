import sys

a = sys.argv[1]

hexcode = ''.join(reversed([r'\x' + a[i:i+2] for i in range(0, len(a), 2)]));print("\n"+hexcode)


