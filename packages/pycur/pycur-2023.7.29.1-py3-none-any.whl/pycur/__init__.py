__version__ = "2023.07.29.1"

class Error(BaseException): pass

class Cursor:
	def __init__(self, mode, *args):
		if mode not in ["new", "read", "open"]:
			raise Error(f"Unknown mode \"{mode}\"")
		if mode == "new":
			self._RAWDATA = b""
		if mode in ["open", "read"]:
			if not len(args):
				raise Error(f"No file specified")
			if not os.path.exists(args[0]):
				raise Error(f"File {args[0]} does not exist")
		if mode == "open":
			with open(fil, "rb") as filIO:
				self._RAWDATA = filIO.read()
	def saveAs(self, fil):
		import os
		if not os.path.exists(fil):
			with open(fil, "x"): pass
		with open(fil, "wb") as filIO:
			filIO.truncate()
			filIO.write(self._RAWDATA)