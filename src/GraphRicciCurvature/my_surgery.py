import networkx as nx
import numpy as np
import importlib
import os,sys
from test_draw_graph import *
from GraphRicciCurvature.util import *
#from util import *

def ARI(G, cc, clustering_label="club"):
    """
    Computer the Adjust Rand Index (clustering accuray) of clustering "cc" with clustering_label as ground truth.
    :param G: A networkx graph
    :param cc: A clustering result as list of connected components list
    :param clustering_label: Node label for clustering groundtruth
    """

    if importlib.util.find_spec("sklearn") is not None:
        from sklearn import preprocessing, metrics
    else:
        print("scikit-learn not installed...")
        return -1

    complexlist = nx.get_node_attributes(G, clustering_label)

    le = preprocessing.LabelEncoder()
    y_true = le.fit_transform(list(complexlist.values()))

    predict_dict = {}
    for idx, comp in enumerate(cc):
        for c in list(comp):
            predict_dict[c] = idx
    y_pred = []
    for v in complexlist.keys():
        y_pred.append(predict_dict[v])
    y_pred = np.array(y_pred)

    return metrics.adjusted_rand_score(y_true, y_pred)

# def save_graph(G,fig):
    # h = nx.Graph()
    # for n in G.nodes():
        # h.add_node(n,value=G.node[n]['value'])
    
    # for (n1,n2) in G.edges():
        # print(e)
        # h.add_edge(n1,n2)

    # nx.write_gml(h,fig)

def my_surgery(G_origin: nx.Graph(), weight="weight",fig_num = 1, input_name ='',cut=0,show_cut_fig = False):
    """
    A simple surgery function that remove the edges with weight above a threshold
    :param G: A weighted networkx graph
    :param weight: Name of edge weight to cut
    :param cut: Manually assign cut point
    :return: A weighted networkx graph after surgery
    """
    G = G_origin.copy()
    w = nx.get_edge_attributes(G, weight)

    assert cut >= 0, "Cut value should be greater than 0."
    if not cut:
        cut = (max(w.values()) - 1.0) * 0.5   # Guess a cut point as default ORIGIN
        #cut = (max(w.values()) - 1.0) * 0.9   # Guess a cut point as default

    to_cut = []
    for n1, n2 in G.edges():
        if G[n1][n2][weight] > cut:
            to_cut.append((n1, n2))
    print("*************** Surgery time ****************",fig_num)
    print("* Cut %d edges." % len(to_cut))
    G.remove_edges_from(to_cut)
    
    print("* Number of nodes now: %d" % G.number_of_nodes())
    print("* Number of edges now: %d" % G.number_of_edges())
    # fig = "grid"+"n.gml"
    # print ("file name = ",fig )
    if G.number_of_edges() ==0:
        print("over")
        os._exit(0)
    cc = list(nx.connected_components(G))
    print("number_connected_components :%d " %( nx.number_connected_components(G)))
    print("* Modularity now: %f " % nx.algorithms.community.quality.modularity(G, cc))
    
    print("* ARI now: %f " % ARI(G, cc))
    print("*********************************************")
    input_name_index = input_name+str(fig_num)+"surgery"
       
    save_graph(G,input_name_index)
    # if show_cut_fig :
    # fig = "grid"+fig+"n.gml"
    # print ("file name = ",fig )
    # save_graph(G,fig)

    return G
