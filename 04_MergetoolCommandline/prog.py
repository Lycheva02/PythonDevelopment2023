import shlex
import cmd
import cowsay

class cowsay_class(cmd.Cmd):
    intro = cowsay.cowsay("Welcome to cowsay!")
    prompt = "\033[3m\033[33m{}\033[0m".format(">>> ")
    
    def do_cowsay(self, args):
        '''Cow says your message. There are some options:
           -e eyes
           -t tongue
           -c cow
        '''
        args = shlex.split(args)
        if not args:
            raise AttributeError("Too few parameters")
        message = args[0]
        eyes = "oo"
        tongue = "  "
        cow = "default"
        a = args[1:]
        while a:
            match a:
                case ["-e", new_eyes, *wtv]:
                    eyes = new_eyes
                    a = a[2:]
                case ["-t", new_tongue, *wtv]:
                    tongue = new_tongue
                    a = a[2:]
                case ["-c", new_cow, *wtv]:
                    if new_cow not in cowsay.list_cows():
                        raise RuntimeError("Invalid cow")
                    cow = new_cow
                    a = a[2:]
                case _:
                    raise AttributeError("Invalid parameters")
        print(cowsay.cowsay(message, eyes=eyes, tongue=tongue, cow=cow))

    def complete_cowsay(self, text, line, begidx, endidx):
        f = ["-e", "-t", "-c"]
        line = shlex.split(line)
        if len(line) < 2:
            return []
        if not text and line[-1][0] == "-":
            c = line[-1]
        elif line[-2][0] == "-":
            c = line[-2]
        else:
            return [i for i in f if i[0] == text]
        match c:
            case "-e":
                eyes_variants = ["oo", "OO", "XX", "xx", "pq", "bd", "--", "**", "==", "''"]
                return [i for i in eyes_variants if i[0] == text]
            case "-t":
                tongue_variants = ["  ", "U", "u", "w", "W", "Y"]
                return [i for i in tongue_variants if tongue[0] == text]
            case "-c":
                cow_variants = cowsay.list_cows()
                return [i for i in cow_variants if i[0] == text]

cmdline = cowsay_class()
try:
    cmdline.cmdloop()
except BaseException as E:
    print(E)
