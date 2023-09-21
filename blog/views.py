from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Post, Board3
from .forms import *

def index(request):
	return render(request, 'blog/index.html', {})


def post(request):
    if request.method == 'POST':
        post = Post()
        post.text = request.POST.get('content')
        post.save()
        return redirect('post')
        # return render(request, 'post_list.html', {'POST':'POST방식입니다!!'})
        
    if request.method == 'GET':
        return render(request, 'blog/post_list.html', {'GET':'GET방식입니다!!'})
    
# post = Post.objects.get(id=1)


def board(request):
    if request.method == 'POST':
        # title = request.POST['title']
        # content = request.POST['content']
        # writer = request.POST['writer']
        
        title = request.POST.get('title')
        content = request.POST.get('content')
        writer = request.POST.get('writer')

        board = Board(
            title=title,
            content=content,
            writer=writer,
        )
        board.save()
        return redirect('board')
    else:
        boardForm = BoardForm
        board = Board.objects.all()
        context = {
            'boardForm': boardForm,
            'board': board,
        }
        return render(request, 'blog/board.html', context)
    
    
def board2(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user = request.user
        board = Board2(
            title=title,
            content=content,
            user=user,
        )
        board.save()

        return redirect('board2')
    else:
        boardForm = BoardForm2
        board = Board2.objects.all()
        context = {
            'boardForm2': boardForm,
            'board2': board,
        }
        return render(request, 'blog/board2.html', context)

def board3(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user = request.user
        img = ""
        try:
            img = request.FILES["imgfile"]
        except:
            pass
        
        board = Board3(
            title=title,
            content=content,
            user=user,
            imgfile=img,
        )
        board.save()
        return redirect('board3')
    else:
        boardForm = BoardForm3
        board = Board3.objects.all()
        context = {
            'boardForm3': boardForm,
            'board3': board,
        }
        return render(request, 'blog/board3.html', context)
    
def boardEdit(request, pk):
    board = Board.objects.get(id=pk)
    if request.method == "POST":
        board.title = request.POST['title']
        board.content = request.POST['content']
        board.user = request.user

        board.save()
        return redirect('board')

    else:
        boardForm = BoardForm
        return render(request, 'update.html', {'boardForm':boardForm})

def boardDelete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('board')

def select_board(request):
    month_text = request.GET.get('month')
    board_list = Board.objects.filter(month=month_text)
    return render(request, 'blog/select.html', {'board_list': board_list})

def my_view(request):
    my_data = ["data1", "data2", "data3", "data4", "data5", "data6", "data7", "data8", "data9", "data10"]
    paginator = Paginator(my_data, 2) # 페이지 당 2개의 아이템을 보여줌
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/page_list.html', {'page_obj': page_obj})


