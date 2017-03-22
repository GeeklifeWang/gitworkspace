import hashlib, os

def md5_string(_str):
    md5 = hashlib.md5()
    md5.update(_str)
    return md5.hexdigest()

def md5_file(path):
    if os.path.isfile(path):
        with open(path, 'rb') as _fp:
            md5 = hashlib.md5()
            data = _fp.read()
            md5.update(data)
            return md5.hexdigest()
    else:
        return None

#print md5_string('wangyouwei')
#print md5_file(r'C:\Users\wangyouwei\Desktop\win32gui.txt')


def sha1_string(_str):
    sha1 = hashlib.sha1()
    sha1.update(_str)
    return sha1.hexdigest()

def sha1_file(path):
    if os.path.isfile(path):
        with open(path, 'rb') as _fp:
            sha1 = hashlib.sha1()
            data = _fp.read()
            sha1.update(data)
            return sha1.hexdigest()
    else:
        return None

#print sha1_string('wangyouwei')
#print sha1_file(r'C:\Users\wangyouwei\Desktop\win32gui.txt')
