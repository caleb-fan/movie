from django.shortcuts import render
from movies import models
# Create your views here.

def index(request):
    movies = models.Movies.objects.all()
    context = {"movies":movies}
    return render(request,"主页.html",context)

def get_types():
    types = models.Movies.objects.all()
    deal_types=['全部']
    for type in types:
        for d_type in type.m_type.split(" "):
            if d_type not in deal_types and d_type !="":
                deal_types.append(d_type)
    return deal_types[:17]

def search(request):
    search = request.GET.get('search')
    movies = models.Movies.objects.filter(m_name__contains=search)
    context = {'movies':movies,'search':search}
    return render(request, "电影分类页.html", context)

def classify(request):
    search = request.GET.get('type')
    movies = models.Movies.objects.filter(m_type__contains=search)
    context = {'movies': movies, 'search': search}
    return render(request, "电影分类页.html", context)
def nation(request):
    search = request.GET.get('type')
    movies = models.Movies.objects.filter(m_nation__contains=search)
    context = {'movies': movies, 'search': search}
    return render(request, "电影分类页.html", context)
def data(request):
    search = request.GET.get('type')
    movies = models.Movies.objects.filter(m_data__contains=search)
    context = {'movies': movies, 'search': search}
    return render(request, "电影分类页.html", context)
def list(request):
    search = request.GET.get('type')
    movies = models.Movies.objects.filter(m_post__istartswith="static/img/"+search)
    context = {'movies': movies, 'search': search}
    return render(request, "电影分类页.html", context)
def denglu (request):
    flag = 1
    movies = models.Movies.objects.all()
    name = request.POST.get('u_name')
    password = request.POST.get('u_pass')
    tel = name
    try:
        u_pass = models.User.objects.get(u_name=name,u_password=password)
        request.session['u_name'] = u_pass.u_name
    except:
            try:
                u_pass = models.User.objects.get(u_tel=tel, u_password=password)
                request.session['u_name'] = u_pass.u_name
            except:
                request.session['u_name'] = None
                flag = 0
    context = {"movies":movies,"flag":flag}
    return render(request, "主页.html", context)

def logout(request):
    movies = models.Movies.objects.all()
    request.session['u_name'] = None
    context = {"movies":movies}
    return render(request, '主页.html', context)
def zhuce(request):
    flag = 1
    movies = models.Movies.objects.all()
    name = request.POST.get('Username')
    password = request.POST.get('Password')
    password2 = request.POST.get('Password2')
    tel = request.POST.get('Phone')
    if password == password2:
        try:
            models.User.objects.create(u_name=name,u_password=password,u_tel=tel)
        except:
            flag = 0
    context = {"movies": movies, "flag": flag}
    return render(request, "主页.html", context)
def get_info(request):
    movie_name = request.GET.get("movie")
    movie = models.Movies.objects.get(m_name=movie_name)
    u_name = request.GET.get("u_name")
    if u_name != "0":
        m_id = movie.m_id
        user = models.User.objects.get(u_name=u_name)
        u_id = user.u_id
        c_u_id = models.Collection.objects.filter(u_id=u_id)
        list = []
        for i in c_u_id:
            if i.m_id == m_id:
                list.append(i.m_id)
        if len(list)== 0:
            flag = "加入收藏"
            value = "在线观看"
            value2 = 0
        else:
            flag = "取消收藏"
            value = "在线观看"
            value2 = 0
    else:
        flag = "登录加入收藏"
        value = "请登录观看"
        value2 = 1
    context = {"movie":movie,"flag":flag,"value":value,"value2":value2}
    return render(request,"get_info.html",context)


def shoucang(request):
    u_name = request.GET.get("username")
    if u_name != "0":
        username = models.User.objects.get(u_name=u_name)
        u_id=username.u_id
        collects=models.Collection.objects.filter(u_id=u_id)
        movies = []
        try:
            for collect in collects:
                movie = models.Movies.objects.get(m_id=collect.m_id)
                movies.append(movie)
        except:
            pass
        context = {"moviess":movies}
    else:
        context = {"moviess": 0}
    return render(request, "shoucang.html", context)
def shoucang_jiaru(request):
    m_name = request.GET.get("m_name")
    u_name = request.GET.get("u_name")
    movie = models.Movies.objects.get(m_name=m_name)
    m_id = movie.m_id
    list=[]
    try:
        user = models.User.objects.get(u_name=u_name)
        u_id = user.u_id
        c_u_id= models.Collection.objects.filter(u_id=u_id)
        for i in c_u_id:
            if i.m_id == m_id:
                list.append(i.m_id)
    except:
        pass
    if len(list) == 0:
        models.Collection.objects.create(u_id=u_id,m_id=m_id)
        flag = "取消收藏"
    else:
        models.Collection.objects.filter(u_id=u_id,m_id=m_id).delete()
        flag = "加入收藏"
    context={"flag2":flag}
    return render(request, "shoucang_jiaru.html", context)
def fenye(request):
    page = request.GET.get("page")
    if page == "1":
        movies = models.Movies.objects.all()
        context = {"movies": movies[0:24]}
    if page == "2":
        movies = models.Movies.objects.all()
        context = {"movies": movies[24:48]}
    if page == "3":
        movies = models.Movies.objects.all()
        context = {"movies": movies[48:72]}
    if page == "4":
        movies = models.Movies.objects.all()
        context = {"movies": movies[72:96]}
    if page == "5":
        movies = models.Movies.objects.all()
        context = {"movies": movies[96:120]}
    if page == "6":
        movies = models.Movies.objects.all()
        context = {"movies": movies[120:144]}
    if page == "7":
        movies = models.Movies.objects.all()
        context = {"movies": movies[144:168]}
    if page == "8":
        movies = models.Movies.objects.all()
        context = {"movies": movies[168:192]}
    if page == "9":
        movies = models.Movies.objects.all()
        context = {"movies": movies[192:216]}
    if page == "10":
        movies = models.Movies.objects.all()
        context = {"movies": movies[216:240]}
    if page == "11":
        movies = models.Movies.objects.all()
        context = {"movies": movies[240:]}
    return render(request, "fenye.html", context)