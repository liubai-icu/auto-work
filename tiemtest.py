import time
# data = time.localtime(time.time())
data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
print(data)