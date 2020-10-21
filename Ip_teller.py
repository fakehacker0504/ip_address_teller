import socket

user_input = input("Enter Your Name:")

hostname = socket.gethostname()

ip_address =socket.gethostbyname(hostname)

print ('Your ip address is',ip_address )

print('_'* 40)

print ("\nHello\t" + user_input)

print("have a great day?.\nIf you like my code then upvote👍👍 it otherwise you can comment👎🙄😬😅 \nThank you😊😇\nHappy coding😎🤘".format(ip_address ))
