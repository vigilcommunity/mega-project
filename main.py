import os

with open('somefile.txt','rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.txt','wb') as f:
    text = 'hello world'
    f.write(text.encode('utf-8')) 