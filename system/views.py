from base64 import urlsafe_b64decode
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.utils.encoding import force_bytes, force_str
from system.models import Contact, Crimelist, Complainlist,User
from . tokens import generate_token
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):

    crime_c = Crimelist.objects.count()
    comp_c = Complainlist.objects.count()

    return render(request, "index.html", {'crime_rec': crime_c, 'comp_rec':comp_c, 'nactive': 'home'})

# ----------------------------------------------------------------------------------------------
# validation
def validateUser(username , email, badge_no, password, password2):
    error_message = None
    if User.objects.filter(username=username):
        error_message = "Username already exits"
        
    if User.objects.filter(email=email):
        error_message = "Email aready exits"

    if len(username)>30:
        error_message = "Username must be under 30 characters"

    if User.objects.filter(badge_no=badge_no):
        error_message = "Badge number is invalid"

    if password != password2:
        error_message = "Password does not match"

    if not username.isalnum():
        error_message = "Username must be alpha-numeric"
    
    return error_message


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        full_name = request.POST['fullname']
        email = request.POST['email']
        address = request.POST['address']
        badge_no = request.POST['badge_no']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        myuser = User(username=username,full_name=full_name, email=email, address=address, badge_no=badge_no, password=password)
        
        error_message = validateUser(username , email, badge_no, password, password2)


        if not error_message:
            myuser.password = make_password(myuser.password)
            myuser.save()

            messages.success(request, "User successfully registered")

            return redirect('signin')
    else:
        error_message = ''

    return render(request, "authentication/signup.html", {'error': error_message})

# ----------------------------------------------------------------------------------------------

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')    

        myuser = authenticate(request, username=username, password=password)

        if myuser is not None:
            login(request, myuser)
            return redirect('home')
        else:
            error_message = "Username or password is incorrect"

    else:
        error_message = ''

    return render(request, "authentication/signin.html", {'error': error_message})


# ----------------------------------------------------------------------------------------------

def profile(request):
    return render(request, "authentication/profile.html")

# ----------------------------------------------------------------------------------------------

def signout(request):
    logout(request)

    return redirect('home')

# ----------------------------------------------------------------------------------------------

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_b64decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'authentication/activation_failed.html')

# --------------------------------------------------------------------------------------------------

def crime(request):
    if request.method == "POST":
        # imp info
        title = request.POST.get('inputCrime')
        city = request.POST.get('addCity')
        street = request.POST.get('addStreet')
        description = request.POST.get('crimeDesc')
        criminalDesc = request.POST.get('criminalDesc')

        # personal info
        reported_by = request.POST.get('name')
        email = request.POST.get('inputEmail')
        phone = request.POST.get('addPhone')

        crime_rec = Crimelist(title=title, city=city, street=street, description=description, criminalDesc=criminalDesc, reported_by=reported_by, email=email, phone = phone)
        crime_rec.save()

    return render(request, 'crime.html', {'nactive': 'crime'})
# --------------------------------------------------------------------------------------------------

def complain(request):
    if request.method == "POST":
        # imp info
        title = request.POST.get('complain')
        city = request.POST.get('addCity')
        street = request.POST.get('addStreet')
        description = request.POST.get('complainDesc')
        # personal info
        reported_by = request.POST.get('name')
        email = request.POST.get('inputEmail')
        phone = request.POST.get('addPhone')

        comp_rec = Complainlist(title=title, city=city, street=street, description=description, reported_by=reported_by, email=email, phone = phone)
        comp_rec.save()

    return render(request, 'complain.html', {'nactive': 'complain'})

# --------------------------------------------------------------------------------------------------

def about(request):
    return render(request, 'about.html', {'nactive': 'about'})

# --------------------------------------------------------------------------------------------------
@login_required(login_url='/signin')
def records(request):
    crime_rec = Crimelist.objects.filter()

    comp_rec = Complainlist.objects.filter()

    return render(request, "records.html", {'crime_rec': crime_rec, 'comp_rec':comp_rec, 'nactive': 'records'})


# --------------------------------------------------------------------------------------------------

def crimedetails(request, id):
    crime = Crimelist.objects.get(id=id)

    if request.method == 'POST':
        Crimelist.objects.filter(id=id).update(status='DONE.')
        user = User.objects.get(id=id)

        return render(request, 'details.html',  {'data':crime, 'user': user, 'nactive': 'details'})

    return render(request, 'details.html',  {'data':crime, 'nactive': 'details'})

def compdetails(request, id):
    complain = Complainlist.objects.get(id=id)

    if request.method == 'POST':
        Complainlist.objects.filter(id=id).update(status='DONE.')

        user = User.objects.get(id=id)

        return render(request, 'details.html',  {'data':complain, 'user': user, 'nactive': 'details'})
    
    return render(request, 'details.html',  {'data':complain, 'nactive': 'details'})
    
# --------------------------------------------------------------------------------------------------

def what_report(request):
    return render(request, 'what-report.html', {'nactive': 'what-report'})

# --------------------------------------------------------------------------------------------------

def contact(request):
    if request.method == "POST":
        name = request.POST.get('yourname')
        email = request.POST.get('youremail')
        subject = request.POST.get('subject')
        conDesc = request.POST.get('yourmessgae')

        cont_rec = Contact(name = name, email = email, subject = subject, conDesc = conDesc)
        cont_rec.save()

    return render(request, 'contact.html', {'nactive': 'contact'})
# --------------------------------------------------------------------------------------------------
