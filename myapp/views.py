from django.shortcuts import render , HttpResponse ,redirect
import pymongo

client = pymongo.MongoClient('mongodb+srv://satwik:aman1234@cluster0.yltwi.mongodb.net/AugmentAi?retryWrites=true&w=majority')
db = client.AugmentAi

def home(request):
    
    grant=db['grant']
    grant=grant.find()
    context={'data':grant}


    return render(request,'home.html',context)


def case_study(request):
    
    case_study=db['case_studies']
    case_study=case_study.find()
    context={'data':case_study}
    return render(request,'Case_study.html',context)   