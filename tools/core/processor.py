import os
import json
import functools

from enum import Enum
from core.writer import writer

class GeneratorType(Enum):
	COLOR 	= 1

class processor:
	def __init__(self, log):
		self.is_log = log
		self.config = self._load_config()
		pass


	def run(self):
		self.resources = self.get_config_with_key("resources")

		raw_data = self.load_data_from_dir(self.resources)

		datas = self.prepare_data(raw_data)
		modules = self.modules()
		if (sorted(list(datas.keys())) != sorted(list(modules.keys()))):
			raise Exception("Modules and datas dont match with each other")

		for key in modules.keys():
			module_name, class_name = modules.get(key)
			data = datas.get(key)
			output_dir = self.get_config_with_key(key)
			
			w = writer(module_name, class_name, data, output_dir)
			w.write()
		pass

	#========================================================================
	# Subclass methods
	#========================================================================
	#	Return config path
	def config_path(self):
		raise Exception("Subclass must implement this method")
		return ""

	#	Return all the components module and class name used in processor
	def modules(self):
		raise Exception("Subclass must implement this method")

	#	Return all the endpoint data to pass into components
	def prepare_data(self, raw_data):
		raise Exception("Subclass must implement this method")

	#	Return all of the raw data related with components
	def load_data_from_dir(self, dir):
		raise Exception("Subclass must implement this method")

	#========================================================================
	# Convenient methods
	#========================================================================
	def get_config_with_key(self, key):
		value = self.config.get(key)
		if (not value):
			raise Exception("Not exists value with key {} in config {}".format(key, self.config_path()))
		return value

	def load_json_from_path(self, path):
		try:
			with open(path, 'r') as f:
				return json.load(f)
		except:
			raise Exception("Invalid json format, please visit web \"https://jsonlint.com\" to check again, path: {}".format(path))

	#========================================================================
	# Heloer methods
	#========================================================================
	def _log(self, msg):
		if (self.is_log):
			print(msg)

	def _load_config(self):
		#	Load configurations
		config_path = self.config_path()
		if (not os.path.isfile(config_path)):
			raise Exception("Not exists config path: {}".format(config_path))

		try:
			config = self.load_json_from_path(config_path)
		except:
			raise Exception("Cannot load config file from path {}".format(config_path))

		return config