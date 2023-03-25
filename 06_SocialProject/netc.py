import cmd
import threading
import time
import readline
import socket
import sys

globalsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
globalsock.connect((sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 1337))
buffer = ''

class simple(cmd.Cmd):

    prompt = '>>> '

    def do_who(self, args):
        globalsock.sendall(('who ' + args.strip() + '\n').encode())
		
    def do_cows(self, args):
        globalsock.sendall(('cows ' + args.strip() + '\n').encode())
		
    def do_login(self, args):
        globalsock.sendall(('login ' + args.strip() + '\n').encode())
		
    def complete_login(self, prefix, line, begidx, endidx):
        globalsock.sendall("LOGIN_COMPLETE\n".encode())
        while not buffer:
            time.sleep(0.1)
        variants = buffer
        buffer = ''
        return [i for i in variants if i.startswith(prefix)]
		
    def do_say(self, args):
        globalsock.sendall(('say ' + args.strip() + '\n').encode())
		
    def complete_say(self, prefix, line, begidx, endidx):
        globalsock.sendall("SAY_COMPLETE\n".encode())
        while not buffer:
            time.sleep(0.1)
        variants = buffer
        buffer = ''
        return [i for i in variants if i.startswith(prefix)]
		
    def do_yield(self, args):
        globalsock.sendall(('yield ' + args.strip() + '\n').encode())
		
    def do_quit(self, args):
        globalsock.sendall(('quit ' + args.strip() + '\n').encode())
        return 1


def spam(cmdline):
    while True:
        data = globalsock.recv(1024).decode().strip()
        if len(data) == 0:
            break
        if data.startswith('['):
            buffer = data[1:-1].split(',')
        else:
            print(f"\n{data}\n>>> {readline.get_line_buffer()}", end='', flush=True)


cmdline = simple()
timer = threading.Thread(target=spam, args=(cmdline,))
timer.start()
cmdline.cmdloop()
