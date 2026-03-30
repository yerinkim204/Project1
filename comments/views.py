from django.shortcuts import render, redirect, get_object_or_404 
from blog.models import Post
from blog.forms import PostModelForm


#게시글 목록 조회
def comment_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "comment_list.html", {"posts" : posts})

#게시글 상세페이지 조회
def comment_detail(request, post_id):
    post = get_object_or_404(Post,id=post_id)
    return render(request, "comment_detail.html", {"post":post})

#게시글 수정
def comment_update(request, id):
    post = get_object_or_404(Post, pk=id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
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