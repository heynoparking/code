import threading
import queue
import os

buffer_size = 100

lock = threading.Lock()
#queue = queue.Queue(buffer_size)
queue_buffer = queue.Queue(buffer_size)
file_count = 0

def producer(top_dir, queue_buffer):
    # Search sub-dir in top_dir and put them in queue
    queueA = queue.Queue()
    queueA.put(top_dir)
    while not queueA.empty():
        top_dir = queueA.get()
        allfiles = os.listdir(top_dir)
        num = len(allfiles)
        for i in range(num):
            p1=os.path.join(top_dir, allfiles[i])
        
            if os.path.isdir(p1):
                queueA.put(p1)
                queue_buffer.put(p1)



def consumer(queue_buffer):
    # search file in directory
    while not queue_buffer.empty():
        top_dir = queue_buffer.get()
        allfiles = os.listdir(top_dir)
        num = len(allfiles)
        for i in range(num):
            p1=os.path.join(top_dir, allfiles[i])

            if os.path.isfile(p1):
                global file_count
                file_count += 1
    
    
    
queue_buffer.put('./testdata/')
producer('./testdata/', queue_buffer)
consumer(queue_buffer)

print(file_count)

    
def main():
    producer_thread = threading.Thread(target = producer, args = ('./testdata', queue))

    consumer_count = 20
    consumers = []
    for i in range(consumer_count):
        consumers.append(threading.Thread(target = consumer, args = (queue,)))

    producer_thread.start()
    for c in consumers:
        c.start()

    producer_thread.join()
    for c in consumers:
        c.join()

    print(file_count, 'files found.')

if __name__ == "__main__":
    main()