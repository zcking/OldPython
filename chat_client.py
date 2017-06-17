import sys
import socket
import select
from os import system

def chat_client():
	if(len(sys.argv) not in (3, 4)):
		print("Usage: python chat_client.py <hostname> <port> <optional-username>\n")
		sys.exit()

	host = sys.argv[1]
	port = int(sys.argv[2])
	username = ""
	if len(sys.argv) == 4: 
		username = sys.argv[3]
	else:
		username = "Guest"

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)

	# Connect to remote host
	try:
		s.connect((host, port))
	except:
		print("Unable to connect")
		sys.exit()

	print("Connected to remote host. You can start sending messages")
	print("***   Press Control-C to log off   ***\n")
	sys.stdout.write("[" + username + "] ")
	sys.stdout.flush()

	while True:
		socket_list = [sys.stdin, s]

		try:
			# Get the list sockets which are readable
			ready_to_read, ready_to_write, in_error = select.select(socket_list, [], [])
		except KeyboardInterrupt:
			system("clear")
			sys.stdout.write("\nYou have logged off\n")
			sys.stdout.flush()
			sys.exit()

		for sock in ready_to_read:
			if sock == s:
				# incoming message from remote server, s
				data = sock.recv(4096)
				if not data:
					print("\nDisconnected from chat server")
					sys.exit()
				else:
					# Print data
					sys.stdout.write(data)
					sys.stdout.write("[" + username + "] ")
					sys.stdout.flush()
			else:
				# User entered a message
				msg = sys.stdin.readline()
				s.send("[" + username + "] " + msg)
				sys.stdout.write("[" + username + "] ")
				sys.stdout.flush()

if __name__ == "__main__":
	sys.exit(chat_client())