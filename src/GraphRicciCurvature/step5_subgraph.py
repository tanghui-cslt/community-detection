import scipy.io as sio
import networkx as nx
import numpy as np
import sys

def find_subgraph(path,seg=1,save_name = ''):
    
    G = nx.read_gml(path,label='id,label,value')
    temp_list = []
    max = 0
    sum_old = 0
    sum_old_old = 0
    sum_new = 0
    for c in sorted(nx.connected_components(G),key=len,reverse=True):
        
        lenc = len(c)
        # print(type(c))      #类型是set
        # print("len" ,len(c))
        
        if seg == 1:
            if lenc< 90 and lenc >0:
                
                # print (c)
                # sub_graph = nx.Graph(c)
                num = get_value(G,c)
                if max < num :
                    max = num 
                    temp_list = list(c)
                # print(lenc, num)
        
        if seg > 1:
            if lenc< 3000 and lenc >0:
                num = get_value(G,c)
                
                if num>0:
                    temp_a = []
                    ratio = num/lenc
                    sum_old_old = sum_old_old + num
                    if ratio >0.6 or ( ratio > 0.49 and lenc < 10) :
                        sum_old = sum_old + num
                        sum_new = sum_new + lenc

                        print(num,lenc,ratio)
                        temp_a = list(c)
                    else:
                        print("------------",num,lenc,ratio)
                        # temp_a = get_list(G,c)

                    temp_list = temp_list + temp_a
   
    #print(temp_list,len(temp_list))
    print(sum_old,sum_new,sum_old_old,len(temp_list))
    return temp_list,sum_old_old

def get_value(G,c):
    num = 0
    for n in c:
        if G.node[n]['value'] == '1':
            num = num + 1
    return num
    
def get_list(G,c):
    temp_list=[]
    temp_str=''
    for n in c:
        if G.node[n]['value'] == '1':
            temp_list.append(n)
    print (temp_list)
    return temp_list

    
def save_mat(sub_graph,path,row,col,dir_name):

    # row = 36
    # col = 31
    data = {}
    label = np.zeros((row,col),dtype = bool)
    for n in sub_graph:
        data_list = n.split('_')
        
        if len(data_list) == 2:
            index1 = int(data_list[0]) - 1
            index2 = int(data_list[1]) - 1
            label[index1][index2] = 1
        else :
            print('just for 2-dim')
    # str_name = "label_left"+path[-2:]
    str_name = dir_name 
    print (str_name)
    data= {str_name:label}
    path = path+'.mat'
    sio.savemat(path,data)
    return data
if __name__ == '__main__':
#           step = 3
#dir_name = 'temp_data_91_1_40_25'
#------------------------------------
    len_temp = 0
    len_old = 0
    str_orient ='left'
    for i in range(1,19):
        num = "%02d" %i 
        name = '6surgery'
        seg = 2
        dir_name = 'data_'+str_orient+num
        # save_name = 'data_'+str_orient
        results_name = 'label_'+str_orient+num
        # row = 36
        # col = 31
        
        #--------------------------------------
        row = 31
        col = 29
        # -------------------------------------
        path = "../../data/step2_results_gml/"+str_orient+"_0.5/"+dir_name+"/"
        result_path = "../../results/"+str_orient+"/gml/"+results_name
        
        file_name = path+name+'.gml'
        print(file_name)
        sub_graph,sum_old_old  =find_subgraph(file_name,seg,dir_name)
        save_mat(sub_graph,result_path,row,col,results_name)
        len_old = len_old + sum_old_old
        len_temp = len_temp + len(sub_graph)
    print (len_old,len_temp)
    # for i in range(7,18):
        # num = "%02d" %i 
        # name = '6surgery'
        # seg = 2
        # dir_name = 'data_right'+num
        # results_name = 'label_right'+num
        # path = "../../data/step2_results_gml/"+dir_name+"/"
        # result_path = "../../results/right/gml/"+results_name
        
        # file_name = path+name+'.gml'
        # print(file_name)
        # sub_graph =find_subgraph(file_name,seg)
        # save_mat(sub_graph,result_path)
