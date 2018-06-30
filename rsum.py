import hashlib
import os
import sys

m = hashlib.sha1()
hash_size = 1*1024*1024
file_size = os.stat(sys.argv[1]).st_size
with open(sys.argv[1], 'rb') as f:
            data = f.read(hash_size)
	            m.update(data)
		            f.seek(file_size//2)
			            data = f.read(hash_size)
				            m.update(data)
					            f.seek(file_size-hash_size)
						            data = f.read(hash_size)
							            m.update(data)
								    m.update(str(file_size))
								    print(m.hexdigest())
