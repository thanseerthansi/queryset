from http.client import HTTPResponse
from multiprocessing.sharedctypes import Value

# 
from django.http import HttpResponse
from django.shortcuts import render 
from django.db import transaction
from django.db.models import Sum,Count,F,Q,When,Case,CharField
from selectedrelated.models import Author, Books, Students, banking, store

# Create your views here.
# class AuthorAPI(List)
#selected related.................................................................
def booksget(request):
    book = Books.objects.all().select_related('author')
    print("query",book.query) 
    ordiset = Books.objects.all()
    print("\nallquery",ordiset.query)
    for book in book:
        book1 = book.author.name
        print("boo",book.author.name)
    
    return HttpResponse ("ok")
# prefetch related ..........................................................
def storeget(request):
    stores = Books.objects.all().prefetch_related('store_set')
    print("query",stores.query)
    print("query",stores.query)
    for storess in stores:
        # book1 = stores.books.book
        print("boo",storess.store_set.all())
    return HttpResponse ("okstore")


 #transactions Automic......................
# @transaction.atomic
def Transaction(request):
    user1 = 2
    user2 = 1
    amount = 1
    try: 
        with transaction.atomic():
            payfro =banking.objects.get(id=user1)
            payfro.balance -= amount
            payfro.save()

            payto =banking.objects.get(id=user2)
            payto.balance += amount 
            payto.save()
            print("ok")
    except:print("\n\ncanncel")
    # print("payfro",payfro.balance)
    # print("payfro",payto.balance)
    return HttpResponse ("ok")

##select for update............................................
def selectforupdate(request):
    user1 = 1
    user2 = 2 
    amount = 50
    with transaction.atomic():
        payfro = banking.objects.select_for_update().get(id=user1)
        payfro.balance -= amount
        payfro.save()

        payto = banking.objects.select_for_update().get(id=user2)
        payto.balance += amount 
        payto.save()

    print("payfro",payfro.balance)
    print("payfro",payto.balance)
    return HttpResponse ("ok")

#aggregate ...................................
def aggregate(request):
    total_bank_balance = banking.objects.aggregate(Sum('balance'))
    print("balance",total_bank_balance)
    return HttpResponse("ok")

#annotate .......................................
def annotate(request):
    total_bank_balance = banking.objects.annotate(new=Sum(Case(When(balance__lt = 500,then=1),When(balance__gt = 500,then=2 )))).values()
    print("balance",total_bank_balance)
    print("balancenew",total_bank_balance.values('new'))
    return HttpResponse("ok")

#values()..................................
def values(request):
    total_bank_balance = banking.objects.annotate(new=Sum('balance')).values()
    print("balance",total_bank_balance.query)
    print("balance",total_bank_balance)
    return HttpResponse("ok")

#f() ..................................
def f(request):
    total_bank_balance = banking.objects.filter(id=1).update(balance=F('balance')+ 1)
    print("balance",total_bank_balance)
    return HttpResponse("f()")



#q()...........................
def q(request):
    total_bank_balance = banking.objects.filter( Q(id=1)| Q(user='a')).update(balance=F('balance')+ 1)
    print("balance",total_bank_balance)
    return HttpResponse("f()") 



#manager..........................
def manager(request):
    stu = Students.students.smaller_than(20).values()
    alldata = Students.objects.all().values()
    print("student",stu)
    print("alldata",alldata)
    return HttpResponse(f"manager{stu}")



# reverse relationship

def revererelation(request):
    auth = Author.objects.filter(id=1)
    for auth  in auth:
        book = auth.auth_name.all().values('book','author')
        print("authloop",auth)
        print("bookloop",book)
    return HttpResponse("revserse relationship")
#bulk create .................................................
def bulkcreate(request):
    auth1 = Author.objects.get(id=1)
    auth2 = Author.objects.get(id=2)
    book =  Books.objects.all().bulk_create([Books(book='bookd',author=auth1),Books(book='booke',author=auth2)])
    print("book",book)
    return HttpResponse("bulkcreate")
#bulk update .................................................
def bulkupdate(request):
    update_queries = []
    a = Books.objects.get(id=3)
    b = Books.objects.get(id=4)
    c = Books.objects.get(id=5)

    #set update value
    a.book="Hello python "
    b.book="Hello django "
    c.book="Hello bulk "
    update_queries.extend((a, b, c))

    book =  Books.objects.all().bulk_update(update_queries,['book'])
    print("book",book)
    return HttpResponse("bulkupdate")


#defer.......(it gives the data other than the defer fields)..................................................

def defer(request):
    stores = banking.objects.defer('balance').values()
    print("store",stores.values())
    print("query",stores.query)
    return HttpResponse(f"defer{stores}")