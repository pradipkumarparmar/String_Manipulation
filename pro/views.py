from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def index(request):
    reversed_sentence = None
    if request.method == "POST":
        name = request.POST["pradip"]
       #print(name)
        word_list = name.split('.')

        print(word_list)

        #rev= word_list[:: 2]

        reversed_list = word_list[:: -1]

        reversed_sentence = " ".join(reversed_list)
    
        print(reversed_sentence)
        
        
#             s = 'you shall.not pass.hello'

#             r = ' '.join(reversed(s.split('.')))

#             print(r)



    return render(request,'index.html',{'getvalue':reversed_sentence})


    
