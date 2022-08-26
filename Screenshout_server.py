import socket
from PIL import Image
from PIL import ImageFilter
import time
Host = '0.0.0.0'
Port = 12234
sk = socket.socket()
sk.bind((Host, Port))
sk.listen(1)

print('启动服务器')
cli, add = sk.accept()
print('已连接')


def receive_once(pixel):
    #循环一次
    #pixel为屏幕分辨率 例：（1920，1080）
    cli.send("sp".encode("utf-8"))
    cli.send("gl".encode("utf-8"))
    image_bytes_len = int(cli.recv(1024).decode())
    

    print(image_bytes_len)
    print("开始接收")
    cli.send("ss".encode("utf-8"))
    rec_size = 0
    image_bytes = b""

    while True:
        if image_bytes_len > rec_size:
            if image_bytes_len-rec_size <= 10240:
                data = cli.recv(image_bytes_len-rec_size)
                image_bytes += data
                rec_size += len(data)
            else:
                data = cli.recv(10240)
                image_bytes += data
                rec_size += len(data)
        else:
            break

    ma = Image.frombytes('RGB', pixel,image_bytes)
    ma.save(r"E:/anything/py/sc/sc4/photo.png","png")
    print("完成")
    return None

def receive_Time (SJ,pixel):
    #循环一定的时间（Time)后停止。
    #pixel为屏幕分辨率 例：（1920，1080）
    cli.send("sp".encode("utf-8"))
    cli.send("gl".encode("utf-8"))
    image_bytes_len = int(cli.recv(1024).decode())
    
    print(image_bytes_len)
    print("开始接收")
    f_n = 0

    t = int(time.time())
    total_time = 0
    SJ = int(SJ)
    print(SJ)
    while total_time  < SJ:
        
        cli.send("ss".encode("utf-8"))
        rec_size = 0
        image_bytes = b""

        while True:
            if image_bytes_len > rec_size:
                if image_bytes_len-rec_size <= 10240:
                    data = cli.recv(image_bytes_len-rec_size)
                    image_bytes += data
                    rec_size += len(data)
                    
                else:
                    data = cli.recv(10240)
                    image_bytes += data
                    rec_size += len(data)
                    
            else:
                
                print('123')
                break

        ma = Image.frombytes('RGB', pixel,image_bytes)
        f_n = f_n + 1
        ma.save('E:/anything/py/sc/sc4/time/{}.png'.format(f_n),"png")
        total_time = int(time.time()) - t
        print('已运行：{}S, 已输出第{}张图片'.format(total_time,f_n))
    print('完成')
    return None

def receive_frequency(fre,pixel):
    #循环一定的次数后停止
    #pixel为屏幕分辨率 例：（1920，1080）
    cli.send("sp".encode("utf-8"))
    cli.send("gl".encode("utf-8"))
    image_bytes_len = int(cli.recv(1024).decode())
    
    print(image_bytes_len)
    print("开始接收")
    f_n = 0

    
    
    fre = int(fre)
    while f_n  <= fre:
        cli.send("ss".encode("utf-8"))
        rec_size = 0
        image_bytes = b""

        while True:
            if image_bytes_len > rec_size:
                if image_bytes_len-rec_size <= 10240:
                    data = cli.recv(image_bytes_len-rec_size)
                    image_bytes += data
                    rec_size += len(data)
                    
                else:
                    data = cli.recv(10240)
                    image_bytes += data
                    rec_size += len(data)
                    
            else:
                
                print('123')
                break

        ma = Image.frombytes('RGB', pixel,image_bytes)
        f_n = f_n + 1
        ma.save('E:/anything/py/sc/sc4/fre/{}.png'.format(f_n),"png")
        print('已输出第{}张图片, 总共有{}站'.format(f_n,fre))
       

    return None

def receive_enter():
    #当按下enter后结束循环（待开发）

    return None


L = int(input('请输入屏幕长:'))
W = int(input('请输入屏幕宽:'))
pixel = (L,W)
while True:
    
    choose = input("请选择：\n 1.循环一次\n 2.按照时间循环\n 3.按照次数循环\n:")

    if choose == "1":
        receive_once(pixel)

    elif choose == "2":
        tiii = input("time:")
        receive_Time(tiii,pixel)
    elif choose == "3":
        fre = input("fre:")
        receive_frequency(fre,pixel)
    else:
        print('error')
        break






print("接受结束")
input("FINISH")