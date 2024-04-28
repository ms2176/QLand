import pandas as pd
import numpy as np


class DesertificationAnalyzer:
    def __init__(self, data):
        self.nvdi_data = data["nvdi_data"]
        self.lst_data = data["lst_data"]
        self.models = data["models"]
        self.features = None
        self.samples = None

    def _init_features_sample_size(self, data_choices: list[str]):
        """Initialize the values for the model features and samples"""
        for data_choice in data_choices:
            if data_choice == "nvdi":
                nvdi_data = pd.read_csv(self.nvdi_data)
            elif data_choice == "lst":
                lst_data = pd.read_csv(self.lst_data)

        # join the data
        data = pd.concat([nvdi_data, lst_data], axis=1)
        samples, features = data.shape

        self.samples = samples
        self.features = features

    def random_forest_resource_estimation(self, num_estimators: int = 100):
        """Determine the run time via complexity of the random forest model

        Returns:
            int: the estimated computational cost
        """
        print("Running Random Forest")
        computational_cost = (
            num_estimators * self.samples * self.features * np.log(self.samples)
        )
        return computational_cost

    def gradient_boosted_trees_resource_estimation(
        self, tree_num: int = 100, depth: int = 100
    ):
        """
        The complexity of training gradient boosted trees depends on several factors including:

        Number of Trees (M): If you have more trees, it takes more time to train each additional tree, adding linearly to the complexity.
        Depth of Trees (D): Trees that are deeper have more nodes and take longer to compute. The depth typically depends on the number of features and the specific configuration of the model. The time to train a tree grows exponentially with depth in the worst case, as deeper trees can potentially split into more branches.
        Number of Data Points (N): More data points mean more computations for splitting nodes at each level of each tree.

        Returns:
            int: the estimated computational cost
        """
        print("Running Gradient Boosted Trees")
        computational_cost = tree_num * self.samples * 2**depth
        return computational_cost

    def support_vector_machines_resource_estimation(self):
        """
        The Big O complexity of training support vector machines generally depends on several factors including the number of trees in the ensemble, the depth of each tree, and the number of data points.

        commonly SVM algorithms has a time complexity of O(n^2)

        Returns:
            int: the estimated computational cost
        """
        print("Running Support Vector Machines")
        computational_cost = self.samples**2
        return computational_cost

    def cnn_resource_estimation(self, k: int = 10, m: int = 23):
        """
        For a CNN layer with a single convolution operation, the time complexity per layer can be expressed as O(n^2 * k^2 * m), where:

        n is the size of the input feature map (width * height),
        k is the size of the convolutional kernel (width * height),
        m is the number of output channels.

        Returns:
            int: the estimated computational cost
        """
        print("Running CNN")
        computational_cost = self.features**2 * k**2 * m
        return computational_cost

    def estimate_resources(self):
        """Returns an estimate of computational cost for all models as a dictionary.

        Returns:
            dict: the models and their normalized estimated computational cost as a key-value pairs
        """

        results = {}
        data_choices = ["nvdi", "lst"]
        self._init_features_sample_size(data_choices)

        for model in self.models:
            if model == "Random Forest":
                results[model] = self.random_forest_resource_estimation()
            elif model == "Gradient Boosted Trees":
                results[model] = self.gradient_boosted_trees_resource_estimation()
            elif model == "Support Vector Machines":
                results[model] = self.support_vector_machines_resource_estimation()
            elif model == "CNN":
                results[model] = self.cnn_resource_estimation()

        # normalize the results
        max_value = max(results.values())
        results = {key: value / max_value for key, value in results.items()}

        return results
