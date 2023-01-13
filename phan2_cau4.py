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
    
def hinh_cau():
    u = np.linspace(0, np.pi, 100)
    v = np.linspace(0, 2*np.pi, 100)
    r=2
    x = r*np.outer(np.cos(u), np.sin(v)) - 2
    y = r*np.outer (np.sin(u), np.sin(v))  + 1
    z = r*np.outer(np.ones(np.size(u)), np.cos(v))  + 4
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    hc= ax.plot_surface(x, y, z, cmap=cm.PuBu, linewidth=0)
    fig.colorbar (hc, shrink=0.6, aspect=30)
    ax.set_xlabel("Trục x")
    ax.set_ylabel("Trục y")
    ax.set_zlabel("Trục z")
    ax.set_title("Đồ thị mặt hình cầu")
    plt.show()
def main():
    x1=np.linspace(-9.5,9.5,10000)
    y1=np.linspace(-9.5,9.5,10000)
    x2=np.linspace(-6,6,10000)
    y2=np.linspace(-9,9,10000)
    do_thi_mat_yen_ngua(x1, y1)
    do_thi_mat_mat_hyperbolic_1_tang(x2,y2)
    hinh_cau()
if __name__=="__main__":
    main()