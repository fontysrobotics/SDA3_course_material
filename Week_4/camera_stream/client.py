import socket
import struct
import cv2
import time
import gzip

class Client():
    def __init__(self, address_ip, address_port, server_hz, camera_id) -> None:
        # Create socket client and connect
        self.socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_client.connect((address_ip, address_port))
        self.socket_client.setblocking(True)

        # Start camera and set resolution
        self.camera_dev = cv2.VideoCapture(camera_id)
        self.camera_dev.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.camera_dev.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)
        self.camera_id_ref = camera_id

        # Read frames at the set frequency
        timestamp = time.time()
        while(True):
            try:
                if(time.time() - timestamp) > (1/server_hz):
                    self.pulse_msg()
                    timestamp = time.time()
            except KeyboardInterrupt:
                self.socket_client.close()
                break

    def pulse_msg(self):
        # Read image 
        res, frame = self.camera_dev.read()
        if res:
            # Convert the frame to bytes
            raw_frame = cv2.imencode(".bmp", frame)[1].tobytes()
            # Compress bytes
            img_msg = gzip.compress(raw_frame, 9)
            # Build header with id and compressed image size
            header_raw = struct.pack("<BI", self.camera_id_ref, len(img_msg))
            # Append body to header
            full_msg = header_raw + img_msg
            # Send message over socket
            self.socket_client.send(full_msg)

if __name__ == "__main__":
    client = Client("127.0.0.1", 9070, 30, 0)