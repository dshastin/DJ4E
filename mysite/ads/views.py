from django.shortcuts import render
from . import owner
from .models import Ad


class AdListView(owner.OwnerListView):
    model = Ad


class AdDetailView(owner.OwnerDetailView):
    model = Ad


class AdCreateView(owner.OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']


class AdUpdateView(owner.OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']


class AdDeleteView(owner.OwnerDeleteView):
    model = Ad
