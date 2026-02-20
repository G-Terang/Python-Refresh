import argparse

parser = argparse.ArgumentParser(description='This is a very simple Calculator')

parser.add_argument("num1", type=float, help="Fist number")
parser.add_argument("num2", type=float, help="Second number")
parser.add_argument("Operation", choices=['add','sub','mul','div'],help="Operations to perform")

args = parser.parse_args()
print(args)

if(args.operations=='add'):
    print(f"{args.num1 + args.num2}")
elif(args.operations=='sub'):
    print(f"{args.num1 - args.num2}")
elif(args.operations=='mul'):
    print(f"{args.num1 * args.num2}")
elif(args.operations=='div'):
    print(f"{args.num1 / args.num2}")
else:
    print("You didn't choose the operation correctly!")