import networkx as nx
from my_surgery import *
from GraphRicciCurvature.FormanRicci import FormanRicci
# from GraphRicciCurvature.OllivierRicci import OllivierRicci
from GraphRicciCurvature.OlliverOld import OllivierRicci
import os 
import sys


#********************************************************
# file_name = '/mnt/f/test/task2/temp_data_82_1.gml'
# path = "/mnt/f/test/task2/GraphRicciCurvature/data/save_grad_"
#********************************************************

#********************************************************
# file_name = '/mnt/f/test/task2/temp_data_86_1.gml'
# path = "/mnt/f/test/task2/GraphRicciCurvature/data=0.2/temp/save_grad_"
#********************************************************

#********************************************************
# name = 'temp_data_86_1_30_15'
# file_name = '/mnt/f/test/task2/'+name+'.gml'
# path = "/mnt/f/test/task2/GraphRicciCurvature/data=0.2/"+name"/save_grad_"
#********************************************************

def mkdir(path):

    is_exists = os.path.exists(path)
    if not is_exists:
        os.makedirs(path)
        print(path+" success")
    else:
        print('is exists')

#print("\n- Import an example NetworkX karate club graph")

# just need to modify the varibale "name" 
# note that reload 
#temp_data_86_1_30_15
# temp_data_91_1_40_25
#-------------------------------------
if __name__ == '__main__':
    data = int(sys.argv[1])
    num = "%02d" % data
    orient = sys.argv[2]
    name = 'data_'+orient+num
    #-------------------------------------

    #file_name = '../../data/step1_right_gml/'+name+'.gml'
    #path = "../../data/step2_results_gml_0.6/"+name+"/"

    file_name = '../../data/step1_'+orient+'_gml/'+name+'.gml'
    path = "../../data/step2_results_gml/"+orient+"_0.5/"+name+"/"

    mkdir(path)

    G = nx.read_gml(file_name,label='id,label,value')
    print("* Number of nodes now: %d" % G.number_of_nodes())
    print("* Number of edges now: %d" % G.number_of_edges())

    orc_Sinkhorn = OllivierRicci(G, alpha=0.2, method="OTD", verbose="INFO")
    orc_Sinkhorn.compute_ricci_flow(iterations=18,step=0.5, surgery=(my_surgery,2,path))





