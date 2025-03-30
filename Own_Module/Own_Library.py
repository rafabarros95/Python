import sys
from Own_Module.Sayings import hello

if (len(sys.argv) < 2):
    sys.exit("Few arguments")

if(len(sys.argv) == 2):
    hello(sys.argv[1])