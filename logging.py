def logThis(logText: str):
    import time


    with open("LOG.log", "a") as log:
        log.write(f"{str(time.time())}, --- , {logText}")
        log.close()


def syncLog(serverIP, serverPORT):
    with open("LOG.log", "r") as log:
        import socket

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect((serverIP, serverPORT))
        s.send(log.encode())

        recieved = s.recv(4096)

        while (len(recieved) > 0):
            print(recieved)
            recieved = s.recv(4096)