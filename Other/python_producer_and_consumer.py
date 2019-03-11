#-*- coding:utf-8
'''
python 的生产者消费者模式

生产者消费之模型就是,比如一个包子铺,中的顾客吃包子,和厨师做包子,
不可能是将包子一块做出来,在给顾客吃,但是单线程只能这麽做,
所以用多线程来执行,厨师一边做包子,顾客一边吃包子,
当顾客少时,厨师做的包子就放在一个容器中,等着顾客来吃,
当顾客多的时候,就从容器中先取出来给顾客吃,厨师继续做包子
用队列来模拟这个容器

# 当做完一个包子后就要给顾客发送一个信号,表示已经做完,让他们吃包子

总结：
python中要想利用好CPU，还是用多进程来做吧。或者，可以使用协程。multiprocessing和gevent在召唤你。
GIL不是bug，Guido也不是水平有限才留下这么个东西。龟叔曾经说过，尝试不用GIL而用其他的方式来做线程安全，结果python语言整体效率又下降了一倍，权衡利弊，GIL是最好的选择——不是去不掉，而是故意留着的。
想让python计算速度快起来，又不想写C？用pypy吧，这才是真正的大杀器。

python的多线程主要实现模块CPYTHON因为有GIL的关系，不是真正意义的多线程，可以用python的多进程编程运行cpu密集型的任务：具体参考
https://www.cnblogs.com/zingp/p/5878330.html

'''
import threading, Queue, time

q = Queue.Queue(10)

def Producer(name):
    count = 0   #表示生产的包子总数
    while count < 10:
        print "厨师{0}在做包子".format(name)
        time.sleep(2)
        q.put(count)  #容器中添加包子
        #当一个包子做完后给顾客发送一个信号，表示已经做完
        print "Producer {0} 已经做好了第{1}个包子".format(name, count)
        count += 1
        print "ok ... ... "


def Consumer(name):
    count = 0   #count 表示被吃的包子总数
    while count < 10:
        time.sleep(2)  #排队取包子
        if not q.empty():
            data = q.get()   #get_nowait 是非阻塞的取，如果队列为空，直接抛出 empty异常, get() 是阻塞的
            print "Consumer {0} 已经把第{1}个包子吃了".format(name, count)
        else:
            print "包子已经被吃完"
        count += 1


if __name__ == '__main__':
    p1 = threading.Thread(target = Producer, args= ('A 君',))
    c1 = threading.Thread(target = Consumer, args = ('B 消费君',))
    c2 = threading.Thread(target = Consumer, args = ('C 消费均',))
    p1.start()
    c1.start()
    c2.start()

































