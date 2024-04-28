import instance
import processor
import ReadWrite as RW
import threading

if __name__=='__main__':

    url="https://www.velmano.com/app"
    
    aninstance=instance.session(url)
    aninstance.start()
    RW.read(aninstance)
    Data=processor.dataClass()
    th=threading.Thread(target=Data.schedule)
    th.start()
    RW.schedule(th,aninstance,Data)
