from multiprocessing import Process, Pipe

def child_process(conn):
    conn.send("Hello from child")
    conn.close()

if __name__ == "__main__":
    # Create a Pipe (two connection objects)
    parent_conn, child_conn = Pipe()

    # Create a new process, passing one end of the pipe to the child
    process = Process(target=child_process, args=(child_conn,))
    process.start()

    # Receive data from the child process
    print("Parent received:", parent_conn.recv())

    # Wait for the child process to finish
    process.join()
