
from PIL import Image
import os

def main():

	counter = 1;
	for x in range(1201,2001):
		fileName = ''
		if len(str(x))==1:
			fileName = 'meter000{}'.format(x)
			print(fileName)
		if len(str(x))==2:
			fileName = 'meter00{}'.format(x)
			print(fileName)
		if len(str(x))==3:
			fileName = 'meter0{}'.format(x)
			print(fileName)
		if len(str(x))==4:
			fileName = 'meter{}'.format(x)
			print(fileName)
		if len(str(x))==5:
			fileName = 'meter{}'.format(x)
			print(fileName)

		transform(fileName)

	
			


def transform(fileName):
	label = 0
	finalX = 0.0
	finalY = 0.0
	finalwidth = 0.0
	finalHeight = 0.0

	image = Image.open("../testing/{}.jpg".format(fileName))
	##image size
	width, height = image.size
	print(width, height)
	
	with open("../testing/{}.txt".format(fileName),"r") as f:

		

		data = []
		String = ""
		for line in f:
			
			data.append(line.strip().replace(':', '').split(" "))
			##print(data)


			if not os.path.exists('results'):
   				 os.makedirs('results')



#position of reading number in counter from left to
		readingNumber = 0
		reading = ''
		for line in data:
				print(line[0])
				if line[0].lower() == 'position':
				
					BoundingBoxW = int(line[3])
					BoundingBoxH = int(line[4])
					label = "Counter"
					finalX = ((int(line[1]))+(BoundingBoxW/2))/width
					finalY = ((int(line[2]))+(BoundingBoxH/2))/height
					finalwidth = (BoundingBoxW/width)
					finalHeight = (BoundingBoxH/height)
					# f= open("results/{}.txt".format(fileName),"a")
					# f.write("{} {} {} {} {}".format(label,finalX,finalY,finalwidth,finalHeight))
					# f.write('\n')
					# f.close()

				if line[0].lower() == 'reading' or line[0].lower() == 'creading' or line[0].lower() == 'qreading':
					
					reading = line[1]

				if line[0].lower() == 'digit':
				
					BoundingBoxW = int(line[4])
					BoundingBoxH = int(line[5])
					label = reading[readingNumber]
					finalX = ((int(line[2])+(BoundingBoxW/2))/width)
					finalY = ((int(line[3])+(BoundingBoxH/2))/height)
					finalwidth = (BoundingBoxW/width)
					finalHeight = (BoundingBoxH/height)
					f= open("results/{}.txt".format(fileName),"a")
					f.write("{} {} {} {} {}".format(label,finalX,finalY,finalwidth,finalHeight))
					f.write('\n')
					f.close()
					readingNumber = readingNumber +1

if __name__ == '__main__':
	main()
