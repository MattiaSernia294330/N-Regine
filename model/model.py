import copy


class Model:
    def __init__(self):
        self._N_soluzioni=0
        self._soluzioni=[]

    def risolvi_n_regine(self,N):
        self._ricorsione([], N)
    def _ricorsione(self, parziale, N):
        #condizione terminale
        if len (parziale)==N:
            #print (parziale)
            if self._soluzione_nuova(parziale):
                self._N_soluzioni+=1
                self._soluzioni.append(copy.deepcopy(parziale))
        else :
            for row in range(N):
                for col in range(N):
                    parziale.append((row,col))
                    if self._regina_ammissibile(parziale):
                        self._ricorsione(parziale, N)
                    parziale.pop()
    def _regina_ammissibile(self,parziale):
        if len(parziale)==1:
            return True
        else :
            ultima_regina=parziale[-1]
            for regina in parziale[:len(parziale)-1]:
                #controllare righe
                if ultima_regina[0]==regina[0]:
                    return False
                if ultima_regina[1]==regina[1]:
                    return False
                if (ultima_regina[0]-ultima_regina[1]==regina[0]-regina[1]):
                    return False
                if (ultima_regina[0]+ultima_regina[1]==regina[0]+regina[1]):
                    return False
            return True
    def _soluzione_nuova(self,parziale):
        for soluzione in self._soluzioni:
            for regina in parziale:
                if regina in soluzione:
                    return False
        return True

if __name__ == '__main__':
    model = Model()
    model.risolvi_n_regine(10 )
    print(model._N_soluzioni)