
import platform
system = ''
if(platform.system()=='Windows'):
    system = 'Window'

elif(platform.system()=='Linux'):
    system = 'Linux'
    import matplotlib as mpl
    mpl.use('Agg')

import networkx as nx
import matplotlib.pyplot as plt


#networkx可以直接通过函数从gml文件中读出数据
def read_gml(data):
    H=nx.read_gml(data)
    return H
    # print(H.edges())
def convert_to_hex(rgba_color) :
    red = int(rgba_color[0]*255)
    green = int(rgba_color[1]*255)
    blue = int(rgba_color[2]*255)
    return '#%02x%02x%02x' % (red, green, blue)

linux = "/mnt/f/test/football/football1.gml"
win = ".//football//football.gml"
fig =''
path =''

if(platform.system()=='Windows'):
    print('Windows')
    path = win
    fig = "win.png"
elif(platform.system()=='Linux'):
    print('Linux')
    path = linux
    fig = "linux.png"




# G = nx.read_gml(".//football//karate.gml",label='id')
# nx.draw_networkx(G)
# nx.draw_networkx(G,with_labels=False)
# print(G.edges())
# print(G.nodes[1])
# print(nx.info(G))
# print(pos)

list0= []
list1= []
list2= []
list3= []
list4= []
list5= []
list6= []
list7= []
list8= []
list9= []
list10= []
list11= []
def read_file():

    G = nx.read_gml(path,label='id,label,value')
    return G

def get_pos(G):
    pos= nx.spring_layout(G)
    return pos

def get_lists(G):
    for n in G.nodes():
        value = G.nodes[n]['value']
        # print(G.nodes[n]['value'])
        if value == 0:
            list0.append(n)
        elif value == 1:
            list1.append(n)
        elif value == 2:
            list2.append(n)
        elif value == 3:
            list3.append(n)

        elif value == 4:
            list4.append(n)

        elif value == 5:
            list5.append(n)

        elif value == 6:
            list6.append(n)

        elif value == 7:
            list7.append(n)

        elif value == 8:
            list8.append(n)

        elif value == 9:
            list9.append(n)

        elif value == 10:
            list10.append(n)

        elif value == 11:
            list11.append(n)

def draw_graph(G,fig = fig ):

    pos= nx.spring_layout(G)
    get_lists(G)
    list_all=[list0,list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11]
    l = list(range(12))

    list_color = ['r','b','g','k','w']
    list_alpha=[0.3,0.6,0.9]
    # print(list_all[11])
    # print(list1)
    sum = 0
    for i in range(12):
        # print (i,i%4,i%3)
        sum += len(list_all[i])
        nx.draw_networkx_nodes(G,pos,nodelist=list_all[i],node_color=list_color[i%4],alpha=list_alpha[i%3])
    # print (sum)  
    nx.draw_networkx_edges(G,pos)
    #for (v1,v2) in G.edges():

    plt.show()
    plt.savefig(fig)

# dram_graph()

# color 
# for(v1,v2) in G.edges():
#     print(v1)
#     if G.nodes[v1]['value'] = 
# print(G.nodes['1'])
# G[17][12]
# print(G.nodes[1])
# if not nx.get_node_attributes(G, value):
    # print("edge not")
# else:
    # print("have value")