import sys
import os

args=sys.argv
file=args[0]
name=args[1]
host=os.environ.get("HOST")
# print(f"Hello {name} from {file}")
print(f"{name}")
print(f"Connecting to {host}")