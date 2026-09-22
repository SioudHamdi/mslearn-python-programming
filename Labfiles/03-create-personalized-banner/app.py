# Load the pyfiglet package
import pyfiglet

# Ask the user for their name
name = input("What is your name? ")

# Turn the name into a banner
banner = pyfiglet.figlet_format(name)

# Print a greeting
print(banner)
print(f"Hello, {name.upper()}! Welcome to VS Code.")
 # Ask the user how they're feeling today and print their answer as a banner
feeling = input("How are you feeling today? ")
feeling_banner = pyfiglet.figlet_format(feeling)
