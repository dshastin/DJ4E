from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Make, Auto
from .forms import AutoForm


class AutoView(LoginRequiredMixin, View):
    def get(self, request):
        make_count = Make.objects.all().count()
        auto_list = Auto.objects.all()

        context = {'make_count': make_count, 'auto_list': auto_list}
        return render(request, 'autos/auto_list.html', context)


class MakeView(LoginRequiredMixin, ListView):
    model = Make

    # def get(self, request):
    #     ml = Make.objects.all()
    #     context = {'make_list': ml}
    #     return render(request, 'autos/make_list.html', context)


class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:make_list')


class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:make_list')


class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    success_url = reverse_lazy('autos:make_list')


class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    success_url = reverse_lazy('autos:all')
    fields = '__all__'


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    success_url = reverse_lazy('autos:all')
    fields = '__all__'


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    success_url = reverse_lazy('autos:all')





