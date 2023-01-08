import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 

def do_thi_mat_yen_ngua(x,y):
    x,y=np.meshgrid(x,y)
    z=(x/3)**2-(y/2)**2
    fig, ax =plt.subplots(subplot_kw={"projection":"3d"})
    do_thi_mat_yen_ngua = ax.plot_surface(x, y, z,cmap=cm.tab20c, linewidth=0, antialiased=True)
    ax.set_xlabel("Trục x")
    ax.set_ylabel("Trục y")
    ax.set_zlabel("Trục z")
    fig.colorbar( do_thi_mat_yen_ngua, shrink=0.7,aspect=50)
    ax.set_title("Đồ thị mặt yên ngựa")
    plt.show()

def do_thi_mat_mat_hyperbolic_1_tang(x,y):
    x,y=np.meshgrid(x,y)
    z1=2*np.sqrt((x/3)**2+(y/5)**2-1)
    z2=-2*np.sqrt((x/3)**2+(y/5)**2-1)
    fig,ax =plt.subplots(subplot_kw={"projection":"3d"})
    ax.plot_surface(x,y,z1,cmap=cm.tab20c,linewidth=0, antialiased=False)
    ax.plot_surface(x,y,z2,cmap=cm.tab20c,linewidth=0, antialiased=False)
    ax.set_xlabel("Trục x")
    ax.set_ylabel("Trục y")
    ax.set_zlabel("Trục z")
    ax.set_title("Đồ thị hyperbolic 1 tầng")
    plt.show()
    
def hinh_cau(x,y):
    x,y=np.meshgrid(x,y)
    z1=(4-(x+2)**2-(y-1)**2)**(1/2)+4
    z2=-(4-(x+2)**2-(y-1)**2)**(1/2)+4
    fig,ax =plt.subplots(subplot_kw={"projection":"3d"})
    ax.plot_surface(x, y, z1,cmap=cm.tab20c, linewidth=0)
    ax.plot_surface(x, y, z2,cmap=cm.tab20c, linewidth=0)
    ax.set_xlabel("Trục x")
    ax.set_ylabel("Trục y")
    ax.set_zlabel("Trục z")
    ax.set_title("Hình cầu")
    plt.show()
def main():
    x1=np.linspace(-9.5,9.5,10000)
    y1=np.linspace(-9.5,9.5,10000)
    x2=np.linspace(-6,6,10000)
    y2=np.linspace(-9,9,10000)
    x3= np.linspace(-4,0,10000)
    y3=np.linspace(-1,3,10000)
    do_thi_mat_yen_ngua(x1, y1)
    do_thi_mat_mat_hyperbolic_1_tang(x2,y2)
    hinh_cau(x3,y3)
if __name__=="__main__":
    main()