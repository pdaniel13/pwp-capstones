#Create TomeRater application that stores Users, Books, and rating information and enables analysis on both Users and Books
class TomeRater:
    #Initialize an empty dictionary, self.users, that will map a user's email to the corresponding User object
    #Initialize an empty dictionary, self.books, that will map a Book object to the number of Users that have read it
    def __init__(self):
        self.users = {}
        self.books = {}

    #creates a new Book object with the given title and isbn 
    def create_book(self, title, isbn):
        return Book(title, isbn)

    #creates a new Fiction object with the given title, author, and isbn
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    #creates a new Non_Fiction object with the given title, subject, level, and isbn
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    #Adds a given book and rating (if applicable) to the given user
    #Adds a User's rating to the book's list of ratings
    #Adds the Book to self.books dictionary (if Book is new) or updates the Book's value in self.books by 1
    def add_book_to_user(self, book, email, rating = None):
        if email in self.users:
            self.users[email].read_book(book, rating)
            if rating != None:
                book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with email {email}!".format(email = email))

    #Adds a User given name and email
    #If Book list is provided, iterate through the list and add each Book to the User
    def add_user(self, name, email, user_books = None):
        new_user = User(name, email)
        if email not in self.users:
            self.users[email] = new_user
            print("{user} has been added".format(user = new_user.name))
            if user_books != None:
                for book in user_books:
                    self.add_book_to_user(book, email)
        else:
            print("User with email {email} already exists".format(email = new_user.email))

    #Prints all Books that have been read by Users
    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    #Prints all Users that have been added to TomeRater
    def print_users(self):
        for user in self.users.values():
            print(user)

    #returns the Book that has been read the most number of times
    def most_read_book(self):
        highest_count = 0
        for book, book_count in self.books.items():
            if book_count > highest_count:
                highest_count = book_count
                most_read_book = book
        return most_read_book

    #returns the Book with the highest average rating
    def highest_rated_book(self):
        top_book_rating = 0
        for book in self.books.keys():
            if book.get_average_rating() > top_book_rating:
                top_book_rating = book.get_average_rating()
                top_book = book
        return top_book

    #returns the User with the highest average rating of Books read
    def most_positive_user(self):
        top_user_rating = 0
        for user in self.users.values():
            if user.get_average_rating() > top_user_rating:
                top_user_rating = user.get_average_rating()
                top_user = user
        return top_user.name

#Create a Book object
class Book:
    #initialize a Book object with a book title (string) and isbn (number)
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    #returns the title of the Book
    def get_title(self):
        return self.title

    #returns the isbn of the book
    def get_isbn(self):
        return self.isbn

    #takes in a new isbn and sets the Book's isbn to the new number
    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        print("{book}\'s ISBN number has been updated to {new_number}".format(book = self.title, new_number = self.isbn))

    #takes in a rating and adds it to a list of the Book's ratings
    #Valid rating is a number between 0 and 4, inclusive
    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid rating")

    #compare two Books where the Books are equal if they have the same title and isbn number
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    #add __hash__ method to make Book hashable
    def __hash__(self):
        return hash((self.title, self.isbn))

    #returns a string displaying the Book's title and ISBN
    def __repr__(self):
        return "Title: {title}, ISBN: {isbn}".format(title = self.title, isbn = self.isbn)

    #calculates the average of all of the Book's ratings and returns this average
    #books without a rating are excluded from the average rating calculation
    def get_average_rating(self):
        total = 0
        no_rating_count = 0
        for rating in self.ratings:
            if rating != None:
                total += rating
            else:
                no_rating_count += 1
        avg_rating = total / (len(self.ratings) - no_rating_count)
        return avg_rating

#create Fiction sublass of Book that inherits from Book parent and has an author
class Fiction(Book):
    #initialize Fiction object with title (string), author (string), and isbn (number)
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    #returns the Book's author
    def get_author(self):
        return self.author

    #returns a string displaying the Book's title and author
    def __repr__(self):
        return "{title} by {author}".format(title = self.title, author = self.author)

#create Non_Fiction subclass of Book that inherits from Book parent and has a subject and level
class Non_Fiction(Book):
    #initialize NonFiction object with title (string), subject (string), level (string), and isbn (number)
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
    
    #returns the book's subject
    def get_subject(self):
        return self.subject

    #returns the book's level
    def get_level(self):
        return self.level

    #returns a string displaying the Book's title, subject, and level
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

#Create a User object to keep track of our users
class User(object):
    #initialize User object with name (string), email(string), and empty dictionary that will map a Book object to the User's rating of the book
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    #returns the User's email
    def get_email(self):
        return self.email

    #takes in a new email and changes the User's email address
    def change_email(self, new_address):
        self.email = new_address
        print("{name}\'s email has been updated to {new_email}".format(name = self.name, new_email = self.email))

    #returns a string describes the User object by printing the User's name, email, and list of books read
    def __repr__(self):
        return "User name: {name}, Email: {email}, Books read: {books}".format(name = self.name, email = self.email, books = self.books)

    #compare users such that a User equals another User if they have the same name and email
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False

    #takes in a Book and rating (optional) and adds Book:rating as a key:value pair to self.books dictionary
    def read_book(self, book, rating = None):
        self.books[book] = rating

    #calculates the average rating of all books read and rated by the User
    #books with no rating are excluded from the average rating calculation
    def get_average_rating(self):
        total = 0
        no_rating_count = 0
        for rating in self.books.values():
            if rating != None:
                total += rating
            else:
                no_rating_count += 1
        avg_rating = total / (len(self.books.keys()) - no_rating_count)
        return avg_rating