syms V I1 I2 VL s
EQ1 = -V + I1*2*s + 2*(I1-I2)==0
EQ2 = 2*(I2-I1) + 2*I2 + 2*s*I2 == 0
EQ3 = VL == 2*s*I2

R = solve([EQ1,EQ2,EQ3],[I1,I2,VL])
R.VL

%%
clear s
s = tf('s')
G = s/(s^2 + 3*s + 1)
step(G)

%%
syms V I1 I2 VL s

EQ1 = -V + 2*I1 + (I1/s) +2*(I1-I2) + (I1-I2)/s  ==0
EQ2 = (I2-I1)/s + 2*(I2-I1) + 2*I2 + VL == 0
EQ3 = VL == 2*s*I2

R = solve([EQ1,EQ2,EQ3],[I1,I2,VL])
R.VL
%%
clear s
s = tf('s')
G = (2*s^2)/(4*s^2 + 6*s + 1)
step(G)
