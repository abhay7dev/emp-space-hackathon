import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Process some arguments.")

# Define the expected argument (in this case, 'argument')
parser.add_argument("argument", help="The argument passed from the command line")

# Parse the arguments
args = parser.parse_args()

# Access the argument
print(f"Received argument: {args.argument}")