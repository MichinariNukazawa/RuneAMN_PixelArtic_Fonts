#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# brief : pixel artic raster image to SVG image.
# usage : this_script.py --source_image=font_source/RuneAMN_PixelArtic_sans_6x10.png
#
# author : MichinariNukazawa / "project daisy bell"
# 	michinari.nukazawa@gmail.com
# 	https://github.com/MichinariNukazawa/RuneAMN_Pro_Series_Fonts
# license : 2-clause BSD license
#
# depend : python3,docopt,pil
# Install :
# 		sudo apt-get install python3-docopt python3-pil
#		or
# 		pip install docopt pil
#

"""Process some integers.

usage: this_script.py [-h] <dst_image> <src_image>

options:
	-h, --help  show this help message and exit
"""

from docopt import docopt
from pprint import pprint
import math
import re
import os
import os.path
from PIL import Image
from xml.etree import ElementTree
from xml.dom import minidom
import re


glyph_height = 1000

def getSetting(args):
	setting = {}
	setting['src_image'] = {
		'filepath':		args['<src_image>'],
		'glyph_width':		6,
		'glyph_height':		10,
		'row':			2,
		'column':		20,
	}
	glyph_width = ( float(setting['src_image']['glyph_width']) / float(setting['src_image']['glyph_height']) ) * glyph_height
	glyph_width = 1000
	setting['dst_image'] = {
		'filepath':		args['<dst_image>'],
		'glyph_width':		glyph_width,
		'glyph_height':		glyph_height,
		# 'base_line':		0,
		'row':			4,
		'column':		7,
	}
	setting['convert'] = {
		'between':		40,
		'extend':		0,
	}

	reSrcFilepath = re.compile('_([0-9]+)x([0-9]+)_[^0-9]*([0-9]+)\.[\w]+$')
	m = reSrcFilepath.search(setting['src_image']['filepath'])
	if None == m:
		return None

	setting['src_image']['glyph_width'] = int(m.group(1)) + 1
	setting['src_image']['glyph_height'] = int(m.group(2))
	setting['convert']['between'] = int(m.group(3))

	# 空隙がゼロの場合に、ドット間に隙間があいてしまわないよう処置
	if 0 == setting['convert']['between']:
		setting['convert']['extend'] = 2

	return setting

def rasterFromImageArea(image, x, y, w, h):
	raster = [[0 for i in range(w)] for j in range(h)]
	for iy in range(h):
		for ix in range(w):
			r,g,b,a = image.getpixel((x + ix,y + iy))
			if a < 128:
				raster[iy][ix] = False
			else:
				raster[iy][ix] = True
	return raster

def readRastersFromImage(src_image):
	rasters = {}
	image = Image.open(src_image['filepath'])
	image = image.convert('RGBA')
	for iy in range(src_image['row']):
		for ix in range(src_image['column']):
			codepoint = ord('A') + (iy * src_image['column']) + ix
			# pprint("%c %d" % (codepoint, codepoint))
			raster = rasterFromImageArea(
					image,
					ix * src_image['glyph_width'], iy * src_image['glyph_height'],
					src_image['glyph_width'], src_image['glyph_height'])
			rasters[codepoint] = raster
	return rasters

def translateFromCodepoint(setting, codepoint):
	index = codepoint - ord('A')
	tx = (index % setting['dst_image']['column'])
	tx *= setting['dst_image']['glyph_width']
	ty = math.floor((index / setting['dst_image']['column']))
	ty *= setting['dst_image']['glyph_height']
	translate = 'translate(%d, %d)' % (tx, ty)
	# pprint("%c %d %d %d" % (codepoint, index, tx, ty))
	return translate

def getRectElement(setting, ix, iy):
	pixel = glyph_height / setting['src_image']['glyph_height']
	element = ElementTree.Element('rect')
	element.set('x', str((pixel * ix) + setting['convert']['between']))
	element.set('y', str((pixel * iy) + setting['convert']['between']))
	element.set('width', str(pixel - setting['convert']['between'] + setting['convert']['extend']))
	element.set('height', str(pixel - setting['convert']['between'] + setting['convert']['extend']))
	return element

def getSvg(setting):
	svg = ElementTree.Element('svg')
	svg.set('width', str(setting['dst_image']['glyph_width'] * setting['dst_image']['column']))
	svg.set('height', str(setting['dst_image']['glyph_height'] * setting['dst_image']['row']))
	svg.set('xmlns', "http://www.w3.org/2000/svg")

	rasters = readRastersFromImage(setting['src_image'])

	for codepoint in range(ord('A'), ord('Z') + 1):
		# pprint("%c %d" % (codepoint, codepoint))
		raster = rasters[codepoint]
		glyph_group = ElementTree.Element('g')
		glyph_group.set('name', '%c' % codepoint)
		translate = translateFromCodepoint(setting, codepoint)
		for iy in range(setting['src_image']['glyph_height']):
			for ix in range(setting['src_image']['glyph_width']):
				if(raster[iy][ix]):
					element = getRectElement(setting, ix, iy)
					element.set('transform', translate)
					glyph_group.append(element)
		svg.append(glyph_group)
	return svg

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="\t")

if __name__ == '__main__':
	args = docopt(__doc__)
	
	# 変換設定を生成
	setting = getSetting(args)
	
	# ピクセルと変換設定からSVGファイルを生成
	svg = getSvg(setting)

	svg_str = prettify(svg)
	filepath = setting['dst_image']['filepath']
	f = open(filepath, 'w')
	f.write(svg_str)
	f.close()



