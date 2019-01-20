"""
https://snap.stanford.edu/data/cit-HepTh.html

Even through many papers that are not in the dataset yet been cited multiple times, there is no paper at all,

However, we can not do a case study is many of the most affected node may not be possible for case study.

We only used the nodes with labels and have edges.

"""
import numpy as np
import datetime
import networkx as nx
import matplotlib.pyplot as plt
from bisect import bisect

def read_edges_file():
    #read the txt file
    lines = np.genfromtxt("Cit-HepTh.txt", dtype = str)
    return lines

def read_node_time_file():
    lines = np.genfromtxt("Cit-HepTh-dates.txt", dtype = str)
    return lines


def generate_cit_Hepth_networks(time_step_number = 3, dynamic_start_date_str = '2000-12-31'):#note that the dataset have already been
    """
    window is generated by month 1 network a month
    :param time_step_number:
    :param dynamic_start_date:
    :return:
    """
    all_edges = read_edges_file()
    all_nodes = read_node_time_file()



    start_day = translate_string_2_date(dynamic_start_date_str)

    for i in range(len(all_nodes)):
        all_nodes[i][0] = int(all_nodes[i][0])#change to int
        all_nodes[i][0] = str(all_nodes[i][0])#change back to str in this way 00111 is translated to 111
        #all_nodes[i][1] = (translate_string_2_date(all_nodes[i][1]) - start_day).days
        #all_nodes[i][1] = translate_string_2_date(all_nodes[i][1])

        #print(all_nodes[i][1])
    #a = set().inter
    edge1 = all_edges[:, 0]
    edge2 = all_edges[:, 1]
    print(edge1)
    print(edge2)
    all_node_existing_in_edges_set = set(edge1).union(set(edge2))
    print(all_node_existing_in_edges_set)
    print(len(edge1)," ",len(edge2)," ",len(all_node_existing_in_edges_set))

    node = set(all_nodes[:, 0])

    node_in_2_files = all_node_existing_in_edges_set.intersection(node)
    print(len(node_in_2_files)," node in 2 files")

    initial_graph = nx.Graph()


    for i in range(len(all_nodes)):
        print("initial graph processed ", i)
        if (translate_string_2_date(all_nodes[i][1]) - start_day).days > 0:
            initial_end_index = i
            break
        else:
            node_name = all_nodes[i][0]
            if (node_name in node_in_2_files) == True:
                initial_graph.add_node(node_name)#add this node
                if (node_name in edge1) == True:#the first is the paper that cite. The second is the papers that been cited
                    indexes = [i for i, j in enumerate(edge1) if j == node_name]
                    for j in range(len(indexes)):
                        cited_paper = edge2[indexes[j]]
                        if (cited_paper in node_in_2_files) == True:
                            initial_graph.add_edge(node_name,cited_paper)

    """
    nx.draw_networkx(initial_graph)
    plt.show()
    """

    start_time = translate_string_2_date(all_nodes[initial_end_index][1])
    final_time = translate_string_2_date(all_nodes[len(all_nodes)-1][1])

    total_time = (final_time-start_time).days
    days_gap = float(total_time)/(time_step_number+1)


    time_step_slots = []

    for i in range(1,time_step_number):
        time_step_slots.append(i*days_gap)

    time_step_slots.append(days_gap+1)

    graphs = []

    for i in range(time_step_number):
        graphs.append(initial_graph.copy())

    for i in range(initial_end_index, len(all_nodes)):
        print("processing node:", i)
        edge_time_tag = float((translate_string_2_date(all_nodes[i][1])-start_time).days)

        calculated_time_step = bisect(time_step_slots, edge_time_tag)
            # print(time_step_slots)

        node_name = all_nodes[i][0]
        if (node_name in node_in_2_files) == True:
            for m in range(calculated_time_step, time_step_number):
                graphs[m].add_node(node_name)  # add this node
            if (node_name in edge1) == True:  # the first is the paper that cite. The second is the papers that been cited
                indexes = [n for n, o in enumerate(edge1) if o == node_name]
                for j in range(len(indexes)):
                    cited_paper = edge2[indexes[j]]
                    if (cited_paper in node_in_2_files) == True:
                        for m in range(calculated_time_step, time_step_number):
                            graphs[m].add_edge(node_name, cited_paper)
    return graphs
                #graphs[j].add_edge((str(sorted_data[i][0])), str(sorted_data[i][1]))



    #all_node_existing_in_node_file()



def translate_string_2_date(date = '1992-02-24'):
    date_list = date.split('-')
    data_time = datetime.date(int(date_list[0]), int(date_list[1]), int(date_list[2]))
    return data_time



if __name__ == '__main__':
    generate_cit_Hepth_networks()
    print((translate_string_2_date('1999-02-24')-translate_string_2_date('1993-03-18')).days)
    a =set([1,2,3])
    b = set([1])
    print(a.intersection(b))