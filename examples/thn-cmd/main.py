import pathlib
import sys

# get path to main script
PATH = str(pathlib.Path(__file__).parent.resolve())

# get path for THN submodule and import thn module
THN_PATH = PATH.split("/")
THN_PATH = THN_PATH[:-2]
THN_PATH.append("src")
THN_PATH = "/".join(THN_PATH)
sys.path.insert(0, THN_PATH)
import thn

# credit: https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
class color:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\x1B[3m'
    END = '\033[0m'

def options():
    print("THN COMMAND OPTIONS:")
    print("   -a : list max number of The-Hacker-News articles")
    print("   -h : list options for thn command")

def main_prints(large_listing):
    global color

    try:
        data = thn.get(large_listing)
        data.reverse()
    except Exception as e:
        print("The following error occurred well try to use the THN library: " + str(e))
        sys.exit()

    for news in data:
        title = str(news["title"])
        url = str(news["url"])
        date = str(news["date"])

        ctitle = color.RED + color.BOLD + color.UNDERLINE + title + color.END
        cdate = color.GREEN + date + color.END
        curl = color.BLUE + color.ITALIC + url + color.END

        print(ctitle)
        print(cdate)
        print(curl)
        print()

if __name__ == '__main__':
    # grab user's script arguments
    args = list(sys.argv)

    # default (no arguments) to simple thn output
    if len(args) == 1:
        main_prints(True)

    # other thn outputs (argument provided)
    elif len(args) > 1:
        param = str(args[1])

        if param == "-a":
            main_prints(False)
        elif param == "-h":
            options()
        else:
            print("Error! Invalid params, try these options:")
            options()
