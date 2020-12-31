import os
from datetime import datetime

def generatedFileHeader(fileName):
	return """//
//	{}
//	ZADesignSystem
//
// 	This file is generated automatically by WSDesignGenerator"
// 	Copyright © 2020 QuocTuyen. All rights reserved.
//
//	WARNING - Do not modify!!!"
// 	Generated time: {}
//""".format(fileName, datetime.today().strftime("%Y-%m-%d (%H:%M)"))

def getImportListString(list_import):
	result = ""
	for impt in list_import:
		result = result + "#import {}\n".format(impt)

	return result