import multiprocessing
import socket
from icgc import calculaImatge
import time

def tracta(connection, address):
    try:
        #print("Connected %r at %r", connection, address)
        #print(time.localtime)
        ############REBEM PARÀMETRES################
        #rebem la x
        x = float(connection.recv(15))
        if x == "":
            print("Socket closed remotely")
        print("x:", x)

        #rebem la y
        y = float(connection.recv(15))
        if y == "":
            print("Socket closed remotely")
        print("y:", y)

        #rebem el step
        step = float(connection.recv(3))
        if step == "":
            print("Socket closed remotely")
        print("step:", step)

        #rebem el tipus d'imatge (0->imatge, 1->relleu)
        tipus = int(connection.recv(1))
        if tipus == "":
            print("Socket closed remotely")
        print("tipus:", tipus)
        ###########CALCULEM IMATGE I LA RETORNEM############
        #print(tipus)
        img = None
        if tipus == 1:
            #print("relleu :)")
            img = calculaImatge(x,y,step,'relleu')
        else:
            #print("notipus")
            img = calculaImatge(x,y,step)
        
        import sys
        #print(sys.getsizeof(img))
        if sys.getsizeof(img) <= 332:
            print(img)
        connection.sendall(img)
        #print("Sent data")
    except Exception as e: 
        print(e)
        print("Problem handling request")
    finally:
        #del x,y,step
        #print("Closing socket")
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
            #print("Got connection")
            process = multiprocessing.Process(target=tracta, args=(conn, address))
            process.daemon = True
            process.start()
            #print("Started process ", process)

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    server = Server("0.0.0.0", 32500)
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