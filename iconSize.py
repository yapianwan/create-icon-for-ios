#encoding=utf-8
#author: wade
#date: 2017-01-05
#function: Automatically generated ios Application Icon
import os
import os.path
import json, types,string  
from PIL import Image
def ResizeImage(filein, fileout, width, height, type):
	mg = Image.open(filein)
	out = mg.resize((width, height),Image.ANTIALIAS) #resize image with high-quality
	out.save(fileout, type)

if __name__ == "__main__":
	filein = r'image/icon.png'
	file_object = open('size.json')
	try:
		all_the_text = file_object.read()
		try:
			jsonDic = json.loads(all_the_text)
			imageArray = jsonDic['images']
			for image in imageArray:
				fileout = r'image/'
				sizeArray = image['size'].split('x')
				width = float(sizeArray[0])
				height = float(sizeArray[1])
				if image['scale']=='1x':
					fileout = fileout+image['idiom']+image['size']+'.png'
				elif image['scale']=='2x':
					fileout = fileout+image['idiom']+image['size']+'@'+image['scale']+'.png'
					width = width * 2
					height = height * 2
				elif image['scale']=='3x':
					fileout = fileout+image['idiom']+image['size']+'@'+image['scale']+'.png'
					width = width * 3
					height = height * 3
				imageType = 'png'
				ResizeImage(filein, fileout, int(width), int(height), imageType)
		except ValueError:
			print 'JSON format is not correct'
	except IOError:
		print 'check json file'
	finally:
		file_object.close( )
