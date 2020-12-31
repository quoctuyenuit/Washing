import os
import json
import glob
import functools
from core.processor import processor as super_processor

class processor(super_processor):
	def __init__(self, log):
		super().__init__(log)
		pass

	def run(self):
		print("******************************************************")
		print("\nColor is processing\n")
		print("******************************************************")
		super().run()

	def config_path(self):
		return './color/config.json'

	def modules(self):
		return {
			"ColorJsonified"	: ("color.components.color_jsonified", "color_jsonified"),
			"UIColor+Washing"	: ("color.components.color_washing", "color_washing"),
			"WSElementColors+Color"	: ("color.components.wsuielement_color", "wsuielement_color"),
		}

	def load_data_from_dir(self, dir):
		color_file_path = os.path.join(dir, "color.json")
		data = self.load_json_from_path(color_file_path)
		return data

	def prepare_data(self, raw_data):
		color_names = list(raw_data.keys())
		jsonified = {"_ColorJsonified": raw_data}
		
		return {
			"ColorJsonified"	: jsonified,
			"UIColor+Washing"	: color_names,
			"WSElementColors+Color"	: color_names
		}