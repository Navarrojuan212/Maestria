clear all
syms vg vC iL L C d R dvC diL

diL=vg/L-(vC*(1-d))/L;
dvC=-vC/(R*C)+(iL*(1-d))/C;

dX=[diL;dvC] %derivadas de las variables de estado
X=[iL;vC]  %vector variables de estado
U=[d;vg]  %vector de entradas
Y=[iL;vC]  %vector de salida

%% Definición de las matroces del SS
Am=jacobian(dX,X)
Bm=jacobian(dX,U)
Cm=jacobian(Y,X)
Dm=jacobian(Y,U)

%% Encontramos los valores del punto de operación
[VC,IL]=solve([diL==0,dvC==0],[vC,iL])
%VC=S.vC
%IL=S.iL
%%
L=1e-6;
C=22e-6;
R=20;
vg=10;
d=0.5;

iL=eval(IL)
vC=eval(VC)

Am=eval(Am)
Bm=eval(Bm)
Cm=eval(Cm)
Dm=eval(Dm)

%%
%FUNCION DE TRANSFERENCIA
syms s

SI = s*eye(2) %MATRIZ IDENTIDAD 2x2
Gs = Cm*((SI-Am)^(-1))*Bm + Dm

Gs=simplify(Gs)
%% SS->Space State
sys=ss(Am,Bm,Cm,Dm)
step(sys)