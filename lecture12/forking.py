from multiprocessing import Process
import os

# Function for the new process
def child_process():
    print(f"Child process, PID: {os.getpid()}")
    print("This is the child process doing its work")

# Main process
if __name__ == "__main__":
    # Create a new process
    process = Process(target=child_process)
    process.start()  # Start the new process
    process.join()   # Wait for the process to complete

    print(f"Parent process, PID: {os.getpid()}")
    print(f"Child process terminated with PID: {process.pid}")
