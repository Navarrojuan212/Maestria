%% 
syms F B1 B2 B3 Xa Xb K1 K2 M1 M2 s

EQ1= F+Xa*(-B3*s-K1-B1*s-M1*s^2)+B3*s*Xb==0
EQ2=Xb*(-B3*s-B2*s-K2-M2*s^2)+B3*s*Xa==0
S=solve([EQ1, EQ2], unique([Xa, Xb]))
S.Xa
S.Xb