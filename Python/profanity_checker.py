from urllib import urlopen

def read_text():
    thefile = open(address)
    content = thefile.read()
    print(content)
    thefile.close()
    check_profanity(content)


def check_profanity(text_to_check):
    connection = urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    connection.close()
    if "true" in output:
        print("Bad Words Detected~")
    elif "false" in output:
        print("This document has no cursed words~.")
    else:
        print("Could not read the document properly~.")


print("Profanity Checker is now running.")
def get_address():
    address = raw_input("Enter the address of the document you wish to check: ")
    return address

address = get_address()
read_text()
