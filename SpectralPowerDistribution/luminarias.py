from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import math
import numpy as np

# Programa para simular el canal VLC en una aplicación de localizción
# El ángulo de apertura luminica del LED (theta medios). 
# En la mayoria de LEDs, el ángulo de apertura es de 60 grados.
theta = 60


# Determinar el coeficiente lambertiano. 
# math.cos(math.radians(180)) //Determina el Coseno en grados
# math.cos() //Determina el Coseno en radianes

m = -math.log10(2)/math.log10(math.cos(math.radians(theta))) #Listo.!!

# Definir potencia para cada LED
P_total  = 500
P_total2 = 500
P_total3 = 500
P_total4 = 500
P_total5 = 500
P_total6 = 500
P_total7 = 500
P_total8 = 500
 
#Área física del detecto.. 1 cm2
#_______// revisar por qué no toma el exponencial normal____////////___
Adet = 10**-3

# Ganancia de un filtro óptico
Ts=1

# Indice de refraccion de la lente del PD
index = 1.5

# FOV del receptor 
FOV = 55*math.pi/180 

# Ganancia del concentrador óptico
G_Con = (index**2)/(math.sin(FOV)**2) #LISTO.!!

# Dimensión del salon en metros 
lx = 3
ly = 3
lz = 3


# Distancia entre la fuente y el plano del receptor en metros
h = 2.5

# Posición del LED
XT  = 1
YT = 0.45

XT2 = 2
YT2 = 0.45

XT3 = 2
YT3 = 1.15

XT4 = 1
YT4 = 1.15

XT5 = 2
YT5 = 1.85

XT6 = 1
YT6 = 1.85

XT7 = 2
YT7 = 2.25

XT8 = 1
YT8 = 2.55

# Número de cuadrícula en el plano del receptor 
Nx = lx*10
Ny = ly*10

# Cuadrícula del plano del receptor
#x=-lx/2:lx/Nx:lx/2
#y=-ly/2:ly/Ny:ly/2

#----------------------------REVISAR.!!!-----------------------------------------
x = np.arange(0,lx+0.1,lx/Nx)
y = np.arange(0,ly+0.1,ly/Ny)
XR, YR = np.meshgrid(x,y)

#_______Vector de distancias desde la fuente 1________
D1 =  np.sqrt((XR-XT)**2 + (YR-YT)**2  + h**2)
D2 = np.sqrt((XR-XT2)**2 + (YR-YT2)**2 + h**2)
D3 = np.sqrt((XR-XT3)**2 + (YR-YT3)**2 + h**2)
D4 = np.sqrt((XR-XT4)**2 + (YR-YT4)**2 + h**2)
D5 = np.sqrt((XR-XT5)**2 + (YR-YT5)**2 + h**2)
D6 = np.sqrt((XR-XT6)**2 + (YR-YT6)**2 + h**2)
D7 = np.sqrt((XR-XT7)**2 + (YR-YT7)**2 + h**2)
D8 = np.sqrt((XR-XT8)**2 + (YR-YT8)**2 + h**2)

# Vector de ángulos Cos(phi) en el Rx
costheta_A1 = h/D1
costheta_A2 = h/D2
costheta_A3 = h/D3
costheta_A4 = h/D4
costheta_A5 = h/D5
costheta_A6 = h/D6
costheta_A7 = h/D7
costheta_A8 = h/D8

# Para determinar el cos(phi), se puede estimar con la altura h y la
# distancia, por tanto es equivalente al Cos(tetha) pero es necesario poner
# el límite del ángulo de visión del sensor el cual es de 55° grados.
# Cosd(55)=0.5736

cosphi_A1=costheta_A1
cosphi_A2=costheta_A2
cosphi_A3=costheta_A3
cosphi_A4=costheta_A4
cosphi_A5=costheta_A5
cosphi_A6=costheta_A6
cosphi_A7=costheta_A7
cosphi_A8=costheta_A8

#####################################################################

## # # Verificar el límite del ángulo phi1
## for R=1:length(cosphi_A1)
##     for L=1:length(cosphi_A1)
##         if cosphi_A1(L,R)<0.5736 
##             cosphi_A1(L,R)=0
##         end
##     end
## end
## # verificar el límite del ángulo phi2          
## for R=1:length(cosphi_A2)
##     for L=1:length(cosphi_A2)
##         if cosphi_A2(L,R)<0.5736 
##             cosphi_A2(L,R)=0
##         end
##     end
## end            
## # verificar el límite del ángulo phi3          
## for R=1:length(cosphi_A3)
##     for L=1:length(cosphi_A3)
##         if cosphi_A3(L,R)<0.5736 
##             cosphi_A3(L,R)=0
##         end
##     end
## end 
## # verificar el límite del ángulo phi4          
## for R=1:length(cosphi_A4)
##     for L=1:length(cosphi_A4)
##         if cosphi_A4(L,R)<0.5736 
##             cosphi_A4(L,R)=0
##         end
##     end
## end 
#
#############################################################

# ___________Ganancia en DC del canal VLC para cada fuente__________
H_A1 = (m + 1)*Adet*costheta_A1**(m)*cosphi_A1/(2*math.pi*D1**2)
H_A2 = (m + 1)*Adet*costheta_A2**(m)*cosphi_A2/(2*math.pi*D2**2)
H_A3 = (m + 1)*Adet*costheta_A3**(m)*cosphi_A3/(2*math.pi*D3**2)
H_A4 = (m + 1)*Adet*costheta_A4**(m)*cosphi_A4/(2*math.pi*D4**2)
H_A5 = (m + 1)*Adet*costheta_A5**(m)*cosphi_A5/(2*math.pi*D5**2)
H_A6 = (m + 1)*Adet*costheta_A6**(m)*cosphi_A6/(2*math.pi*D6**2)
H_A7 = (m + 1)*Adet*costheta_A7**(m)*cosphi_A7/(2*math.pi*D7**2)
H_A8 = (m + 1)*Adet*costheta_A8**(m)*cosphi_A8/(2*math.pi*D8**2)

# Potencia recibida desde la fuente 1
P_rec = ((P_total*H_A1) + (P_total2*H_A2) + (P_total3*H_A3) + (P_total4*H_A4) + (P_total5*H_A5) + (P_total6*H_A6) + (P_total7*H_A7) + (P_total8*H_A8))*Ts*G_Con
P_rec_dBm = 10*np.log10(P_rec)
z = P_rec_dBm


#P_rec2=(P_total2*H_A2)+*Ts*G_Con
#P_rec2_dBm=10*log10(P_rec2)

# Gráficas
#meshc(x,y,P_rec_dBm)
#meshc(x,y,P_rec2_dBm)
#xlabel('Length (m)')
#ylabel('Width (m)')
#zlabel('Received Optical Power (dBm)')
#axis([-lx/2 lx/2 -ly/2 ly/2 min(min(P_rec_dBm)) max(max(P_rec_dBm))])
#axis([0 lx 0 ly min(min(P_rec_dBm)) max(max(P_rec_dBm))])

#Creamos la Figura
Fig = plt.figure()

#Agregamos plano 3D
ax1 = Axes3D(Fig)

# plot_wireframe nos permite agregar los datos x, y, z. Por ello 3D
# Es necesario que los datos esten contenidos en un array bi-dimensional
ax1.plot_surface(XR, YR, z, rstride=1, cstride=1,cmap='viridis', edgecolor='none')

# Añado etiquetas
plt.title('Distribution of Optical Power')
plt.xlabel('Length (m)')
plt.ylabel('Width (m)')

#Mostramos el Gráfico
plt.show()
