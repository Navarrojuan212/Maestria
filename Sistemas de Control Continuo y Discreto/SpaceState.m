syms V R1 R2 L1 L2 L3 I1 I2 I3 dI1 dI2 dI3 dVc Vc C s


EQ1=-V+R1*(I1-I3)+R2*(I1-I2)+L1*(dI1-dI2)==0;
EQ2=L2*(dI2-dI3)+L3*dI2+R2*(I2-I1)+L1*(dI2-dI1)==0;
EQ3=Vc+L2*(dI3-dI2)+R1*(I3-I1)==0;
EQ4=dVc==I3/C

R=solve([EQ1,EQ2,EQ3,EQ4], [dI1,dI2,dI3,dVc])
%%
dX=[R.dI1,R.dI2,R.dI3,R.dVc];
X=[I1,I2,I3,Vc];
U=[V];
Y=[I1,I2,I3,Vc];

Am = jacobian(dX,X)
Bm = jacobian(dX,U)
Cm = jacobian(Y,X)
Dm = jacobian(Y,U)
%%
%FUNCION DE TRANSFERENCIA
syms s

SI = s*eye(4) %MATRIZ IDENTIDAD 4x4
Gs = Cm*((SI-Am)^(-1))*Bm + Dm

Gs=simplify(Gs)

%%
%LINEALIZAR EN EL PUNTO DE OPERACION DESEADO
R1=1;
R2=1;
L1=2;
L2=4;
L3=3;
C=1;

Am = eval(Am)
Bm = eval(Bm)
Cm = eval(Cm)
Dm = eval(Dm)
%%
sys=ss(Am,Bm,Cm,Dm)
step(sys)

%%
%OBTENER LA FT DE FORMA NUMERICA
Input=1;
[Num,Den] = ss2tf(Am,Bm,Cm,Dm,Input)

GI1_V = tf(Num(1,:),Den)%FT DE SALIDA i1 RESPECTO A V.
GI2_V = tf(Num(2,:),Den)%FT DE SALIDA i2 RESPECTO A V.
GI3_V = tf(Num(3,:),Den)%FT DE SALIDA i2 RESPECTO A V.
GVc_V = tf(Num(4,:),Den)%FT DE SALIDA i2 RESPECTO A V.

step(GVc_V)