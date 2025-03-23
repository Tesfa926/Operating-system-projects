import threading
import time

def thread_task(name):
    print(f"Thread {name} | Thread ID: {threading.get_ident()}")
    time.sleep(2)
    print(f"Thread {name} is done\n")

if __name__ == "__main__":
    t1 = threading.Thread(target=thread_task, args=("T1",))
    t2 = threading.Thread(target=thread_task, args=("T2",))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All threads completed")
