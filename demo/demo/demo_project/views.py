from django import forms
from django.shortcuts import render, redirect
from demo.demo_project.models import Profile, Cars, Accessories


class Form(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', "last_name", 'email', 'password']


def cart_count():
    profile = get_profile()
    count = profile.favourite_cars.count() + profile.favourite_accessories.count()
    return count


def get_profile():
    profile = Profile.objects.filter(logged=1)
    if profile:
        return profile[0]
    return False


def show_home_page(request):
    profile = get_profile()
    cart = False
    if profile:
        if profile.logged:
            request.session['cart_count'] = cart_count()

            if request.session['cart_count'] > 0:
                cart = True
    if not cart:
        request.session['cart_count'] = 0

    return render(request, "home.html", {'title': "CarsWorld"})


def show_profile(request):
    is_logged = False
    profile = get_profile()

    if profile:
        if profile.logged:
            is_logged = True

    if request.method == "POST":
        print(request)

    context = {
        "is_logged": is_logged,
        "profile": profile,
        "title": 'Profile Page',
    }

    return render(request, "profile.html", context)


def register_user(request):
    if request.method == "POST":
        form = Form(request.POST)

        if form.is_valid():
            email = request.POST.get('email')
            emails = Profile.objects.values("email")

            for el in emails:
                if el["email"] == email:
                    error = "Already have user with this email! Please Login"
                    return render(request, "register.html", {"error": error})

            new_profile = Profile(**form.cleaned_data)
            new_profile.save()
            return redirect("profile")
    else:
        return render(request, "register.html", {'title': "Register Page"})


def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        profile = Profile.objects.get(email=email)

        have_account = False
        if profile:
            password = request.POST.get("password")
            if profile.password == password:
                profile.logged = True
                have_account = True
                profile.save()
                return redirect("home")
        if not have_account:
            return render(request, "profile.html", {"message": "Incorrect email or password!", 'title': "Profile Page"})
    else:
        return render(request, "profile.html")


def log_out(request):
    profile = get_profile()
    profile.logged = False
    profile.save()
    return redirect("home")


def add_img(request):
    img = request.FILES["img"]
    profile = get_profile()
    profile.img = img
    profile.save()
    return redirect("profile")


def show_cars(request):
    mercedes_cars = Cars.objects.filter(brand="Mercedes")
    bmw_cars = Cars.objects.filter(brand="BMW")
    toyota_cars = Cars.objects.filter(brand="Toyota")
    audi_cars = Cars.objects.filter(brand="Audi")

    context = {
        "mercedes_cars": mercedes_cars,
        "bmw_cars": bmw_cars,
        "toyota_cars": toyota_cars,
        "audi_cars": audi_cars,
        'title': "Cars Page",
    }
    return render(request, "cars.html", context)


def add_car_to_cart(request):
    profile = get_profile()
    not_logged = True

    if profile:
        if profile.logged:
            not_logged = False
            request.session['not_logged'] = False

            car_id = request.POST.get("car_id")
            car = Cars.objects.get(id=car_id)
            profile.favourite_cars.add(car)

            profile.save()

            return redirect("cart")
    if not_logged:
        request.session['not_logged'] = True
        return redirect("profile")


def show_accessories(request):
    accessories = Accessories.objects.all()
    context = {
        "accessories": accessories,
        'title': 'Accessories Page',
    }
    return render(request, "accessories.html", context)


def add_accessory_to_cart(request):
    profile = get_profile()
    not_logged = True

    if profile:
        if profile.logged:
            not_logged = False
            request.session['not_logged'] = False
            id = request.POST.get("id")
            accessory = Accessories.objects.get(id=id)
            profile.favourite_accessories.add(accessory)
            profile.save()
            return redirect("cart")
    if not_logged:
        request.session['not_logged'] = True
        return redirect("profile")


def show_cart(request):
    profile = get_profile()
    items_in_cart = []
    favourite_cars = profile.favourite_cars.all()
    favourite_accessories = profile.favourite_accessories.all()
    items_in_cart += favourite_accessories
    items_in_cart += favourite_cars
    total_price = 0
    request.session['cart_count'] = cart_count()

    for item in items_in_cart:
        total_price += item.price

    context = {
        "favourite_cars": favourite_cars,
        "favourite_accessories": favourite_accessories,
        "total": total_price,
        'title': "Cart Page",
    }
    return render(request, "cart.html", context)


def delete_item_from_cart(request, id, type):
    profile = get_profile()

    if type == "car":
        object = Cars.objects.get(id=id)
        profile.favourite_cars.remove(object)
    else:
        object = Accessories.objects.get(id=id)
        profile.favourite_accessories.remove(object)

    profile.save()
    request.session["cart_count"] = cart_count()
    return redirect("cart")


def edit_profile(request):
    if request.method == "GET":
        profile = get_profile()

        context = {
            "profile": profile,
            "title": 'Edit Page',
        }
        return render(request, 'edit.html', context)
    else:
        img = request.FILES["img"]
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        email = request.POST.get("email")

        profile = get_profile()
        profile.img = img
        profile.first_Name = firstName
        profile.last_Name = lastName
        profile.email = email

        profile.save()

        return redirect('profile')


def successful_order(request):
    if request.method == "GET":
        return render(request, 'successfulOrder.html')
    else:
        profile = get_profile()

        profile.favourite_cars.clear()
        profile.favourite_accessories.clear()
        profile.save()

        request.session['cart_count'] = 0
        return redirect('cars')

