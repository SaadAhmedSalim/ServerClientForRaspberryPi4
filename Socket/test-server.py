try:
    import socket
    import numpy as np
    import encodings
    import RPi.GPIO as GPIO
    import dht11
    import time
    import sys
    import adafruit_dht
    import board
    print("All Module loaded")
except Exception as e:
    print("Error: {}".format(e))



HOST = '192.168.0.106'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

"""
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
instance = dht11.DHT11(pin=17)




def random_data():
    pin = 17
    #sensor = Adafruit_DHT.DHT11
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)

    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        print("data was written on database T{} H{}".format(temperature,humidity))
        data = '{},{}'.format(temperature,humidity)
        return data
    

# Initial the dht device, with data pin connected to:


# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)
"""
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT11(board.D17)

def random_data():
    count = 0 ;
    while True:
        try:
            
            # Print the values to the serial port
            count = count+1;
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
            print(
                "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
                )
            )
            print(count)
            data = '{},{}'.format(temperature_c,humidity)
            return data
            #time.sleep(5.0)
            dhtDevice.exit()
            

            """
            result= instance.read()
            if result.is_valid():
                data = '{},{}'.format(result.temperature, result.humidity)
                return data
                #print("Temp: %d C" % result.temperature + ' '+"Humidity: %d %%" % result.humidity)
                count+=1
                time.sleep(3)

                
                if count==5:
                    data = '{},{}'.format(result.temperature, result.humidity)
                    return data
                    sys.exit("Taken 5 value")
                """

                   
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(5.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
            

        break




def my_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Server Started waiting for client to connect ")
        s.bind((HOST, PORT))
        s.listen(5)
        conn, addr = s.accept()

        print('Got connection from', addr)
        conn.sendall(b'Thank you for connecting')
            

        while True:
                  
                data = conn.recv(1024).decode('utf-8')

                if str(data) == "Data":

                    print("Ok Sending data ")

                    my_data = random_data()

                    x_encoded_data = my_data.encode('utf-8')

                    conn.sendall(x_encoded_data)
                    sys.exit("Taken")

                elif  str(data) == "Quit":
                    print("shutting down server ")
                    break


                if not data:
                    break
                else:
                    pass

                conn.close()

        
       
if __name__ == '__main__':
    while True:
        my_server()
