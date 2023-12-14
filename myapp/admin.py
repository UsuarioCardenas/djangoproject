from django.contrib import admin
from .forms import ElegirInlineFormset
from .models import *

# Register your models here.

class ElegirRespuestaInLine(admin.TabularInline):
    model = ElegirRespuesta
    can_delete=False
    model= ElegirRespuesta
    max_num=ElegirRespuesta.MAXIMO_RESPUESTA
    min_num=ElegirRespuesta.MAXIMO_RESPUESTA
    formset= ElegirInlineFormset

class PreguntaAdmin(admin.ModelAdmin):
    model = Pregunta
    inlines = (ElegirRespuestaInLine, )
    list_display = ['texto' ,]
    search_fields = ['texto', 'preguntas__texto']


class PreguntasRespondidasAdmin(admin.ModelAdmin):
    list_display= ['pregunta', 'respuesta', 'correcta', 'puntaje_obtenido']

    class Meta:
        model = PreguntasRespondidas



admin.site.register(PreguntasRespondidas)
admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(ElegirRespuesta)
admin.site.register(QuizUsuario)
admin.site.register(Prueba_regular)
admin.site.register(Adjetivo)
admin.site.register(Irregular)
admin.site.register(tiempoverbal)