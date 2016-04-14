""" IRC Connection and interface. Connects to freenode network and will
remain connected. Nick: Malle_Bot User: Malle_Bot RealName: Malle_Bot
NetworkInput: chat.freenode.net:6667
Made by Mykhaylo Kuzma on April 14, 2016"""

import socket

class ircConnect:
	def __init__(self, hostName, port, nick, user, realName):
		self.hostName = hostName
		self.port = port
		self.nick = nick
		self.user = user
		self.realName = realName
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def __repr__(self):
		return "Establishes an irc connection given details such as:\n \
		hostName, port, nick, user, and real name."

	def connectIrc(self):
		print("Command connect")
		address = (self.hostName, int(self.port))
		self.socket.connect(address)
		print("Connected")
		self.sendMsg("NICK " + self.nick + "\n")
		print("Nick sent")
		self.sendMsg("USER " + self.user + " 0 * :" \
			+ self.realName + "\n")
		print("User sent")
		#self.socket.shutdown("SHUT_RDWR")
	def sendMsg(self, message):
		self.socket.send((message + "\\r\\n").encode())

	def listenTo(self):
		time = 0
		print("Listening")
		while time < 10000:
			msg = str(self.socket.recv(9000))
			print(str(msg))
			msgComp = msg.split(":")
			server = msgComp[1].split(" ")[0]
			if "PING" in msg:
				self.sendMsg(("Test"))
			time += 1


def main():
	host = "chat.freenode.net:6667"
	#input("What is the address + port? ")
	address = host.split(":")[0]
	port = host.split(":")[1]
	nick = "Tester"
	#input("Enter nick: ")
	user = "Tester"
	#input("Enter user: ")
	real = "Tester"
	#input("Enter real: ")

	connection = ircConnect(address, port, nick, user, real)
	connection.connectIrc()
	connection.listenTo()
main()