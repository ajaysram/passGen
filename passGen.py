import string
import random
import argparse

parser = argparse.ArgumentParser(description='passGen cli')
parser.add_argument("-l","--len",help="Length of password to generate",nargs='?',type=int,default=16)
args = parser.parse_args()
password = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$*_&") for _ in range(args.len))
print(password)