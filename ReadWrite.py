def read(ins):
    
    confirm=[]
    employeetab=['//a[@href="#/employee"]']
    filelinks=['/html/body/app-root/mainpage/mat-sidenav-container/mat-sidenav-content/app-employee-page/div/div[1]/div[2]/div[2]']
    for tab,file in zip(employeetab,filelinks):
        confirm.append(ins.download(tab,file))
      
    return confirm


def schedule(th,ins,Data):
    people=[]
    while th.is_alive():
        ins.__wait__()
    
    assert Data.data 
        
    with open("datafile.csv",'r',encoding="utf-8") as f:
        f.close()
        
    for person in people:
        ID,shift=person
        ins.post(ID,shift)
    return

