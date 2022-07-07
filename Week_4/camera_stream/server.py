import struct
import socket
import select
import cv2
import gzip
import numpy as np

class Server():
    def __init__(self, address_ip, address_port) -> None:
        # Bind and start the socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((address_ip, address_port))
        self.server_socket.listen(2)
        self.server_socket.setblocking(True)
        self.socket_read_list = [self.server_socket]
        while(True):
            self.loop_data_read()

    def loop_data_read(self):
        # Iterate and select, the code looks over only ready for read sockets
        try:
            read_ready, _, _ = select.select(self.socket_read_list, [], [], 0.1)
        except KeyboardInterrupt:
            for item in self.socket_read_list:
                item.close()
                exit(0)

        try:
            for item in read_ready:
                # Check if the server receives a new connection request
                if item == self.server_socket:
                    new_client, _ = self.server_socket.accept()

                    # Check is there are already two clients and the server, refuse in that case
                    if len(self.socket_read_list) == 3:
                        new_client.close()
                    else:
                        self.socket_read_list.append(new_client)
                
                # Handle new data packet from a client
                else:
                    # Check for closed signal from client socket
                    # Is the socket is ready but there is no data it means the socket closes
                    if len(item.recv(1, socket.MSG_PEEK)) == 0:
                        self.remove_socket(item)
                        continue
                    # Header contains information for the stream data: 1 byte for camera id and 4 byte for message size
                    raw_header = item.recv(5)
                    (header_id, header_size) = struct.unpack("<BI", raw_header)
                    # Read body data to match target size
                    body_msg = bytes()
                    while(len(body_msg) < header_size):
                        body_msg += item.recv(header_size - len(body_msg)) 
                    # Render image
                    self.render_image(header_id, body_msg)

        except Exception as ex:
            self.remove_socket(item)
            print(f"Dropped message for reason: {ex}")

    def remove_socket(self, closing_socket):
        self.socket_read_list.remove(closing_socket)
        closing_socket.close()
        cv2.destroyAllWindows()

    def render_image(self, id, msg):
        # Decompress bytes
        frame_bytes = gzip.decompress(msg)
        # Convert bytes to numpy array
        frame_raw = np.frombuffer(frame_bytes, np.uint8)
        # Convert numpy array to map
        frame = cv2.imdecode(frame_raw, cv2.IMREAD_COLOR)
        # Display image
        cv2.imshow(f"Camera: {id}", frame)
        cv2.waitKey(2)


if __name__ == "__main__":
    server = Server("127.0.0.1", 9070)