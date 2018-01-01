#自由落体句酷总和

S = 100
H = S / 2
for i in range(2, 11):
    S += H * 2
    H /= 2
print(S)