import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering

class Cluster:
    def __init__(self, data = None):
        self.data = data
        
        
    def categorical_to_numerical(self, data):
        s = (data.dtypes == 'object')
        object_cols = list(s[s].index)
        # Use encoder for categorical datatypes
        encoder = LabelEncoder()
        for i in object_cols:
            data[i] = data[[i]].apply(encoder.fit_transform)
        return data


    def scaler_values(self, data):
        scaler = StandardScaler()
        scaler.fit(data)
        scaled_data = pd.DataFrame(scaler.transform(data), columns=data.columns)
        return scaled_data


    def get_clustering(self, targets, n_clusters):
        # Remove columns 
        data = self.data.filter(targets, axis=1)
        data = self.categorical_to_numerical(data)
        data = self.scaler_values(data)
        # Initiating the Agglomerative Clustering model 
        agg_cluster = AgglomerativeClustering(n_clusters = n_clusters)
        # fit model and predict clusters
        cluster_values = agg_cluster.fit_predict(data)
        self.data["clusters"] = cluster_values
        return self.data