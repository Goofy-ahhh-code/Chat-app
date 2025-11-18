import socket
import os
# i added these comments not chatgpt
filename = "username"
user = ""

if os.path.exists(filename):
  with open(filename, "r") as f:
    saved_user = f.read().strip()
    user = saved_user
    logged_in = True
else:
  new_username = input("Enter a username: ").strip()
  with open(filename, "w") as f:
    f.write(new_username)
  user = new_username

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8080))
message = ""
while message != "end":
  message = input("Enter your message: ")
  s.send(f"{user}: {message}".encode())

s.close()
