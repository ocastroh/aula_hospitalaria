from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Sede, Matricula, ProgresoAlumno, NotasAlumno, AntecedentesFamiliares
from .serializers import SedeSerializer, MatriculaSerializer, ProgresoAlumnoSerializer, NotasAlumnoSerializer, AntecedentesFamiliaresSerializer
from personas.models import Persona, Alumno
from personas.serializers import AlumnoSerializer, ApoderadoSerializer

@api_view(['GET', 'POST'])
def sede_list(request):
    if request.method == 'GET':
        sedes = Sede.objects.all()
        serializer = SedeSerializer(sedes, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SedeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def sede_detail(request, pk):
    try:
        sede = Sede.objects.get(pk=pk)
    except Sede.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SedeSerializer(sede)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SedeSerializer(sede, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        sede.delete()
        return Response({"mensaje": f"Sede ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)
    
@api_view(['GET', 'POST'])
def matricula_list(request):
    if request.method == 'GET':
        matriculas = Matricula.objects.all()
        respuesta = []

        serializer = MatriculaSerializer(matriculas, many=True)
        for matricula in serializer.data:
            alumno = Alumno.objects.get(pk=matricula['alumno'])
            serializer_alumno = AlumnoSerializer(alumno)
            matricula['info_alumno'] = serializer_alumno.data
            respuesta.append(matricula)
        return Response(respuesta)

    elif request.method == 'POST':
        # Extraer datos del alumno desde el JSON
        print("Datos del alumno:", request.data['info_alumno'])
        alumno_data = request.data['info_alumno']
        curso_id = request.data['curso_id']
        identificador_curso = request.data['identificador_curso']

        # Extraer datos del apoderado desde el JSON
        print("Datos del apoderado:", request.data['info_apoderado'])
        apoderado_data = request.data['info_apoderado']
        from personas.models import Apoderado
        # Buscar si el apoderado ya existe
        apoderado, created = Apoderado.objects.get_or_create(
            rut=apoderado_data['rut'],
            nombres=apoderado_data['nombres'],
            apellido_paterno=apoderado_data['apellido_paterno'],
            apellido_materno=apoderado_data['apellido_materno'],
            fecha_nacimiento=apoderado_data['fecha_nacimiento'],
            direccion=apoderado_data['direccion'],
            comuna_id=apoderado_data['comuna'],
            email=apoderado_data['email'],
            telefono=apoderado_data['telefono'],
            parentezco=apoderado_data['parentezco']
        )

        if created:
            print(f"Nuevo apoderado guardado con ID: {apoderado.id}")
        else:
            print(f"Apoderado existente encontrado con ID: {apoderado.id}")
        print(apoderado.id)
        from personas.models import Apoderado_backup
        apoderado_backup_data = request.data['info_apoderado_backup']
        # Buscar si el apoderado backup ya existe
        apoderado_backup, created = Apoderado_backup.objects.get_or_create(
            rut=apoderado_backup_data['rut'],
            nombres=apoderado_backup_data['nombres'],
            apellido_paterno=apoderado_backup_data['apellido_paterno'],
            apellido_materno=apoderado_backup_data['apellido_materno'],
            fecha_nacimiento=apoderado_backup_data['fecha_nacimiento'],
            direccion=apoderado_backup_data['direccion'],
            comuna_id=apoderado_backup_data['comuna'],
            email=apoderado_backup_data['email'],
            telefono=apoderado_backup_data['telefono'],
            parentezco=apoderado_backup_data['parentezco']
        )

        if created:
            print(f"Nuevo apoderado backup guardado con ID: {apoderado_backup.id}")
        else:
            print(f"Apoderado backup existente encontrado con ID: {apoderado_backup.id}")

        antecedentes_familiares_data = request.data['info_alumno']['antecedentes_familiares']

        antecedentes, created = AntecedentesFamiliares.objects.get_or_create(
            nombre_padre=antecedentes_familiares_data['nombre_padre'],
            fecha_nac_padre=antecedentes_familiares_data['fecha_nac_padre'],
            nombre_madre=antecedentes_familiares_data['nombre_madre'],
            fecha_nac_madre=antecedentes_familiares_data['fecha_nac_madre'],
            convivientes=antecedentes_familiares_data['convivientes'],
            cantidad_personas_hogar=antecedentes_familiares_data['cantidad_personas_hogar'],
            total_hermanos=antecedentes_familiares_data['total_hermanos'],
            posicion_familiar=antecedentes_familiares_data['posicion_familiar']
        )
        #Obtener la ide de los antecedentes familiares
        antecedentes_familiares_id = antecedentes.id

        # Buscar si el alumno ya existe
        alumno, created = Alumno.objects.get_or_create(
            nombres=alumno_data['nombres'],
            apellido_paterno=alumno_data['apellido_paterno'],
            apellido_materno=alumno_data['apellido_materno'],
            fecha_nacimiento=alumno_data['fecha_nacimiento'],
            colegio_origen=alumno_data['colegio_origen'],
            curso_id=curso_id,
            rut=alumno_data['rut'],
            direccion=alumno_data['direccion'],
            comuna_id=alumno_data['comuna'],
            email=alumno_data['email'],
            telefono=alumno_data['telefono'],
            apoderado_id=apoderado.id,
            apoderado_backup_id=apoderado_backup.id,
            identificador_curso=identificador_curso,
            antecedentes_familiares_id=antecedentes_familiares_id
            
        )

        if created:
            print(f"Nuevo alumno guardado con ID: {alumno.id}")
        else:
            print(f"Alumno existente encontrado con ID: {alumno.id}")

        
        # Guardar Matrícula
        request.data['alumno'] = alumno.id  # Asignar ID del alumno
        request.data['apoderado_id'] = apoderado.id 
        print("ID APODERADO", request.data['apoderado_id']) # Asignar ID del apoderado
        serializer = MatriculaSerializer(data=request.data)

        if serializer.is_valid():
            matricula = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Errores en MatriculaSerializer:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET', 'POST'])
# def matricula_list(request):
#     if request.method == 'GET':
#         matriculas = Matricula.objects.all()
#         respuesta=[]       
            
#         serializer = MatriculaSerializer(matriculas, many=True)
#         for matricula in serializer.data:
#             alumno=Alumno.objects.get(pk=matricula['alumno'])
#             serializer_alumno=AlumnoSerializer(alumno)
#             matricula['info_alumno']=serializer_alumno.data
#             respuesta.append(matricula)
#         return Response(respuesta)
    # elif request.method == 'POST':
    #     print(request.data['info_alumno'])
    #     serializer_alumno = AlumnoSerializer(data=request.data['info_alumno'])
    #     print(serializer_alumno.is_valid())
    #     if serializer_alumno.is_valid():
    #         serializer_alumno.save()
        
    #         print(serializer_alumno.data['id'])
    #     return
    #     serializer_apoderado = ApoderadoSerializer(data=request.data['info_apoderado'])
    #     if serializer_apoderado.is_valid():
    #        serializer_apoderado.save()
            
    #     serializer = MatriculaSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def matricula_detail(request, pk):
    try:
        matricula = Matricula.objects.get(pk=pk)
    except Matricula.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MatriculaSerializer(matricula)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MatriculaSerializer(matricula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        matricula.delete()
        return Response({"mensaje": f"Matricula ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def progreso_alumno_list(request):
    if request.method == 'GET':
        progresos = ProgresoAlumno.objects.all()
        serializer = ProgresoAlumnoSerializer(progresos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProgresoAlumnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def progreso_alumno_detail(request, pk):
    try:
        progreso = ProgresoAlumno.objects.get(pk=pk)
    except ProgresoAlumno.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProgresoAlumnoSerializer(progreso)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProgresoAlumnoSerializer(progreso, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        progreso.delete()
        return Response({"mensaje": f"ProgresoAlumno ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def notas_alumno_list(request):
    if request.method == 'GET':
        notas = NotasAlumno.objects.all()
        serializer = NotasAlumnoSerializer(notas, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = NotasAlumnoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def notas_alumno_detail(request, pk):
    try:
        nota = NotasAlumno.objects.get(pk=pk)
    except NotasAlumno.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NotasAlumnoSerializer(nota)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = NotasAlumnoSerializer(nota, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        nota.delete()
        return Response({"mensaje": f"NotasAlumno ID: {pk} ha sido eliminado correctamente"}, status=status.HTTP_200_OK)