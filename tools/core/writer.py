import os
import importlib

class writer:
	def __init__(self, module_name, class_name, data, output_dir):
		if (not os.path.isdir(output_dir)):
			raise Exception("Not exists output directory on path {}".format(output_dir))

		self.data = data
		self.output_dir = output_dir
		self.class_object = getattr(importlib.import_module(module_name), class_name)
		pass

	def write(self):
		self.instance = self.class_object(self.data, self.output_dir)
		self.instance.exportData()
