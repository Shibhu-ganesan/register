from django.shortcuts import render, redirect
from .Forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group


def dashboard(request):
    context = {}
    return render(request, "joinwithmeapp/dashboard.html", context)


def startup_page(request):
    context = {}
    return render(request, "joinwithmeapp/startup.html", context)


def member_page(request):
    context = {}
    return render(request, "joinwithmeapp/member.html", context)


def investor_page(request):
    context = {}
    return render(request, "joinwithmeapp/investor.html", context)


def startup_form(request):
    form = StartUpForm()
    if request.method == "POST":
        form = StartUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, 'joinwithmeapp/startup_form.html', context)


def member_form(request):
    form = MemberForm()
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form": form}

    return render(request, 'joinwithmeapp/member_form.html', context)


def investor_form(request):
    form = InvestorForm()
    if request.method == "POST":
        form = InvestorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {"form": form}

    return render(request, 'joinwithmeapp/investor_form.html', context)


def l_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            group = request.user.groups.all()[0].name
            if group == 'member':
                return member_page(request)
            elif group == 'investor':
                return investor_page(request)
            elif group == 'startup_seeker':
                return startup_page(request)
            group = None
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'joinwithmeapp/login.html', context)


def member_register(request):
    group = None
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='member')
            user.groups.add(group)
            Member.objects.create(
                user=user,
                Name=user.username
            )
            messages.success(request, "Hell yeah Welcome" + username)
            return redirect("login")
    context = {"form": form}
    return render(request, 'joinwithmeapp/member_register.html', context)


def investor_register(request):
    group = None
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='investor')
            user.groups.add(group)
            Investor.objects.create(
                user=user,
                Name=user.username
            )

            messages.success(request, "Hell yeah Welcome" + username)
            return redirect("login")
    context = {"form": form}
    return render(request, 'joinwithmeapp/investor_register.html', context)


def startup_register(request):
    group = None
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='startup_seeker')
            user.groups.add(group)
            StartUp.objects.create(
                user=user,
                Name=user.username
            )

            messages.success(request, "Hell yeah Welcome" + username)
            return redirect("login")
    context = {"form": form}
    return render(request, 'joinwithmeapp/startup_register.html', context)


def reg_before(request):
    context = {}
    return render(request, 'joinwithmeapp/reg_before_page.html', context)
