# Last modified: 13feb21 (FEG)
# --------------------------------------------
from tkinter import *
from tkinter import messagebox as MessageBox
from sympy import FiniteSet
from matplotlib_venn import venn2, venn2_circles
import matplotlib.pyplot as plt
import random


def conjunto(*args): # Devuelve un conjunto definido por extensión con los elementos dados en el argumento, separados por comas
  """
  Devuelve un conjunto definido por extensión con los elementos dados en el argumento, separados por comas

  Parámetros:

  *args-tipo variable: Representa el conjunto de elemntos separados por coma que se usarán para crear el conjunto.
  """
  return set(args)

def cardinalidad(A): # Devuelve la cardinalidad de un conjunto
  """
  Devuelve un entero que representa el cardinal del conjunto

  Parámetros:

  A-tipo Set: Es el conjunto cuyo cardinal se desea averiguar
  """
  return len(A)

def pertenece(x,A): # Devuelve True si el elemento x pertenece al conjunto A, False de lo contrario
  """
  Permite saber si un determinado elemento pertenece o no a un conjunto en particular.

  Parámetros:

  x-tipo variable: Representa el elemento que se desea averiguar si forma o no parte de un conjunto.
  A-tipo Set: Es el conjunto en el cual se revisará si el objeto pasado como parámetro pertenece o no.

  Retorno:

  Retorna True en caso que el elemento x pertenezca al conjunto A. En caso contrario, retorna False.
  """
  return x in A

def subconjunto(A,B): # Devuelve True si A es subconjunto de B, False de lo contrario
  """
  Permite determinar si el conjunto A pertenece al conjunto B o no

  Parámetros:

  A-tipo Set: Es el conjunto para el cual se desea saber si está o no incluido en el conjunto B
  B-tipo Set: Es el conjunto usado para saber si el conjunto A está incluido o no en él.

  Retorno:

  Retorna True si el conjunto A está incluido en el conjunto B. Caso contrario, retorna False.
  """
  return A.issubset(B)

def union(A,B): # Devuelve la unión de A y B
  """
  Permite obtener por extensión el conjunto resultante de la unión entre los conjuntos A y B.

  Parámetros:

  A-tipo Set: El primer conjunto de la operación
  B-tipo Set: El segundo conjunto de la operación

  Retorno:

  Retorna un conjunto que representa el resultado de la unión entre A y B
  """
  return A.union(B)

def interseccion(A,B): # Devuelve la intersección de A y B
  """
  Permite obtener por extensión el conjunto resultante de la intersección entre los conjuntos A y B.

  Parámetros:

  A-tipo Set: El primer conjunto de la operación
  B-tipo Set: El segundo conjunto de la operación

  Retorno:

  Retorna un conjunto que representa el resultado de la intersección entre A y B
  """
  return A.intersection(B)

def producto_cartesiano(A,B): # Devuelve un conjunto con los elementos del producto cartesiano de A y B
  """
  Permite obtener por extensión el conjunto resultante del producto cartesiano entre los conjuntos A y B.

  Parámetros:

  A-tipo Set: El primer conjunto de la operación
  B-tipo Set: El segundo conjunto de la operación

  Retorno:

  Retorna un conjunto que representa el resultado del producto cartesiano entre A y B cpmo un conjunto de pares ordenados
  """
  return set([i for i in FiniteSet(*A) * FiniteSet(*B)])

def simetricdif(A,B):
  """
  Permite obtener por extensión el conjunto resultante de la diferencia simétrica entre los conjuntos A y B.

  Parámetros:

  A-tipo Set: El primer conjunto de la operación
  B-tipo Set: El segundo conjunto de la operación

  Retorno:

  Retorna un conjunto que representa el resultado de la diferencia simétrica entre A y B
  """
  return A.symmetric_difference(B) 

# Diagramas de Venn
# https://pypi.org/project/matplotlib-venn/

