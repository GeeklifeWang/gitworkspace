import traceback
import sys
try:
    print a
except Exception,e:
    pass
try:
    print b
except Exception,e:
    pass
print traceback.format_exc()
print sys.exc_info()
