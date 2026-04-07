from django.shortcuts import render, redirect, get_object_or_404 
from blog.models import Post, Reply
from blog.forms import PostModelForm, ReplyForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

#게시글 목록 조회
def comment_list(request):
    posts = Post.objects.all().order_by('-created_at')
    my_paginator = Paginator(posts, 5)
    page_num = request.GET.get('page')
    posts = my_paginator.get_page(page_num)
    return render(request, "comment_list.html", {"posts" : posts})

#게시글 상세페이지 조회
def comment_detail(request, post_id):
    post = get_object_or_404(Post,id=post_id)
    reply_form = ReplyForm()
    context = {
        'post': post,
        'reply_form': reply_form,
        'replies': post.replies.all()
    }
    return render(request, 'comment_detail.html', context)

#게시글 수정
def comment_update(request, id):
    post = get_object_or_404(Post, pk=id)

    if request.method == 'POST'or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:   #GET이면
        form = PostModelForm(instance=post)
        return render(request, 'form_create.html', {'form':form, 'post':post})
    
#게시글 삭제
def comment_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('comment_list')

def resume_view(request):
    return render(request, "resume.html")


# 댓글 작성

def create_reply(request, id):
    filled_form = ReplyForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=id)
        finished_form.author = request.user
        finished_form.save()

    return redirect('comment_detail', id)

# 댓글 수정
def update_reply(request, post_id, com_id):
    reply = get_object_or_404(Reply, id=com_id)
        
    if request.method == "POST": 
        updated_form = ReplyForm(request.POST, instance=reply)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('comment_detail', post_id)
            
    else:
        reply_form = ReplyForm(instance=reply)
        context = {'reply_form': reply_form,'post_id': post_id,
        'com_id': com_id}
        return render(request, 'reply_update.html', context)
    
# 댓글 삭제
def delete_reply(request, post_id, com_id):
    reply = Reply.objects.get(id=com_id)
    reply.delete()
    return redirect('comment_detail', post_id)