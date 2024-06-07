from django.shortcuts import render, redirect
from books import models


def index(request):
    return redirect('/login')


def login(request):
    if request.method == 'GET':
        return render(request, 'admin/admin.html')
    if request.method == 'POST':
        user_number = request.POST.get('user_number')
        user_password = request.POST.get('user_password')

        manage = models.Manage.objects.filter(user_number=user_number, user_password=user_password)
        if manage.exists():
            name = manage.first().user_name
            request.session['user_name'] = name
            books_obj_list = models.Book.objects.all()
            return render(request, 'books/book_list.html', {'books_obj_list': books_obj_list, 'user_name': name})

        return redirect('/login')


def add_publisher(request):
    if "user_name" not in request.session:
        return redirect("/login")
    # 直接访问(get请求)，跳转界面
    if request.method == "GET":
        return render(request, 'publisher/add_publisher.html', {"name": request.session["user_name"]})
    # 提交表单请求(POST)，处理数据库,跳转到列表页面
    if request.method == "POST":
        publisher_name = request.POST.get("publisher_name")
        publisher_address = request.POST.get("publisher_address")
        # 将数据保存到数据库中(insert)
        models.Publisher.objects.create(
            publisher_name=publisher_name,
            publisher_address=publisher_address,
        )
        # 重添加成功，返回出版社列表
        return redirect("/publisher_list")



def publisher_list(request):
    if "user_name" not in request.session:
        return redirect("/login")

    publisher_obj_list = models.Publisher.objects.all()

    return render(request, 'publisher/publisher_list.html', {'publisher_obj_list': publisher_obj_list, 'name': request.session["user_name"]})


def edit_publisher(request):
    if "user_name" not in request.session:
        return redirect('/login')
    if request.method == "POST":
        id = request.POST.get('id')
        publisher_name = request.PosT.get("publisher_name")
        publisher_address = request.PosT.get("publisher_address")
        publisher_obj = models.Publisher.objects.get(id=id)
        publisher_obj.publisher_name = publisher_name
        publisher_obj.publisher_address = publisher_address
        publisher_obj.save()
        return redirect("/publisher_list")
    else:
        id = request.GET.get('id')
        publisher_obj = models.Publisher.objects.get(id=id)
        publisher_obj_list = models.Publisher.objects.all()
        return render(request, 'publisher/edit_publisher.html',
                      {'publisher_obj': publisher_obj, 'publisher_obj_list': publisher_obj_list, 'name': request.session["user_name"]})


def delete_publisher(request):
    if "user_name" not in request.session:
        return redirect("/login")
    id = request.GET.get('id')
    models.Publisher.objects.get(id=id).delete()
    return redirect("/publisher_list")


def add_book(request):

    if "user_name" not in request.session:
        return redirect('/login')
    if request.method == "GET":
        return render(request, 'books/add_book.html', {"name": request.session["user_name"]})
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        sale_num = request.POST.get('sale_num')
        publisher_id = request.POST.get('publisher_id')
        models.Book.objects.create(name=name, price=price, inventory=inventory, sale_num=sale_num, publisher_id=publisher_id)

        return redirect('/book_list')


def book_list(request):
    if "user_name" not in request.session:
        return redirect("/login")
    book_obj_list = models.Book.objects.all()
    return render(request, 'books/book_list.html', {'book_obj_list': book_obj_list, 'name': request.session["user_name"]})


def edit_book(request):
    if "user_name" not in request.session:
        return redirect("/login")
    if request.method == 'GET':
        id = request.GET.get('id')
        book_obj = models.Book.objects.get(id=id)
        publisher_obj_list = models.Publisher.objects.all()
        book_obj_list = models.Book.objects.all()
        return render(request, 'books/book_list.html',
                      {'book_obj': book_obj, 'book_obj_list': book_obj_list, 'publisher_obj_list': publisher_obj_list,
                                'name': request.session["user_name"]})
    else:
        id = request.GET.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')
        inventory = request.POST.get('inventory')
        sale_num = request.POST.get('sale_num')
        publisher_id = request.POST.get('publisher_id')
        models.Book.objects.filter(id=id).update(name=name, price=price, inventory=inventory, sale_num=sale_num, publisher_id=publisher_id, )
        return redirect('/book_list')


def delete_book(request):
    if "user_name" not in request.session:
        return redirect("/login")
    id = request.GET.get('id')
    models.Book.objects.filter(id=id).delete()
    return redirect('/book_list')


def add_author(request):
    if "user_name" not in request.session:
        return redirect('/login')
    if request.method == "GET":
        book_obj_list = models.Book.objects.all()
        return render(request, 'author/add_author.html', {'book_obj_list': book_obj_list, 'name': request.session["user_name"]})
    else:
        name = request.POST.get('user_name')
        book_ids = request.POST.get('books')
        author_obj = models.Author.objects.create(name=name)
        author_obj.books.set(book_ids)
        return redirect('/author_list')


def author_list(request):
    if "user_name" not in request.session:
        return redirect('/login')
    res_list = []
    author_obj_list = models.Author.objects.all()
    for author_obj in author_obj_list:
        book_obj_list = models.Book.objects.all()
        ret_dict = {'book_obj': book_obj_list, 'author_obj': author_obj}
        res_list.append(ret_dict)
        return render(request, 'author/author_list.html', {'res_list': res_list, 'name': request.session['user_name']})


def edit_author(request):
    if "user_name" not in request.session:
        return redirect('/login')
    if request.method == 'GET':
        id = request.GET.get('id')
        author_obj = models.Author.objects.get(id=id)
        book_obj_list = models.Book.objects.all()
        return render(request, 'author/edit_author.html',
                      {'author_obj': author_obj, 'book_obj_list': book_obj_list, 'name': request.session['user_name']})
    else:
        id = request.POST.get('id')
        name = request.POST.get('name')
        book_ids = request.POST.getlist('books')
        author_obj = models.Author.objects.filter(id=id).first()
        author_obj.author_name = name
        author_obj.books.set(book_ids)
        author_obj.save()
        return redirect('/author_list')


def delete_author(request):
    if "user_name" not in request.session:
        return redirect("/login")
    id = request.GET.get('id')
    models.Author.objects.filter(id=id).delete()
    return redirect('/author_list')


def logout(request):
    request.session.flush()
    # return redirect(request, 'admin/admin.html')
    return redirect('/login')
