import numpy as np, matplotlib.pyplot as plt
X,Y = np.meshgrid( np.arange(-4,4,.2), np.arange(-4,4,.2) ) # The fields
Ex = (X + 1)/((X+1)**2 + Y**2) - (X - 1)/((X-1)**2 + Y**2)
Ey = Y/((X+1)**2 + Y**2) - Y/((X-1)**2 + Y**2)
plt.figure()
plt.streamplot(X,Y,Ex,Ey)
plt.title('Streamplot')
plt.figure()
plt.quiver(X,Y,Ex,Ey,scale=50)
plt.title('Quiver')
