from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, Http404
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    return render(request, 'index.html')


def seleccion(request):
	return render(request, 'seleccion.html')


def jugar(request):

	QuizUser, created = QuizUsuario.objects.get_or_create(usuario=request.user)

	if request.method == 'POST':
		pregunta_pk = request.POST.get('pregunta_pk')
		pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
		respuesta_pk = request.POST.get('respuesta_pk')

		try:
			opcion_selecionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
		except ObjectDoesNotExist:
			raise Http404

		QuizUser.validar_intento(pregunta_respondida, opcion_selecionada)

		return redirect('jugar')
	else:
		pregunta = QuizUser.obtener_nuevas_preguntas()
		if pregunta is not None:
			QuizUser.crear_intentos(pregunta)

		context = {
			'pregunta':pregunta
		}

	return render(request, 'jugar.html', context)


def resultado_pregunta(request, pregunta_respondida_pk):
	respondida = get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

	context = {
		'respondida':respondida
	}
	return render(request, 'resultados.html', context)


def registro(request):
    if request.method == 'GET':
        return render(request, 'registrar.html', {'form': UserCreationForm})
    else:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if not username or not password1 or not password2:
            return render(request, 'registrar.html', {'form': UserCreationForm, 'error': 'Por favor, complete todos los campos'})

        if password1 == password2:
            try:
                user = User.objects.create_user(username=username, password=password1)
                user.save()
                login(request, user)
                return redirect('seleccion')
            except IntegrityError:
                return render(request, 'registrar.html', {'form': UserCreationForm, 'error': 'El usuario ya existe'})
        else:
            return render(request, 'registrar.html', {'form': UserCreationForm, 'error': 'Las contraseñas no coinciden'})

def salida(request):
    logout(request)
    return redirect('index')


