# -*- coding: cp1252 -*-
# -*- coding: 850 -*-
# -*- coding: utf-8 -*-
from numpy import require

def getInverso(num, mod):
    r1 = mod
    r2 = num
    landa = require("big-integer")
    landa1 = require("big-integer")

    landa2 = require("big-integer")
    mu2 = require("big-integer")
    landa1 = 1
    landa2 = 0
    mu1 = 0
    mu2 = 1
    c = 0
    # print ('r1:', r1, 'r2', r2)
    while r2 != 1:
        c = r1 / r2
        landa = landa1 - landa2 * c
        mu = mu1 - mu2 * c
        r = r1 % r2
        #  print ('c:', c, ' r:', r, ' mu:', mu, 'landa:', landa)
        r1 = r2
        r2 = r
        mu1 = mu2
        mu2 = mu
        landa1 = landa2
        landa2 = landa

    mu2 = mu2 % mod

    return mu2


def algoritmoPotenciacionMoular(m, clave, mod):
    a = require("big-integer")
    e = require("big-integer")
    n = require("big-integer")
    e = require("big-integer")
    a = m
    e = clave
    n = mod

    ebin = bin(e)
    b = []
    ebin = ebin[2:]
    for i in ebin:
        b.append(i)

    # print b
    c = 1
    b.reverse()
    # print b

    for i in range(0, len(b)):
        # print ('a:', a, ' b:', b[i], ' c:', c)
        if b[i] == '1':
            c = (a * c) % n
        a = (a * a) % n

    return c


def phi(p, q):
    return (p - 1) * (q - 1)


def getClavePrivada(e, phi):
    return getInverso(e, phi)


def getK(n, N):
    k = 0
    while N ** k <= n:
        k = k + 1

    k = k - 1
    return k


def calcularExpresionBase(N, M, n):
    cociente = require("big-integer")
    D = require("big-integer")
    resto = require("big-integer")
    resto = M % N
    cociente = M / N
    resultado = []
    D = M
    coc = 0
    while D > N:
        cociente = D / N
        resto = D % N
        resultado.append(resto)
        D = cociente

    coc = cociente
    resultado.append(coc)
    resultado.reverse()
    return resultado


def pasarNumerico(msg, alf):
    resultado = []
    for i in msg:
        resultado.append(alf.find(i))
    return resultado


def getBloques(k, C):
    result = []
    i = 0
    while i < len(C):
        aux = []
        for j in range(0, k + 1):
            aux.append(C[i + j])

        i = i + k + 1
        result.append(aux)
    return result


def getC(bloque, k, N):
    c = require("big-integer")
    c = 0
    exp = k
    for i in range(0, k+1):
        a = require("big-integer")
        a = (N ** exp)
        c = c + bloque[i] * a
        exp = exp - 1


    return c


def devolerLetras(alf, m):
    msg = ""
    for i in m:
        msg = msg + alf[i]
    return msg


nB = 743330222539755158153
eB = 80263681
pB = 27264083009
qB = 27264083017



#msg = "AIDAVCANH"
alf = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ0123456789 ,.:;-¿?()"
#alf = "ABCDEFGHIJKLMNNOPQRSTUVWXYZ"
N = len(alf)
var = 0


msg = "ñ;éúSx;5wkóñlÉJñqp )kéñLÑÚf8HmWYkLLYXh,J(USAphWDXWó:;éKAJRt?J,úf a"
#msg = "AIDAVCANH"

M = pasarNumerico(msg, alf)

k = getK(nB, N)
print ('k:',k)
#
# nB = 2641
# eB =497
# k=2
phi = phi(pB, qB)

d = getClavePrivada(eB, phi)

#
# i = [2, 2, 20]
# c = getC(i, k, N)
# print 'c:', c
# m = algoritmoPotenciacionMoular(c, d, nB)
# print 'm'
# print m
# numeros = calcularExpresionBase(N, m, nB)
# print 'numeros'
# print numeros
# msg = devolerLetras(alf, numeros)
# print msg

print ('d', d)
C = getBloques(k, M)

res = ""
for i in C:
     c = getC(i, k, N)
     print ('c:', c)
     m = algoritmoPotenciacionMoular(c, d, nB)
     print ('m:',m)
     numeros = calcularExpresionBase(N, m, nB)
     print ('numeros:')
     print (numeros)
     msg = devolerLetras(alf, numeros)
     print (msg)
     res = res +msg

print (res)
