import functools

from core.file import File
import core.utils
from core.component import Component

class wsuielement_color(Component):
	def __init__(self, colors, output_dir):
		super().__init__("WSElementColors+Color", output_dir)
		self.colors = colors
		pass

	#------------------------------------------------------------
	# Header	
	#------------------------------------------------------------

	def writeHeaderBegin(self, hFile):
		super().writeHeaderBegin(hFile)

	def headerImports(self):
		return ["\"WSElementColors.h\""]

	def writeContentHeader(self, hFile):
		hFile.appendStringWithDoubleEndline("@interface WSElementColors (Color)")

		for name in self.colors:
			line = "@property (nonatomic, strong, readonly) UIColor *{};".format(name)
			hFile.appendStringEndline(line)

	def writeHeaderEnd(self, hFile):
		super().writeHeaderEnd(hFile)

	#------------------------------------------------------------
	# Implementation	
	#------------------------------------------------------------
	def implementImports(self):
		return [
			"\"WSElementColors+Private.h\""
		]

	def writeContentImplement(self, iFile):
		iFile.appendStringWithDoubleEndline("@implementation WSElementColors (Color)")

		#-------------------------------------------------------
		#	Init colors value
		#-------------------------------------------------------
		for name in self.colors:
			line = """
- (UIColor *){} {{
	return [self.colorPalettes colorWithKey:@"{}"];
}}""".format(name, name)
			iFile.appendStringEndline(line)

	def writeImplementEnd(self, iFile):
		super().writeImplementEnd(iFile)
