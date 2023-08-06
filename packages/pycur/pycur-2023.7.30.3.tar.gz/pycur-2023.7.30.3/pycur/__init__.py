__version__ = "2023.07.30.3"

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
			self._RAWDATA = b""
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