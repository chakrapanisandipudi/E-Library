import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from accounts import forms, models
from accounts.forms import Book_updateForm

from accounts.models import Book, IssuedBook, Student

# Create your views here.
def about_us(request):

    return render(request, "about.html")

def contact_us(request):

    return render(request, "contact.html")

def show_login(request):

    return render(request, "show_login.html")

def register(request):

    return render(request, "register.html")

#### Admin Templates ####-->

def admin_dashboard(request):
    return render(request, "admin_templates/admin_index.html")

@login_required(login_url = 'show_login')
def add_book(request):
    if request.method == "POST":
        title = request.POST['title']
        author = request.POST['author']
        isbn = request.POST['isbn']
        category = request.POST['category']
        copies = request.POST['copies']
        publication = request.POST['publication']
        pub_name = request.POST['pub_name']
        copyright = request.POST['copyright']
        Date_added = request.POST['Date_added']
        status = request.POST['status']

        books = Book.objects.create(title=title, author=author, isbn=isbn, category=category,
                                    copies=copies, publication=publication, pub_name=pub_name, copyright=copyright,
                                    Date_added=Date_added, status=status)
        books.save()
    return render(request, "admin_templates/add_book.html")

def book_list(request):
    books = Book.objects.all()
    return render(request, "admin_templates/book_list.html",{'books':books})


@login_required(login_url = 'show_login')
def issue_book(request):
    form = forms.IssueBookForm()
    if request.method == "POST":
        form = forms.IssueBookForm(request.POST)
        if form.is_valid():
            obj = models.IssuedBook()
            obj.student_id = request.POST['name2']
            obj.isbn = request.POST['isbn2']
            obj.save()
            alert = True
            return render(request, "admin_templates/issue_book.html", {'obj':obj, 'alert':alert})
    return render(request, "admin_templates/issue_book.html", {'form':form})

def student_list(request):
    students = Student.objects.all()
    return render(request, "admin_templates/students_list.html",{'students': students})

#### Student Templates ####-->

def student_dashboard(request):
    return render(request, "student_templates/student_index.html")

def student_register(request):
    return render(request, "student_templates/student_register.html")


def student_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        Department = request.POST['Department']
        adm_number = request.POST['adm_number']
        password = request.POST['password']

        # if password != confirm_password:
        #     passnotmatch = True
        #     return render(request, "student_registration.html", {'passnotmatch':passnotmatch})

        user = User.objects.create_user(username=username, email=email, password=password)
        student = Student.objects.create(user=user, phone=phone, Department=Department, adm_number=adm_number)
        user.save()
        student.save()
        alert = True
        return render(request, "student_templates/student_register.html", {'alert':alert})
    return render(request, "student_templates/student_register.html")

def student_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return HttpResponse("You are not a student!!")
            else:
                return redirect("student_issued_books")
        else:
            alert = True
            return render(request, "student_login.html", {'alert':alert})
    return render(request, "student_login.html")


def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                return redirect("student_list")
            else:
                return HttpResponse("You are not an admin.")
        else:
            alert = True
            return render(request, "admin_templates/admin_login.html", {'alert':alert})
    return render(request, "admin_templates/admin_login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

from datetime import date

@login_required(login_url = 'student_login')
def student_issued_books(request):
    student = Student.objects.filter(user_id=request.user.id)
    issuedBooks = IssuedBook.objects.filter(student_id=student[0].user_id)
    li1 = []
    li2 = []

    for i in issuedBooks:
        books = Book.objects.filter(isbn=i.isbn)
        for book in books:
            t=(request.user.id, request.user.username, book.title,book.author)
            li1.append(t)

        days=(date.today()-i.issued_date)
        d=days.days
        fine=0
        if d>15:
            day=d-14
            fine=day*5
        t=(issuedBooks[0].issued_date, issuedBooks[0].expiry_date, fine)
        li2.append(t)
    return render(request,'student_templates/student_issued_books.html',{'li1':li1, 'li2':li2})

@login_required(login_url = '/admin_login')
def view_issued_book(request):
    issuedBooks = IssuedBook.objects.all()
    details = []
    for i in issuedBooks:
        days = (date.today()-i.issued_date)
        d=days.days
        fine=0
        if d>14:
            day=d-14
            fine=day*5
        books = list(models.Book.objects.filter(isbn=i.isbn))
        students = list(models.Student.objects.filter(user=i.student_id))
        i=0
        for l in books:
            t=(students[i].user,students[i].user_id,books[i].title,books[i].isbn,issuedBooks[0].issued_date,issuedBooks[0].expiry_date,fine)
            i=i+1
            details.append(t)
    return render(request, "admin_templates/view_issued_book.html", {'issuedBooks':issuedBooks, 'details':details})


@login_required(login_url = 'student_login')
def student_profile(request):
    return render(request, "student_templates/student_profile.html")

@login_required(login_url = '/student_login')
def edit_profile(request):
    student = Student.objects.get(user=request.user)
    if request.method == "POST":
        email = request.POST['email']
        phone = request.POST['phone']
        Department = request.POST['Department']
        adm_number = request.POST['adm_number']

        student.user.email = email
        student.phone = phone
        student.Department = Department
        student.adm_number = adm_number
        student.user.save()
        student.save()
        alert = True
        return render(request, "edit_profile.html", {'alert':alert})
    return render(request, "edit_profile.html")


@login_required(login_url = 'student_login')
def student_borrow_books(request):
    return render(request, "student_templates/student_borrowed_books.html")

@login_required(login_url = 'student_login')
def student_requested_books(request):
    return render(request, "student_templates/student_recieved_books.html")

@login_required(login_url = 'student_login')
def student_received_books(request):
    return render(request, "student_templates/student_recieved_books.html")

@login_required(login_url = 'student_login')
def student_rejected_books(request):
    return render(request, "student_templates/student_rejected_books.html")

## Other templates ##
def error404(request):
    return render(request,'404.html')

def maintenance(request):
    return render(request,'maintenance.html')


def coming_soon(request):
    return render(request,'coming-soon.html')


def delete_book(request, myid):
    books = Book.objects.filter(id=myid)
    books.delete()
    return redirect("book_list")


def view_book(request, myid):
    books = Book.objects.get(id=myid)
    return render(request,'admin_templates/view_book.html',{'books':books})


# def edit_book(request, id):
#     books = Book.objects.get(id=id)
#     return render(request,'admin_templates/edit_book.html',{'books':books})

def book_update(request,pk):
    book= get_object_or_404(Book, pk=pk)
    form = Book_updateForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    context = {
        'form': form
    }
    return render(request,'admin_templates/edit_book.html', context )

def admin_accepted_books(request):
    return render(request,'admin_templates/admin_accepted_books.html')

def admin_requested_books(request):
    return render(request,'admin_templates/admin_requested_books.html')

def admin_recieved_books(request):
    return render(request,'admin_templates/admin_returned_books.html')