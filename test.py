from src import thn

# credit: https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
def get_colors():
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

    return color

def test_thn_get():
    color = get_colors()

    data = thn.get()
    
    for news in data:
        title = str(news["title"])
        url = str(news["url"])
        date = str(news["date"])
        detail = str(news["details"])

        print(color.RED + color.BOLD + color.UNDERLINE + "TITLE:" + color.END, title)
        print(color.GREEN + color.BOLD + color.UNDERLINE + "DATE:" + color.END, date)
        print(color.BLUE + color.BOLD + color.UNDERLINE + "URL:" + color.END, url)
        print(color.YELLOW + color.BOLD + color.UNDERLINE + "DETAIL:" + color.END, "\n"+detail)
        print("\n")
    
    print(color.PINK + color.BOLD + color.UNDERLINE + "Check Out Official Website:" + color.END, "https://thehackernews.com/")
    print()
    
if __name__ == '__main__':
    test_thn_get()
