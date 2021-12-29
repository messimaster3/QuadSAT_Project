#import bagpy
#from bagpy import bagreader
'''
bag = rosbag.Bag('/dataFiles/drone_2021-09-12-16-13-35.bag')
for topic, msg, t in bag.read_messages(topics=['FCU/GPS_Int_Data', 'altitude']):
    print(msg)
bag.close()

b = bagreader('/dataFiles/drone_2021-09-12-16-13-35.bag')

# get the list of topicspi
print(b.topic_table)
'''
"""
from rosbags.rosbag2 import Reader
from rosbags.serde import deserialize_cdr
"""
"""
f = open("dataFiles/drone_2021-09-12-16-13-35./metadata.yaml", "r")
print(f.read())
"""
"""
with Reader('dataFiles/drone_2021-09-12-16-13-35') as reader:
    for connection, timestamp, rawdata in reader.messages(['/FCU/GPU_Int_Data']):
        msg = deserialize_cdr(rawdata, connection.msgtype)
        print(msg.header.frame_id)        
"""

from rosbags.rosbag1 import Reader
from rosbags.serde import deserialize_cdr, ros1_to_cdr

# create reader instance
with Reader('dataFiles/drone_2021-09-12-16-13-35.bag') as reader:
    # topic and msgtype information is available on .connections dictionary
   # for connection in reader.connections.values():
       # print("Connection type " + connection.topic)
       # print(type(connection.msgtype))



 # iterate over messages
    for connection, timestamp, rawdata in reader.messages():
        if connection.topic == '/FCU/GPS_Int_Data':
            msg = deserialize_cdr(ros1_to_cdr(rawdata, connection.msgtype), connection.msgtype)
            #print(msg.header.frame_id)