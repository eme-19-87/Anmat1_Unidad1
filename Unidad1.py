# Last modified: 13feb21 (FEG)
# --------------------------------------------
from tkinter import *
from tkinter import messagebox as MessageBox
from sympy import FiniteSet
from matplotlib_venn import venn2, venn2_circles
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import random

class Unidad1:
  def conjunto(self,*args): 
    """
    Trasforma los argumentos pasados en un conjunto
    Parámetros:
    args-tipo Lista/Tupla: Es el objeto que se quiere transformar en conjunta

    Retorno:
    Retorna un objeto de tipo Set
    """
    return set(args)

  def cardinalidad(self,A): 
    """
    Permite obtener la cardinalidad del conjunto argumento
    Parámetros:
    args-tipo Lista/Tupla: Es el objeto del cual se quiere conocer su cardinalidad

    Retorno:
    Retorna un entero que representa la cardinalidad
    """
    return len(A)

  def pertenece(self,x,A): # Devuelve True si el elemento x pertenece al conjunto A, False de lo contrario
    return x in A

  def subconjunto(self,A,B): # Devuelve True si A es subconjunto de B, False de lo contrario
    return A.issubset(B)

  def union(self,A,B): # Devuelve la unión de A y B
    return A.union(B)

  def interseccion(self,A,B): # Devuelve la intersección de A y B
    return A.intersection(B)

  def producto_cartesiano(self,A,B): # Devuelve un conjunto con los elementos del producto cartesiano de A y B
    return set([i for i in FiniteSet(*A) * FiniteSet(*B)])

  def simetricdif(self,A,B):
    return A.symmetric_difference(B) 

  # Diagramas de Venn
  # https://pypi.org/project/matplotlib-venn/

  def venn(self,A,B):
    """
    Permite realizar un diagrama de Venn con dos conjuntos exclusivos con valores numéricos.
    Parámetros:
    A-Tipo Set De Numeros: Reprsenta el primer conjunto de números que se usará para graficar
    B-Tipo Set De Numeros: Reprsenta el segundo conjunto de números que se usará para graficar
    """
    A = FiniteSet(*A) # Convierto el conjunto al objeto de sympy para graficar
    B = FiniteSet(*B) # Convierto el conjunto al objeto de sympy para graficar
    
    plt.figure(figsize = (6,8)) # Creo la figura
    v = venn2(subsets = [A,B],set_labels = ('A','B')) # Creo los dos conjuntos
    v.get_label_by_id('10').set_text(A - B)
    v.get_label_by_id('11').set_text(A.intersection(B))
    v.get_label_by_id('01').set_text(B - A)
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    c[0].set_ls('solid')
    plt.show()


  def __graficarInterseccion(self,conj1,conj2):
    """
    Grafica la intersección entre dos conjuntos. Si el resultado es vacío, mostrará ambos conjuntos separados, sin intersección
    alguna.

    Parámetros:

    conj1-tipo Set de Int: Es el primer conjunto para la operación. Este conjunto ya ha sido formateado para su uso.
    conj2-tipo Set de Int: Es el segundo conjunto para la opeación. Este conjunto ya ha sido formateado para su uso.
    """
    A = FiniteSet(*conj1) # Convierto el conjunto al objeto de sympy para graficar
    B = FiniteSet(*conj2) # Convierto el conjunto al objeto de sympy para graficar
    operacion="A" +"∩"+ "B"
    resultado=self.interseccion(A,B)

    plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    v = venn2(subsets = [A,B],set_labels = ('A','B')) # Creo los dos conjuntos
    
    #controlo si es vacío y si lo es, vuelvo blanco ambos conjuntos y desaparezco las etiquetas
    if self.cardinalidad(resultado)==0:
      c[0].set_color("white")
      c[1].set_color("white")
    else:
      v.get_label_by_id('10').set_text("Excluido")
      v.get_label_by_id('11').set_text(resultado)
      v.get_label_by_id('01').set_text("Excluido")
      v.get_label_by_id('10').set_color('black')
      v.get_label_by_id('01').set_color('black')
      c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
      c[0].set_ls('solid')
    
   
    self.__tablaResultados(A,B,operacion,resultado)
    plt.show()

  def __graficarUnion(self,conj1,conj2):
    """
    Permite graficar la unión de ambos conjuntos. Por cuestiones de las bibliotecas usadas se pintan ambos conjuntos para
    indicar que todos los miembros del mismo forman parte del conjunto. La leyenda en el centro de la gráfica resalta que
    sólo se tienen en cuenta cada elemento una vez. Falta controlar que sucede si la unión es vacía.

    Parámetros:

    conj1-tipo Set de Int: Es el primer conjunto para la operación. Este conjunto ya ha sido formateado para su uso.
    conj2-tipo Set de Int: Es el segundo conjunto para la opeación. Este conjunto ya ha sido formateado para su uso.
    """
    A = FiniteSet(*conj1) # Convierto el conjunto al objeto de sympy para graficar
    B = FiniteSet(*conj2) # Convierto el conjunto al objeto de sympy para graficar
    operacion="AUB"
    resultado=self.union(A,B)
    plt.figure(figsize = (6,8)) # Creo la figura
    v = venn2(subsets = [A,B],set_labels = ('A','B')) # Creo los dos conjuntos

    v.get_label_by_id('11').set_text(resultado)
    v.get_label_by_id('A').set_color('white')

    c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
    c[1].set_color("red")
    c[0].set_color('red')
    v.get_label_by_id('10').set_visible(False)
    v.get_label_by_id('01').set_visible(False)
    
    self.__tablaResultados(A,B,operacion,resultado)
    plt.show()

  def __graficaDiferencia(self,conj1,conj2,eleccion):
    """
    Grafica la diferencia entre conjuntos. En caso de ser vacía, la gráfica se pintará de blanco para indicar que el resultado es
    el conjunto vacío.

    Parámetros:
    conj1-tipo Set De Int: Es el primer conjunto para la operación. Este conjunto ya ha sido formateado para su uso.
    conj2-tipo Set De Int: Es el segundo conjunto para la opeación. Este conjunto ya ha sido formateado para su uso.
    elección-tipo boolean: Determina si la operación es conj1-conj2 ó conj2-conj1. Si es True se dará el primer caso. Si es False se 
    dará el segundo caso.
    """
    A = FiniteSet(*conj1) # Convierto el conjunto al objeto de sympy para graficar
    B = FiniteSet(*conj2) # Convierto el conjunto al objeto de sympy para graficar
    resultado=None
    operacion=""
    primerCirculo="red"
    segundoCirculo="white"
    v=None
    c=None
    plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
    
    #determina cual conjunto se resaltará más dependiendo la diferencia
    if eleccion:
      v = venn2(subsets = [A,B],set_labels = ('A','B')) # Creo los dos conjuntos
      c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
      v.get_label_by_id('10').set_text(A-B)
      resultado=A-B
      operacion="A-B"
    else:
      primerCirculo="blue"
      v = venn2(subsets = [B,A],set_labels = ('B','A')) # Creo los dos conjuntos
      c = venn2_circles(subsets = [B,A],linestyle = 'dashed')
      v.get_label_by_id('10').set_text(B-A)
      resultado=B-A
      operacion="B-A"
    
    #oculta la información de los conjuntos que no son importantes en la diferencia
    c[0].set_ls('solid') 
    v.get_label_by_id('01').set_visible(False)
    v.get_label_by_id('11').set_visible(False)

    #si el resultado diese vacío, vuelvo toda blanca la pantalla
    if self.cardinalidad(resultado)==0:
      primerCirculo="white"
      segundoCirculo="white"
      v.get_label_by_id('10').set_visible(False)

    #configura las características de los circulos
    for circle, color in zip(c, [primerCirculo, segundoCirculo]):
          circle.set_lw(2.0)
          circle.set_alpha(1)
          circle.set_color(color)
    


    self.__tablaResultados(A,B,operacion,resultado)
    plt.show()

  def __graficarDifSim(self,conj1,conj2,eleccion):
   
    A = FiniteSet(*conj1) 
    B = FiniteSet(*conj2)
    resultado=None
    operacion=""
    primerCirculo="red"
    segundoCirculo="white"
    v=None
    c=None
    plt.figure(figsize = (6,8),linewidth=10, edgecolor="black", facecolor="white") # Creo la figura
    
    #determina cual conjunto se resaltará más dependiendo la diferencia
    if eleccion:
      v = venn2(subsets = [A,B],set_labels = ('A','B')) # Creo los dos conjuntos
      c = venn2_circles(subsets = [A,B],linestyle = 'dashed')
      v.get_label_by_id('10').set_text(self.interseccion(self.simetricdif(A,B),A))
      v.get_label_by_id('01').set_text(self.interseccion(self.simetricdif(A,B),B))
      v.get_label_by_id('11').set_text(chr(216))
      resultado=self.simetricdif(A,B)
      operacion="A∆B"
    else:
      v = venn2(subsets = [B,A],set_labels = ('B','A')) # Creo los dos conjuntos
      c = venn2_circles(subsets = [B,A],linestyle = 'dashed')
      v.get_label_by_id('10').set_text(self.interseccion(self.simetricdif(A,B),B))
      v.get_label_by_id('01').set_text(self.interseccion(self.simetricdif(A,B),A))
      v.get_label_by_id('11').set_text(chr(216))
      resultado=self.simetricdif(B,A)
      operacion="B∆A"
    

    #si el resultado diese vacío, vuelvo toda blanca la pantalla
    if self.cardinalidad(resultado)==0:
      v.get_label_by_id('10').set_visible(False)
      v.get_label_by_id('01').set_visible(False)
      


    self.__tablaResultados(A,B,operacion,resultado)
    plt.show()

  def crearInterfaz(self):

    """
    Crea la interfaz necesaria para visualizar las operaciones elementales entre conjuntos.
    Todos los resultados se imprimirán en la fila de Jupyter Notebook y servirá como una documentación para
    que el alumno revise los resultados.
    """
    root = Tk() #esto representa a la ventana
    seleccion=IntVar() #sierve para saber qué debe graficarse
    conj1=StringVar()
    conj2=StringVar()
    root.wm_title("Grafica insertada en Tkinter")
    root.maxsize(600,250)       #las dimensiones de la ventana
    root.minsize(600,250)
    miFrame=Frame() #el marco donde se colocarán los elementos de la ventana como botones, etiquetas y demás
    miFrame.pack()
    miFrame.config(width=800,height=800)
    lblTitulo=Label(miFrame,text="Teoria De Conjuntos") #las etiquetas
    lblTitulo.grid(row=0,columnspan=12)
    lblConjunto1=Label(miFrame,text="Conjunto A")
    lblConjunto2=Label(miFrame,text="Conjunto B")
    txbConjunto1=Entry(miFrame,textvariable=conj1) #las cajas de texto
    txbConjunto2=Entry(miFrame,textvariable=conj2)
    rbtUnion=Radiobutton(miFrame,text="Union",variable=seleccion,value=1) #los radiobutton
    rbtIntersec=Radiobutton(miFrame,text="Interseccion",variable=seleccion,value=2)
    rbtAMB=Radiobutton(miFrame,text="A-B",variable=seleccion,value=3)
    rbtBMA=Radiobutton(miFrame,text="B-A",variable=seleccion,value=4)
    rbtDifSimAB=Radiobutton(miFrame,text="A∆B",variable=seleccion,value=5)
    rbtDifSimBA=Radiobutton(miFrame,text="B∆A",variable=seleccion,value=6)

    #Al presionar el botón, creo el diagrama. Paso como parámetro el contenido de ambas cajas de texto y el frame para que sea 
    #el contenedor del digrama
    btnGraficar=Button(miFrame,text="Graficar Diagrama",command=lambda: self.__visualizarDiagrama(txbConjunto1.get(),txbConjunto2.get(),root,seleccion))
    btnGenerar=Button(miFrame,text="Generar",command=lambda:self.__generarAleatorios(conj1,conj2))
    btnExplicacion=Button(miFrame,text="Instrucciones",command=lambda:self.instruccionesUso())


    #----Posiciono los elementos dentro del marco.El posicionamiento es similar a una grilla-----
    lblConjunto1.grid(row=1,column=0)
    txbConjunto1.grid(row=1,column=1)
    lblConjunto2.grid(row=1,column=3)
    txbConjunto2.grid(row=1,column=4)
    btnGenerar.grid(row=1,column=5)
    rbtUnion.grid(row=2,column=0)
    rbtIntersec.grid(row=2,column=1)
    rbtAMB.grid(row=2,column=2)
    rbtBMA.grid(row=2,column=3)
    rbtDifSimAB.grid(row=2,column=4)
    rbtDifSimBA.grid(row=2,column=5)
    btnGraficar.grid(row=3,column=2)
    btnExplicacion.grid(row=4,column=2)
    mainloop() #El bucle de la ventana. Constantemente está oyendo si se produce algun evento como el presionar un botón

  def __visualizarDiagrama(self,conjunto1,conjunto2,contenedor,seleccion):
    """
    Muestra el diagrama de Venn según los conjuntos pasados y la operación seleccionada
    Parámetros:
    conjunto1-tipo string: Es el primer conjunto ingresado mediante la interfaz. En caso de estar en blanco, tener caracteres que
    no sean numéricos y que no sean comas, el programa mostrará una ventana emergente avisando del error.

    conjunto2-tipo string: Es el segundo conjunto ingresado mediante la interfaz. En caso de estar en blanco, tener caracteres que
    no sean numéricos y que no sean comas, el programa mostrará una ventana emergente avisando del error.

    seleccion tipo int: Es el radiobutton elegido en la interfaz.Cada uno está identificado con un valor único que permite diferenciar
    las diversas operaciones.

    contenedor tipo Frame: Es el contenedor del diagrama. Será necesario si se decide modificar el enfoque y mostrar el diagrama en
    la interfaz y no en JupyterNotebook
    """
    #determina qué se graficará
    seleccionado=seleccion.get()

    #quita los espacios en blanco a principio y final
    conj1=conjunto1.strip()
    conj2=conjunto2.strip()
    #verifica que haya sólo ',' y números enteros. Las comas se usan para crear una lista de enteros a partir del string
    correctos=self.__valoresAdmitidos(conj1) and self.__valoresAdmitidos(conj2)
    if correctos :
      #creo la lista de elementos string. Como la coma es un caracter válido, filtro los elementos sobrantes que pudieron crearse de dos
      #o más comas consecutivas
      listaNum1=[]
      listaNum2=[]
      listaStr1=self.__filtroComas(list(conj1.split(',')));
      listaStr2=self.__filtroComas(list(conj2.split(',')));

      #creo listas nuevas de enteros
      for elemento in listaStr1:
          listaNum1.append(int(elemento))

      for elemento in listaStr2:
          listaNum2.append(int(elemento))
     
      if seleccionado==1:
        self.__graficarUnion(listaNum1,listaNum2)
      elif seleccionado==2:
        self.__graficarInterseccion(listaNum1,listaNum2)
      elif seleccionado==3:
        self.__graficaDiferencia(listaNum1,listaNum2,True)
      elif seleccionado==4:
        self.__graficaDiferencia(listaNum1,listaNum2,False)
      elif seleccionado==5:
        self.__graficarDifSim(listaNum1,listaNum2,True)
      elif seleccionado==6:
        self.__graficarDifSim(listaNum1,listaNum2,False)
      else:
        MessageBox.showinfo("¡Advertencia!", "Seleccione una opción para graficar")
        
      
    else:
      MessageBox.showinfo("¡Advertencia!", "Por favor separa los miembros del conjunto con comas sin espacios entre conjuntos.\n No coloques simbolos distintos a números y comas")
    #crearDibujo(contenedor,venn)


  #def crearDibujo(self,contenedor,diagramaVenn):
    """
    Este código servirá por si se quiere pasar el diagrama a la interfaz directamente.
    """

    #imagen = FigureCanvasTkAgg(diagramaVenn, master=contenedor,tag="venn")  # CREAR AREA DE DIBUJO DE TKINTER.
    #imagen.draw() 
    #imagen.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
    


  def __valoresAdmitidos(self,conjunto):
    """
    Comprueba si ambos conjuntos tienen valores válidos. Sólo se permiten valores numéricos enteros y comas como separadores. 
    No debe haber espacios entre las comas y los números. 
    Parámetros:

    conjunto-tipo String: Representa la lista de elementos que se revisará.

    Retorno

    Retorna True si el conjunto cumple con las restricciones. Caso contrario, retorna False.
    """
    control="0123456789,"
    valido=True
    if len(conjunto)==0:
      valido=False
    else:
      for elemento in conjunto:
        if elemento not in control:
          valido=False

    return valido

  def __filtroComas(self,lista):
    """
    Filtra las comas excedentes ya que, al ser un símbolo válido, alguna puede escaparse.
    Parámetros:

    lista-tipo List De String: Una lista de elementos en los cuales puede haber elementos vacíos debido al excedente de comas. 
    Dichos elementos serán eliminados de la lista.

    Retorno:

    Retorna una nueva lista de elementos donde sólo figuran los números válidos
    """
    listaValida=[]
    for elemento in lista:
      if elemento!='':
        listaValida.append(elemento)
    return listaValida

  def __tablaResultados(self,A,B,operacion,resultado):
    """
    Muestra una leyenda con los conjuntos, operación, resultado y cardinalidades

    Parámetros:

    A-tipo FiniteSet De Int: Primer conjunto resultante después de pasar por todos los controles.
    B-tipo FiniteSet De Int: Segundo conjunto resultante después de pasar por todos los controles.
    operación-tipo String: Representa qué operación fue realizada.
    resultado-tipo FiniteSet De Int: El conjunto resultado de la operación.
    """
    resultadoFinal=resultado
    if self.cardinalidad(resultado)==0:
      resultadoFinal=chr(216)# el vacío

    print("----------------------Señalando Datos Y Diagrama de la Operación " +operacion+"------------------------------")
    print("*************************************************************************************************************")
    print(" A=",A,"\n","B=",B,"\n","Cardinal A=",self.cardinalidad(A),"\n","Cardinal B=",self.cardinalidad(B),"\n",
      operacion+"=",resultadoFinal,"\n","Cardinal "+ operacion+"=",self.cardinalidad(resultado))
    print("************************************************************************************************************")

  def __generarAleatorios(self,strConj1,strConj2):
    """
    Sierve para crear un conjunto aleatorio en cada una de las caja de texto
    Parámetros:

    strConj1-tipo StringVar: Variable asociada a la caja de texto para el primer conjunto. Es necesario para modificar el valor
    de la caja de texto en tiempo de ejecución.

    strConj2-tipo StringVar: Variable asociada a la caja de texto para el segundo conjunto. Es necesario para modificar el valor
    de la caja de texto en tiempo de ejecución.
    """
    limiteInf=2
    limiteSup=10
    totalConj1=random.randint(limiteInf,limiteSup)
    totalConj2=random.randint(limiteInf,limiteSup)
    datosConj1=""
    datosConj2=""
    while totalConj1>0:
      datosConj1=datosConj1+","+str(random.randint(limiteInf,limiteSup))
      totalConj1=totalConj1-1

    while totalConj2>0:
      datosConj2=datosConj2+","+str(random.randint(limiteInf,limiteSup))
      totalConj2=totalConj2-1

    strConj1.set(datosConj1.strip())
    strConj2.set(datosConj2.strip())

  def documentacion(self):
      help(Unidad1.crearInterfaz)
      help(Unidad1.instruccionesUso)
      help(Unidad1.venn)
      help(Unidad1.conjunto)
      help(Unidad1.cardinalidad)

  def instruccionesUso(self):
    """
    MUestra en una ventana emergente las instrucciones para agregar datos correctos en el programa.
    """
    consejo="Para ingresar los datos debe hacerlo en el siguiente formato: "+"\n"
    consejo+="1-Sólo admite números separados por comas. No deben quedar espacios en blanco entre una coma y un número."+"\n\n"
    consejo+="a)Formato Válido: 1,2,3,4,5"+"\n\n"
    consejo+="b)Formatos Inválidos: 1, 2, 3,4 // 1,     2//af,1,32,asf,78."+"\n\n"  
    consejo+="Por favor, sólo use el indicado en el apartado a)."
    consejo+="\n\n"+"2-Las comas en exceso son rechazadas y sólo se tiene en cuenta los valores numéricos. Pero dará error si tienen cualquier otro "
    consejo+="caracter que no sea numérico."+"\n\n"
    consejo+="3-Por el momento, sólo coloque valores enteros positivos. Estamos trabajando para que acepte todo tipo de caracteres."+"\n\n"
    consejo+="4-Si presiona el botón 'Generar' obtendrá valores enteros aleatorios. Uselo como guía para el formato de los datos de entrada."
    MessageBox.showinfo("Consejo",consejo)