# Laboratorio-SNR
Estudiando el comportamiento de una señal RF en ambientes outdoor e indoor
La Figura X.  muestra dos diagramas de caja que representan las mediciones SNR para una emisora de radiodifusión en FM a 103.5MHz en dos escenarios diferentes: al aire libre – outdoor, y a nivel de interiores – Indoor; en un laboratorio. 

El diagrama Outdoor muestra una SNR más alta con una mediana de aproximadamente 
23.57dB. Los cuartiles superior e inferior se encuentran alrededor de 23.93 dB 
y 22.83 dB respectivamente, lo que indica una variabilidad relativamente baja 
en las mediciones dentro de un rango pequeño. En la representación Indoor que 
tuvo lugar en un laboratorio Telecomunicaciones del ITM, se puede observar una 
SNR significativamente más baja con una mediana de 12.76 dB. Los cuartiles 
superior e inferior son aproximadamente 13.9225 dB y 12.23 dB respectivamente, 
lo que evidencia una variabilidad mucho más baja que en el escenario Outdoor. 


# Valores Atípicos  

Para este primer caso usamos las ecuaciones generales tomadas de  :  

IQR = qU−qL
𝐼
𝑄
𝑅
 
=
 
𝑞
𝑈
−
𝑞
𝐿
 
                                 
(1).
1
.
 
 

AtipicoInferior= qL−1.5(IQR)
𝐴
𝑡
𝑖
𝑝
𝑖
𝑐
𝑜
𝐼
𝑛
𝑓
𝑒
𝑟
𝑖
𝑜
𝑟
=
 
𝑞
𝐿
−
1
.
5
𝐼
𝑄
𝑅
 
                                                                          
(2).
2
.
 
 

AtipicoSuperior= qU+1.5(IQR)
𝐴
𝑡
𝑖
𝑝
𝑖
𝑐
𝑜
𝑆
𝑢
𝑝
𝑒
𝑟
𝑖
𝑜
𝑟
=
 
𝑞
𝑈
+
1
.
5
𝐼
𝑄
𝑅
 
                                                                          
(3).
3
.
 
              

 

La línea por encima del boxplot es sospechosamente larga. Esto sugiere el concepto de un valor atípico, un valor que está a más de 1.5 veces el IQR por encima o por debajo del boxplot; donde 1.5 es puramente convencional.  

Un valor atípico indica que algo podría haber salido mal en la recopilación de los datos, o simplemente valores singulares de la muestra. 

 

Escenario Outdoor 

Tenemos n=21 y por lo tanto 
qM=X11=23.57 dB
𝑞
𝑀
=
𝑋
11
=
23
.
57
 
𝑑
𝐵
 
                                   (Si el número de valores del conjunto es impar, entonces 
qM
𝑞
𝑀
 
      es el valor más central cuando se ordenan los datos). 

La dispersión de valores se puede medir por el rango 
R=xmax−xmin
𝑅
=
𝑥
𝑚
𝑎
𝑥
−
𝑥
𝑚
𝑖
𝑛
 
,                           

el valor máximo menos el valor mínimo. Entonces tenemos 
R=25.55 dB−21.26 dB  
𝑅
=
25
.
55
 
𝑑
𝐵
−
21
.
26
 
𝑑
𝐵
 
 
 
 

Una mejor información sobre la dispersión la proporciona el rango intercuartílico 
IQR=qU−qL
𝐼
𝑄
𝑅
=
𝑞
𝑈
−
𝑞
𝐿
 
. 

Aquí 
qU 
𝑞
𝑈
 
 
    es el valor más central de los valores en los datos por encima de la mediana, y 
qL 
𝑞
𝐿
 
 
     es el valor más central de los valores en los datos por debajo de la mediana. Por lo tanto, en (2) tenemos: 

qU=23.93 dB 
𝑞
𝑈
=
23
.
93
 
𝑑
𝐵
 
 
,                            

qL= 22.83 dB
𝑞
𝐿
=
 
22
.
83
 
𝑑
𝐵
 
,                           luego 
IQR=23.93 dB − 22.83 dB 
𝐼
𝑄
𝑅
=
23
.
93
 
𝑑
𝐵
 
−
 
22
.
83
 
𝑑
𝐵
 
 
 

El boxplot en la Figura X se extiende verticalmente desde 
qL
𝑞
𝐿
 
    hasta 
qU
𝑞
𝑈
 
;   tiene una altura 

IQR=1.1 dB  
𝐼
𝑄
𝑅
=
1
.
1
 
𝑑
𝐵
 
 
 
 

Las líneas verticales por debajo y por encima del boxplot se extienden desde 

 
Xmin=21.26 dB
𝑋
𝑚
𝑖
𝑛
=
21
.
26
 
𝑑
𝐵
 
                                 hasta 
Xmax=25.55 dB
𝑋
𝑚
𝑎
𝑥
=
25
.
55
 
𝑑
𝐵
 
