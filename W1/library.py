#could be made better/more complex by using objects instead of a multiple lists but i cant be bothered rn
#could also make it write/read from a file
#book's title, author, and genre
IDs = []
titles = []
authors = []
genres = []

def AddBook():
    IDs.append(len(IDs) + 1)
    titles.append(input("Enter the title of the book: "))
    authors.append(input("Enter the author of the book: "))
    genres.append(input("Enter a genre for the book: "))
    print("Book added") 
    
def ShowBooks():
    if len(IDs) > 0:
        for i in range(0,len(IDs)):
            PrintDetails(i)
    else:
        print("There are no books")

def FindBook():
    search = input("Enter the name of the book you want to find: ")
    try:
        index = titles.index(search)
    except:
        print("Book not found")
    else:
        PrintDetails(index)

def PrintDetails(i):
    print("#" + str(IDs[i]), end=": ")
    print(titles[i], authors[i], genres[i], sep=", ")
    
#code starts here
print("Welcome to the library")
inp = "0"
while not inp == '4':
    print("Enter '1' to add a book, '2' to show all books, '3' to find a specific book, or '4' to exit:")
    inp = input()
    if inp == "1":        
        AddBook()
    elif inp == "2":
        ShowBooks()
    elif inp == "3":
        FindBook()
    
    input()