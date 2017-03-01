"""
Functions for loading the BBTXT files.

A BBTXT file is formatted like this:
filename label confidence xmin ymin xmax ymax
filename label confidence xmin ymin xmax ymax
filename label confidence xmin ymin xmax ymax
...
"""

__date__   = '12/02/2016'
__author__ = 'Libor Novak'
__email__  = 'novakli2@fel.cvut.cz'

from classes import BB2D


####################################################################################################
#                                            FUNCTIONS                                             # 
####################################################################################################

def load_bbtxt(path_bbtxt):
	"""
	Loads a BBTXT file into a dictionary indexed by file names.

	Input:
		path_bbtxt: Path to a BBTXT file
	Returns:
		dictionary of lists of BB2d objects
	"""
	with open(path_bbtxt, 'r') as infile:
		# Ok, the file is open so we can start reading
		image_dict = {}

		for line in infile:
			line = line.rstrip('\n')
			data = line.split(' ')

			filename = data[0]
			if filename not in image_dict:
				# This image is not in the list yet -> initialize it
				image_dict[filename] = []

			image_dict[filename].append(BB2D(xmin=float(data[3]), ymin=float(data[4]),
											 xmax=float(data[5]), ymax=float(data[6]),
											 label=int(data[1]), confidence=float(data[2])))

		return image_dict

	print('ERROR: File "%s" could not be opened!'%(path_bbtxt))
	exit(1)
