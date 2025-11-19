# Reverse shell with C and python

This is a proof of reverse shell utilizing C and python with the sockets library

```bash
# compile C code
gcc main.c -o server

# run c code, replace 8080 with correct port
./server 8080

# run python client
python3 main.py
```
# To use

First, find your LAN Internet Protocol (IP) address with the linux command:
```bash
ip addr show
```
then run ./server {port} on the victim:
```bash
python3 main.py
```
