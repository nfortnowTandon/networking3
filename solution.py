from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv) #You can use these print statement to validate return codes from the server.
    # if recv[:3] != '220':
    #    print('220 (???) reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    # if recv1[:3] != '250':
    #    print('250 (helo) reply not received from server.')

    # Send MAIL FROM command and handle server response.
    # Fill in start
    mfCommand = 'MAIL FROM: <Alice>\r\n'
    clientSocket.send(mfCommand.encode())
    recv2 = clientSocket.recv(1024).decode()
    # Fill in end
    # if recv2[:3] != '250':
    #     print('250 (mailfrom) reply not received from server.')

    # Send RCPT TO command and handle server response.
    # Fill in start
    rcptCommand = 'RCPT TO: <Bob>\r\n'
    clientSocket.send(rcptCommand.encode())
    recv3 = clientSocket.recv(1024).decode()
    # Fill in end
    # if recv3[:3] != '250':
    #     print('250 (rcpt) reply not received from server.')

    # Send DATA command and handle server response.
    # Fill in start
    clientSocket.send("DATA".encode())
    recv4 = clientSocket.recv(1024).decode()
    # Fill in end
    # if recv4[:3] != '354':
    #     print('354 (data) reply not received from server.')

    # Send message data.
    # Fill in start
    clientSocket.send(msg.encode())
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start
    clientSocket.send(endmsg.encode())
    recv5 = clientSocket.recv(1024).decode()
    # Fill in end
    # if recv5[:3] != '250':
    #     print('250 (endmsg) reply not received from server.')

    # Send QUIT command and handle server response.
    # Fill in start
    clientSocket.send("QUIT".encode())
    recv6 = clientSocket.recv(1024).decode()
    # Fill in end
#     if recv6[:3] != '221':
#             print('221 (quit) reply not received from server.')
#
#
# smtp_client(1025, '127.0.0.1')
