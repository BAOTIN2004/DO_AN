from sympy import*

def giai_he_phuong_trinh():
    x,y,z=symbols('x y z')
    pt1=Eq(2*x-5*y+z ,-5)
    pt2=Eq(4*x+2*y-2*z,2)
    pt3=Eq(x+y-z,0)
    kq=solve((pt1,pt2,pt3),(x,y,z))
    print(kq)
    
def tinh_gioi_han():
    x=symbols('x')
    y=(x**3-3*x**2)**(1/3)+sqrt(x*x-2*x)
    kq=limit(y,x,+00)
    print(kq)
    
def tinh_dao_ham(a,b):
    x=symbols('x')
    y=(a*x-1)/(b*x+2)
    kq=diff(y,x)
    print(kq)
    
def tinh_nguyen_ham():
    x=symbols('x')
    y=x/(x*x+1)
    kq=integrate(y,x)
    print(kq)
    
def tinh_tich_phan():
    x=symbols('x')
    y=(1-tan(x)*x)/(x**2*cos(x)+x)
    y1=x*x
    kq=integrate(y,(x,pi,2*pi/3))
    print(kq)
    
def main():
    giai_he_phuong_trinh()
    tinh_gioi_han()
    tinh_dao_ham(2,1)
    tinh_nguyen_ham()
    tinh_tich_phan()
if __name__=="__main__":
    main()