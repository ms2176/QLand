import pandas as pd
import numpy as np

class DesertificationAnalyzer:
    def __init__(self, nvdi_data, lst_data, models):
        self.nvdi_data = nvdi_data
        self.lst_data = lst_data
        self.models = models
        self.features = None
        self.samples = None

    def _get_features_sample_size(self,data_choices):
        for data_choice in data_choices:
            if data_choice == 'nvdi':
                nvdi_data = pd.read_csv(self.nvdi_data)
            elif data_choice == 'lst':
                lst_data = pd.read_csv(self.lst_data)
        # join the data
        data = pd.concat([nvdi_data, lst_data], axis=1)
        samples, features  =  data.shape
        self.samples = samples
        self.features = features
        return samples, features

    def random_forest_resource_estimation(self, data_choices, num_estimators = 100):
        print("Running Random Forest")
        # we determine the run time via complexity of the model
        computational_cost = num_estimators *self.samples * self.features * np.log(samples)
        return computational_cost

    def gradient_boosted_trees_resource_estimation(self,data_choices,tree_num=100, depth=100):
        print("Running Gradient Boosted Trees")
        """
        The Big O complexity of training gradient boosted trees generally depends on several factors including the number of trees in the ensemble, the depth of each tree, and the number of data points. Here's a breakdown:

        Number of Trees (M): If you have more trees, it takes more time to train each additional tree, adding linearly to the complexity.
        Depth of Trees (D): Trees that are deeper have more nodes and take longer to compute. The depth typically depends on the number of features and the specific configuration of the model. The time to train a tree grows exponentially with depth in the worst case, as deeper trees can potentially split into more branches.
        Number of Data Points (N): More data points mean more computations for splitting nodes at each level of each tree.
        Given these parameters, the Big O complexity of training gradient boosted trees is generally O(M * N * 2^D). This assumes that each tree is built sequentially, and the depth of the trees can lead to exponential growth in complexity dependi
        """ 
        samples, _features = self._get_features_sample_size(data_choices)
        # we determine the run time via complexity of the model
        computational_cost = tree_num * samples * 2**depth
        return computational_cost
    
    def support_vector_machines_resource_estimation(self):
        print("Running Support Vector Machines")
        # we determine the run time via complexity of the model
    
    def cnn_resource_estimation(self):
        print("Running CNN")

    
    def estimate_resources(self):
        results = {}
        for model in self.models:
            if model == "Random Forest":
                results[model] = self.random_forest_resource_estimation(['nvdi', 'lst'])
            elif model == "Gradient Boosted Trees":
                results[model] = self.gradient_boosted_trees_resource_estimation(['nvdi', 'lst'])
            elif model == "Support Vector Machines":
                results[model] = self.support_vector_machines_resource_estimation()
            elif model == "CNN":
                results[model] = self.cnn_resource_estimation()
        # normalize the results
        max_value = max(results.values())
        results = {key: value/max_value for key, value in results.items()}
        {
            'Random Forest': 0.5,
            'Gradient Boosted Trees': 0.8,
            'Support Vector Machines': 0.2,
            'CNN': 1.0
        }

        
        return results

