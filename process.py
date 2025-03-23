import multiprocessing
import time
import os

def process_task(name):
    print(f"Process {name} | PID: {os.getpid()} | Parent PID: {os.getppid()}")
    time.sleep(2)
    print(f"Process {name} is done\n")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=process_task, args=("P1",))
    p2 = multiprocessing.Process(target=process_task, args=("P2",))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("All processes completed")