def ingreso(request):
    if request.method == 'GET':
        return render(request, 'iniciar.html',{'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'iniciar.html', {'form': AuthenticationForm, 'error': 'Usuario o contraseña incorrectos'})
        else:
            login(request, user)
            return redirect('seleccion')


def list_irregulares(_request):
     irregulares=list(Irregular.objects.values())
     data={'irregulares':irregulares}
     return JsonResponse(data)



def list_adjetivos(_request):
     adjetivos=list(Adjetivo.objects.values())
     data={'adjetivos':adjetivos}
     return JsonResponse(data)


def puntajes(request):
	total_usaurios_quiz = QuizUsuario.objects.order_by('-puntaje_total')[:10]
	contador = total_usaurios_quiz.count()

	context = {

		'usuario_quiz':total_usaurios_quiz,
		'contar_user':contador
	}

	return render(request, 'puntajes.html', context)

def queEsregularesQuesEs1_5(request):
    pruebas_regulares = Prueba_regular.objects.all()
    return render(request, 'QueEs/regularesQuesEs1_5.html', {'pruebas_regulares': pruebas_regulares})


def indexverbos(request):
     return render(request, 'opciones/indexverbos.html')

def comparativosSuperlativos(request):
     return render(request, 'opciones/comparativosSuperlativos.html')

def pasadoQueEs(request):
     return render(request, 'QueEs/pasadoQueEs.html')

def presente(request):
     return render(request, 'opciones/presente.html')

def futuro(request):
     return render(request, 'opciones/futuro.html')

def regularesQuesEs(request):
     return render(request, 'QueEs/regularesQuesEs.html')

def irregularesQuesEs(request):
     irregulares= Irregular.objects.all()
     return render(request, 'QueEs/irregularesQuesEs.html', {'irregulares': irregulares})

def verboRegular(request):
     return render(request, 'ejemplos/verboRegular.html')

def regularesQuesEs2(request):
     return render(request, 'QueEs/regularesQuesEs2.html')

def verboIrregulares(request):
     return render(request, 'ejemplos/verboIrregulares.html')

def irregularesQuesEs2(request):
     return render(request, 'QueEs/irregularesQuesEs2.html')

def comparativosQuesEs(request):
     return render(request, 'QueEs/comparativosQueEs.html')

def superlativosQueEs(request):
     return render(request, 'QueEs/superlativosQueEs.html')

def ejemplossuperlativos(request):
     return render(request, 'ejemplos/superlativos.html')

def ejemploscomparativos(request):
     return render(request, 'ejemplos/comparativos.html')

def opcionespasado(request):
     return render(request, 'opciones/pasado.html')

def queEspasadoSimpleQueEs(request):
     tiempos_verbales = tiempoverbal.objects.all()
     return render(request, 'QueEs/pasadoSimpleQueEs.html', {'tiempos_verbales': tiempos_verbales} )

#def queEsregularesQuesEs1_5(request):
    #pruebas_regulares = Prueba_regular.objects.all()
    #return render(request, 'QueEs/regularesQuesEs1_5.html', {'pruebas_regulares': pruebas_regulares})

def queEspasadoContinuoQueEs(request):
     return render(request, 'QueEs/pasadoContinuoQueEs.html')

def queEspasadoPerfectoSimpleQueEs(request):
     tiempos_verbales = tiempoverbal.objects.all()
     return render(request, 'QueEs/pasadoPerfectoSimpleQueEs.html', {'tiempos_verbales': tiempos_verbales} )

def queEspasadoPerfectoContinuoQueEs(request):
     return render(request, 'QueEs/pasadoPerfectoContinuoQueEs.html')

def queEspasadoCondicionalPerfectoQueEs(request):
     return render(request, 'QueEs/pasadoCondicionalPerfectoQueEs.html')

def queEspasadoCondicionalPerfectoContinuoQueEs(request):
     return render(request, 'QueEs/pasadoCondicionalPerfectoContinuoQueEs.html')

def ejemplospasadoSimple(request):
     return render(request, 'ejemplos/pasadoSimple.html')

def ejemplospasadoContinuo(request):
     tiempos_verbales = tiempoverbal.objects.all()
     return render(request, 'ejemplos/pasadoContinuo.html', {'tiempos_verbales': tiempos_verbales} )

def ejemplospasadoPerfectoSimple(request):
     tiempos_verbales = tiempoverbal.objects.all()
     return render(request, 'ejemplos/pasadoPerfectoSimple.html' , {'tiempos_verbales': tiempos_verbales} )

def ejemplospasadoPerfectoContinuo(request):
     tiempos_verbales = tiempoverbal.objects.all()
     return render(request, 'ejemplos/pasadoPerfectoContinuo.html' , {'tiempos_verbales': tiempos_verbales})

def ejemplospasadoCondicionalPerfecto(request):
     tiempos_verbales = tiempoverbal.objects.all()
     return render(request, 'ejemplos/pasadoCondicionalPerfecto.html' , {'tiempos_verbales': tiempos_verbales})

def ejemplospasadoCondicionalPerfectoContinuo(request):
     tiempos_verbales = tiempoverbal.objects.all()
     return render(request, 'ejemplos/pasadoCondicionalPerfectoContinuo.html', {'tiempos_verbales': tiempos_verbales})

def queEspresenteSimpleQueEs(request):
     return render(request, 'QueEs/presenteSimpleQueEs.html')

def queEspresenteContinuoQueEs(request):
     tiempos_verbales = tiempoverbal.objects.all()
     return render(request, 'QueEs/presenteContinuoQueEs.html', {'tiempos_verbales': tiempos_verbales})

def queEspresentePerfectoQueEs(request):
     tiempos_verbales = tiempoverbal.objects.all()
     return render(request, 'QueEs/presentePerfectoQueEs.html',  {'tiempos_verbales': tiempos_verbales})

def queEspresentePerfectoContinuoQueEs(request):
     tiempos_verbales = tiempoverbal.objects.all()
     return render(request, 'QueEs/presentePerfectoContinuoQueEs.html' ,  {'tiempos_verbales': tiempos_verbales})

def queEspresenteCondicionalSimpleQueEs(request):
     return render(request, 'QueEs/presenteCondicionalSimpleQueEs.html')

def ejemplospresenteCondicionalSimple(request):
     return render(request, 'ejemplos/presenteCondicionalSimple.html')

def ejemplospresenteContinuo(request):
     return render(request, 'ejemplos/presenteContinuo.html')

def ejemplospresentePerfectoContinuo(request):
     return render(request, 'ejemplos/presentePerfectoContinuo.html')

def ejemplospresentePerfecto(request):

     return render(request, 'ejemplos/presentePerfecto.html')

def ejemplospresenteSimple(request):
     return render(request, 'ejemplos/presenteSimple.html')

def queEsfuturoSimpleQueEs(request):

     return render(request, 'QueEs/futuroSimpleQueEs.html')

def queEsfuturoSimple2QueEs(request):
     return render(request, 'QueEs/futuroSimple2QueEs.html')

def queEsfuturoContinuoQueEs(request):
     tiempos_verbales = tiempoverbal.objects.all()
     return render(request, 'QueEs/futuroContinuoQueEs.html',  {'tiempos_verbales': tiempos_verbales})

def queEsfuturoPerfectoQueEs(request):
     tiempos_verbales = tiempoverbal.objects.all()
     return render(request, 'QueEs/futuroPerfectoQueEs.html',  {'tiempos_verbales': tiempos_verbales})

def queEsfuturoPerfectoContinuoQueEs(request):
     tiempos_verbales = tiempoverbal.objects.all()
     return render(request, 'QueEs/futuroPerfectoContinuoQueEs.html',  {'tiempos_verbales': tiempos_verbales})

def ejemplosfuturoSimple(request):
     return render(request, 'ejemplos/futuroSimple.html')

def ejemplosfuturoSimple2(request):
     return render(request,'ejemplos/futuroSimple2.html')

def ejemplosfuturoContinuo(request):
     return render(request, 'ejemplos/futuroContinuo.html')

def ejemplosfuturoPerfecto(request):
     return render(request, 'ejemplos/futuroPerfecto.html')

def ejemplosfuturoPerfectoContinuo(request):
     return render(request, 'ejemplos/futuroPerfectoContinuo.html')

def ejemplosfuturocontinuo(request):
     return render(request, 'ejemplosfuturocontinuo.html')

