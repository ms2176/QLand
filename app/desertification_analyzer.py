import sys


class DesertificationAnalyzer:
    def __init__(self, nvdi_data, lst_data, models):
        self.nvdi_data = nvdi_data
        self.lst_data = lst_data
        self.models = models

    def random_forest_resource_estimation(self):
        print("Running Random Forest")
        # we determine the run time via complexity of the model
        n,m,s = self.nvdi_data.shape
        return 

    def gradient_boosted_trees_resource_estimation(self):
        print("Running Gradient Boosted Trees")
        # we determine the run time via complexity of the model

    
    def support_vector_machines_resource_estimation(self):
        print("Running Support Vector Machines")
        # we determine the run time via complexity of the model
    
    def cnn_resource_estimation(self):
        print("Running CNN")

