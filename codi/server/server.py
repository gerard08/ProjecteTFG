import multiprocessing
import socket

def tracta(connection, address):
    try:
        print("Connected %r at %r", connection, address)
        data = connection.recv(4)
        if data == "":
            print("Socket closed remotely")
        print("Received data %r", data)

        data = connection.recv(4)
        if data == "":
            print("Socket closed remotely")
        print("Received data %r", data)

        connection.sendall(b'tot ok bro :)')
        print("Sent data")
    except:
        print("Problem handling request")
    finally:
        print("Closing socket")
        connection.close()

class Server(object):
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def start(self):
        print("listening")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.hostname, self.port))
        self.socket.listen(1)

        while True:
            conn, address = self.socket.accept()
            print("Got connection")
            process = multiprocessing.Process(target=tracta, args=(conn, address))
            process.daemon = True
            process.start()
            print("Started process ", process)

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    server = Server("0.0.0.0", 9000)
    try:
        logging.info("Listening")
        server.start()
    except:
        logging.exception("Unexpected exception")
    finally:
        logging.info("Shutting down")
        for process in multiprocessing.active_children():
            logging.info("Shutting down process %r", process)
            process.terminate()
            process.join()
    logging.info("All done")