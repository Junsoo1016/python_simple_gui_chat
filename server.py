from http import client
import socket
import threading

HOST = '127.0.0.1' # ipconfig
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

client = []
nicknames = []

