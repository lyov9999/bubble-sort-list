class Book:
  def __init__(self, title, author, year):
    self.title = title
    self.author = author
    self.year = year

  def __str__(self):
    return self.title + " " + self.author +  " " + str(self.year)

book1 = Book("The Da Vinci Code", "Tom Egeland", 2003)
book2 = Book("Treasure Island", "Robert Louis Stevenson", 1882)
book3 = Book("100 years of solitude", "Gabriel Garcia Marquez", 1967)

books = [book1, book2, book3]

def bubble_sort(my_list): 
  for obj in range(len(my_list)-1, -1, -1):
    swapped = False
    for i in range(obj):
        if my_list[i].year < my_list[i+1].year:
            my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
            swapped = True
    if not swapped:
        break
  return my_list

sorted_books = bubble_sort(books)

for book in sorted_books:
  print(str(book))
