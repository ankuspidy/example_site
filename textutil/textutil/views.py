# This file is created by me-- Nitikesh
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')


def analyze(request):
    djtext = request.POST.get('text','default')
    djtext1 = request.POST.get('removepunc','off')
    djtext2 = request.POST.get('caps','off')
    djtext3 = request.POST.get('charcount','off')

   # print(djtext)

    #if(first_name == 'on' and last_name == 'on' and e_mail == 'on' and pwd == 'on'):
    #params2 = {'first_name':first_name,'last_name':last_name,'e_mail': e_mail,'passwd':pwd}
    #return render(request,'analyze.html',params2)




    #analyzed = djtext
    analyzed = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


    if(djtext1 == 'on'):


       # str = []
        count = 0
        for char in djtext:


            if char not in punctuations:
                #str.append(char)         Why it is appending  carriage return
                analyzed += char
                #count += 1


        #print(analyzed)
        #print(str)
       # print(type(analyzed))
        #print(count)

        #params = {'purpose': 'Your typed sentence is: ','purpose1':'After removing punctuation: ','prev_punc':djtext,'analyzed_text': analyzed}
        #analyzed = djtext
        #djtext = analyzed
        params = {'purpose': 'Your typed sentence is: ','purpose1':'After removing punctuation: ','prev_punc':djtext,'analyzed_text': analyzed}

        return render(request,'analyze.html',params)

    if(djtext2 == 'on'):
        analyzed = ""
        for char in djtext:
            analyzed += char.upper()

        djtext = analyzed
        params = {'purpose': 'Your typed sentence is: ','purpose1':'After capitalization: ','prev_punc':djtext,'analyzed_text':analyzed}

        return render(request, 'analyze.html',params)

    if(djtext3 == 'on'):
        analyzed = len(djtext)
        params = {'purpose': 'Your typed sentence is: ', 'purpose1': 'Number of characters: ', 'prev_punc': djtext,
                  'analyzed_text': analyzed}
        #djtext = analyzed
        return render(request, 'analyze.html', params)
    if(djtext1 != 'on' and djtext2 != 'on' and djtext3 != 'on'):
        params = {'purpose': 'Your typed sentence is: ', 'purpose1': 'Oops! something went wrong','prev_punc': djtext,'analyzed_text':'Oops something went wrong'}


    return render(request, 'analyze.html', params)







#def capfirst(request):
 #   return HttpResponse('''<h1>Hey me from capitalize first</h1>''')


#def newlineremove(request):
 #   return HttpResponse('''<h1>Hey me from newline remove</h1>''')


#def spaceremove(request):
 #   return HttpResponse('''<h1>Hey me from space remove</h1>''')

#def charcount(request):
 #   return HttpResponse('''<h1>Hey me from charcount</h1>''')


