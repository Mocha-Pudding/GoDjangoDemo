from django.shortcuts import render, HttpResponse, redirect
from firstapp.models import People, Article, Comment
from django.template import Context, Template
from firstapp.form import CommentForm

# Create your views here.
def first_try(request):
    person = People(name='Charles', job='officer')
    html_string = '''
        <html>
            <head>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.6/semantic.css" media="screen" title="no title">
                <title>firstapp</title>
            </head>
            <body>
                <h1 class="ui center aligned icon header">
                    <i class="hand spock icon"></i>
                    Hello, {{ person.name }}
                </h1>
            </body>
        </html>

    '''
    t =Template(html_string)
    c = Context({'person':person})
    web_page = t.render(c)
    return HttpResponse(web_page)

def index(request):
    print(request)
    print('==='*30)
    print(dir(request))
    print('==='*30)
    print(type(request))
    queryset = request.GET.get('tag')
    if queryset:
        article_list = Article.objects.filter(tag=queryset)
    else:
        article_list = Article.objects.all()
    print(queryset)
    context = {};

    context['article_list'] = article_list
    index_page = render(request, 'first_web_2.html', context)
    return index_page

def detail(request, page_num):
    if request.method == 'GET':
        form = CommentForm
    if request.method == 'POST':
        form= CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            a = Article.objects.get(id=page_num)
            c = Comment(name=name, comment=comment, belong_to=a)
            c.save()
            return redirect(to='detail', page_num=page_num)
    context = {}
    # comment_list = Comment.objects.all()
    a = Article.objects.get(id=page_num)
    best_comment = Comment.objects.filter(best_comment=True, belong_to=a)
    if best_comment:
        context['best_comment'] = best_comment[0]
    article = Article.objects.get(id=page_num)
    context['article'] = article
    # context['comment_list'] = comment_list
    context['form'] = form
    return render(request, 'detail.html', context)
