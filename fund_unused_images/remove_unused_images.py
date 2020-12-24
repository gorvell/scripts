# coding=utf-8

import glob
import os
import re
from find_xcassets import *

# 搜索的目标路径
path = '/Users/mac/Desktop/Code/beijingbus_ios/BJBus'
# 忽略的图片名称正则数组
ignores = {r'guide_\d+'}


def find_unused_images_at_path(root):
	xcassets = find_xcassets(root)
	unused_images = []
	for xcasset in xcassets:
		images = glob.glob(xcasset + '/*/*.imageset')
		unused_images += find_unused_images(images)

	text_path = 'unused_images.txt'
	text = '\n'.join(sorted(unused_images))
	os.system('echo "%s" > %s' % (text, text_path))
	print 'unused res:%d' % (len(unused_images))
	print 'Done!'


def find_unused_images(images):
	image_names = [os.path.basename(image)[:-len(".imageset")] for image in images]
	unused_images = []
	for i in range(0, len(images)):
		image_name = image_names[i]
		if is_ignore(image_name):
			continue
		command = 'ag "%s" %s' % (image_name, path)
		result = os.popen(command).read()
		if result == '':
			unused_images.append(images[i])
			print 'remove %s' % (images[i])
            os.system('rm -rf %s' % (images[i]))

	return unused_images


def is_ignore(image_name):
    for ignore in ignores:
        if re.match(ignore, image_name):
            return True
    return False


if __name__ == '__main__':
    find_unused_images_at_path(path)