from core.file import File
import core.utils as utils
import os

class Component:
	def __init__(self, class_name, output_dir):
		if (not os.path.isdir(output_dir)):
			raise Exception("Output directory \"{}\" is not exists".format(output_dir))

		self.class_name = class_name;
		self.hFile = File(self.header(), output_dir)
		self.iFile = File(self.implement(), output_dir)
		pass

	def header(self):
		return self.class_name + ".h"

	def implement(self):
		return self.class_name + ".m"

	def haveAssumeNonNull(self):
		return True

	def macro_define(self):
		return None

	#------------------------------------------------------------
	# Header	
	#------------------------------------------------------------

	def writeHeaderBegin(self, hFile):
		pass

	def headerImports(self):
		return []

	def writeContentHeader(self, hFile):
		pass

	def writeHeaderEnd(self, hFile):
		hFile.appendEndline(1)
		hFile.appendStringWithDoubleEndline("@end")
		pass

	#------------------------------------------------------------
	# Implementation	
	#------------------------------------------------------------

	def implementImports(self):
		return []

	def writeImplementBegin(self, iFile):
		pass

	def writeContentImplement(self, iFile):
		pass

	def writeImplementEnd(self, iFile):
		iFile.appendEndline(1)
		iFile.appendStringWithDoubleEndline("@end")
		pass
		
	#------------------------------------------------------------
	def writeHeader(self):
		#Write title
		self.hFile.appendStringWithDoubleEndline(utils.generatedFileHeader(self.header()))
		#Write begin
		if (self.macro_define()):
			self.hFile.appendStringWithDoubleEndline("#import \"{}FeatureDefines.h\"".format(common_config.prefix))
			self.hFile.appendStringWithDoubleEndline("#if {}".format(self.macro_define()))

		self.hFile.appendStringEndline("#ifndef {}_h".format(self.class_name.replace("+", "_")))
		self.hFile.appendStringWithDoubleEndline("#define {}_h".format(self.class_name.replace("+", "_")))
		self.writeHeaderBegin(self.hFile)
		#Write import
		self.hFile.appendStringEndline(utils.getImportListString(self.headerImports()))

		if (self.haveAssumeNonNull()):
			self.hFile.appendStringWithDoubleEndline("NS_ASSUME_NONNULL_BEGIN")
		#Write content
		self.writeContentHeader(self.hFile)
		#Write end
		
		self.writeHeaderEnd(self.hFile)

		if (self.haveAssumeNonNull()):
			self.hFile.appendStringEndline("NS_ASSUME_NONNULL_END")
		
		self.hFile.appendEndline(1)
		self.hFile.appendStringEndline("#endif /* {}_h */".format(self.class_name.replace("+", "_")))

		if (self.macro_define()):
			self.hFile.appendStringEndline("#endif /* {} */".format(self.macro_define()))

		return self.hFile.writeToFile()
		

	def writeImplement(self):
		#Write title
		self.iFile.appendStringWithDoubleEndline(utils.generatedFileHeader(self.implement()))
		
		#Write import
		imports = self.implementImports()
		imports.insert(0, "\"{}.h\"".format(self.class_name))
		self.iFile.appendStringEndline(utils.getImportListString(imports))

		if (self.macro_define()):
			self.iFile.appendStringWithDoubleEndline("#if {}".format(self.macro_define()))

		#write begin
		self.writeImplementBegin(self.iFile)
		#Write content
		self.writeContentImplement(self.iFile)
		#Write fotter
		self.writeImplementEnd(self.iFile)

		if (self.macro_define()):
			self.iFile.appendStringEndline("#endif /* {} */".format(self.macro_define()))

		return self.iFile.writeToFile()

	def exportData(self):
		print("---------------------------------------------")
		headerPath = self.writeHeader()
		implPath = self.writeImplement()
		if (headerPath and headerPath != ""):
			print("{}".format(os.path.abspath(headerPath)))

		if (implPath and implPath != ""):
			print("{}".format(os.path.abspath(implPath)))
		
