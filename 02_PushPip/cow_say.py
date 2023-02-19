import argparse
import cowsay


parser = argparse.ArgumentParser(
    prog='cowsay',
    description='Реализует дополненную работу исходной программы cowsay',
    epilog='Конец help, дальше сами')

parser.add_argument('message', type=str, help='text for cow')
parser.add_argument('-e', type=str, default='oo', help='symbols to use eyes')
parser.add_argument('-f', type=argparse.FileType('r'), help='cowfile')
parser.add_argument('-l', action='store_true', help='calls the cowlist')
parser.add_argument('-n', action='store_false', help='not to wrap the message')
parser.add_argument('-T', type=str, default='', help='specify a tongue')
parser.add_argument('-W', type=int, default=40, help='the width of the text bubble')
parser.add_argument('-b', action='store_true', help='borg mode')
parser.add_argument('-d', action='store_true', help='dead mode')
parser.add_argument('-g', action='store_true', help='greedy mode')
parser.add_argument('-p', action='store_true', help='paranoia mode')
parser.add_argument('-s', action='store_true', help='stoned mode')
parser.add_argument('-t', action='store_true', help='tired mode')
parser.add_argument('-w', action='store_true', help='wired mode')
parser.add_argument('-y', action='store_true', help='young mode')

args = parser.parse_args()
if args.l:
    print(cowsay.list_cows())
else:
    prst = ''
    if args.b:
        prst += 'b'
    if args.d:
        prst += 'd'
    if args.g:
        prst += 'g'
    if args.p:
        prst += 'p'
    if args.s:
        prst += 's'
    if args.t:
        prst += 't'
    if args.w:
        prst += 'w'
    if args.y:
        prst += 'y'
    if prst == '-':
        prst += 'bggpstwy'
    print(cowsay.cowsay(message=args.message, preset=prst, eyes=args.e, tongue=args.T, width=args.W, wrap_text=args.n, cowfile=args.f))
