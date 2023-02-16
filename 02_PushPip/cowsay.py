import argparse
import cowsay


parser = argparse.ArgumentParser(
    prog='cowsay',
    description='Реализует дополненную работу исходной программы cowsay',
    epilog='Конец help, дальше сами')

parser.add_argument('-e', type=str, default='oo', help='the first two characters of the string are used as eyes')
parser.add_argument('-f', type=argparse.FileType('r'), help='cowfile')
parser.add_argument('-l', action='store_true', help='calls the cowlist')
parser.add_argument('-n', action='store_true', help='not to wrap the message')
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
print(args)
print(args.e)

