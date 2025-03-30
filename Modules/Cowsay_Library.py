import cowsay
import sys

if len(sys.argv) < 2:
    sys.exit(print("Few Arguments passed"))
elif len(sys.argv) > 2:
    sys.exit(print("Too many arguments passed"))
else:
    # cowsay.cow(f"Hello: {sys.argv[1]}")  Cow saying Hello 
    cowsay.trex(f"Hello: {sys.argv[1]}")   # Dino saying Hello