
import os

class File:
	def __init__(self, filename, directory):
		self.filename = filename
		self.directory = directory
		self.data = ""
		pass

	def appendString(self, str):
		if (str):
			self.data = self.data + str

	def appendStringEndline(self, str):
		if (str):
			self.data = self.data + str
			self.appendEndline(1)

	def appendStringWithDoubleEndline(self, str):
		if (str):
			self.data = self.data + str
			self.appendEndline(2)

	def appendEndline(self, number_of_lines):
		if (number_of_lines > 0):
			for index in range(0, number_of_lines):
				self.data = self.data + "\n"

	def writeToFile(self):
		if (not os.path.isdir(self.directory)):
			raise Exception("Directory \"{}\" is not exists!".format(self.directory))
			return ""

		filepath = os.path.join(self.directory, self.filename)

		try:
			with open(filepath, "w") as file:
				file.write(self.data)
				return filepath
		except Exception as e:
			print("[Error] Error from writeToFile\n{}".format(e))
			return ""


