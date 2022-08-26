from re import L
import socket
from tracemalloc import stop
from PIL import ImageGrab
import time







def send_pre():
    image = ImageGrab.grab()
    image_bytes = image.tobytes()
    image_bytes_len = len(image_bytes)
    return image_bytes, image_bytes_len
    

def get_len(image_bytes_len):
    #发送长度

    sk.send(str(image_bytes_len).encode())
    
    
    return None

def send_start(image_bytes_len):
    #输入长度和图像比特数据并发送
    image = ImageGrab.grab()
    image_bytes = image.tobytes()
    send_size = 0
    while True:
        if image_bytes_len - send_size >= 10240:
            sk.send(image_bytes[send_size:send_size+10240])
            send_size += 10240
        else:
            difference = image_bytes_len - send_size
            sk.send(image_bytes[send_size:send_size+difference])
            send_size += difference
            break
    return None
while True:
    try:
        while True:
            try:
                print("start")
                sk = socket.socket()
                Host = '192.168.101.100'
                Port = 12234
                print("wating server")
                sk.connect((Host, Port))
                
                print('cs')
                break

            except:
                print('ss')
                time.sleep(10)
                continue

        while True:
            print("wating")
            choo = sk.recv(1024).decode()
            if choo == "sp":
                image_bytes, image_bytes_len = send_pre()
                print("sp")
                print(image_bytes_len)
            elif choo == "gl":
                get_len(image_bytes_len)
                print("gl")
            elif choo == "ss":
                send_start(image_bytes_len)
                print("ss")
            else:
                break
    except:
        continue
