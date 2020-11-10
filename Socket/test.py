import socket
import threading
import time


HOST = '192.168.0.106'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


def process_data_from_server(x):
    x1, y1 = x.split(",")
    return x1,y1


def my_client():
    threading.Timer(11, my_client).start()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

        try:
            s.connect((HOST, PORT))

        except socket.error as e:
            print(str(e))
            s.connect((HOST, PORT))

        my = input("Enter command ")

        my_inp = my.encode('utf-8')

        s.sendall(my_inp)

        data = s.recv(1024).decode('utf-8')

        x_temperature,y_humidity = process_data_from_server(data)
        print("Temperature in Celcius {}".format(x_temperature))
        print("Humidity in Percentage {}".format(y_humidity))

        s.close()
        time.sleep(5)


if __name__ == "__main__":
    while True:
        my_client()
