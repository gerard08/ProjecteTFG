import multiprocessing
import socket
from icgc import calculaImatge

def tracta(connection, address):
    try:
        print("Connected %r at %r", connection, address)
        
        ############REBEM PARÀMETRES################
        #rebem la x
        x = float(connection.recv(6))
        if x == "":
            print("Socket closed remotely")
        #print("Received data %r", x)

        #rebem la y
        y = float(connection.recv(6))
        if y == "":
            print("Socket closed remotely")
        #print("Received data %r", data)

        #rebem el step
        step = float(connection.recv(3))
        if step == "":
            print("Socket closed remotely")
        #print("Received data %r", data)

        # #rebem la direccio
        # direccio = connection.recv(1)
        # if direccio == "":
        #     print("Socket closed remotely")
        # #print("Received data %r", data)
        
        ###########CALCULEM IMATGE I LA RETORNEM############

        img = calculaImatge(x,y,step)#,direccio)
        import cv2
        file = open('original.jfif', 'wb')
        file.write(img)
        file.close()
        import sys
        myint = 12
        print(sys.getsizeof(img))
        connection.sendall(img)
        print("Sent data")
    except:
        print("Problem handling request")
    finally:
        #del x,y,step
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