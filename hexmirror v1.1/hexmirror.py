#!/usr/bin/python2

import argparse
import sys

args = argparse.ArgumentParser()
args.add_argument('hex',help='hex or path',metavar='')


group = args.add_mutually_exclusive_group()
group.add_argument('-b','--byte',help='Byte ;)',action="store_true")
group.add_argument('-P','--Path',help='Path ;)',action="store_true")



args = args.parse_args()



def HexMirror(hex_code):
	a = hex_code
	#hexcode = ''.join(reversed([r'\x' + a[i:i+2] for i in range(0, len(a), 2)]));print(hexcode)
	for i in range(0, len(a), 2):
		out = r'\x'+a[i:i+2]
		sys.stdout.write(out)
	print "\x0a"

def HexPath(path):
	rev = path[::-1]
	return rev.encode('hex')


def main():
	if args.byte:
		HexMirror(args.hex)
	if args.Path:
		print "0x" + HexPath(args.hex)	


if __name__ == '__main__':
	main()		
