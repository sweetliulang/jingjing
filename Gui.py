import serial
import matplotlib.pyplot as plt
ser=serial.Serial("COM2",115200)

window_width = 200
plt.ion() #开启interactive mode 成功的关键函数
plt.figure(1)
t = []
for i in range(window_width+1):
    t.append(0)
t_now = 0
m = []
for i in range(window_width+1):
    m.append(0)


for i in range(2000):
    t_now = i*0.1
    if i<=window_width:
        t[i]=t_now      #模拟数据增量流入
        # m[i]=1
        # a=int((ser.read()).hex())
        # print(a,type(a))
        m[i]=int((ser.read()).hex(),16) #模拟数据增量流入  bytes --> str（变成了asc码） --> int(类型变了，数值还是asc码的值）未解决
        plt.xlim(0,20)#横坐标范围
        plt.plot(t[0:i], m[0:i], 'r')
    else:
        t[0:window_width] = t[1:window_width+1]
        t[window_width] = t_now
        m[0:window_width] = m[1:window_width+1]
        m[window_width]=int((ser.read()).hex(),16)
        plt.xlim(int(t[0]),(t[window_width]))
        plt.plot(t[0:window_width+1],m[0:window_width+1],'r')
    plt.show()#注意此函数需要调用
    plt.pause(0.001)#没有此句不显示曲线
ser.close()