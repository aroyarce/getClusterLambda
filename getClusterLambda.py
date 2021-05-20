'''
Created on 15-05-2021

@author: sambe
'''
import json
import math
from http import HTTPStatus

def lambda_handler(event, context):
    # TODO implement
    print("Evento = ", event)
    
    print("#"*90)
    print("Iniciando Programas\n")
    
    print("Obteniendo Cluster")
    #grid = [[0,1],[0,2],[2,3],[4,3],[7,3],[8,5],[8,7],[8,8]]
    #distancia = 3
    
    if event["queryStringParameters"] is None:
        resultado = {}
        resultado["error"] = "Ningun parametro incluido."
        resultado = json.dumps(resultado)
        return {
            'statusCode': HTTPStatus.BAD_REQUEST.value,
            'body': resultado
        }
    
    key_to_lookup = 'd'
    if key_to_lookup in event["queryStringParameters"]:
        distancia = int(event["queryStringParameters"]["d"])
    else:
        resultado = {}
        resultado["error"] = "Parametro Distancia no incluido"
        resultado = json.dumps(resultado)
        return {
            'statusCode': HTTPStatus.BAD_REQUEST.value,
            'body': resultado
        }
    
    
    grids_ord = []
    key_to_lookup = 'grid'
    if key_to_lookup in event["multiValueQueryStringParameters"]:
        grids = event["multiValueQueryStringParameters"]["grid"]
        for grid in grids:
            largo_menos = len(grid)-1
            aux = grid[1:largo_menos].split(",")
            aux[0] = int(aux[0])
            aux[1] = int(aux[1])
            grids_ord.append(aux)
    
        for x in grids_ord:
            print(x)
        clusterFinal = getcluster(distancia, grids_ord)
    else:
        grids = [[0,1],[0,2],[2,3],[4,3],[7,3],[8,5],[8,7],[8,8]]
        clusterFinal = getcluster(distancia, grids)

    
    imprimir = "\nResultado Cluster para Distancia = {0}\nCluster = {1}"
    impresion = imprimir.format(distancia, clusterFinal)
    print(impresion)
    
    for x in clusterFinal:
        print(x)
    
    print("\nFin de Programa")
    print("#"*90)
    
    resultado = {}
    resultado["cluster"] = clusterFinal
    resultado = json.dumps(resultado)
    return {
        'statusCode': 200,
        'body': resultado
    }

def removeDup(arreglo):    
    salida = []
    largoArreglo = len(arreglo)
    
    ind = 0
    while(ind < (largoArreglo)):
        salida.append(arreglo[ind])
        for i in range(ind,largoArreglo):                        
            if(arreglo[ind] == arreglo[i]):
                if(i == largoArreglo-1):
                    ind = largoArreglo
                continue
            else:
                ind = i
                break
    
    return salida
    
def calculoDistancia(d, x, y):
    diff_1 = math.fabs(x[0]-y[0])
    diff_2 = math.fabs(x[1]-y[1])
    
    if( (diff_1 <= d) and (diff_2 <= d) ):
        return True
    else:
        return False

def getcluster(d, grid):
    imprimir = "Distancia = \t{0}\nGrid = \t\t{1}"
    impresion = imprimir.format(d, grid)
    print(impresion)
    resultado = []
    
    largoGrid = len(grid)
    res = False
    subCluster = []
    for i in range(largoGrid):
        res = False
        subCluster = []
        subCluster.append(grid[i])
        for j in range(largoGrid):        
            if(i == j):
                continue    
            salida = calculoDistancia(d, grid[i], grid[j])
            res = res + salida
            imprimir = "grid_i = {0} grid_j = {1}\tSalida = {2}"
            impresion = imprimir.format(grid[i], grid[j], salida)
            #print(impresion)
            
            if(salida):
                subCluster.append(grid[j])
        subCluster.sort()
        resultado.append(subCluster)
    
    resultado.sort()
    resultado = removeDup(resultado)
    return resultado
