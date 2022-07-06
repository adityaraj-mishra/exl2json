import os
from django.http import HttpResponse
from django.shortcuts import render
import pandas as pd
import pip
pip.main(["install", "openpyxl"])
from . models import fileupload
# Create your views here.

path=''
def index(request):
    if request.method == 'POST':
        # do something
        exlfile = request.FILES['file']
        # do something with file
        read_file = pd.read_excel (exlfile)
        read_file.to_csv (r'files/record.csv', index = None, header=True)

        df = pd.read_csv('files/record.csv')
        df.to_json('json/record.json', orient='records')
    output = 'Your File Converted to Json successfully !'
    print(output)
    path = 'json/record.json'
    return render(request, 'index.html',{'output':output, 'path':path})
