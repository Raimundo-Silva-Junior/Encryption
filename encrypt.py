import random
import pickle
import os

class Encrypt:
    
    def __init__(self):
        
        letter_lower = "abcdefghijklmnopqrstuvwxyz"
        letter_upper = letter_lower.upper()
        other_letters_lower = "çáãéêâîíõôóúàèìòùú'"
        other_letters_upper = other_letters_lower.upper()
        numbers = "0123456789"
        symbols = r'\/?°´ª[{]}-+=§!@#$%¨&*()$£¢¬º^~:;.<>,| "'

        self.characteres = letter_lower + letter_upper + numbers + symbols + other_letters_lower + other_letters_upper
        
    def create_encryption(self, language_name: str):
        
        encripytion_language = {key:" " for key in self.characteres }
        
        for value in encripytion_language: 
            
            while True:
                letter = "".join(random.choices(self.characteres, k=2))
                if letter not in encripytion_language.values():
                    encripytion_language[value] = letter
                    break
        encripytion_language.update({"\n": "\n"+ random.choice(self.characteres)})       
        with open(f"Languages/{language_name}.pkl", "wb") as file:
            pickle.dump(encripytion_language, file)
            
    def encrypt_message(self,language_name: str, message: str):
        #message = message.replace("\n", "|")
                
        with open(f"Languages/{language_name}.pkl", "rb") as file:
            lang = pickle.load(file)
        
        encrypted_message_list = [lang[letter] for letter in message]
        
        return "".join(encrypted_message_list)

    def decrypt_message(self, language_name: str, message:str):
        with open(f"Languages/{language_name}.pkl", "rb") as file:
            lang: dict = pickle.load(file)
        
        original, encrypted = [value for value in lang.keys()], [value for value in lang.values()]
        encrypted_message_list = [message[i:i + 2] for i in range(0, len(message)) if i%2 == 0]

        decrypted_message_list = []
        for value in encrypted_message_list:
            index = encrypted.index(value)
            decrypted_message_list.append(original[index])
    
        return "".join(decrypted_message_list)
    
    def get_Language_dictionary(self, language_name: str):
        
        try:
            with open(f"Languages/{language_name}.pkl", "rb") as file:
                lang: dict = pickle.load(file)
        except FileNotFoundError:
            lang = "No language in your local language folder..."
            
        return lang
        
if __name__ == "__main__":
    
    encrypt = Encrypt()
    
    title = "ENCRYPTION LANGUAGE SOFTWARE"
    ornament = "_"*len(title)
    
    if os.path.exists("EncryptedMessages") is False:
        os.mkdir("EncryptedMessages")
    if os.path.exists("Messages") is False:
        os.mkdir("Messages")
    if os.path.exists("Languages") is False:
        os.mkdir("Languages")
    
    print(ornament, title, ornament,"\n")
    
    def encrypt_type(reverse=False):
        print("\nLanguage list: ", end="")
        if os.listdir("Languages"):
            lang_list = []
            
            size = len(os.listdir("Languages"))
            for index, languages in enumerate(os.listdir("Languages"), start=1):
                languages = languages.replace(".pkl", "")
                lang_list.append(languages)
                if index == size:
                    print(languages, "\n")
                    continue
                print(languages, end=", ")
            
            
            while True:
                lang_name = input("Chosse one of the following languages name: ")
                if lang_name in lang_list:
                    break
            print()
            if reverse is False:
                messages = os.listdir("Messages")
                for message in messages:
                    with open(f'Messages\{message}', "rt", encoding="utf-8") as text:
                        msg = text.read()
                    msg = encrypt.encrypt_message(lang_name, msg)

                    new_message_name = f'{message.replace(".txt", "_encrypted.txt")}'
                    with open(f"EncryptedMessages\{new_message_name}", "wt", encoding="utf-8") as file:
                        file.write(msg)
                    print(f'Message {message} finshed!')
                print("\nMessages were encrypted!\n") 
            else:
                messages = os.listdir("EncryptedMessages")
                for message in messages:
                    with open(f'EncryptedMessages\{message}', "rt", encoding="utf-8") as text:
                        msg = text.read()
                    msg = encrypt.decrypt_message(lang_name, msg)
                    new_message_name = f'{message.replace("_encrypted.txt", ".txt")}'
                    with open(f"Messages\{new_message_name}", "wt", encoding="utf-8") as file:
                        file.write(msg)                  
                    print(f'Message {message} finshed!')
                print("\nMessages were decrypted!\n") 

    while True:
        print("\n****menu****\n")
        print("[1] Create a language")
        print("[2] Encrypt language")
        print("[3] Decrypt language")
        print("[4] Sair")

        while True:
            option = input("\nEscolha uma das opções: ")
            if option in("1", "2", "3", "4"):
                break
            
        option = int(option)
         
        if option == 1:
            lang_name = input("\nChoose a name for you language: ")
            encrypt.create_encryption(lang_name)
            print("\nEncryption Language was created!\n")
            input("Press ENTER to continue\n")
            os.system("cls")
        elif option == 2:
            encrypt_type()
            input("Press ENTER to continue\n")
            os.system("cls")   
        elif option == 3:
            encrypt_type(reverse=True)
            input("Press ENTER to continue\n")
        elif option == 4:
            break
    
    
    
        
        