import logging
import networkx as nx

logger = logging.getLogger("GraphRicciCurvature")

import platform
system = ''
if(platform.system()=='Windows'):
    system = 'Window'

elif(platform.system()=='Linux'):
    system = 'Linux'
    # import matplotlib as mpl
    # mpl.use('Agg')

import networkx as nx
# import matplotlib.pyplot as plt


def set_verbose(verbose="ERROR"):
    if verbose == "INFO":
        print("------------------verbose:--------",verbose)
        logger.setLevel(logging.INFO)
    elif verbose == "DEBUG":
        logger.setLevel(logging.DEBUG)
    elif verbose == "ERROR":
        logger.setLevel(logging.ERROR)
    else:
        print('Incorrect verbose level, option:["INFO","DEBUG","ERROR"], use "ERROR instead."')
        logger.setLevel(logging.ERROR)
        
def save_graph(G,path,show_figer = False):
    h = nx.Graph()
    # i = 0
    for n in G.nodes():
        # i = i + 1
        # if i%100 == 0:
            # print(G.node[n]['desc'])
        h.add_node(n,value=G.node[n]['value'])
        # h.add_node(n,value=G.node[n]['value'],weight= G.node[n]['weight'],desc = G.node[n]['desc'])
        
    
    for (n1,n2) in G.edges():
        # print(e)
        h.add_edge(n1,n2,weight = G[n1][n2]['weight'])
    file_name = path+".gml"
    nx.write_gml(h,file_name)
    h.clear()
    
def show_fig(G,fig='test.png'):

    # pos= nx.spring_layout(G)
    pos = nx.spring_layout(G)
    nx.draw_networkx(G,pos)
    # plt.show()
    plt.savefig(fig)
    plt.clf()
    
# - circular_layout：节点在一个圆环上均匀分布
# - random_layout：节点随机分布
# - shell_layout：节点在同心圆上分布
# - spring_layout： 用Fruchterman-Reingold 算法排列节点（这个算法我不了解，样子类似多中心放射状）
# - spectral_layout：根据图的拉普拉斯特征向量排列节 
def show_fig_test(number=11,index = 0):
    # path = "/mnt/f/test/code/curvature/GraphRicciCurvature/data/save_grad_"
    path = "/mnt/f/test/task2/GraphRicciCurvature/data/save_grad_"
    for i in range(number):
        file_name = path +str(i)+".gml"
        G = nx.read_gml(file_name,label='id,label,value')
        fig_name = ''
        if index == 0:
            pos = nx.circular_layout(G)
            fig_name = path +str(i)+"_circular_layout.png"
        elif index == 1:
            pos = nx.random_layout(G)
            fig_name = path +str(i)+"_random_layout.png"
        elif index == 2:
            pos = nx.shell_layout(G)
            fig_name = path +str(i)+"_shell_layout.png"
        elif index == 3:
            pos = nx.spring_layout(G)
            fig_name = path +str(i)+"_spring_layout.png"
        elif index == 4:
            pos = nx.spectral_layout(G)
            fig_name = path +str(i)+"_spectral_layout.png"
        else :
            pos = nx.spectral_layout(G)
            fig_name = path +str(i)+"_spectral_layout.png"
        nx.draw_networkx(G,pos)        
        # plt.show()
        plt.savefig(fig_name)
        plt.clf()
        
if __name__ == '__main__':
    show_fig_test(index=0)
    show_fig_test(index=2)
    show_fig_test(index=4)   