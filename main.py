import os

if __name__ == '__main__':
    print("welcome to RoboSpeaker - Created by Jenish: ")
    while True:
        x = input("Enter whatever you want me to speak : ")
        if x == "q":
            os.system("say 'bye bye friend'")
            break
        command = f"say {x}"
        os.system(command)