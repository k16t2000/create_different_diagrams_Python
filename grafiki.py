import matplotlib
import numpy as np
import matplotlib.pyplot as plt

#parabola
x=np.arange(-8,5,0.5) #na4 zna4enie, kone4noe, shag
#sama funkzija y=|x**2 + 4x - 5|
y=abs(x**2+4*x-5)

#dobovlaem liniju
y2=[9]*len(x)#sdvigaem liniju na osi x na 9,4tobi bilo vidno


#koordinatnaja ploskost
plt.subplots()

#zagolovok
plt.title("y=abs(x**2+4*x-5)")

#koordinat ploskost
plt.xlabel("ось OX")#x avtomati4eski pole ot 0 do 1
plt.ylabel("ось OY")#y

#grid-setka
plt.grid(True)

#dobavim fukziju na koordinatnoj ploskosti
plt.plot(x,y,'--k',linewidth=5,label="Парабола")#''- obozna4aem kakuju liniju hotim, zvet eto pervaja bukva zveta(r-red)
plt.plot(x,y2,'-.b',marker="+",linewidth=2,label="Прямая")#-.-eto shtrih punktir

#legenda
plt.legend()
#tekst
plt.text(-4,30,"Изучаем графику:\nПарабола,\nПрямая")#1-ge hotim videt na4alo teksta,po y-30
#anotazija s dop elementom
#r-redaktiruem tekst,$oformlenie drobej$frac-drob,xy-to4ki gde budet,xytekst-gde budet nahoditsa, arrowprops-strelka, napravlenie idet k xy(-2,9)
plt.annotate(r"Вершина параболы:$\frac{-b}{2a}=\frac{-4}{2}=-2$",xy=(-2,9),xytext=(-5,15), arrowprops=dict(facecolor="black"))

#sohranit vo vremja prozessa figuru
plt.savefig("image.png")
#osj ox dolzna izobrazit liniju
plt.show()

#krugovaja diagramma
data=[
    ["Питание", 484.7],
    ["Одежда", 691.6],
    ["Учеба", 221.2],
    ["Прочие", 59.4],
    ["Доходы от продажи имущества", 26.7],
    ["Безвозмездные поступления", 75.7]
]
values=[x[1] for x in data]
labels=[x[0] for x in data]
plt.pie(values, labels=labels,autopct="%.1f%%", radius=0.7)
plt.show()

#-------------------------------------------------------------------------------
#diagramma s osju i figuroj
title="Kinokülastased, 2008-2018"
fig,(ax1,ax2)=plt.subplots(ncols=2)#v 1 okne 2 diagrammi, ncols-2kolonki, 1 goriz, dr-vertikalnaja
fig.canvas.set_window_title(title)#canva-ploskost

#figuri
ax1.set_xlabel("Aastat")
ax1.set_ylabel("100 elaniku kohta arv")
ax2.set_ylabel("Aastat")
ax2.set_xlabel("100 elaniku kohta arv")
#zna4enija
data=[
    [2008,127],
    [2009,128],
    [2010,158],
    [2011,175],
    [2012,186],
    [2013,194],
    [2014,198],
    [2015,235],
    [2016,250],
    [2017,267],
    [2018,275]
]
#v bar ukazat dlinu stolbikov, kol-vo stolbikov i labels
size=[x[1] for x in data]
nums=[x+1 for x in range(len(size))]#t k ne s 0, berem so zna4eniem size
tick_label=[(x[0]%100) for x in data]#goda
#izobrazaem 1ju liniju
ax1.bar(nums,size,tick_label=tick_label,width=0.5,color="#a500ff")
ax2.barh(nums,size,tick_label=tick_label,height=0.7,color="#e600ff")#gorizontalnie zna4enija-barh

plt.show()
