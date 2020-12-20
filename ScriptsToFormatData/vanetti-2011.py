
import os
import xml.etree.ElementTree as ET

def main():

	x=0
	y=0
	width = 0
	height = 0


	path = 'Annotations'
	for filename in os.listdir(path):
		if not filename.endswith('.xml'):continue
		fullname = os.path.join(path, filename)
		xmlName = filename.replace('.xml','')
		tree = ET.parse(fullname)
		root = tree.getroot()

		for size in root.iter('size'):
		##value = type_tag.get('bndbox')
			imgWidth = int(size.find('width').text)
			imgHeight = int(size.find('height').text)
			print(imgHeight,imgWidth)

		for size in root.iter('bndbox'):
		##value = type_tag.get('bndbox')
			xMax = int(size.find('xmax').text)
			xMin = int(size.find('xmin').text)
			yMax = int(size.find('ymax').text)
			yMin = int(size.find('ymin').text)
			

			##calculate(imgWidth,imgHeight,xMax,xMin,yMax,yMin,xmlName,'Counter')


	findDigits()

	
def calculate(imgWidth,imgHeight,xMax,xMin,yMax,yMin,xmlName,label):
	
	x = (xMin+((xMax - xMin)/2))/imgWidth
	y = (yMin+((yMax - yMin)/2))/imgHeight
	width = (xMax-xMin)/imgWidth
	height = (yMax-yMin)/imgHeight

	if object=='Counter':
		counterYoloFormat(x,y,width,height,xmlName,label)
	if object!='Counter':
		digitYoloFormat(x,y,width,height,xmlName,label)

	


def counterYoloFormat(x,y,width,height,xmlName,label):
	
	if not os.path.exists('yolo'):
		os.makedirs('yolo')
	

	f= open("yolo/{}.txt".format(xmlName),"a")
	f.write("{} {} {} {} {}".format(label,x,y,width,height))
	f.write('\n')
	f.close()
				
def digitYoloFormat(x,y,width,height,xmlName,label):
	
	if not os.path.exists('yolo'):
		os.makedirs('yolo')
	

	f= open("yolo/{}.txt".format(xmlName),"a")
	f.write("{} {} {} {} {}".format(label,x,y,width,height))
	f.write('\n')
	f.close()


def findDigits():


	path = '../Rough-Digit-Classification/Annotations'
	for filename in os.listdir(path):
		if not filename.endswith('.xml'):continue
		fullname = os.path.join(path, filename)
		xmlName = filename.replace('.xml','')
		tree = ET.parse(fullname)
		root = tree.getroot()


		for size in root.iter('size'):
		##value = type_tag.get('bndbox')
			imgWidth = int(size.find('width').text)
			imgHeight = int(size.find('height').text)
			print(imgHeight,imgWidth)

		for size in root.iter('object'):
		##value = type_tag.get('bndbox')
			digit = int(size.find('name').text)
			print(digit)
			xMax = int(size.find('bndbox').find('xmax').text)
			xMin = int(size.find('bndbox').find('xmin').text)
			yMax = int(size.find('bndbox').find('ymax').text)
			yMin = int(size.find('bndbox').find('ymin').text)
			print(xMax,xMin,yMax,yMin)

		
			calculate(imgWidth,imgHeight,xMax,xMin,yMax,yMin,xmlName,digit)



		
					


if __name__ == '__main__':
	main()