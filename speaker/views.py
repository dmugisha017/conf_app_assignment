from django.shortcuts import render

# Create your views here.
def Home(request):
    speaker={
        "Person1":{
        "id":1,
        "names":"yves",
        "Bios":"Developer",
        "Email":"yves@exmple.com",
        "Phone":"0788517392"
        },
        "Persnal2":{
        "id":2,
        "names":"Desire",
        "Bios":"Engeenger",
        "Email":"desire@exmple.com",
        "Phone":"07885175692"
        },
         "Persnal3":{
        "id":3,
        "names":"Eric",
        "Bios":"Designer",
        "Email":"kurikyimana@exmple.com",
        "Phone":"0782517392"
        },
           "Persnal4":{
        "id":4,
        "names":"abijuru",
        "Bios":"techinician",
        "Email":"abijuru@exmple.com",
        "Phone":"0788517392"
        },
          
        "Persnal5":{
        "id":5,
        "names":"Maniriho sandrine",
        "Bios":"Software developer",
        "Email":"sandrine@exmple.com",
        "Phone":"0788517395"
        },
          
            }
    return render(request,'index.html',{'data':speaker})

def Form(request):
    return render(request,"Form.html")
def Specific(request,id):
    speaker={
        1:{
        "id":1,
        "names":"yves",
        "Bios":"Developer",
        "Email":"yves@exmple.com",
        "Phone":"0788517392"
        },
        2:{
        "id":2,
        "names":"Desire",
        "Bios":"Engeenger",
        "Email":"desire@exmple.com",
        "Phone":"07885175692"
        },
         3:{
        "id":3,
        "names":"Eric",
        "Bios":"Designer",
        "Email":"kurikyimana@exmple.com",
        "Phone":"0782517392"
        },
           4:{
        "id":4,
        "names":"abijuru",
        "Bios":"techinician",
        "Email":"abijuru@exmple.com",
        "Phone":"0788517392"
        },
          
        5:{
        "id":5,
        "names":"Dennis",
        "Bios":"Software developer",
        "Email":"dennis@exmple.com",
        "Phone":"0788517395"
        },
          
            }
   
    data=speaker.get(id)
    # person_id = "Person1"
    # id_value = speaker[person_id]["id"]
  
    return render(request,'specific.html',{'person':data})
def Update(request,id):
    speaker={
        1:{
        "id":1,
        "names":"yves",
        "Bios":"Developer",
        "Email":"yves@exmple.com",
        "Phone":"0788517392"
        },
        2:{
        "id":2,
        "names":"Desire",
        "Bios":"Engeenger",
        "Email":"desire@exmple.com",
        "Phone":"07885175692"
        },
         3:{
        "id":3,
        "names":"Eric",
        "Bios":"Designer",
        "Email":"kurikyimana@exmple.com",
        "Phone":"0782517392"
        },
           4:{
        "id":4,
        "names":"abijuru",
        "Bios":"techinician",
        "Email":"abijuru@exmple.com",
        "Phone":"0788517392"
        },
          
        5:{
        "id":5,
        "names":"Dennis",
        "Bios":"Software developer",
        "Email":"dennis@exmple.com",
        "Phone":"0788517395"
        },
          
            }
   
    data=speaker.get(id)
    return render(request,'update.html',{'person':data})
def Delete(request,id):
    speaker={
        1:{
        "id":1,
        "names":"yves",
        "Bios":"Developer",
        "Email":"yves@exmple.com",
        "Phone":"0788517392"
        },
        2:{
        "id":2,
        "names":"Desire",
        "Bios":"Engeenger",
        "Email":"desire@exmple.com",
        "Phone":"07885175692"
        },
         3:{
        "id":3,
        "names":"Eric",
        "Bios":"Designer",
        "Email":"kurikyimana@exmple.com",
        "Phone":"0782517392"
        },
           4:{
        "id":4,
        "names":"abijuru",
        "Bios":"techinician",
        "Email":"abijuru@exmple.com",
        "Phone":"0788517392"
        },
          
        5:{
        "id":5,
        "names":"Dennis",
        "Bios":"Software developer",
        "Email":"dennis@exmple.com",
        "Phone":"0788517395"
        },
          
            }
   
    datas=speaker.get(id)
    return render(request,'delete.html',{'person':datas})