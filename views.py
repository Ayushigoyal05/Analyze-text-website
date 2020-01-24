from django.http import HttpResponse
from django.shortcuts import render


def index3(request):
	return render(request,'index3.html')
 	
def analyze(request):
    djtext = request.GET.get('text', 'default')
    print(djtext)

    
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    charcount=request.GET.get('charcount','off')

    
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r": 
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)
    if (charcount=="on"):
    	analyzed=0
    	for char in djtext:
    		if (char==" "):
    		    pass
    		else:
    			analyzed=analyzed+1
    	params = {'purpose': 'no of characters', 'analyzed_text': analyzed}
    	#return render(request, 'analyze.html', params)


    if(charcount!="on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on" and removepunc!="on"):
        return HttpResponse("Error")
    return render(request, 'analyze.html', params)

 	