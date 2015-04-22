# http://picamera.readthedocs.org/en/release-1.9/recipes1.html#recording-to-a-network-stream last example

import socket
import time
import picamera

with picamera.PiCamera() as camera:
    #camera.resolution = (640, 480)
    #camera.framerate = 24
    camera.resolution = (320, 240)
    camera.framerate = 15

    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 8000))
    server_socket.listen(0)

    # Accept a single connection and make a file-like object out of it
    connection = server_socket.accept()[0].makefile('wb')
    try:
        camera.start_recording(connection, format='h264')
        camera.wait_recording(6000)
        camera.stop_recording()
    finally:
        #camera.stop_recording()
        connection.close()
        server_socket.close()
