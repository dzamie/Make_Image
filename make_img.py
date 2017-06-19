from PIL import Image
import argparse
import math

wd = 8

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--reverse", help="change image to file", action="store_true")
parser.add_argument("-v", "--verbose", help="display extra information", action="store_true")
parser.add_argument("-W", "--white", help="draw 00 as white instead of black (reverse: interpret #ffffff as 00)",action="store_true")
parser.add_argument("-w", "--width", type=int, help="desired output width (reverse: no effect)")
parser.add_argument("-o", "--output", help="specify non-default filename with filetype (normal: defaults to .png, reverse: defaults to .txt)")
parser.add_argument("file", help="input file")
args = parser.parse_args()

if args.width:
	wd = args.width


def tup_to_bytes(input):
	out = []
	for (r,g,b) in input:
		if(b == 136): # 88 blue value - end of file
			break
		if(args.white and r+g+b==255*3):
			out.append(0)
		else:
			out.append(int(16*(r/17) + (g/17)))
	print(str(out))
	return bytearray(out)

def img_to_bin():
	name = args.file[:args.file.find(".")] # filename before first period, used for default
	#note: list([img].getdata()) returns a list of (r,g,b) int tuples
	image = Image.open(args.file)
	if args.verbose:
		print("Decoding \"{}\" from an image...".format(args.file))
	bytelist = tup_to_bytes(list(image.getdata()))
	if args.verbose:
		print("Filesize: {} bytes".format(len(bytelist)))
	if args.output:
		name = args.output
	else:
		name += ".txt" 			# default filetype is .txt to avoid issues
	bfile = open(name,"wb") 	# w flag makes a new, empty file
	bfile.write(bytelist)
	if args.verbose:
		print("Done! The file was saved as \"{}\"".format(name))
	

def bin_to_img():
	name = args.file[:args.file.find(".")] # filename before first period, used for default
	bfile = open(args.file, "rb")
	imgdata = bfile.read()
	len = bfile.tell()
	ht = math.ceil(len / wd)

	if args.verbose:
		print("Turning \"{}\" into an image...".format(args.file))
		print("Width: {}\nHeight: {}".format(wd,ht))

	image = Image.new("RGB",(wd,ht),"#00ff88") # 88 blue val makes it distinct, impossible to generate
	pixels = image.load()

	for i in range(0,len):
		bt = imgdata[i]
	
		if(bt == 0 and args.white):
			red = green = blue = 255
		else:
			red = int(bt / 16)*17
			green = (bt % 16)*17
			blue = 0
	
		pixels[i % wd, int(i/wd)] = (red, green, blue)

	if args.output:
		name = args.output
	else:
		name += ".png"
	image.save(name)

	if args.verbose:
		print("Done! The image was saved as \"{}\"".format(name))
	
if args.reverse:
	img_to_bin()
else:
	bin_to_img()

