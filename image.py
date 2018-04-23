from PIL import Image
import StringIO

def convert(data):
	tempBuff = StringIO.StringIO()
	tempBuff.write(data)
	tempBuff.seek(0)
	image = Image.open(tempBuff)
	image.save('face.jpg')
