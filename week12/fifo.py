import multiprocessing

def child_process(pipe_conn):
    # Send a message through the pipe
    pipe_conn.send("Hello from the child process!")
    print("Child process: Data sent to pipe.")
    pipe_conn.close()

if __name__ == "__main__":
    # Create a pipe
    parent_conn, child_conn = multiprocessing.Pipe()

    # Start child process
    process = multiprocessing.Process(target=child_process, args=(child_conn,))
    process.start()

    # Parent process reads the data from the pipe
    message = parent_conn.recv()
    print("Parent process: Data received from pipe:", message)

    # Wait for the child process to finish
    process.join()
