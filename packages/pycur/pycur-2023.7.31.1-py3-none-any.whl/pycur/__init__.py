__version__ = "2023.07.31.1"

class Error(BaseException): pass

class Color:
	def __init__(self, r, g, b):
		if True in [(mode > 255 or mode < 0) for mode in [r, g, b]]:
			raise Error("RGB values must be in the range of 0-255")
		self.r = r
		self.g = g
		self.b = b
	def inverse(self):
		self.r = 255 - self.r
		self.g = 255 - self.g
		self.b = 255 - self.b
	def __str__(self):
		return f"rgb({str(self.r)}, {str(self.g)}, {str(self.b)})"

class Cursor:
	def __init__(self, mode, *args):
		if mode not in ["new", "open"]:
			raise Error(f"Unknown mode \"{mode}\"")
		if mode == "new":
			import struct # Only for this time! (Maybe?)
			self.hotspot = (0, 0)
			if args[0].__class__ != ().__class__:
				raise Error("Invalid size specified.")
			self.size = args[0]
			# Unofficial file format docs: https://www.daubnet.com/en/file-format-cur
			# 1 bit: struct.pack("<B", 12)
			# 2 bits: struct.pack('<H', 12)
			# 4 bits: struct.pack('<I', 12)
			self._RAWDATA = b"\x00\x00\x02\x00\x01\x00" # Reserved #1, Type, Count
			self._RAWDATA += b"\x00" * 24 # Entries
			self._RAWDATA += struct.pack("<B", args[0][0]) # Width
			self._RAWDATA += struct.pack("<B", args[0][1]) # Height
			self._RAWDATA += "\x00\x00" # ColorCount + Reserved #2
			self._RAWDATA += struct.pack("<H", self.hotspot[0]) # XHotspot
			self._RAWDATA += struct.pack("<H", self.hotspot[1]) # YHotspot
			self._RAWDATA += "\x00\x00\x00\x00" # SizeInBytes
			self._RAWDATA += struct.pack("<I", len(self._RAWDATA) + 4) # FileOffset
			# Community, I think you can continue this... - RixTheTyrunt
		self._MODE = mode
		if mode == "open":
			if not len(args):
				raise Error(f"No file specified for mode `open`")
			if not os.path.exists(args[0]):
				raise Error(f"File {args[0]} does not exist")
			with open(fil, "rb") as filIO:
				self._RAWDATA = filIO.read()
		self._DRAWOBJS = []
	def line(self, pos, col=None):
		if col is None:
			col = Color(0, 0, 0)
		if [pos.__class__, col.__class__] != [[].__class__, Color]: # `list` can be overridden as a variable, I use `[].__class__` instead for no conflicts ;)
			raise Error(f"Invalid values for arguments `pos` and/or `col`")
		self._DRAWOBJS.push({"type": "line", col: col, pos: pos})
	def saveAs(self, fil):
		import os
		if not os.path.exists(fil):
			with open(fil, "x"): pass
		with open(fil, "wb") as filIO:
			filIO.truncate()
			filIO.write(self._RAWDATA)