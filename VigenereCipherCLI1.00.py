import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_home_screen():
    red = "\033[31m"
    reset = "\033[0m"
    ascii_art = f"""{red}
██╗   ██╗██╗ ██████╗ ███████╗███╗   ██╗███████╗██████╗ ███████╗
██║   ██║██║██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔════╝
██║   ██║██║██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝█████╗  
╚██╗ ██╔╝██║██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══╝  
 ╚████╔╝ ██║╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║███████╗
  ╚═══╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚══════╝
                                                               
 ██████╗██╗██████╗ ██╗  ██╗███████╗██████╗                     
██╔════╝██║██╔══██╗██║  ██║██╔════╝██╔══██╗                    
██║     ██║██████╔╝███████║█████╗  ██████╔╝                    
██║     ██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗                    
╚██████╗██║██║     ██║  ██║███████╗██║  ██║                    
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                    
{reset}"""
    print(ascii_art)
    print("By Joshua M Clatney - Ethical Pentesting Enthusiast. Version 1.00")
    print("-----------------------------------------------------")
    print("Options:")
    print("1. Encrypt text")
    print("2. Decrypt text\n")

def encrypt(text: str, keyphrase: str) -> str:
    result = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(keyphrase[key_index]) - ord('A')
            new_char = chr(((ord(char.upper()) - ord('A') + shift) % 26) + ord('A'))
            result.append(new_char)
            key_index = (key_index + 1) % len(keyphrase)
        else:
            result.append(char)
    return "".join(result)

def decrypt(cipher_text: str, keyphrase: str) -> str:
    result = []
    key_index = 0
    for char in cipher_text:
        if char.isalpha():
            shift = ord(keyphrase[key_index]) - ord('A')
            new_char = chr(((ord(char.upper()) - ord('A') - shift + 26) % 26) + ord('A'))
            result.append(new_char)
            key_index = (key_index + 1) % len(keyphrase)
        else:
            result.append(char)
    return "".join(result)

def process_encrypt():
    text = input("Enter text to encrypt: ").upper()
    keyphrase = input("Enter keyphrase: ").replace(" ", "").upper()

    if not any(c.isalpha() for c in text):
        print("Error: Text must contain at least one alphabetic character.")
        return

    if not keyphrase.isalpha() or keyphrase == "":
        print("Error: Keyphrase must consist of alphabetic characters only.")
        return

    result = encrypt(text, keyphrase)
    print("\nEncrypted text:", result)

def process_decrypt():
    text = input("Enter text to decrypt: ")
    keyphrase = input("Enter keyphrase: ").replace(" ", "").upper()

    if not any(c.isalpha() for c in text):
        print("Error: Text must contain at least one alphabetic character.")
        return

    if not keyphrase.isalpha() or keyphrase == "":
        print("Error: Keyphrase must consist of alphabetic characters only.")
        return

    result = decrypt(text, keyphrase)
    print("\nDecrypted text:", result)

def main():
    while True:
        clear_screen()
        print_home_screen()
        choice = input("Choose an option (1 or 2): ").strip()
        if choice == '1':
            process_encrypt()
        elif choice == '2':
            process_decrypt()
        else:
            print("Invalid option. Please choose 1 or 2.")

        input("\nPress Enter to return to the home screen...")

if __name__ == "__main__":
    main()