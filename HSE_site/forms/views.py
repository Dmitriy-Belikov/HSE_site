from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView
from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail



def forms(request):
    forms = Articles.objects.all()[::-1]
    paginator = Paginator(forms, 10)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    return render(request, 'forms/forms.html', {'page_obj': page_obj})



class ObservationMap(DetailView):
    model = Articles
    template_name = 'forms/observation_map.html'
    context_object_name = 'form'


def send_email(id_card, email, formm):
    data = f'''
                Добрый день!
                Ваша {formm} зарегестрирована с номером {id_card}.
                '''

    try:
        send_mail(f'{formm} № {id_card}', data, "HSE_Site", [email], fail_silently=True)
        print(f'Письмо отправлено {formm} № {id_card} пользователю {email}' )
    except:
        print('Письмо не отправлено')

def create(request):

    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)



        if form.is_valid():
            form.save()

            cards = Articles.objects.all()[::-1]
            id_card = ''
            email = ''
            formm = ''
            for i in cards:
                id_card = i.id
                email = i.email
                formm = i.form
                break
            try:
                send_email(id_card, email, formm)
            except:
                print('Error')
                pass
            return redirect('forms/'+str(id_card))

        else:
            print(form.errors)
            error = 'Ошибка заполнения'


    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'forms/create.html', data)





