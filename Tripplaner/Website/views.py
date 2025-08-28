from django.shortcuts import render ,redirect
from django.http import HttpResponse
import mysql.connector as mc
from django.contrib import messages


con = mc.connect(host = 'localhost', user = 'root', password = 'root', db = 'trip_userdata')
con_data = mc.connect(host = 'localhost', user = 'root', password = 'root', db = 'triplanner')

# Create your views here.
timeout = 0
username = ""
state_name = ""
def index(request):
    global timeout
    data_user = {
        "username":username,
        "timeout":timeout
    }
    return render(request ,"index.html",{"data_user":data_user})
def login(request):
    global timeout 
    global username
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username ,password)
        my = con.cursor()
        my.execute("select username from signup;")
        details = my.fetchall()
        for user in details:
            if username in user:
                my = con.cursor()
                my.execute("select password from signup where username = '{}';".format(username))
                saved_password = my.fetchone()
                print(saved_password)
                if str(password) == saved_password[0] :
                    timeout = 1
                    data_user = {
                        "username":username,
                        "timeout":timeout
                    }
                    return render(request , "index.html" , {"data_user":data_user} )
                else:
                    messages.success(request, 'The password is incorrect')
                    return render(request , "index.html" )

    else:
        return render(request,"login.html")
    
def signout(request):
    global timeout 
    timeout = 0
    data_user = {
        "timeout":timeout
    }
    messages.success(request, 'logged out successfully')
    return render(request,"index.html",{"data_user":data_user})

def signup(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        con_password = request.POST.get('con_password')
        print(fname,lname,email,username,password,con_password)
        my = con.cursor()
        my.execute("insert into signup values('{}','{}','{}','{}','{}');".format(username,password,email,
        fname,lname))
        con.commit()
        return redirect('login')
    else:
        return render(request,"signup.html")

def choose(request):
    indian_states = {
    "Andhra Pradesh": "Known for its rich cultural heritage and historical landmarks.",
    "Arunachal Pradesh": "Home to breathtaking Himalayan landscapes and diverse indigenous cultures.",
    "Assam": "Famous for tea plantations and the mighty Brahmaputra River.",
    "Bihar": "Renowned for its ancient history and religious significance.",
    "Chhattisgarh": "Known for its lush forests and tribal communities.",
    "Goa": "A popular tourist destination with beautiful beaches and vibrant nightlife.",
    "Gujarat": "The birthplace of Mahatma Gandhi and a center of trade and commerce.",
    "Haryana": "A rapidly developing state in northern India.",
    "Himachal Pradesh": "A haven for nature lovers with its picturesque mountain scenery.",
    "Jharkhand": "Abundant in mineral resources and natural beauty.",
    "Karnataka": "Home to IT hubs like Bangalore and diverse landscapes.",
    "Kerala": "Known for its backwaters, lush greenery, and Ayurvedic traditions.",
    "Madhya Pradesh": "Rich in historical sites and national parks.",
    "Maharashtra": "Economic powerhouse and cultural hub with Mumbai as its capital.",
    "Manipur": "Known for its distinct dance forms and scenic landscapes.",
    "Meghalaya": "Famous for its living root bridges and stunning waterfalls.",
    "Mizoram": "Known for its lush green hills and unique culture.",
    "Nagaland": "Diverse tribal cultures and scenic beauty.",
    "Odisha": "Home to ancient temples, vibrant art, and picturesque coastline.",
    "Punjab": "Famous for its agriculture, rich cuisine, and Sikh heritage.",
    "Rajasthan": "Land of palaces, forts, and desert landscapes.",
    "Sikkim": "A small state with stunning Himalayan scenery and Buddhist culture.",
    "Tamil Nadu": "Known for classical arts, temples, and cuisine.",
    "Telangana": "Home to Hyderabad, a major IT and business hub.",
    "Tripura": "Known for its rich history and scenic beauty.",
    "Uttar Pradesh": "India's most populous state with a wealth of historical sites.",
    "Uttarakhand": "Abundant in natural beauty and pilgrimage destinations.",
    "West Bengal": "Famous for the city of Kolkata and cultural diversity."
}
    global timeout
    global username
    global state_name
    state_name = request.GET.get("name")
    print(state_name)
    if state_name is not None:
        return redirect("display")
    else:
        return render(request, "choose.html", {"indian_states":indian_states , "timeout":timeout ,
        "username":username})
   
def display(request):
    global timeout
    global username
    global state_name

    my = con_data.cursor()
    my.execute("select searchloc from details where state = '{}' ".format(state_name))
    searchloc = my.fetchall()
    districts = []
    print(searchloc)
    for i in searchloc:
        districts.append(i[0])
    print(districts)
    days = [1,2,3,4,5,6,7]
    plan = ["Budget Traveler", "Mid-Range Traveler", "Luxury Traveler"]
    if request.method == 'POST':
        plans = request.POST.get('plan')
        district = request.POST.get('district')
        print(plans,district)
        my = con_data.cursor()
        my.execute("select description , places from details where state = '{}' and searchloc = '{}' "
        .format(state_name,district))
        place = my.fetchall()
        desc = place[0][0].replace(";",",")
        visit = place[0][1].replace(";",",")
        visit = visit.split(",")
        print(desc , visit)
        print(place)
        return render(request , "display.html" , {"desc":desc , "visit":visit , "district":district
         ,"timeout":timeout ,"username":username, "districts":districts ,"days":days ,"plan":plan})
    else:
        return render(request , "display.html", {"timeout":timeout ,"username":username, "districts"
        :districts ,"days":days ,"plan":plan})