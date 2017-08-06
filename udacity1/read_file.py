import urllib

def read_file():
    quotes = open("D:\python practice\movie.txt")
    contents_file = quotes.read()
    print(contents_file)
    quotes.close()
    check_profanity(contents_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output=connection.read()
    if "true" in output:
        print("profanity alert!!")
    elif "false" in output:
        print("no curse words present")
    else:
        print("cannot scan the document properly")
    #print(output)
    connection.close()

read_file()


