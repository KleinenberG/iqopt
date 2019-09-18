#!/usr/bin/env python

from minio import Minio
from minio.error import ResponseError

client = Minio('192.168.10.3:9000', access_key='GJ1SUM26WPKUN17JX46J', secret_key='NANQKuboSKbI3UwZ95qkokADSblFohPuyZtBEECn', secure=False)
#client.make_bucket('second')
#client.fput_object('second', 'test.jpg', '/home/devup/projects/iqopt/test.jpg')
#data = client.fget_object('first', 'test.jpg', '/home/devup/projects/test.jpg')

try:
    data = client.fget_object('first', 'test.jpg', '/home/devup/projects/iqopt/test.jpg')
    with open('test.jpg', 'r+') as new_data:
        i = 0
        while i <= 1000:
            new_data.write(' ')
            i=i+1
        new_data.close()
    data = new_data


except ResponseError as err:
 print(err)



 #try:
 #    data = 1.sh
 #    with open('1.sh', 'a+') as new_data:
 #        for d in data.stream(32*1024):
 #           new_data.write(d)

#
