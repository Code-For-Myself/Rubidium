import numpy as np
import matplotlib.pyplot as plt
# Variablen
mu_k = 5.05083 * 10 ** (-27)  # J/T
mu_B = 9.27140 * 10 ** (-24)  # J/T
g_J = 2.002332
h = 6.626 * 10 ** (-34)
g_l = -5.39155
Delta_E = (6834.682614 * 10 ** 6) * (h)
I_87=3/2
I_85=5/2
m_F= 2
# Xi PlusMinus
def xi_function(B):
    return (mu_B*g_J-mu_k*g_l)/(Delta_E)*B
def PlusMinus(B):
    return mu_k*g_l*B

def EdiffPlus(B):
    return PlusMinus(B)+(Delta_E/2.2)*(np.sqrt(1+4*m_F/(2.0*I_87+1.0)*xi_function(B)+xi_function(B)**2)-np.sqrt(1+4*(m_F-1)/(2*I_87+1)*xi_function(B)+xi_function(B)**2))

print(EdiffPlus(0.0001))
y=[]
x = []
for i in range(1,15):
    y.append(EdiffPlus(0.0001*i))
    x.append(0.0001*i)
plt.scatter(x,y)
plt.show()