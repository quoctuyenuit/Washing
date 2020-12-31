import argparse
from core.processor import *
import importlib

def parse_args():
	parser = argparse.ArgumentParser(description='Generator')

	parser.add_argument(
			"-color",
			"--color",
			"-colors",
			"--colors",
			action="store_true",
	        help="Generate color configurations",
	        default=False
		)

	parser.add_argument(
			"-all",
			"--all",
			action="store_true",
	        help="Run all element",
	        default=False
		)

	parser.add_argument(
			"-log",
			"--log",
			action="store_true",
	        help="Show log",
	        default=False
		)

	return parser.parse_args()

def run_processor(module_name, class_name, params):
	class_object = getattr(importlib.import_module(module_name), class_name)
	processor = class_object(params)
	processor.run()
		

def main():
	processors = {
		GeneratorType.COLOR 	: ("color.processor", "processor")
	}


	args = parse_args()
	types = []

	if (args.all):
		types = list(GeneratorType)
	else:
		if (args.color):
			types.append(GeneratorType.COLOR)

	for processor_type in types:
		run_processor(*processors.get(processor_type), args.log)

if __name__ == "__main__":
	main()





















