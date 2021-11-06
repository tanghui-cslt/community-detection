# step2 
import scipy.io as sio
import numpy as np
import networkx as nx
import platform,os
if(platform.system()=='Windows'):
    system = 'Window'

elif(platform.system()=='Linux'):
    system = 'Linux'
    import matplotlib as mpl
    mpl.use('Agg')

import networkx as nx
import matplotlib.pyplot as plt


def get_data(data_name = 'temp_data_86_1',label_name = 'temp_label_86_1_30_15',path=''):

    
    data_format = path + data_name +".mat"
    # load_fn = data_format
    load_data = sio.loadmat(data_format)
    load_matrix = load_data[data_name]
    data_arr = np.array(load_matrix)
    
    label_format = path + label_name + ".mat"
    label_data = sio.loadmat(label_format)
    label_arr = np.array(label_data[label_name])
     
    b = np.nonzero(label_arr)
    # print(b[0].size,b[1].size)
    # print(b[0],type(b[0]),b[0].size)
    # row = 2
    # col = b[0].size
    # for i in range(col):
        # print(b[0][i],b[1][i])
    # print(b)

    return data_arr,b

    
def manual_data(data_arr,label,data_name,path ):

    shape = data_arr.shape
    temp_col = label[0].size
    # print (temp_col)
    temp_list = []
    for i in range(temp_col):
        temp_list.append([label[0][i],label[1][i]])
        # print(label[0][i],label[1][i])
        
    # print(temp_list)
    
    rows = shape[0]
    cols = shape[1]
    H= nx.grid_2d_graph(rows,cols)
    G = nx.Graph()
    dic = {}
    classfier = ''

    for i,n in enumerate(H.nodes()):
        temp_len = len(n)
        temp_str = ''
        # print (n)
        for j in range(temp_len):
            temp_str = temp_str+"_"+str(n[j]+1)
            
        temp_str =temp_str[1:]
        dic[n] = temp_str
        # dic[str(i)] = [n]
        dic[temp_str] = n
        list1 = [n[0],n[1]]
        data = data_arr[n[0]][n[1]]
        if list1 in temp_list:
            classfier = '1'
            # print (list1)
        else:
            classfier = '0'
        
        G.add_node(temp_str,id = i,weight=str(data),value=classfier,desc=temp_str)
    # os._exit(0)
    # find max value
    max_num=0
    for (n1,n2) in H.edges():
        row = dic[n1]
        col = dic[n2]
        
        data1 = int(G.node[row]['weight'])
        data2 = int(G.node[col]['weight'])
        weight = abs(data1-data2)
        if max_num < weight :
            max_num = weight

    
    # i = 0        
    for (n1,n2) in H.edges():
        row = dic[n1]
        col = dic[n2]
        # print("--------n1,row-----",n1,row)
        data1 = int(G.node[row]['weight'])
        data2 = int(G.node[col]['weight'])
        
        
        if data1 !=0 and data2 != 0:
            weight = abs(data1-data2)/max_num
            if weight > 1e-10:
                G.add_edge(dic[n1],dic[n2],weight=weight)
            
    iso_list = list(nx.isolates(G))
    iso_sum = iso_zero_pint(G,nx.isolates(G))
    # print('sum = ',iso_sum,len(iso_list))
    # G.remove_nodes_from(iso_list)
        # if judge_position(G,row,col,shape)==False:
            # print("-----------judge-----------",row,col)
            # os._exit(0)
            
    threshold = 500
    for n in G.nodes():
        data1 = judge_position_left(G,n,shape,threshold,iso_list)
        data2 = judge_position_right(G,n,shape,threshold,iso_list)
        weight = data1[1]/max_num
        if data1[2] == True and weight > 1e-10:
            # print(data1[0],n)
            G.add_edge(data1[0],n,weight=weight)
            
        weight = data2[1]/max_num
        if data2[2] == True and weight > 1e-10:
            G.add_edge(n,data2[0],weight=weight)
    # print("--------------------------------------")
    # for n in G.nodes():
        # data2 = judge_position_right(G,n,shape,threshold,iso_list)
        # if data2[2] == True:
            # G.add_edge(n,data2[0],weight=data2[1]/max_num)
           
    print('------iso point -----',len(list(nx.isolates(G))))
    print("* Number of nodes now: %d" % G.number_of_nodes())
    print("* Number of edges now: %d" % G.number_of_edges())
    save_name = path + data_name + ".gml"
    nx.write_gml(G,save_name)
    return iso_sum
    # nx.write_gml(G,save_name)
    

