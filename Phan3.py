class NhanVien():
    def __init__(self, hoten:str, tuoi:int,luong:str):
        self.hoten=hoten
        self.tuoi=tuoi
        self.luong=luong
    def __str__(self):
        nv=f'[Họ và tên: {self.hoten}; Tuổi: {self.tuoi}; Lương: {self.luong}$]'
        return nv
    def __gt__(self,other):
        return (self.tuoi>other.tuoi)
    def __ge__(self,other):
        return(self.tuoi>=other.tuoi)
    def __lt__(self,other):
        return(self.tuoi<other.tuoi)
    def __le__(self,other):
        return(self.tuoi<=other.tuoi)
    def __eq__(self,other):
        return(self.tuoi==other.tuoi)
        
def nhap_du_lieu_nv():
    so=1
    Nv=[]
    while so==1:
        hoten,tuoi,luong= input('Mời bạn nhập lần lượt họ tên, tuổi, lương của nhân viên: ').split(";")
        nv=NhanVien(hoten,tuoi,luong)
        Nv.append(nv)
        so=int(input('Bấm số 1 nếu muốn tiếp tục thêm nhân viên: '))
    return Nv

def hien_thi(nv):
    for item in nv:
        print(item)

def sap_xep_nhan_vien(nv):
    sap_xep=sorted(nv,reverse=True)
    
import os,pickle
def luu_nv(a,path:str,filename:str):
    try:
        with open(os.path.join(path,filename),'ab') as f:
            print('Lưu danh sách sinh viên thành công.')
            return pickle.dump(a,f)
    except Exception as e: print(e)
    
def doc_nv(path:str,filename:str):
    try:
        with open(os.path.join(path,filename),'rb') as f:
            return pickle.load(f)
    except Exception as e: print(e)
    
def doc_nhi_phan(nv):
    for item in nv:
        print(item)
        
def main():
    path='E:\\DO_AN\\Phan3'
    filename="du_lieu_nhan_vien.txt"
    a=nhap_du_lieu_nv()
    b=hien_thi(a)
    c=sap_xep_nhan_vien(a)
    d=luu_nv(a,path,filename)
    e=doc_nv(path,filename)
    doc_nhi_phan(e)
if __name__=="__main__":
     main()