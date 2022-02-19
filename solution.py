from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))

    recv = clientSocket.recv(1024).decode()
    # if recv[:3] != '220':
    #    print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024).decode()
    # print("HELO CMD: ", repr(recv))  # Used for testing.

    # Send MAIL FROM command and handle server response.
    clientSocket.send('MAIL FROM:ab10146@nyu.edu\r\n'.encode())
    recv = clientSocket.recv(1024).decode()
    # print("MAIL FROM CMD: ", repr(recv))  # Used for testing.

    # Send RCPT TO command and handle server response.
    clientSocket.send('RCPT TO:ab10146@nyu.edu\r\n'.encode())
    recv = clientSocket.recv(1024).decode()
    # print("RCPT TO CMD: ", repr(recv))  # Used for testing.

    # Send DATA command and handle server response.
    clientSocket.send('DATA\r\n'.encode())
    recv = clientSocket.recv(1024).decode()
    # print("DATA CMD1: ", repr(recv))  # Used for testing.

    # Send message data.
    clientSocket.send(msg.encode())

    # Message ends with a single period, send message end and handle server response.
    clientSocket.send(endmsg.encode())
    recv = clientSocket.recv(1024).decode()
    # print("DATA CMD2: ", repr(recv))  # Used for testing.

    # Send QUIT command and handle server response.
    clientSocket.send('QUIT\r\n'.encode())
    recv = clientSocket.recv(1024).decode()
    # print("QUIT CMD: ", repr(recv))  # Used for testing.

    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
    # smtp_client(25, 'smtp.nyu.edu')  # Used for testing.
