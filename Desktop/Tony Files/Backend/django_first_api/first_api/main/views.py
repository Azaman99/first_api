from rest_framework import status
from rest_framework.fields import ReadOnlyField
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BookSerializer, StudentSerializer
from .models import Student, Book
from drf_yasg.utils import swagger_auto_schema


# Create your views here.
@swagger_auto_schema(methods=["POST"], request_body=StudentSerializer())
@api_view(["GET", "POST"])
def students(request):
    """
    Takes in a student id and returns the http response depending on the http method.
    Args:
    student_id: Integer

    Allowed methods:
    GET - Gets the detail of all the student.
    POST - Allows the user to create a new student.
    """
    if request.method == "GET":
        all_students = Student.objects.all()
        serializer = StudentSerializer(all_students, many=True)### serialize the data

        data = {
            "message" : "Success",
            "data" : serializer.data
        }## prepare the response

        return Response(data, status=status.HTTP_200_OK) ### send the response

    elif request.method == "POST":

        serializer = StudentSerializer(data=request.data) ## get and deserialize the data

        if serializer.is_valid(): ## check if the data is valid
            serializer.save() ## save the data
            
            data = {
                "message" : "Success",
                "data" : serializer.data
            }

            return Response(data, status=status.HTTP_200_OK)

        else:
            error = {
                "message" : "Failed",
                "errors" : serializer.errors
            }

            return Response(error, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=["POST"], request_body=BookSerializer())
@api_view(["GET", "POST"])
def books(request):
    if request.method == "GET":
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)

        data = {
            "message" : "Success",
            "data" : serializer.data
        }

        return Response(data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            data = {
                "message" : "Success",
                "data" : serializer.data
            }

            return Response(data, status=status.HTTP_200_OK)

        else:
            error = {
                "message" : "Failed",
                "errors" : serializer.errors
            }

            return Response(error, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(methods=["PUT", "DELETE"], request_body=StudentSerializer())
@api_view(["GET", "PUT", "DELETE"])
def student_detail(request, student_id):
    """
    Takes in a student id and returns the http response depending on the http method.
    Args:
    student_id: Integer

    Allowed methods:
    GET - Gets the detail of a single student.
    PUT - Allows the student detail to edit/ modify.
    DELETE - This logic deletes the students record from the database.
    """
    try:
        student = Student.objects.get(id = student_id) ## get the data from the model
    except Student.DoesNotExist:
        error = {
                "message" : "Failed",
                "errors" : f"Student with id {student_id} does not exist."
            }

        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = StudentSerializer(student)
        data = {
            "message" : "Success",
            "data" : serializer.data
        }  #prepare the response data

        return Response(data, status = status.HTTP_200_OK) ## Send the response.

    elif request.method == "PUT":
        serializer = StudentSerializer(student, data=request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            serializer = StudentSerializer(student)
            data = {
                "message" : "Success",
                "data" : serializer.data
            }  #prepare the response data

            return Response(data, status = status.HTTP_202_ACCEPTED)

        else:
            error = {
                "message" : "Failed",
                "data" : serializer.errors
            }

            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE": 
        student.delete()

        return Response({"message":"Success"}, status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(methods=["PUT", "DELETE"], request_body=BookSerializer())
@api_view(["GET", "PUT", "DELETE"])
def book_detail(request, book_id):
    """
    Takes in a book id and returns the http response depending on the http method.
    Args:
    Book_id: Integer

    Allowed methods:
    GET - Gets the detail of a single Book of a Student.
    PUT - Allows the book detail to edit/ modify the book.
    DELETE - This logic deletes the book record from the database.
    """
    try:
        book = Book.objects.get(id = book_id) ## get the data from the model
    except Book.DoesNotExist:
        error = {
                "message" : "Failed",
                "errors" : f"Student with id {book_id} does not exist."
            }

        return Response(error, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = BookSerializer(book)
        data = {
            "message" : "Success",
            "data" : serializer.data
        }  #prepare the response data

        return Response(data, status = status.HTTP_200_OK) ## Send the response.

    elif request.method == "PUT":
        serializer = BookSerializer(book, data=request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            serializer = BookSerializer(book)
            data = {
                "message" : "Success",
                "data" : serializer.data
            }  #prepare the response data

            return Response(data, status = status.HTTP_202_ACCEPTED)

        else:
            error = {
                "message" : "Failed",
                "data" : serializer.errors
            }

            return Response(error, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE": 
        book.delete()

        return Response({"message":"Success"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def cohort_list(request):
    if request.method == "GET":
        cohorts = Student.objects.values_list("cohort", flat = True).distinct()

        data = {cohort:{
            "count":Student.objects.filter(cohort=cohort).count(),
            "data":Student.objects.filter(cohort=cohort).values()
            } 
            
            for cohort in cohorts}

        return Response(data, status=status.HTTP_204_NO_CONTENT)
