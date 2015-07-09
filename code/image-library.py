
import numpy as np
import IPython

class Image(object):
	def __init__(self, w, h, pixel_format='', pixel_type='', initial=None):
		""" initializes an image object """

		if not (isinstance(w, int) and isinstance(h, int)):
			print "Width and height must be integer"
			raise ValueError

		if pixel_format not in ['int', 'float']:
			print "Pixel format must be 'int' or 'float'"
			raise ValueError

		if pixel_type not in ['rgb', 'grey']:
			print "Pixel type must be 'rgb' or 'grey'"
			raise ValueError



		self.__pixel_format = pixel_format
		self.__pixel_type = pixel_type

		if initial != None:

			self.__image = np.zeros((initial.shape[0],initial.shape[1],initial.shape[2]),dtype=initial.dtype)

		else:

			if pixel_format == 'int':
				if pixel_type == 'rgb':
					self.__image = np.zeros((w,h,3),dtype=np.int)
				else:
					self.__image = np.zeros((w,h,1),dtype=np.int)
			else:
				if pixel_type == 'rgb':
					self.__image = np.zeros((w,h,3),dtype=np.float)
				else:
					self.__image = np.zeros((w,h,1),dtype=np.float)

	def width(self):
		""" returns the width of an image """
		return self.__image.shape[0]

	def height(self):
		""" returns the height of an image """
		return self.__image.shape[1]

	def copy(self):
		""" returns an identical copy of the image """
		return Image(self.width(), self.height(), self.__pixel_format, self.__pixel_type, initial=self.__image)


	def get(self, w, h):
		""" returns the pixel value(s) at the specified location """
		return self.__image[w,h,:]

	def set(self, w, h, val):
		""" sets the pixel value(s) at the specified location """
		self.__image[w,h,:] = val

	def convolve(self, kernel):
		# convole image with kernel of 3x3 pixels
		# create new image with the result

		return

	def scale(self, sca):
		""" scales the image down by the scale factor in each direction """
		# scale image
		# half in width and half in height

		return



def main():
	image = Image(20, 30, 'boo', 'rgb')
	print image
	print image.width()
	print image.height()
	print image.copy()
	print image.get(2, 3)
	image.set(2, 3, [2, 3, 4])
	print image.get(2,3)
	print '--------'



if __name__ == "__main__":
    main()