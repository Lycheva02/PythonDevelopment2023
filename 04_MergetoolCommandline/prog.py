import shlex
import cmd
import cowsay

class cowsay_class(cmd.Cmd):
    intro = cowsay.cowsay("Welcome to cowsay!")
    prompt = "\033[3m\033[33m{}\033[0m".format(">>> ")
    eyes_variants = ["oo", "OO", "XX", "xx", "pq", "bd", "--", "**", "==", "''"]
    tongue_variants = ["  ", "U", "u", "w", "W", "Y"]
    
    def do_cowsay(self, args):
        '''Cow says your message. There are some options:
           -e eyes
           -t tongue
           -c cow
        '''
        args = shlex.split(args)
        if not args:
            raise AttributeError("Too few parameters")
        eyes = "oo"
        tongue = "  "
        cow = "default"
        a = args[1:]
        while a:
            if len(a) < 2:
                raise AttributeError(str(a) + " needs an attribute")
            match a[:2]:
                case "-e", eyes:
                    a = a[2:]
                case "-t", tongue:
                    a = a[2:]
                case "-c", cow:
                    if cow not in cowsay.list_cows():
                        raise RuntimeError("Invalid cow")
                    a = a[2:]
                case _:
                    raise AttributeError("Invalid parameters")
        print(cowsay.cowsay(args[0], eyes=eyes, tongue=tongue, cow=cow))

    def complete_cowsay(self, text, line, begidx, endidx):
        line = shlex.split(line)
        if len(line) < 2:
            return list()
        if begidx == endidx:
            c = line[-1]
        else:
            c = line[-2]
        match c:
            case "-e":
                return [i for i in self.eyes_variants if i.startswith(text)]
            case "-t":
                return [i for i in self.tongue_variants if tongue.startswith(text)]
            case "-c":
                return [i for i in cowsay.list_cows() if i.startswith(text)]

    def do_cowthink(self, args):
        '''Cow thinks about your message. There are some options:
           -e eyes
           -t tongue
            -c cow
        '''
        args = shlex.split(args)
        if not args:
            raise AttributeError("Too few parameters")
        eyes = "oo"
        tongue = "  "
        cow = "default"
        a = args[1:]
        while a:
            if len(a) < 2:
                raise AttributeError(str(a) + " needs an attribute")
            match a[:2]:
                case "-e", eyes:
                    a = a[2:]
                case "-t", tongue:
                    a = a[2:]
                case "-c", cow:
                    if cow not in cowsay.list_cows():
                        raise RuntimeError("Invalid cow")
                    a = a[2:]
                case _:
                    raise AttributeError("Invalid parameters")
        print(cowsay.cowthink(args[0], eyes=eyes, tongue=tongue, cow=cow))


    def complete_cowthink(self, text, line, begidx, endidx):
        line = shlex.split(line)
        if len(line) < 2:
            return list()
        if begidx == endidx:
            c = line[-1]
        else:
            c = line[-2]
        match c:
            case "-e":
                return [i for i in self.eyes_variants if i.startswith(text)]
            case "-t":
                return [i for i in self.tongue_variants if tongue.startswith(text)]
            case "-c":
                return [i for i in cowsay.list_cows() if i.startswith(text)]

            
    def do_make_bubble(self, args):
        '''Your message returns in a bubble. There is an option:
        -b: brackets for bubble
        '''
        if len(args) < 1:
            raise AttributeError("Too few parameters")
        args = shlex.split(args)
        brackets = cowsay.THOUGHT_OPTIONS["cowsay"]
        a = args[1:]
        while a:
            match a:
                case "-b", br_type, *wtv:
                    if br_type not in ["cowsay", "cowthink"]:
                        raise AttributeError("Wrong brackets type")
                    brackets = cowsay.THOUGHT_OPTIONS[br_type]
                    a = a[2:]
                case _:
                    raise AttributeError("Invalid parameters")
        print(cowsay.make_bubble(args[0], brackets))


    def complete_make_bubble(self, text, line, begidx, endidx):
        line = shlex.split(line)
        if len(line) < 2:
            return list()
        if not text and line[-1][0] == "-" or line[-2][0] == "-":
            variants = ["cowsay", "cowthink"]
            return [i for i in variants if i.startswith(text)]
        else:
            return ["-b"]
            

    def do_list_cows(self, args):
        '''List of existing cows'''
        print(', '.join(cowsay.list_cows()))


cmdline = cowsay_class()
try:
    cmdline.cmdloop()
except BaseException as E:
    print(E)
