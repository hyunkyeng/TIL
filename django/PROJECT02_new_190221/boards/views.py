# <모듈 import 순서> 
# 1. 파이썬 표준 라이브러리        ex) os, random ...
# 2. core django : 장고 프레임워크에 내장되어 있는 것
# 3. 3rd party library : pip로 설치한 것들. django-extension
# 4. 장고프로젝트 app       ex)from .models import Board

from django.shortcuts import render, redirect
from .models import Board

# Create your views here.
def index(request):
    #boards = Board.objects.all()[::-1]      #원래 결과를 파이썬이 변경
    boards = Board.objects.order_by('-id')       # db가 애초에 정렬을 바꿔서 보내주는것. 위랑 같은 것이지만 차이가 있음.
    return render(request, 'boards/index.html', {'boards': boards})

def new(request):
    return render(request, 'boards/new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    
    board = Board(title=title, content=content)
    board.save()
    
    #위 두줄을 아래와 같이 한줄로도 쓸 수 있다.
    #Board.objects.create(title=title, content=content)
    
    
    #return render(request, 'boards/index.html') 이렇게 쓰면
    #처음에 글이 보이지 않았던 이유는 보여지는 페이지 자체는 index이지만 index의 url로는 돌아가지 못했기 때문이다. 즉, 단순이 html 문서만 보여준 것 이다. 
    #create는 model에 record를 생성해! 라는 요청이기 때문에, 단순히 페이지를 달라고 하는 GET방식보다는 POST 가 의미상 더 적절하다 
    #( 그리고 모델과 관련된 데이터이기 때문에 url 에 직접 보여지는 것은 좋지 않다. )
    # 따라서 POST방식으로 redirect 해줘야 한다. 
    
    
    return redirect('/boards/')
    # return redirect(index)   #두가지 방법다 사용가능
    
def detail(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'boards/detail.html', {'board': board})
    
def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('/boards/')
    
def edit(request, pk):
    board = Board.objects.get(pk=pk)
    return render(request, 'boards/edit.html', {'board': board})
    
def update(request, pk):
    board = Board.objects.get(pk=pk)
    board.title = request.POST.get('title')
    board.content = request.POST.get('content')
    board.save()
    return redirect(f'/boards/{board.pk}/')