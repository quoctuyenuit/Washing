import os
import core.utils
from core.component import Component

class color_washing(Component):
	def __init__(self, color_names, output_dir):
		super().__init__("UIColor+Washing", output_dir)
		self.color_names = sorted(color_names)
		pass

	#------------------------------------------------------------
	# Header	
	#------------------------------------------------------------

	def headerImports(self):
		return ["<UIKit/UIKit.h>"]

	def writeContentHeader(self, hFile):
		hFile.appendStringWithDoubleEndline("@interface UIColor (Washing)")
		for name in self.color_names:
			line = "@property (class, nonatomic, readonly) UIColor *{};".format(name)
			hFile.appendStringEndline(line)

	#------------------------------------------------------------
	# Implementation	
	#------------------------------------------------------------

	def implementImports(self):
		return ["\"WSElementColors+Color.h\""]

	def writeContentImplement(self, iFile):
		iFile.appendStringEndline("@implementation UIColor (Washing)")
		for name in self.color_names:
			line = """
+ (UIColor *){} {{
	return [WSElementColors shared].{};
}}""".format(name, name)
			iFile.appendStringEndline(line)
		pass

