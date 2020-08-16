from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from .forms import CreateUserForm, UserUpdateForm, ProfileUpdateForm, CurrencyForm, TaskForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import is_authenticated
from datetime import datetime


def budget_assembly(budget):
    total_budget = 0
    for i in budget:
        total_budget += i.amount
    return total_budget


def spendings_assembly(spendings):
    total_spendings = 0
    for i in spendings:
        total_spendings += i.amount
    return total_spendings


def spendings_percentages_of_buget(budget, spendings):
    spendings_percent = 0
    if budget > 0:
        spendings_percent = round((spendings / budget) * 100, 2)
    return spendings_percent


def savings_percentages_of_buget(budget, savings):
    savings_percent = 0
    if budget > 0:
        savings_percent = round((savings / budget) * 100, 2)
    return savings_percent


@login_required
def dashboard(request):
    current_month = datetime.now().month
    current_year = datetime.now().year
    currency = Currency.objects.filter(user=request.user)
    budget = Budget.objects.filter(
        user=request.user, date_created__year=current_year, date_created__month=current_month)
    spendings = Spending.objects.filter(
        user=request.user, date_created__year=current_year, date_created__month=current_month)
    total_budget = round(budget_assembly(budget), 2)
    total_spendings = round(spendings_assembly(spendings), 2)
    total_savings = round(total_budget - total_spendings, 2)
    spendings_percent = spendings_percentages_of_buget(
        total_budget, total_spendings)
    savings_percent = savings_percentages_of_buget(total_budget, total_savings)
    context = {
        'title': 'Dashboard',
        'total_spendings': total_spendings,
        'total_budget': total_budget,
        'total_savings': total_savings,
        'spendings_percent': spendings_percent,
        'savings_percent': savings_percent,
        'spendings': spendings,
        'budget': budget,
        'currency': currency,
    }
    return render(request, 'users/dashboard.html', context)


@login_required
def notes(request):
    notes = Note.objects.filter(user=request.user)
    context = {
        'title': 'Notes',
        'notes': notes,
    }
    return render(request, 'users/notes.html', context)


@login_required
def tasks(request, pk):
    note = Note.objects.get(id=pk)
    tasks = Task.objects.filter(note=note)
    if request.method == 'POST':
        title = request.POST['task_text']
        create_task(request, pk, title)
    context = {
        'title': 'Tasks',
        'tasks': tasks,
    }
    return render(request, 'users/tasks.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        c_form = CurrencyForm(request.POST, instance=request.user.currency)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid() and c_form.is_valid():
            c_form.save()
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        c_form = CurrencyForm(instance=request.user.currency)
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'c_form': c_form,
        'title': 'Profile',
    }
    return render(request, 'users/profile.html', context)


@is_authenticated
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {
        'form': form,
        'title': 'Register',
    }
    return render(request, 'users/register.html', context)


@login_required
def create_spending(request):
    Spending.objects.create(user=request.user, name=request.POST['spending_name'],
                            category=request.POST['category'], amount=request.POST['amount'])
    return redirect('dashboard')


@login_required
def delete_spending(request, pk):
    spending = Spending.objects.get(id=pk)
    if request.method == 'POST':
        spending.delete()
        return redirect('dashboard')
    context = {
        'item': spending
    }
    return render(request, 'users/delete_spending.html', context)


@login_required
def create_note(request):
    Note.objects.create(
        user=request.user, title=request.POST['note_title'], category=request.POST['category'])
    return redirect('notes')


@login_required
def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    context = {
        'note': note,
    }
    return render(request, 'users/delete_note.html', context)


@login_required
def create_task(request, pk, title):
    note = Note.objects.get(id=pk)
    Task.objects.create(note=note, title=title)
    return redirect('tasks', pk)


@login_required
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    note_id = task.note.id
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('tasks', note_id)
    context = {
        'form': form,
        'id': note_id,
    }
    return render(request, 'users/update_task.html', context)


@login_required
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    note_id = task.note.id
    if request.method == 'POST':
        task.delete()
        return redirect('tasks', note_id)
    context = {
        'task': task,
        'id': note_id,
    }
    return render(request, 'users/delete_task.html', context)


@login_required
def add_budget(request):
    Budget.objects.create(
        user=request.user, amount=request.POST['budget_amount'])
    return redirect('dashboard')
