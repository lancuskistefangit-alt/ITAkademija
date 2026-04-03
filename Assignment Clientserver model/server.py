import socket
import random

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("localhost", 8080))
server_socket.listen()
print("Server is listening...")

client_socket, addr = server_socket.accept()
print("Welcome")

secret_number = random.randint(1, 10)
print(f"[SERVER] Secret number is: {secret_number}")

client_socket.send(b"Guess the number - enter a number between 1 and 10")

while True:
    data = client_socket.recv(32).decode("utf-8").strip()
    print(f"[CLIENT] Sent: {data}")

    try:
        guess = int(data)
    except ValueError:
        client_socket.send(b"Invalid input! Enter a number from 1 to 10:")
        print("[SERVER] Invalid input received")
        continue

    if guess < 1 or guess > 10:
        client_socket.send(b"Number out of range! Enter a number from 1 to 10:")
        print(f"[SERVER] Out of range input: {guess}")
        continue

    if guess == secret_number:
        client_socket.send(b"Correct!")
        print(f"[SERVER] Client guessed correctly: {guess}")
    else:
        client_socket.send(f"Wrong. The secret number was {secret_number}".encode("utf-8"))
        print(f"[SERVER] Client guessed wrong: {guess}")
    break

client_socket.close()
server_socket.close()
input("Press Enter to exit...")