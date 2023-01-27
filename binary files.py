import struct
f = open("C:\\Users\\libia\\Downloads\\wallpapersden.com_war-devil-4k-chainsaw-man-digital-art_3840x2160.bmp", "rb")
header_field = f.read(2)
size = f.read(4)
fsize = struct.unpack("i", size)
print(f"file size is {fsize}")

offset = f.read(12)
w = f.read(4)
width = struct.unpack("i", w)
h = f.read(4)
height = struct.unpack("i", h)
print("width of the bmp image is", width, "pixels")
print("height of the bmp image is", height, "pixels")