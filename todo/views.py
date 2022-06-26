from django.shortcuts import render, redirect
from .forms import ToDoForm
from .models import TodoItem
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    log_user = request.user
    try:
        todoitems = TodoItem.objects.filter(user=log_user)
        form = ToDoForm()
        no_of_todo = TodoItem.objects.filter(complete=False, user=log_user).count()
        return render(request, 'index.html', {'todoitems': todoitems,
        'form': form, 'count':no_of_todo})
    except:
        return render(request, 'index.html')
    

def edit(request, pk):
    task = TodoItem.objects.get(todo_id=pk)
    form = ToDoForm(request.POST, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Edited Successfully!!')
            return redirect(index)
    else:
        form = ToDoForm(instance=task)

    return render(request, 'edit.html', {'form': form})

def delete(request, pk):
    TodoItem.objects.get(todo_id=pk, user=request.user).delete()
    messages.success(request, 'Deleted Todo Successfully!!')
    return redirect(index)

def additem(request):
    if request.method == 'POST':
        addtitle = request.POST['addtitle']
        adddesc = request.POST['adddesc']
        if addtitle == '':
            messages.error(request, 'Title must be Given!')
        else:
            add = TodoItem(title = addtitle, desc= adddesc, user=request.user)
            add.save()
            messages.success(request, 'Added Todo Successfully!!')
        return redirect(index)
    else:
        return redirect(index)

def signup(request):
    if request.method == 'POST':
        username = request.POST['usernamesignup']
        password = request.POST['passwordsignup']
        confirmpassword = request.POST['confirmpassword']
        fname = request.POST['fname']
        lname = request.POST['lname']
        
        if password != confirmpassword:
            messages.error(request, "Passwords Don't match!")
            return redirect(index)
        if len(username) > 20:
            messages.error(request, "Username must be less than 20 charecters")
            return redirect(index)
        if not username.isalnum():
            messages.error(request, "Username must contain letters and numbers only")
            return redirect(index)
        if len(password) < 8:
            messages.error(request, "Password must be al least 8 charecters")
            return redirect(index)

        
        try:
            User._default_manager.get(username=username)
            messages.error(request, 'Username is already taken!')

        except User.DoesNotExist:
            createuser = User.objects.create_user(username=username, password=password)
            createuser.first_name = fname
            createuser.last_name = lname
            createuser.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Your AniToDo Account has been created and you have logged in Successfully!')
            
        return redirect(index)

    else:
        return redirect(index)


def loginuser(request):
    if request.method == 'POST':
        usernamelogin = request.POST['usernamelogin']
        passwordlogin = request.POST['passwordlogin']
        user = authenticate(username=usernamelogin, password=passwordlogin)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully!!')
            return redirect(index)
        else:
            messages.error(request, 'Username or Password is wrong!\nPlease try again! ')
            return redirect(index)

    return redirect(index)

def logoutuser(request):
    logout(request)
    messages.success(request, 'Successfully Logged out!!')
    return redirect(index)

def pagenotfound(request):
    return render(request, '404.html')
