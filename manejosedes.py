import os, csv
import frmPrincipal

def validarSede(mtzsede):
    auxreader = []
    if os.stat('listadosedes.csv').st_size==0:
        guardarSede(mtzsede)
    else:
        with open('listadosedes.csv', 'r', encoding="utf8") as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                auxreader.append(row)
        f.close()
        
        #print(len(auxreader))
        for i in range(len(auxreader)):
            if auxreader[i][0] == mtzsede[0]:
                return(True)
        #endfor
        return(False)
                
    #endif

def guardarSede(mtzsede):
    with open('listadosedes.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        writer.writerow([mtzsede[0],
                        mtzsede[1],
                        mtzsede[2],
                        mtzsede[3],
                        mtzsede[4],
                        mtzsede[5],
                        mtzsede[6],
                        mtzsede[7],
                        mtzsede[8],
                        mtzsede[9]])
    csvfile.close()
    
    return(True)

def actualizarSedes():
    auxreader = []
    if os.stat('listadosedes.csv').st_size==0:
        mtzactualizarsedes = ["0","0","0","0","0","0","0","0","0","0"]
        auxreader.append(mtzactualizarsedes)
        return(auxreader)
    else:
        with open('listadosedes.csv', 'r', encoding="utf8") as f:
            reader = csv.reader(f, delimiter=',')
            reader.line_num
            for row in reader:
                auxreader.append(row)
        f.close()
        #for row in auxreader:
            #print(row, end='\n')
        return(auxreader)

def cantidadSedes():
    mtzsubRegion = [["BAJO CAUCA",0],
                    ["MAGDALENA MEDIO",0],
                    ["NORDESTE",0],
                    ["NORTE",0],
                    ["OCCIDENTE",0],
                    ["ORIENTE",0],
                    ["SUROESTE",0],
                    ["URABA",0],
                    ["VALLE DEL ABURRA",0]]
    cantBajoCauca = 0
    cantMagdalenaMedio = 0
    cantNordeste = 0
    cantNorte = 0
    cantOccidente = 0
    cantOriente = 0
    cantSurOeste = 0
    cantUraba = 0
    cantValleAburra = 0
    auxreader = []
    cantSedes = 0
    with open('listadosedes.csv', 'r', encoding="utf8") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            auxreader.append(row)
    f.close()
    for i in range(len(auxreader)):
        if auxreader[i][5]=="BAJO CAUCA":
            cantBajoCauca += 1
            mtzsubRegion[0][1] = cantBajoCauca
        if auxreader[i][5]=="MAGDALENA MEDIO":
            cantMagdalenaMedio += 1
            mtzsubRegion[1][1] = cantMagdalenaMedio
        if auxreader[i][5]=="NORDESTE":
            cantNordeste += 1
            mtzsubRegion[2][1] = cantNordeste
        if auxreader[i][5]=="NORTE":
            cantNorte += 1
            mtzsubRegion[3][1] = cantNorte
        if auxreader[i][5]=="OCCIDENTE":
            cantOccidente += 1
            mtzsubRegion[4][1] = cantOccidente
        if auxreader[i][5]=="ORIENTE":
            cantOriente += 1
            mtzsubRegion[5][1] = cantOriente
        if auxreader[i][5]=="SUROESTE":
            cantSurOeste += 1
            mtzsubRegion[6][1] = cantSurOeste
        if auxreader[i][5]=="URABA":
            cantUraba += 1
            mtzsubRegion[7][1] = cantUraba
        if auxreader[i][5]=="VALLE DEL ABURRA":
            cantValleAburra += 1
            mtzsubRegion[8][1] = cantValleAburra
    cantSedes = len(auxreader)
    return(cantSedes,mtzsubRegion)

def buscarSede(buscarDaneSede):
    auxreader = []
    mtzResult = []
    with open('listadosedes.csv', 'r', encoding="utf8") as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            auxreader.append(row)
    f.close()
    
    for i in range(len(auxreader)):
        if auxreader[i][0] == buscarDaneSede:
            mtzResult[0] = auxreader[i][1]
            mtzResult[1] = auxreader[i][2]
            mtzResult[2] = auxreader[i][3]
            mtzResult[3] = auxreader[i][4]
            mtzResult[4] = auxreader[i][5]
            mtzResult[5] = auxreader[i][6]
            mtzResult[6] = auxreader[i][7]
            mtzResult[7] = auxreader[i][8]
            mtzResult[8] = auxreader[i][9]
            return(mtzResult)
        else:
            mtzResult[0] = 'No se encuentra la sede'
            mtzResult[1] = 'No se encuentra la sede'
            mtzResult[2] = 'No se encuentra la sede'
            mtzResult[3] = 'No se encuentra la sede'
            mtzResult[4] = 'No se encuentra la sede'
            mtzResult[5] = 'No se encuentra la sede'
            mtzResult[6] = 'No se encuentra la sede'
            mtzResult[7] = 'No se encuentra la sede'
            mtzResult[8] = 'No se encuentra la sede'
            return(mtzResult)