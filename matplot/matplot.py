import matplotlib.pyplot as plt
import numpy as np
'''
xpoints=np.array([0,6])
ypoints=np.array([0,250])

#change axis 
xpoints=np.array([20,100])
ypoints=np.array([20,80])
plt.plot(xpoints,ypoints,'o')


#markers 
ypoints=np.array([3,8,1,10])
plt.plot(ypoints,marker = 'o')

#dotted line represneted by : and colour red by r 
plt.plot(ypoints,'o:r')

#marker size (ms) #marker colour (mec) # face colour (mfc)
plt.plot(ypoints, marker = 'o', ms = 5,mec = 'g',mfc = 'hotpink')

#linestyle and color and linewidth
plt.plot(ypoints, linestyle= 'dashdot',color = 'r',linewidth=40)



#plotting two lines 
x1=np.array([0,1,2,3])
y1=np.array([3,8,1,10])
x2=np.array([0,1,2,3])
y2=np.array([6,2,7,11])
plt.plot(x1,y1,x2,y2)

#for two lines
plt.plot(y1)
plt.plot(y2)


x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x,y)
#changing fonts
font1 = {'family':'serif','color':'blue','size':30}
font2 = {'family':'serif','color':'darkred','size':20}

#addint titles and labels with fonts 
plt.xlabel('Average pulse',fontdict=font2 )
plt.ylabel('Calorie burnage',fontdict=font2 )
#moving title left and right
plt.title('sports watch data',fontdict=font1,loc = 'center' )

#subplots

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 1)
plt.plot(x,y)
plt.title('plot 1',size='10')
plt.grid(color = 'green',linestyle='--',linewidth=0.5)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 2)
plt.plot(x,y)
plt.title('plot 2',size='10')
plt.grid(color = 'green',linestyle='--',linewidth=0.5)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 3)
plt.plot(x,y)
plt.title('plot 3',size='10')
plt.grid(color = 'green',linestyle='--',linewidth=0.5)


x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 4)
plt.plot(x,y)
plt.title('plot 4',size='10')
plt.grid(color = 'green',linestyle='--',linewidth=0.5)

x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(2, 3, 5)
plt.plot(x,y)
plt.title('plot 5',size='10')
plt.grid(color = 'green',linestyle='--',linewidth=0.5)

x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(2, 3, 6)
plt.plot(x,y)
plt.title('plot 6',size='10')
plt.grid(color = 'green',linestyle='--',linewidth=0.5)



#scatter 
x=np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y=np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])
plt.scatter(x,y, c=colors ,cmap='rainbow',s=sizes,alpha=0.5)
#adding the colorbar key
plt.colorbar()
#comparing scatter

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x,y,color='hotpink')

#random scatter chart
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
'''

#bar charts
x=np.array(["A", "B", "C", "D"])
y=np.array([3, 8, 1, 10])
plt.bar(x,y,color='hotpink',width='0.9')





#adding grid and  binding it to x or y axis (axis = 'x')
#plt.grid(color = 'green',linestyle='--',linewidth=0.5)

#supertitle for the subplots
plt.suptitle('SUPERTITLE',size='20')
#shows the chart and saves it as a png to view 
print(plt.show())
plt.savefig('Graph.png')