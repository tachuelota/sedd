# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from proyecto.app.api.handlers import ServicioValidadorHandler 
from proyecto.app.api.handlers import PeriodoEvaluacionHandler
from proyecto.app.api.handlers import PeriodoAcademicoHandler 
from proyecto.app.api.handlers import ResultadosHandler 
from proyecto.app.api.handlers import ParametrosHandler
from proyecto.app.api.handlers import UsuarioHandler 

authapi = HttpBasicAuthentication(realm='seddrealm')

periodo_academico_handler = Resource(PeriodoAcademicoHandler)
periodo_evaluacion_handler = Resource(PeriodoEvaluacionHandler, authentication=authapi)
servicio_validador_handler = Resource(ServicioValidadorHandler, authentication=authapi)
resultados_handler = Resource(ResultadosHandler, authentication=authapi)
parametros_handler = Resource(ParametrosHandler)
usuario_handler = Resource(UsuarioHandler, authentication=authapi)


urlpatterns = patterns('',
    url(r'^periodos_academicos/', periodo_academico_handler),
    url(r'^periodos_evaluacion/', periodo_evaluacion_handler),
    url(r'^verificar/(?P<id_periodo_evaluacion>\d{1,2})/(?P<dni>\w{7,})/', servicio_validador_handler),
    url(r'^resultados/(?P<id_periodo_evaluacion>\d{1,2})/(?P<dni>\w{7,})/', resultados_handler),
    url(r'^parametros/', parametros_handler),
    url(r'^docentes/actualizar', usuario_handler),
    ###url(r'^estudiantes/actualizar', usuario_handler),
)
