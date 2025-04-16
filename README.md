# Python-week-5

Assignment 1

class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")

class FictionBook(Book):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre

    def display_details(self):
        super().display_details()
        print(f"Genre: {self.genre}")

class NonFictionBook(Book):
    def __init__(self, title, author, publication_year, topic):
        super().__init__(title, author, publication_year)
        self.topic = topic

    def display_details(self):
        super().display_details()
        print(f"Topic: {self.topic}")

book1 = FictionBook("How I Met Her", "Katlego Lesetedi", 2025, "Romance")

print("Book 1 Details:")
book1.display_details()


Activity 2

class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🛥️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()

vehicles = [car, plane, boat, bicycle]
for vehicle in vehicles:
    vehicle.move()

