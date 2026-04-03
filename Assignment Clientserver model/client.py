import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("localhost", 8080))

welcome = client_socket.recv(64).decode("utf-8")
print(welcome)

while True:
    guess = input("Enter a number between 1 and 10: ")
    client_socket.send(guess.encode("utf-8"))
    
    response = client_socket.recv(64).decode("utf-8")
    print(response)
    
    if response == "Correct!" or response.startswith("Wrong"):
        break

client_socket.close()
input("Press Enter to exit...")