def venn(A,B):
  #A = FiniteSet(*A) # Convierto el conjunto al objeto de sympy para graficar
  #B = FiniteSet(*B) # Convierto el conjunto al objeto de sympy para graficar
  print(A)
  plt.figure(figsize = (6,8)) # Creo la figura
  v = venn2(subsets = [A,B],set_labels = ('A','B')) # Creo los dos conjuntos
  v.get_label_by_id('10').set_text(A - B)
  v.get_label_by_id('11').set_text(A.intersection(B))
  v.get_label_by_id('01').set_text(B - A)
  c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
  c[0].set_ls('solid')
  plt.show()


def graficar_interseccion(conj1,conj2,etiqueta1='A',etiqueta2='B'):
  """
  Grafica la intersección entre dos conjuntos y muestra los datos de la operación

  Parámetros:

  conj1-tipo Set : Es el primer conjunto para la operación. Este conjunto ya ha sido formateado para su uso.
  conj2-tipo Set : Es el segundo conjunto para la opeación. Este conjunto ya ha sido formateado para su uso.
  etiqueta1-tipo String: Es la etiqueta para el primer conjunto. Por defecto se etiqueta como 'A'
  etiqueta2-tipo String: Es la etiqueta para el segundo conjunto. Por defecto se etiqueta como 'B'
  """
  A = conj1 # Convierto el conjunto al objeto de sympy para graficar
  B = conj2 # Convierto el conjunto al objeto de sympy para graficar
  operacion=etiqueta1 +" ∩ "+ etiqueta2
  resultado=interseccion(A,B)

  plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
  
  if cardinalidad(A)==0 and cardinalidad(B)==0:
    C={1,2,3,4,5,6,7}
    v = venn2(subsets = [C,C],set_labels = (operacion,'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [C,C],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(chr(216))
    v.get_label_by_id('10').set_visible(False)
    v.get_patch_by_id('10').set_color('green')
    v.get_patch_by_id('11').set_color('green')
  elif cardinalidad(A)==0:
    v = venn2(subsets = [B,B],set_labels = (operacion,'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [B,B],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(resultado)
  elif cardinalidad(B)==0:
    v = venn2(subsets = [A,A],set_labels = (operacion,'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,A],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(resultado)
  elif cardinalidad(resultado)==0:
    v = venn2(subsets = [A,B],set_labels = (etiqueta1,etiqueta2)) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B])
    v.get_label_by_id('01').set_text(B)
    v.get_label_by_id('10').set_text(A)
  else:
    v = venn2(subsets = [A,B],set_labels = (etiqueta1,etiqueta2)) # Creo los dos conjuntos
    v.get_label_by_id('10').set_visible(False)
    v.get_label_by_id('11').set_text(resultado)
    v.get_label_by_id('01').set_visible(False)
    v.get_patch_by_id('10').set_color('white')
    v.get_patch_by_id('01').set_color('white')
    v.get_label_by_id('10').set_color('black')
    v.get_label_by_id('01').set_color('black')
    c = venn2_circles(subsets = [A,B])
    c[0].set_ls('solid')
    c[1].set_ls('solid')

  tablaResultados(A,B,operacion,resultado,etiqueta1,etiqueta2)
  plt.show()

def graficar_union(conj1,conj2,etiqueta1="A",etiqueta2="B"):
  """
  Permite graficar la unión de ambos conjuntos y muestra los datos de la operación

  Parámetros:

  conj1-tipo Set : Es el primer conjunto para la operación. Este conjunto ya ha sido formateado para su uso.
  conj2-tipo Set : Es el segundo conjunto para la opeación. Este conjunto ya ha sido formateado para su uso.
  etiqueta1-tipo String: Es la etiqueta para el primer conjunto. Por defecto se etiqueta como 'A'
  etiqueta2-tipo String: Es la etiqueta para el segundo conjunto. Por defecto se etiqueta como 'B'
  """
  A = conj1 # Convierto el conjunto al objeto de sympy para graficar
  B = conj2 # Convierto el conjunto al objeto de sympy para graficar
  carA=cardinalidad(A)
  carB=cardinalidad(B)
  operacion=etiqueta1 + " U " + etiqueta2
  resultado=union(A,B)
  lista=resultado #sirve para crear el diagrama y adaptarlo en caso de que el resultado sea vacio
  elementos=resultado #sirve para mostrar los elementos resultabtes de la operacion y adaptarla en caso que sea vacío
  if cardinalidad(resultado)==0:
    elementos=chr(216)
    lista={1,2,3,4,5,6,7}

  plt.figure(figsize = (6,8)) # Creo la figura
  v = venn2(subsets = [lista,lista],set_labels = (operacion,'')) # Creo los dos conjuntos
  c = venn2_circles(subsets = [lista,lista],linestyle = 'dashed')
  v.get_label_by_id('11').set_text(elementos)
  v.get_label_by_id('01').set_visible(False)
  v.get_label_by_id('10').set_visible(False)
  	
  #v.get_label_by_id('A').set_color('white')
 # v.get_patch_by_id('11').set_color('green')
 # v.get_patch_by_id('10').set_color('green')
 # v.get_patch_by_id('01').set_color('green')
 # v.get_label_by_id('10').set_visible(False)
  #v.get_label_by_id('01').set_visible(False)
  
  tablaResultados(A,B,operacion,resultado,etiqueta1,etiqueta2)
  plt.show()

def graficar_diferencia(conj1,conj2,etiqueta1='A',etiqueta2='B',eleccion=True):
  """
  Grafica la diferencia entre conjuntos y muestras los datos de la operación

  Parámetros:
  conj1-tipo Set : Es el primer conjunto para la operación. Este conjunto ya ha sido formateado para su uso.
  conj2-tipo Set : Es el segundo conjunto para la opeación. Este conjunto ya ha sido formateado para su uso.
  etiqueta1-tipo String: Es la etiqueta para el primer conjunto. Por defecto se etiqueta como 'A'
  etiqueta2-tipo String: Es la etiqueta para el segundo conjunto. Por defecto se etiqeuta como 'B'
  eleccion-tipo Integer: Sirve para saber qué conjunto graficar. Ignorar si no se usa interfaz gráfica.
  """
  if eleccion:
    A=conj1
    B=conj2
  else:
    A=conj2
    B=conj1

  lbl1=etiqueta1
  lbl2=etiqueta2
  resultado=None
  operacion=etiqueta1 + " - " + etiqueta2
  incluido=subconjunto(A,B)
  v=None
  c=None
  resultado=A-B
  plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
   
 
    
  if(cardinalidad(resultado)==0) and cardinalidad(B)!=0:
    v = venn2(subsets = [B,B],set_labels = ('',etiqueta1+"-"+etiqueta2)) # Creo los dos conjuntos
    c = venn2_circles(subsets = [B,B],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(chr(216))
    v.get_label_by_id('10').set_visible(False)
    v.get_patch_by_id('10').set_color('green')
    v.get_patch_by_id('11').set_color('green')
  elif cardinalidad(A)==0 and cardinalidad(B)==0:
    C={1,2,3,4,5,6,7}# un conjunto accesorio para poder graficar el diagrama ya que ambos son vacíos
    v = venn2(subsets = [C,C],set_labels = ('',etiqueta1+"-"+etiqueta2)) # Creo los dos conjuntos
    c = venn2_circles(subsets = [C,C],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(chr(216))
    v.get_label_by_id('10').set_visible(False)
    v.get_patch_by_id('10').set_color('green')
    v.get_patch_by_id('11').set_color('green') 
  elif cardinalidad(A)!=0 and cardinalidad(B)==0:
    v = venn2(subsets = [A,A],set_labels = (etiqueta1+"-"+etiqueta2,'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,A],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(A-B) 
  elif(cardinalidad(interseccion(A,B))==0):
    v = venn2(subsets = [A,B],set_labels = (str(etiqueta1),str(etiqueta2))) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v.get_label_by_id('10').set_text(resultado)
    #v.get_patch_by_id('11').set_color('white')
    v.get_patch_by_id('01').set_color('white')
    v.get_label_by_id('01').set_visible(False)
    c[0].set_ls('solid')
    #v.get_label_by_id('11').set_visible(False)
  else:
    v = venn2(subsets = [A,B],set_labels = (str(etiqueta1),str(etiqueta2))) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v.get_label_by_id('10').set_text(resultado)
    v.get_patch_by_id('11').set_color('white')
    v.get_patch_by_id('01').set_color('white')
    v.get_label_by_id('01').set_visible(False)
    v.get_label_by_id('11').set_visible(False)
 
  
  tablaResultados(A,B,operacion,resultado,etiqueta1,etiqueta2)
  plt.show()

def graficar_difsim(conj1,conj2,etiqueta1='A',etiqueta2='B',eleccion=True):
  """
  Permite graficar la diferencia simétirica entre dos conjuntos y muestra los datos de la operación
  Parámetros:

  conj1-tipo Set : Es el primer conjunto para la operación. Este conjunto ya ha sido formateado para su uso.
  conj2-tipo Set : Es el segundo conjunto para la opeación. Este conjunto ya ha sido formateado para su uso.
  etiqueta1-tipo String: Es la etiqueta para el primer conjunto. Por defecto se etiqueta como 'A'.
  etiqueta2-tipo String: Es la etiqueta para el segundo conjunto. Por defecto se etiqeuta como 'B'.
  eleccion-tipo Integer: Sirve para saber qué conjunto graficar. Ignorar si no se usa interfaz gráfica.
  """

  if eleccion:
    A=conj1
    B=conj2
  else:
    A=conj2
    B=conj1

  resultado=None
  operacion=etiqueta1+" ∆ "+etiqueta2
  difAB=A-B
  difBA=B-A
  c=None
  plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
  resultado=simetricdif(A,B)

  if (cardinalidad(A)==0 and cardinalidad(B)==0) or A==B:
    C={1,2,3,4,5,6,7}# un conjunto accesorio para poder graficar el diagrama ya que ambos son vacíos
    v = venn2(subsets = [C,C],set_labels = ('',operacion)) # Creo los dos conjuntos
    c = venn2_circles(subsets = [C,C],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(chr(216))
    v.get_label_by_id('10').set_visible(False)
    v.get_patch_by_id('10').set_color('green')
    v.get_patch_by_id('11').set_color('green') 
  elif cardinalidad(A)==0:
    v = venn2(subsets = [A,B],set_labels = ('',str(etiqueta2))) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v.get_label_by_id('01').set_text(B)
    v.get_label_by_id('10').set_visible(False)
  elif cardinalidad(B)==0:
    v = venn2(subsets = [A,B],set_labels = (str(etiqueta1),'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v.get_label_by_id('10').set_text(A)
    v.get_label_by_id('01').set_visible(False)
  elif subconjunto(A,B):
    v = venn2(subsets = [A,B],set_labels = (operacion,'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v.get_label_by_id('01').set_text(resultado)
    v.get_patch_by_id('11').set_color('white')
    v.get_patch_by_id('10').set_color('white')
    v.get_label_by_id('10').set_visible(False)
    v.get_label_by_id('11').set_visible(False)
  elif subconjunto(B,A):
    v = venn2(subsets = [A,B],set_labels = (operacion,'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v.get_label_by_id('10').set_text(resultado)
    v.get_patch_by_id('11').set_color('white')
    v.get_patch_by_id('01').set_color('white')
    v.get_label_by_id('01').set_visible(False)
    v.get_label_by_id('11').set_visible(False)
  else:
    v = venn2(subsets = [A,B],set_labels = (str(etiqueta1),str(etiqueta2))) # Creo los dos conjuntos
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v.get_patch_by_id('11').set_color('white')
    v.get_label_by_id('11').set_visible(False)
    v.get_label_by_id('10').set_text(interseccion(simetricdif(A,B),A))
    v.get_label_by_id('01').set_text(interseccion(simetricdif(A,B),B))
   
    
  tablaResultados(A,B,operacion,resultado,etiqueta1,etiqueta2)
  plt.show()
 

def graficar_conjunto(conjunto1,etiqueta="A"):
   """
   Permite graficar y mostrar los datos de un sólo conjunto.

   Parámetros:
   conjunto1-tipo Set: Es el conjunto que se graficará
   etiqueta: Representa la etiqueta que se colocará al conjunto. Por defecto se etiqueta como 'B'
   """
   v=None
   c=None
   plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
   
   if cardinalidad(conjunto1)==0:
    C={1,2,3,4,5,6,7}# un conjunto accesorio para poder graficar el diagrama ya que ambos son vacíos
    v = venn2(subsets = [C,C],set_labels = (etiqueta,'')) # Creo los dos conjuntos
    c = venn2_circles(subsets = [C,C],linestyle = 'dashed')
    v.get_label_by_id('11').set_text(chr(216))
    v.get_label_by_id('10').set_visible(False)
    v.get_patch_by_id('10').set_color('green')
    v.get_patch_by_id('11').set_color('green')
   else:
    v = venn2(subsets = [conjunto1,conjunto1],set_labels = (str(etiqueta),''))
    c = venn2_circles(subsets = [conjunto1,conjunto1],linestyle = 'dashed')


   tabla_conj_unico(conjunto1,etiqueta1)
   plt.show()


def tablaResultados(A,B,operacion,resultado,etiqueta1,etiqueta2):
  """
  Muestra una leyenda con los conjuntos, operación, resultado y cardinalidades

  Parámetros:

  A-tipo Set: Primer conjunto resultante después de pasar por todos los controles.
  B-tipo Set: Segundo conjunto resultante después de pasar por todos los controles.
  etiqueta1-tipo String: Se usa para etiquetar al primer conjunto.
  etiqueta2-tipo String: Se usa para etiquetar al segundo conjunto.
  operación-tipo String: Representa qué operación fue realizada.
  resultado-tipo FiniteSet De Int: El conjunto resultado de la operación.
  """
  resultadoFinal=resultado
  lbl1=etiqueta1
  lbl2=etiqueta2
  resul1=None
  resul2=None
  if cardinalidad(resultado)==0:
    resultadoFinal=chr(216)# el vacío
  
  if cardinalidad(A)==0:
    resul1=chr(216)
  else:
    resul1=A

  if cardinalidad(B)==0:
    resul2=chr(216)
  else:
    resul2=B
  

  print("----------------------Señalando Datos Y Diagrama de la Operación " +operacion+"------------------------------")
  print("*************************************************************************************************************")
  print( " " + lbl1 + " = ",resul1,"\n",lbl2 + " = ",resul2,"\n","Cardinal " + lbl1 + " = ",cardinalidad(A),"\n","Cardinal " + lbl2+" = ",
    cardinalidad(B),"\n", operacion+" = ",resultadoFinal,"\n","Cardinal "+ operacion+" = ",cardinalidad(resultado))
  print("************************************************************************************************************")


def tabla_conj_unico(conjunto,nombre_conjunto):
  """
  Muestra los datos de un único conjunto
	Parámetros:
	conjunto-tipo Set: Es el conjunto cuyos datos se mostrará
	nombre_conjunto-tipo String: Es el nombre del conjunto

  """
  resultadoFinal=conjunto
  if cardinalidad(conjunto)==0:
   resultadoFinal=chr(216)# el vacío

  print("----------------------Señalando Datos Y Diagrama de " + nombre_conjunto +"------------------------------")
  print("*************************************************************************************************************")
  print(" "+nombre_conjunto + " = ",resultadoFinal,"\n","Cardinal " + nombre_conjunto + " = ",cardinalidad(conjunto),"\n")
  print("************************************************************************************************************")


def documentacion():
    help(graficar_diferencia)
    print("------------------------------------------------------------------------------------------------------------------")
    help(graficar_interseccion)
    print("------------------------------------------------------------------------------------------------------------------")
    help(graficar_union)
    print("------------------------------------------------------------------------------------------------------------------")
    help(graficar_difsim)
    print("------------------------------------------------------------------------------------------------------------------")
    help(graficar_conjunto)
    print("------------------------------------------------------------------------------------------------------------------")
    help(conjunto)
    print("------------------------------------------------------------------------------------------------------------------")
    help(cardinalidad)
    print("------------------------------------------------------------------------------------------------------------------")
    help(pertenece)
    print("------------------------------------------------------------------------------------------------------------------")
    help(subconjunto)
    print("------------------------------------------------------------------------------------------------------------------")
    help(union)
    print("------------------------------------------------------------------------------------------------------------------")
    help(interseccion)
    print("------------------------------------------------------------------------------------------------------------------")
    help(producto_cartesiano)
    print("------------------------------------------------------------------------------------------------------------------")
    help(simetricdif)



