from django.test import TestCase
import request
# Create your tests here.
url = "http://localhost:8000/students/"

res = request.get(url)

print(url.join())