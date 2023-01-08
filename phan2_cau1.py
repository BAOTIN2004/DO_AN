import numpy as np
def cau1 (m,n):
    x=np.random.randint(-10,10,n)
    A=np.random.randint(-10,10,(m,n))
    print(f"Vector x:\n{x}\nMa trận A:\n{A}")
    print(f"Kết quả phép nhân vector x với ma trận A:\n {x*A}")

def cau2(m,n):
    A=np.random.randint(-10,10,(m,n))
    B=np.random.randint(-10,10,(m,n))
    print("Ma trận A:\n",A,"\nMa trận B:\n",B)
    print(f'Kết quả phép nhân ma trận A với ma trận B:\n',A@B)
    print("Kết quả phép nhân ma trận chuyển vị của ma trận A với ma trận B:\n",(A.T)@B)

def main():
    cau1(2,4)
    cau2(3,3)
if __name__=="__main__":
    main()
