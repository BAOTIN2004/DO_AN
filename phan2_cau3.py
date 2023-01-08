import matplotlib.pyplot as plt
import numpy as np
def ham_so(x):
    y=x**4-2*x**2-3
    return y
def dao_ham_cap_1(x):
    y=4*x**3-4*x
    return y
def dao_ham_cap_2(x):
    y=12*x**2-4
    return y
def dao_ham_cap_3(x):
    y=24*x
    return y

def main():
    x=np.linspace(-10,10,100)
    y=ham_so(x)
    y1=dao_ham_cap_1(x)
    y2=dao_ham_cap_2(x)
    y3=dao_ham_cap_3(x)
    fig,ax=plt.subplots()
    ax.plot(x,y,'.',label=r'$y=x^4-2x^2-3$')
    ax.plot(x,y1,'*',label=r"$y'=4x^3-4x$")
    ax.plot(x,y2,'+',label=r"$y''=12x^2-4$")
    ax.plot(x,y3,'_',label=r"$y'''=24x$")
    ax.set_xlabel("Trục x")
    ax.set_ylabel("Trục y")
    ax.set_title("Đồ thị hàm số")
    ax.legend()
    plt.show()
if __name__=="__main__":
    main()