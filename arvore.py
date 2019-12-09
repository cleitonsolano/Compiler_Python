class NoAv(object):

    def __init__(self, val = None, typ = None):
        self.val = val
        self.typ = typ

    def getValor(self):
        return self.val

    def setValor(self, val):
        self.val = val

    def getTipo(self):
        return self.typ

    def setTipo(self, typ):
        self.typ = typ


class NoTerminalAv(object):
    vet = []
    tamanhoVetor = None

    def __init__(self, typ = None, vetor = False, tamanhoVetor = 1):
        self.typ = typ
        self.terminal = vetor
        self.vetTam = tamanhoVetor

    def inicializavet(self):
        if self.terminal == True:
            for i in range(self.vetTam):
                self.vet.insert(i, NoAv(self.typ))

    def getVet(self, posicao = None):
        if self.terminal == False:
            return self.vet[0]
        elif self.terminal == True and posicao < self.vetTam and posicao >= 0:
            return self.vet[posicao].getValor()

    def setVet(self, valor = None, posicao = None):
        if self.terminal == False:
            self.vet[0] = valor
        elif self.terminal == True and posicao < self.vetTam and posicao >= 0:
            self.vet[posicao].setValor(vet)

    def getTamVet(self):
        return self.vetTam

    def getElemVet(self, posicao):
        if posicao < self.vetTam and posicao >= 0:
            return self.vet[posicao]

    def setTyp(self, typ):
        self.typ = typ

    def getTyp(self):
        return self.typ


class EscopoAV(object):
    escopo = {}
    pai = None
    filho = []

    def __init__(self, escopo, pai, filho):
        self.Escopo = escopo
        self.pai = pai

    def getEscopo(self):
        return self.Escopo


    def setEscopo(self, escopo):
        self.Escopo = escopo

    
    def addFilho(self, filho):
        self.filho.append(filho)


    def addPai(self, pai):
        self.pai = pai


    def getPai(self):
        return self.pai


    def getFilho(self):
        return self.filho


class NoFuncAv(object):

    def __init__(self, param = None, retorno = None):
        self.parametros = param
        self.retorno = retorno
        

    def getParam(self, posicao_Parametro):
        return self.parametros[posicao_Parametro]
    

    def setParam(self, posicao_Parametro):
        self.parametros.append(posicao_Parametro)


class Escopo(object):
    
    def __init__(self, nomeEscopo = None, variaveisEscopo = None):
        self.nomeEscopo = nomeEscopo
        self.variaveisEscopo = variaveisEscopo