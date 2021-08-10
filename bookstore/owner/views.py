from django.shortcuts import render

# Create your views here.
# 8000/owner/books/add
# 8000/owner/books/list
# 8000/owner/books/change/id
# 8000/owner/books/remove/id
def book_create(request):
    if request.method=="GET":
        return render(request,"book_add.html")
    elif request.method=="POST":
        # print("inside post book")
        # print(request)
        # print(request.headers)
        print(request.POST)
        # request.POST={'bookname':'two states'}
        bookname=request.POST["bookname"]
        author=request.POST["author"]
        price=request.POST["price"]
        copies=request.POST["copies"]
        print(bookname,author,price,copies)
        return render(request, "book_add.html")
        # pass


def book_list(request):
    return render(request,"list_book.html")

def book_update(request,id):
    return render(request,"change_book.html")
def book_remove(request,id):
    return render(request,"book_remove.html")
