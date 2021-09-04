from django.shortcuts import render
from main.models import Post, Category, CommentItem, About, Contact, GetInTouch
from django.http import JsonResponse
# Create your views here.



def aboutHandler(request):
    galleries = Post.objects.all().order_by('-rating')[:8]
    recent_posts = Post.objects.all().order_by('-rating')[:3]
    info = About.objects.all()
    return render(request, 'about.html', {'galleries':galleries,'recent_posts':recent_posts, 'info':info})



def blogHandler(request ):
    galleries = Post.objects.all().order_by('-rating')[:8]
    recent_posts = Post.objects.all().order_by('-rating')[:3]
    categories = Category.objects.filter()
    category_id = int(request.GET.get('category_id', 0))
    post_count = Post.objects.all().count()
    item_count = Post.objects.all().count()

    limit = int(request.GET.get('limit', 8))
    current_page = int(request.GET.get('page', 1))
    stop = current_page * limit
    start = stop - limit

    posts = Post.objects.filter()[start:stop]
    total = Post.objects.count()

    prev_page = current_page - 1
    next_page = 0
    if total > stop:
        next_page = current_page + 1

    return render(request, 'blog.html', {'galleries':galleries, 'recent_posts':recent_posts,
                                         'current_page': current_page,
                                         'prev_page': prev_page,
                                         'next_page': next_page,
                                         'total': total,
                                         'limit': limit,
                                         'posts':posts,
                                         'categories': categories,
                                         'category_id':category_id,
                                         'post_count':post_count,
                                         'item_count':item_count
                                         })


def postItemHandler(request, post_id):
    post = Post.objects.get(id=int(post_id))

    return render(request, 'single.html', {'post':post})

def contactHandler(request):
    galleries = Post.objects.all().order_by('-rating')[:8]
    recent_posts = Post.objects.all().order_by('-rating')[:3]
    return render(request, 'contact.html', {'galleries':galleries,'recent_posts':recent_posts})

def eventHandler(request):
    posts = Post.objects.all()[:6]
    galleries = Post.objects.all().order_by('-rating')[:8]
    recent_posts = Post.objects.all().order_by('-rating')[:3]

    q = request.GET.get('q', '')

    if q:
        posts = Post.objects.filter(status = 1).filter(title__contains=q).order_by('-rating')
    else:
        posts = Post.objects.all()[:6]

    limit = int(request.GET.get('limit', 8))
    current_page = int(request.GET.get('page', 1))
    stop = current_page * limit
    start = stop - limit

    posts = Post.objects.filter()[start:stop]
    total = Post.objects.count()

    prev_page = current_page - 1
    next_page = 0
    if total > stop:
        next_page = current_page + 1

    return render(request, 'event.html', {'galleries':galleries, 'recent_posts':recent_posts, 'posts':posts, 'q':q,
                                          'current_page': current_page,
                                          'prev_page': prev_page,
                                          'next_page': next_page,
                                          'total': total,
                                          'limit': limit,

                                          })

def homeHandler(request):
    head_post = Post.objects.all().order_by('-rating')[:4]
    posts = Post.objects.all()[:6]
    categories = Category.objects.all()
    galleries = Post.objects.all().order_by('-rating')[:8]
    recent_posts = Post.objects.all().order_by('-rating')[:3]

    return render(request, 'home.html', {'posts':posts, 'categories':categories, 'head_post':head_post, 'galleries':galleries,
                                         'recent_posts':recent_posts})

def singleHandler(request, post_id):
    galleries = Post.objects.all().order_by('-rating')[:8]
    recent_posts = Post.objects.all().order_by('-rating')[:3]
    post = Post.objects.get(id=int(post_id))
    comment_items = CommentItem.objects.filter(post__id=post_id)

    s = 0

    for i in comment_items:
        s = s + 1
    a = s + 1
    print(s, a)
    print("*"*100)


    if request.POST:

        c = CommentItem()

        name = request.POST.get('name', '')
        comment = request.POST.get('name', '')

        c.author = name
        c.comment = comment
        c.save()

        CommentItem.rating = a


    return render(request, 'single.html', {'galleries':galleries, 'recent_posts':recent_posts, 'post':post, 'comment_items':comment_items})

def travelHandler(request):
    posts = Post.objects.all()[:6]
    galleries = Post.objects.all().order_by('-rating')[:8]
    recent_posts = Post.objects.all().order_by('-rating')[:3]

    limit = int(request.GET.get('limit', 8))
    current_page = int(request.GET.get('page', 1))
    stop = current_page * limit
    start = stop - limit

    posts = Post.objects.filter()[start:stop]
    total = Post.objects.count()

    prev_page = current_page - 1
    next_page = 0
    if total > stop:
        next_page = current_page + 1

    return render(request, 'travel.html', {'posts':posts, 'galleries':galleries, 'recent_posts':recent_posts,
                                           'current_page': current_page,
                                           'prev_page': prev_page,
                                           'next_page': next_page,
                                           'total': total,
                                           'limit': limit,
                                           })


def contactHandler(request):
    contact = Contact.objects.all()


    if request.POST:

        r = GetInTouch()

        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        title = request.POST.get('title', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')

        r.firstname = firstname
        r.lastname = lastname
        r.email = email
        r.title = title
        r.message = message
        r.save()


    return render(request, 'contact.html', {'contact':contact})







