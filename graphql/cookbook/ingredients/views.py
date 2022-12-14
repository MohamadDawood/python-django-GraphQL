from django.shortcuts import render

# Create your views here.
from django.utils.decorators import decorator_from_middleware


@decorator_from_middleware('')
def test_decorator():
    pass