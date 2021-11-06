import scipy.io as sio
import networkx as nx
import numpy as np
import os


def find_subgraph(file_name):
    
    G = nx.read_gml(file_name,label='id,label,value')
    temp_list = None
    max = 0
    sum_num = 0
    temp_list =[]
    for c in sorted(nx.connected_components(G),key=len,reverse=True):
        
        lenc = len(c)
        # print(type(c))      #类型是set
        # print("len" ,len(c))
        
        num = get_value(G,c)
        sum_num = sum_num + num
        if lenc< 100 and lenc >2:
            
            # print (c)
            # sub_graph = nx.Graph(c)
        # num = get_value(G,c)
            if max < num :
                max = num 
                temp_list = c
            # print(lenc, num)
            
        print(sum_num,len(temp_list),max,num)
    
    return temp_list

def get_value(G,c):
    num = 0
    for n in c:
        if G.node[n]['value'] == '1':
            num = num + 1
    return num

if __name__ == '__main__':
#dir_name = 'temp_data_91_1_40_25'
    
    path = "/mnt/f/test/task2/GraphRicciCurvature/data=0.2/"
    top_name = 'temp_data_'
    bot_name = '_1_30_15/'
#-------------------------------------
    start_id = 80
    end_id = 91
    name_list = ['3surgery','4surgery','4_1_new_surgery','2_1_new_surgery','4surgery','4surgery','save_grad_3surgery(best)','save_grad_3surgery','save_grad_2surgery','save_grad_4surgery','4surgery']
#------------------------------------
    for i,id in enumerate(range(start_id,end_id)):
        id = str(id)
        file_dir = path+ top_name + id + bot_name+name_list[i]+'.gml'
        # name = '4surgery'
        
        
        
        if os.path.exists(file_dir):
            print(file_dir)
        else :
            print("file not exists")
        sub_graph =find_subgraph(file_dir)
        
        # os.system("pause")
        input()

    
