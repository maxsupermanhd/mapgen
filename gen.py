from pprint import pprint
from random import randrange, randint
import json5

#
# 0 -> +x
# |
# \/
# +y
#

def PrintLayout(l):
	for r in range(len(l)):
		for c in range(len(l[r])):
			print("%02d" % (l[r][c]), end = "")
		print()

def GenerateLayout(mapx = 150, mapy = 150, mapbordpadding = 30, roomlen = 50):
	layout = []
	for i in range(mapy):
		layer = []
		for j in range(mapx):
			layer.append(0)
		layout.append(layer)
	startx = randrange(mapy-mapbordpadding*2)+mapbordpadding
	starty = randrange(mapx-mapbordpadding*2)+mapbordpadding
	roomsleft = roomlen
	currposx = startx
	currposy = starty
	while roomsleft > 1:
	 	# 0u 1r 2d 3l
		if currposx >= mapx or currposy >= mapy or currposx < 0 or currposy < 0:
			break
		if layout[currposx][currposy] == 0:
			roomsleft -= 1
		layout[currposx][currposy] = roomsleft
		direction = randint(0, 3)
		if direction == 0:
			currposy -= 1
		elif direction == 1:
			currposx += 1
		elif direction == 2:
			currposy += 1
		else:
			currposx -= 1
	return layout

def LayoutStripper(l):
	s = 0
	for r in range(len(l)):
		for c in range(len(l[r])):
			s += l[r][c]
	if s == 0:
		raise Exception('Empty-tileset', 'Nothing to trim!')
	r = 0
	while r < len(l):
		s = 0
		c = 0
		while c < len(l[r]):
			s += l[r][c]
			c += 1
		if s == 0:
			del l[r]
		else:
			r += 1
	c = 0
	while c < len(l[0]):
		s = 0
		r = 0
		while r < len(l):
			s += l[r][c]
			r += 1
		if s == 0:
			r = 0
			while r < len(l):
				del l[r][c]
				r += 1
		else:
			c += 1
	return l

def GenerateEmptyTileWithDirs(rt = 5, ct = 5, s = "udlr"):
	if rt < 3 or ct < 3:
		raise Exception('Too-small', 'Tile must be at least 3x3')
	if s == "":
		return ["#"*ct]*rt
	firstrow = "#" * ct
	if "u" in s:
		ba = bytearray(firstrow, encoding='utf8')
		ba[int(rt/2)] = ord(' ')
		firstrow = ba.decode("utf-8")
	o = [firstrow]
	for r in range(rt-2):
		nrow = bytearray(str("#" + str(" " * (ct-2)) + "#"), encoding='utf8')
		if "l" in s and int(rt/2) == r+1:
			nrow[0] = ord(' ')
		if "r" in s and int(rt/2) == r+1:
			nrow[ct-1] = ord(' ')
		if randrange(3) == 1 and int(rt/2) == r+1:
			nrow[int(ct/2)] = ord('1')
		o.append(nrow.decode("utf-8"))
	lastrow = "#" * ct
	if "d" in s:
		ba = bytearray(lastrow, encoding='utf8')
		ba[int(rt/2)] = ord(' ')
		lastrow = ba.decode("utf-8")
	o.append(lastrow)
	return o

def OpenParseDataset(n):
	with open("tileset1.json5") as t:
		print(json5.load(t))

def FindSingleTileInDataset(d, s):
	a = 0

def RealizeLayout(l, t):
	mapgenrows = 3
	mapgencols = 3
	map = [""]*(len(l)*mapgenrows);
	for r in range(len(l)):
		for c in range(len(l[r])):
			dirs = ""
			if l[r][c] != 0:
				if r-1 >= 0 and l[r-1][c] != 0:
					dirs += "u"
				if c-1 >= 0 and l[r][c-1] != 0:
					dirs += "l"
				if r+1 < len(l) and l[r+1][c] != 0:
					dirs += "d"
				if c+1 < len(l[r]) and l[r][c+1] != 0:
					dirs += "r"
			tile = GenerateEmptyTileWithDirs(rt = mapgenrows, ct = mapgencols, s = dirs)
			for i in range(mapgenrows):
				map[r*mapgenrows+i] += tile[i]
	for r in range(len(map)):
		print(map[r])

if __name__ == "__main__":
	print("Generating initial layout")
	l = GenerateLayout()
	print("Stripping empty space")
	l = LayoutStripper(l)
	PrintLayout(l)
	print("Realizing layout in map format")
	RealizeLayout(l, "sample.json5")
