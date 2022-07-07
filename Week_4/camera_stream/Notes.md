# Camera assignment
### Target of the assignment
Create two applications in python:
- Server application that waits for clients to connect and stream video data, each client has a dedicated display window
- Client application that reads the video stream from physical cameras and packages to be sent to the main server

### References and tutorials:
References for python functions and classes:
- **cv2** : Wrapper for the opencv library, used to read camera video stream and display it on the screen
- **numpy** : High performance matrix mathematics library 
- **socket** : Low level networking interface, used to create sockets using various protocols, documentation available at: https://docs.python.org/3/library/socket.html
- **select** : Object for managing efficiently IO operations and avoiding blocking operations, documentation available at: https://docs.python.org/3/library/select.html
- **gzip** : Object used to compress and decompress raw binary data using the gzip format, the documentation is available at: https://docs.python.org/3/library/gzip.html

For a compressive tutorial on python sockets see: https://realpython.com/python-sockets/

### Important notes for the sample applications:
When binding the address for the server socket is important to note:
- For servers accessible for only the same machine use "127.0.0.1"
- To make the server listen to a specific interface (wifi/ethernet) use the ip address assigned to that interface
- To make the server accept clients from any source, use "0.0.0.0" as address

For both server and client is important to set the parameters to:
- In the constructor: AF_INET (IPv4), SOCK_STREAM (TCP)
- Set the socket to blocking mode, to make the program wait for the operation finish executing.

For the server use an execution loop with the following elements:
- "select" object wrapped in a catch "KeyboardInterrupt":
    - "select" is used as it is available on most operating systems.
    - Call select with the array of client sockets and server socket as read parameter, the function will return an array with sockets that have data to be read from or an empty array when it times out
    - The other two arguments are not used for this assignment
    - Catch keyboard interrupt (Ctrl + C) and cleanly close all the active sockets

- For each ready to be read socket:
    - Check is the ready socket is the server, in this case it means a new client socket requested to connect. Accept the socket and append it to the managed list or refuse if to many sockets are active
    - Do a "peek" receive of size 1, if the function returns 0 it means the client gracefully disconnects and needs to be closed on the server side
    - Read header component, first element is an unsigned byte representing the client ID, the second element is an UInt32 representing the size of the video frame data
    - Read from the socket until receiving a body with a size matching the header
    - Display the image
    - If an error is encountered, close the socket and remove it from the managed list

Steps to display a video frame:
- Read data from socket based on header => compressed video frame
- Gzip decompress => raw binary video frame
- Numpy array conversion with type int8 => numpy object
- OpenCV decode with flag *IMREAD_COLOR* => cv2 frame
- OpenCV image show

Steps to read and package a video frame:
- OpenCV read from camera => cv2 frame
- OpenCV encode to format ".bmp" and convert to bytes => raw binary video frame
- Gzip compress with level 9 => compressed video frame
- Build header with camera id and compressed video frame size => binary header
- Append body of message to the header => binary header + compressed video header
- Send package thorough socket