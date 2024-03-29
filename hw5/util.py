from sklearn.cluster import KMeans
import numpy as np


def cluster_user_data(input_data, emotional_col_start=4, emotional_col_end=9, n_clusters=3):
    '''
        This function cluster user data based on KMeans algorithm
        By default, it will split your data into three groups
        '''
    # collect answers for five emotional questions
    # which are located from 4th col to 9th col
    emotional_data = [i[emotional_col_start:emotional_col_end]
                      for i in input_data]
    # use kmeans to cluster data
    kmeans = KMeans(n_clusters).fit(emotional_data)
    # return cluster labels
    return kmeans.labels_


def split_user_data(input_data, labels, n_clusters=3):
    '''
    this function will split input data into groups
    based on labels
    '''
    result_list = []
    for i in range(n_clusters):
        # find indices of each group elements, without [0] the result is tuple
        tmp_indices = np.where(labels == i)[0]
        result_list.append([input_data[i] for i in tmp_indices])

    return result_list 
    
def split_data_for_hw(input_data):
	
	ym = []
	om = []
	yf = []
	of = []
	for data in input_data:
		if data[3].lower() == 'male':
			if data[2] <= 35:
				ym.append(data)
			else:
				om.append(data)
		else:
			if data[2] <= 35:
				yf.append(data)
			else:
				of.append(data)
	result_list = []
	result_list.append(ym)
	result_list.append(om)
	result_list.append(yf)
	result_list.append(of)
	return result_list
