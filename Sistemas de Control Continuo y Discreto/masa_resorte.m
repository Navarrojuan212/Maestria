%% Masa de resorte amortiguador
m = 1;
k = 1;
b = 0.2;
s = tf('s');

H = 1/(m*s^2 + b*s + k);
step(H)

%% Impulse Response
impulse(H)