,                               de modo que muestran 
R=4.29 dB 
𝑅
=
4
.
29
 
𝑑
𝐵
 
 
. 

 

Valores Atípicos Escenario Outdoor 

AtipicoInferior= 22.83 dB−1.5(1.1 dB)
𝐴
𝑡
𝑖
𝑝
𝑖
𝑐
𝑜
𝐼
𝑛
𝑓
𝑒
𝑟
𝑖
𝑜
𝑟
=
 
22
.
83
 
𝑑
𝐵
−
1
.
5
1
.
1
 
𝑑
𝐵
 
 

AtipicoInferior= 21.18 dB
𝐴
𝑡
𝑖
𝑝
𝑖
𝑐
𝑜
𝐼
𝑛
𝑓
𝑒
𝑟
𝑖
𝑜
𝑟
=
 
21
.
18
 
𝑑
𝐵
 
 

 

AtipicoSuperior= 23.93 dB+1.5(1.1 dB)
𝐴
𝑡
𝑖
𝑝
𝑖
𝑐
𝑜
𝑆
𝑢
𝑝
𝑒
𝑟
𝑖
𝑜
𝑟
=
 
23
.
93
 
𝑑
𝐵
+
1
.
5
1
.
1
 
𝑑
𝐵
 
 

AtipicoSuperior=25.58 dB
𝐴
𝑡
𝑖
𝑝
𝑖
𝑐
𝑜
𝑆
𝑢
𝑝
𝑒
𝑟
𝑖
𝑜
𝑟
=
25
.
58
 
𝑑
𝐵
 
 

 
 

Escenario Indoor 

Tenemos también 
n = 21 
𝑛
 
=
 
21
 
 
,         no se toma la regla cuando el número de valores del conjunto es impar. Para este caso se utiliza Numpy, librería de Python para cálculo científico ya que los datos difieren por escalas muy pequeñas.  

Se obtiene 
qM=np.median(data['SNR'])=12.76 dB
𝑞
𝑀
=
𝑛
𝑝
.
𝑚
𝑒
𝑑
𝑖
𝑎
𝑛
𝑑
𝑎
𝑡
𝑎
′SNR′
=
12
.
76
 
𝑑
𝐵
 
,                                                                    como valor más central cuando los datos son ordenados. La dispersión R para esta condición Indoor se evidencia como valor de dispersión: 

R = Xmax −Xmin
𝑅
 
=
 
𝑋
𝑚
𝑎
𝑥
 
−
𝑋
𝑚
𝑖
𝑛
 
,                               el valor máximo menos el valor mínimo. Entonces tenemos; 

R = 14.55 dB − 11.05 dB = 3.5 dB 
𝑅
 
=
 
14
.
55
 
𝑑
𝐵
 
−
 
11
.
05
 
𝑑
𝐵
 
=
 
3
.
5
 
𝑑
𝐵
 
 
 

  

El rango intercuartílico 
IQR = qU−qL
𝐼
𝑄
𝑅
 
=
 
𝑞
𝑈
−
𝑞
𝐿
 
.                         . En este escenario según la Figura X  

qU= 13.9225 dB
𝑞
𝑈
=
 
13
.
9225
 
𝑑
𝐵
 
                                  y  
qL= 12.23 dB
𝑞
𝐿
=
 
12
.
23
 
𝑑
𝐵
 
                         ,  luego 
IQR = 1.6925 dB 
𝐼
𝑄
𝑅
 
=
 
1
.
6925
 
𝑑
𝐵
 
 
.  

  

Valores Atípicos Escenario Indoor  

AtipicoInferior= 12.23 dB−1.5(1.6925 dB)
𝐴
𝑡
𝑖
𝑝
𝑖
𝑐
𝑜
𝐼
𝑛
𝑓
𝑒
𝑟
𝑖
𝑜
𝑟
=
 
12
.
23
 
𝑑
𝐵
−
1
.
5
1
.
6925
 
𝑑
𝐵
 
 

AtipicoInferior= 9.69125 dB
𝐴
𝑡
𝑖
𝑝
𝑖
𝑐
𝑜
𝐼
𝑛
𝑓
𝑒
𝑟
𝑖
𝑜
𝑟
=
 
9
.
69125
 
𝑑
𝐵
 
  

  

AtipicoSuperior= 13.9225 dB +1.5(1.6925 dB)
𝐴
𝑡
𝑖
𝑝
𝑖
𝑐
𝑜
𝑆
𝑢
𝑝
𝑒
𝑟
𝑖
𝑜
𝑟
=
 
13
.
9225
 
𝑑
𝐵
 
+
1
.
5
1
.
6925
 
𝑑
𝐵
 
 

AtipicoSuperior= 16.46125 dB
𝐴
𝑡
𝑖
𝑝
𝑖
𝑐
𝑜
𝑆
𝑢
𝑝
𝑒
𝑟
𝑖
𝑜
𝑟
=
 
16
.
46125
 
𝑑
𝐵
 
 

 

 