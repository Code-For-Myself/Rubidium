import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data1 = pd.read_csv('File4.csv', sep=',')

def Scatterer(Pfad, i):
    data1 = pd.read_csv(Pfad, sep=',')
    a = 200
    b = 225
    x = data1["f/MHz"]
    y = data1["AbsorbSpectrum"]
    g= min(y[a:b])
    l =max(y[a:b])
    c = min(y)
    d = max(y)
    SNR = (l-g)/(2*(d-c))
    plt.scatter(x, y)
    plt.axvline(x=x[200], linewidth=2, color='k')
    plt.axvline(x=x[225], linewidth=2, color='k')
    plt.show()
    print('Signal', i, SNR)
    return i, SNR

index = []
snratio = []
for i in range(0, 18):
        x,y = Scatterer('File'+ str(i+1) + '.csv', i+1)
        index.append(x)
        snratio.append(y)


plt.bar(index, snratio)
plt.ylabel('signal-noise-ratio')
plt.xlabel('Signalnummer')
plt.xticks(np.arange(19))
#plt.savefig('SNRMessung2.png')
plt.show()
df = pd.DataFrame({'Signalnummer': index,
                   'Signal-Noise-Ratio': snratio,
                  })



#df = df.style.format(decimal=',', thousands='.', precision=3)
#df.to_csv('SNR_Messung2.txt', sep=',', index=False)
