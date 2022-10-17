# Remote Shell

Remote shell is a client server architecture provides the server to connect with client machine and execute the commands run in the client machine. This utility built on top of python's `socket` module which comes built in with python.

## Usage

This repo has two files `server.py` and `client.py`. The server machine should have `server.py` and client machine should have `client.py` files respectively. 

1. Run `server.py` file in server

```
python3 server.py
```

The server waits for any active client connection

2. Run `client.py` file in server.Once you ran the command it would prompt to provide Server IP and Port details

```
python3 client.py
Server IP: 192.168.29.138
Server PORT: 8080
```
As soon as we entered the server detail, the connection would be established between client and server.

3. The server has `>` prompt to enter the remote command. From server user can pass any command to client machine and get the output. 

```
$ python3 server.py 
Connected to remote server
> lsb_release -a
output:
No LSB modules are available.
Distributor ID:	Debian
Description:	Debian GNU/Linux 11 (bullseye)
Release:	11
```

Refer the screenshot of both server and client side by side

![remote-shell](https://i.imgur.com/2q2gkxe.png)

4. Best part is we have log creation facility with this program. `clientlogs.txt` in the client and `serverlogs.txt` in the server would be generated. Please find the below screenshot of the files. (sample files attached in repo as well)

![remote-shell-logs](https://i.imgur.com/lyenH7r.png)

**NOTE:** The program works with one server and one client only.



