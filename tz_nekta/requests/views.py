import json
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import *
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .forms import *
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': "Личный кабинет", 'url_name': 'personalarea'}
]



def index(request):
    return render(request, 'requests/index.html', {'menu': menu, 'title': 'Главная страница'})

def about(request):
    return render(request, 'requests/about.html', {'menu': menu, 'title': 'О сайте'})




def personal_area(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request, 'requests/personal_area.html', {'menu': menu, 'title': 'Личный кабинет'})

def register(request):
    return render(request, 'requests/register.html', {'menu': menu, 'title': 'Зарегистрироваться'})




class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'requests/register.html'
    success_url = reverse_lazy('login')


class NewRequest(CreateView):
    def form_valid(self, form):

        return HttpResponseRedirect(self.get_success_url())

    template_name = 'requests/newrequest.html'

    def post(self, *args, **kwargs):
        form_class = AddRequestForm(self.request.POST)
        self.object = form_class.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return redirect(reverse_lazy('newmail', kwargs={'request_id': self.object.id}))

    def get(self, *args, **kwargs):
        form_class = AddRequestForm()
        return self.render_to_response({'form': form_class})


class RequestListView(ListView):
    model = Request
    template_name = "requests/request_list.html"
    def get_context_data(self, *args, **kwargs):
        context = super(RequestListView, self).get_context_data(*args, **kwargs)
        context['object_list'] = Request.objects.filter(user=self.request.user)
        return context



class NewRequestMessage(CreateView):
    def form_valid(self, form):

        return HttpResponseRedirect(self.get_success_url())

    template_name = 'requests/request_mail.html'

    def post(self, *args, **kwargs):
        form_class = AddMessageForm(self.request.POST)
        self.object = form_class.save(commit=False)
        self.object.user = self.request.user
        self.object.request = kwargs.get('request_id')
        self.object.save()
        return redirect(reverse_lazy('personalarea'))

    def get(self, *args, **kwargs):
        form_class = AddMessageForm()
        return self.render_to_response({'form': form_class, 'request_id': kwargs.get('request_id')})



class RequestMessageById(CreateView):
    def get(self, *args, **kwargs):
        form_class = AddMessageFormById()
        return self.render_to_response({'form': form_class})

    template_name = 'requests/request_mail.html'

    def post(self, *args, **kwargs):
        form_class = AddMessageFormById(self.request.POST)
        self.object = form_class.save(commit=False)
        if form_class.is_valid():
               if not form_class.has_changed():
                  form_class.add_error(None, "Ошибка заполнения формы")
                  return self.render_to_response({'form': form_class})
               if cur_request:= Request.objects.filter(id=self.object.request):
                   if cur_request[0].user == self.request.user:
                       self.object.save()
                       return redirect(reverse_lazy('personalarea'))
        form_class.add_error(None, 'Ошибка')
        return self.render_to_response({'form': form_class})



class RequestsInfo(CreateView):
    def get(self, *args, **kwargs):
        form_class = FindRequestsInfo()
        return self.render_to_response({'form': form_class})

    template_name = 'requests/request_info.html'

    def post(self, *args, **kwargs):
        form_class = FindRequestsInfo(self.request.POST)
        if form_class.is_valid():

            if not form_class.has_changed():
                form_class.add_error(None, "Ошибка заполнения формы")
                return self.render_to_response({'form': form_class})
            if cur_request := Request.objects.filter(id=self.request.POST.get('requestid')):
                if cur_request[0].user == self.request.user:

                    return redirect(reverse_lazy('requestinfobyid', kwargs={'request_id': self.request.POST.get('requestid')}))

        form_class.add_error(None, 'Ошибка')
        return self.render_to_response({'form': form_class})


class RequestsInfoById(ListView):
    model = Request
    template_name = "requests/request_list_by_id.html"
    def get_context_data(self, *args, **kwargs):
        context = super(RequestsInfoById, self).get_context_data(*args, **kwargs)
        context['object_list'] = Request.objects.filter(id=self.kwargs.get('request_id'))[0]
        context['message_by_request_list'] = RequestMessage.objects.filter(request=self.kwargs.get('request_id'))
        context['user_name'] = self.request.user

        return context

class RequestMessages(CreateView):
    def get(self, *args, **kwargs):
        form_class = FindRequestsInfo()
        return self.render_to_response({'form': form_class})

    template_name = 'requests/request_mail_list_by_id.html'

    def post(self, *args, **kwargs):
        form_class = FindRequestsInfo(self.request.POST)
        if form_class.is_valid():

            if not form_class.has_changed():
                form_class.add_error(None, "Ошибка заполнения формы")
                return self.render_to_response({'form': form_class})
            if cur_request := Request.objects.filter(id=self.request.POST.get('requestid')):
                if cur_request[0].user == self.request.user:

                    return redirect(reverse_lazy('requestmessagesbyid', kwargs={'request_id': self.request.POST.get('requestid')}))

        form_class.add_error(None, 'Ошибка')
        return self.render_to_response({'form': form_class})


class RequestMessagesById(ListView):
    model = Request
    template_name = "requests/request_mail_list.html"

    def get_context_data(self, *args, **kwargs):
        context = super(RequestMessagesById, self).get_context_data(*args, **kwargs)
        context['object_list'] = Request.objects.filter(id=self.kwargs.get('request_id'))[0]
        context['message_by_request_list'] = RequestMessage.objects.filter(request=self.kwargs.get('request_id'))
        return context

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'requests/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return redirect('login')