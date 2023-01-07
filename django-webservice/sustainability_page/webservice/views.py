import orjson as json

from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from webservice.models import SusPageUser

# TODO: Figure out why CSRF is not functioning as expected.
#       It might be a conflict between corsheaders.middleware.CorsMiddleware and django.middleware.csrf.CsrfViewMiddleware
@csrf_exempt
def signup(request) -> HttpResponse:
    if request.method == 'POST':
        try:
            data = json.loads(request.body)['data']
        except KeyError:
            return JsonResponse({}, status=400)

        username = data.get('username', None)
        if username is None:
            return JsonResponse({'errors': ['username']}, status=401)

        email = data.get('email', None)
        if email is None:
            return JsonResponse({'errors': ['email']}, status=401)

        if SusPageUser.objects.filter(username=username).exists():
            return JsonResponse({'errors': ['username']}, status=401)

        if SusPageUser.objects.filter(email=email).exists():
            return JsonResponse({'errors': ['email']}, status=401)

        user = SusPageUser.objects.create(username=username, email=email)
        password = get_user_model().objects.make_random_password()
        user.set_password(password)
        user.newsletterAgree = True
        user.save()
        user = authenticate(email=user.email, password=password)
        login(request, user)

        return JsonResponse({}, status=201)

    return JsonResponse({}, status=405)

def signup_username_check(request) -> HttpResponse:
    if request.method == 'GET':
        username = request.GET.get('username', None)
        if username is None:
            return JsonResponse({'errors': ['username']}, status=400)

        if SusPageUser.objects.filter(username=username).exists():
            return JsonResponse({}, status=400)

        else:
            return JsonResponse({'errors': ['username']}, status=200)

    return JsonResponse({}, status=405)

@csrf_exempt
@login_required
def signup_password(request) -> HttpResponse:
    if request.method == 'POST':
        try:
            data = json.loads(request.body)['data']
        except KeyError:
            return JsonResponse({}, status=400)

        password = data.get('password', None)
        if password is None:
            return JsonResponse({'errors': ['password']}, status=400)

        # Recheck password length and capitalization
        if len(password) < 16:
            return JsonResponse({'errors': ['password']}, status=400)

        if any([letter.isupper() for letter in password]) is False:
            return JsonResponse({'errors': ['password']}, status=400)

        
        user = request.user
        user.set_password(password)
        user.save()
        login(request, user)
        return JsonResponse({}, status=200)

    return JsonResponse({}, status=405)

@csrf_exempt
@login_required
def onboard(request) -> HttpResponse:
    if request.method == 'POST':
        try:
            data = json.loads(request.body)['data']
        except KeyError:
            return JsonResponse({}, status=400)
                
        name = data.get('name', None)
        if name is None:
            return JsonResponse({'errors': ['name']}, status=400)

        industry = data.get('industry', None)
        if industry is None:
            return JsonResponse({'errors': ['industry']}, status=400)

        user = request.user
        user.business_name = name
        user.industry = industry
        user.save()
        login(request, user)
        return JsonResponse({}, status=201)
    
    return JsonResponse({}, status=405)