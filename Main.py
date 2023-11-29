
import CleanDir
import Cleaner

def help(st: str = None) -> None:
    print(commandList.keys())

commandList = {
    "clean_file": Cleaner.check_dir,
    "clean_dir" : CleanDir.check_empty_dir,
    "help"      : help
}

if __name__ == "__main__":
    while True:
        command = input("请输入指令：")

        commandTree = [command]
        if " " not in command:
            commandTree = command.split(" ")

        if commandTree[0] == "exit":
            exit(0)

        if commandTree[0] in commandList:
            commandList[commandTree[0]](commandTree[-1])
