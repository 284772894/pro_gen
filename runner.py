from multiprocessing import Process
from gevent import monkey; monkey.patch_all()
import gevent

import requests

url = "XXX"

class Producer(object):
    def __init__(self):
       self._rungevent()
    def _rungevent(self):
        jobs = []
        for i in range(1000): # 启动1000个协程请求，有socket的1024端口限制
            jobs.append(gevent.spawn(self.produce))
        gevent.joinall(jobs)
    def produce(self):
        r = requests.get(url)
        if r.status_code == 200:
            r.encoding = 'UTF-8'
            print(r.text)
            return r.text
        else:
            print("失败咯")
        return {}
def main():
    p = Process(target = Producer, args=()) # 每个进程启动1000个请求
    p.start()

    p1 = Process(target = Producer, args=())
    p1.start()


if __name__ == '__main__':
    main()
