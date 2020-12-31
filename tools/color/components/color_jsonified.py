import os
import json

from core.file import File
import core.utils
from core.component import Component

class color_jsonified(Component):
	def __init__(self, configurations, output_dir):
		super().__init__("ColorJsonified", output_dir)
		self.configurations = configurations
		pass

	def haveAssumeNonNull(self):
		return False
	#------------------------------------------------------------
	# Header	
	#------------------------------------------------------------

	def writeHeaderBegin(self, hFile):
		pass

	def headerImports(self):
		return ["<Foundation/Foundation.h>"]

	def writeContentHeader(self, hFile):
		for key in self.configurations.keys():
			hFile.appendStringWithDoubleEndline("FOUNDATION_EXTERN NSString *const {};".format(key))

	def writeHeaderEnd(self, hFile):
		pass

	#------------------------------------------------------------
	# Implementation	
	#------------------------------------------------------------
	def implementImports(self):
		return super().implementImports()

	def writeContentImplement(self, iFile):
		for key, value in self.configurations.items():
			valueStr = json.dumps(value)
			iFile.appendStringEndline("NSString *const {} = @\"{}\";".format(key, valueStr.replace("\"", "\\\"")))

	def writeImplementEnd(self, iFile):
		pass
