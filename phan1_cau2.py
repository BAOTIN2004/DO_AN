def tao_list(a,b,n):
    import random
    lst=[random.uniform(a,b) for i in range(n)]
    return lst

def sap_xep_list(lst,rs):
    lst.sort(reverse=rs)
    return lst
    
def tim_kiem(lst):
    n=float(input('nhap so can tim:'))
    saiso=0.00001 
    vitri=[]
    for i in range(len(lst)):
       if abs(lst[i]-n)<saiso:
            vitri.append(i)
    if len(vitri)>0: print(vitri)
    else: print(f'Khong tim thay so {n} trong list')
    
def luu_list(path,filename,lst,mod):
    if mod=="vanban": mode="w"
    else: mode="wb"
    import os
    try: 
        with open(os.path.join(path,filename),mode) as f:
            f.write(str(lst))
            f.close()
    except Exception as e :print(e)

def main():
    path="E:\\DO_AN\\Phan1"
    filename1="list.txt"
    filename2="sapxep.txt"
    a=tao_list(-10,10,10)
    b=luu_list(path,filename1,a,mod="vanban")
    c=sap_xep_list(a,False)
    d=luu_list(path,filename2,sap_xep_list(a,False),mod="vanban")
    e=tim_kiem(sap_xep_list(a,False))
if __name__=="__main__":
    main()