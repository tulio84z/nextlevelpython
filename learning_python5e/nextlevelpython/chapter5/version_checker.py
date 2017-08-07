import sys

print("version_checker FILE")

def is_version_27():
	return check_version("2.7")

def is_version_36():
    return check_version("3.6")

def check_version(ver):
	print(ver)
	curr_ver = sys.version.split(" ")[0]
	if curr_ver.startswith(ver):
	   return True
	return False

def get_supported_versions():

	return list("2.7","3.6")