def iso_zero_pint(G,iso_list):
    sum = 0
    for n in iso_list:
        if G.node[n]['value'] == '1':
            sum = sum + 1
            
        # row_list = i.split('_')
    # print('sum = ',sum)
    return sum 
def judge_position_right(G,row,shape,threshold,iso_list):

    row_list = row.split('_')
    
    lenlist = len(row_list)
    next_row = ''
    # print(shape[0],shape[1])
    
    for i in range(lenlist):
        if i == 0:
            int_row1 =  int (row_list[i])
            next_row = str(int_row1+1)
        elif i == 1:
            int_row1 =  int (row_list[i])-2
            next_row = next_row +'_'+str(int_row1+1)
        else :
            int_row1 = int(row_list[i])
            next_row = next_row +'_'+str(int_row1+1)
            # pre_col = pre_col +'_'+str(int_col1+1)
            
        if int_row1 < 0 or int_row1 >= shape[i]:
            return (-1,0,False)
            
    # return (1,1,True)
    if next_row in iso_list:
        return (-1,0,False)
    
    data1 = int(G.node[next_row]['weight'])
    data2 = int(G.node[row]['weight'])
    res = abs(data1 - data2)
    if abs(data1 - data2) > threshold :
        return (-1,0,False)
        
    return (next_row,res ,True)
        

def judge_position_left(G,row,shape,threshold,iso_list):

    row_list = row.split('_')
    
    lenlist = len(row_list)
    pre_row = ''
    
    for i in range(lenlist):
        int_row1 = int (row_list[i])
       
        int_row1 = int_row1 - 2
      
        if i == 0:
            pre_row = str(int_row1+1)
           
        else :
            pre_row = pre_row +'_'+str(int_row1+1)
            # pre_col = pre_col +'_'+str(int_col1+1)
            
        
        if int_row1 < 0 or int_row1 >= shape[i]:
            return (-1,0,False)
            
        # if int_col1 < 0 or int_col1 >= shape[i]:
            # return False
    
    # row_list = pre_row.split('_')
    if pre_row in iso_list:
        return (-1,0,False)
    
    data1 = int(G.node[pre_row]['weight'])
    data2 = int(G.node[row]['weight'])
    res = abs(data1 - data2)
    if abs(data1 - data2) > threshold :
        return (-1,0,False)
        
    return (pre_row,res ,True)
        # print(pre_row,pre_col)    

        

if __name__ == '__main__':
# just need to modify the varibale "data_name"  and  "label_name"

#--------------------------------------------------
    # data_name = 'temp_data_91_1_40_25'
    # label_name = 'temp_label_91_1_40_25'
#--------------------------------------------------
#--------------------------------------------------
    sum = 0
    iso_sum = 0
    for i in range(1,19):
        num = "%02d" %i 
        # data_name = 'data_right'+num
        # label_name = 'label_right'+num
        data_name = 'data_left'+num
        label_name = 'label_left'+num
        print (data_name,label_name)
    #--------------------------------------------------
        # data_path = '../data/step0_right_data/'
        # save_path = '../data/step1_right_gml/'
        data_path = '../data/step0_left_data/'
        save_path = '../data/step1_left_gml/'
        data_arr,label = get_data(data_name,label_name,data_path)
        sum = sum + label[0].size
        iso_num =  manual_data(data_arr,label,data_name,save_path)
        print('iso_num', iso_num)
        iso_sum = iso_sum + iso_num
    print(sum,iso_sum)
