import datetime

class Library:

    def __init__(self, dictofbooks: dict, libraryname):
        self.dictofbooks = dictofbooks
        self.libraryname = libraryname
        try:
            f = open(f"{self.libraryname}_issued_books.txt", "x")
            f.close()
        except Exception as e:
            print()
        # print("constructor added")

    def display_books(self):
        print(f"Hello, Welcome to {self.libraryname}\nThe following books are available")

        for key,value in self.dictofbooks.items():
            print(key,":",value)

    def lend_books(self):
        print("Which book do you want to lend?")
        whichbook = input()
        if whichbook in self.dictofbooks.keys():
            if self.dictofbooks[whichbook] != 0:
                # global issuedbook
                issuedbook = whichbook
                print("The book is available for lending. Just give us a few information")
                print("Please enter your full name.")
                name = input().upper()
                print("Your institution?")
                inst = input().upper()
                # print(name, inst)
                time_issue = str(datetime.datetime.now())
                f = open(f"{self.libraryname}_issued_books.txt", "w")
                f.write(issuedbook + "\n")
                f.write(f"This book was issued by {name} from {inst} on {time_issue}")
                f.close
                print("NOTE: YOU WILL HAVE TO RETURN THE BOOK AFTER 30 DAYS FROM THE DATE OF ISSUE\n"
                      "OTHERWISE, A FINE WILL BE IMPOSED")

                # take information later and use timestamp to add it to a text file
                self.dictofbooks[whichbook] -= 1
            elif self.dictofbooks[whichbook] == 0:
                print("Sorry, the book is not available at the moment\n")
        else:
            print("The given book is not available in our library")

    def donate(self):
        print("Which book do you want to donate?\n")
        donatebook = input()
        print("How many copies do you want to donate?\n")
        no_of_copies = int(input())
        self.dictofbooks.update({donatebook:no_of_copies})
        print("Thank you so much for the donation")


bookdict = {"Maths":1,"science":2, "history":3, "politics":0, "philosopy": 3, "english": 2}
akash = Library(bookdict, "Akash Library")

while True:

    print("")
    print("Do you want to display the books and their availability, lend, donate or return books")
    print("please enter the number corresponding to the option you want")
    print("display = 1, lend = 2, donate = 3, return = 4")
    option = int(input())
    if option == 1:
        akash.display_books()
    elif option == 2:
        akash.lend_books()
    elif option == 3:
        akash.donate()
    else:
        print("something wrong happened")