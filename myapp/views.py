from tkinter.messagebox import NO
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from .models import Book
from .serializers import BooksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def index(request):
  return render(request, "myapp/index.html")

def get(request):
  return render(request, "myapp/get.html")

def post(request):
  return render(request, "myapp/post.html")

def put(request):
  return render(request, "myapp/put.html")

def delete(request):
  return render(request, "myapp/delete.html")

@api_view(['GET', 'POST'])
def book_list(request):
  if request.method == 'GET':
    # get all books
    # serialize them
    # return as JSON , instead of having a list make it object
    # Response of rest framework is more better
    books = Book.objects.all()
    serializer = BooksSerializer(books, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    # take json data
    # deserialize it
    # create an object out of it
    serializer = BooksSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def book_detail(request , id):
  # checking if valid request
  try:
    book = Book.objects.get(pk=id)
  except Book.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':
    serializer = BooksSerializer(book)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer = BooksSerializer(book, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'PUT':
    serializer = BooksSerializer(book, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    book.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)