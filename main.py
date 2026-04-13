import sys

def cli_interface():
    print("You have chosen the CLI interface.")
    # Implement your CLI logic here

def web_interface():
    print("You have chosen the Web interface.")
    # Implement your Web logic here

if __name__ == '__main__':
    print("Choose your interface:")
    print("1. CLI")
    print("2. Web")
    choice = input("Enter choice (1 or 2): ")
    
    if choice == '1':
        cli_interface()
    elif choice == '2':
        web_interface()
    else:
        print("Invalid choice. Please select either 1 or 2.")