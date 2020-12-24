# coding=utf-8

import os
import re 

root_path = "/Users/mac/Desktop/Code/beijingbus_ios/BJBus"
xcasset_paths = []


def find_xcassets(root):
	items = os.listdir(root)
	for item in items:
		path = os.path.join(root, item)
		if is_xcassets_dir(item):
			xcasset_paths.append(path)
			print '[+] %s' % path
		elif os.path.isdir(path):
			find_xcassets(path)

	return xcasset_paths


def is_xcassets_dir(dir):
	return re.search(r'.xcassets', dir)


if __name__ == '__main__':
	find_xcassets(root_path)