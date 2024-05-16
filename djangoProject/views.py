from django.shortcuts import render
from django.core.cache import cache
from . import program_work


def base(request):
    return render(request, "base.html")


def answers(request):
    terms = program_work.get_terms_for_table()
    return render(request, "results.html", context={"terms": terms})


def wishes(request):
    terms = program_work.get_wishes_for_table()
    return render(request, "wishes.html", context={"terms": terms})


def test(request):
    return render(request, "test.html")


def add_wishes(request):
    return render(request, "add_wish.html")


def test_result_personal(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        user_email = request.POST.get("email", "")
        balls = 0
        option1 = request.POST.get('group1')
        option2 = request.POST.get('group2')
        option3 = request.POST.get('group3')
        option4 = request.POST.get('group4')
        option5 = request.POST.get('group5')
        option6 = request.POST.get('group6')
        option7 = request.POST.get('group7')
        option8 = request.POST.get('group8')
        option9 = request.POST.get('group9')
        option10 = request.POST.get('group10')
        context = {"user": user_name}
        if len(user_name) == 0:
            context["success"] = False
            context["comment"] = "Имя должно быть не пустым"
        elif len(user_email) == 0:
            context["success"] = False
            context["comment"] = "Email должен быть не пустым"
        elif option1 is None or option2 is None or option3 is None or option4 is None or option5 is None or option6 is None or option7 is None or option8 is None or option9 is None or option10 is None:
            context["success"] = False
            context["comment"] = "Отметьте все поля"
        else:
            context["success"] = True
            context["comment"] = "Тест успешно завершен"
            if option1 == "option11":
                balls += 1
            if option2 == 'option22':
                balls += 1
            if option3 == 'option33':
                balls += 1
            if option4 == 'option42':
                balls += 1
            if option5 == 'option53':
                balls += 1
            if option6 == 'option61':
                balls += 1
            if option7 == 'option72':
                balls += 1
            if option8 == 'option81':
                balls += 1
            if option9 == 'option92':
                balls += 1
            if option10 == 'option103':
                balls += 1
            program_work.write_info(user_name, user_email, balls)
        if context["success"]:
            context["success-title"] = ""
        context["balls"] = balls
        return render(request, "test_result_personal.html", context)
    else:
        test(request)


def show_results(request):
    stats = program_work.get_info_stats()
    return render(request, "statistic.html", stats)


def wishes_result_personal(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        user_email = request.POST.get("email", "")
        wish = request.POST.get("wish_for_prj", "").replace(";", ",")
        context = {"user": user_name}
        if len(user_name) == 0:
            context["success"] = False
            context["comment"] = "Имя должно быть не пустым"
        elif len(user_email) == 0:
            context["success"] = False
            context["comment"] = "Email должен быть не пустым"
        elif len(wish) == 0:
            context["success"] = False
            context["comment"] = "Добавьте пожелание"
        else:
            context["success"] = True
            context["comment"] = "Пожелание успешно добавлено"
            program_work.write_wish(user_name, user_email, wish)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "wish_result_personal.html", context)
    else:
        add_wishes(request)
