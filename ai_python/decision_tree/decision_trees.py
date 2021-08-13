import math
from DecisionNode import DecisionNode
import random
import numpy as np


def entropy(class_vector):
    """Compute the entropy for a list
    of classes (given as a list of values being 0 or 1)."""
    # TODO: calculate and return entropy
    if len(class_vector) == 0:
        return 0
    return function_B(class_vector.count(1)/len(class_vector))


def function_B(q):
    """Compute the value of B(q) as per the book's formula and class instruction"""
    # TODO: calculate and return B(q)
    if q == 0 or q == 1:
        return 0
    if q == 0.5:
        return 1
    return -(q*math.log(q, 2)+(1-q)*math.log((1-q), 2))


def information_gain(previous_classes, current_classes):
    """Compute the information gain between the previous and current classes (each
    a list of 0 and 1 values)."""
    # TODO: calculate and return information gain
    #print(previous_classes)
    prev_entropy = entropy(previous_classes)
    remainder = 0
    for item in current_classes:
        remainder += (len(item)/len(previous_classes)) * entropy(item)
    return prev_entropy - remainder


class OutcomeMetrics():
    def __init__(self, classifier_labels, actual_labels):
        self.classifier_labels = classifier_labels
        self.actual_labels = actual_labels
        self.confusion_matrix = self.__build_confusion_matrix()

    def __build_confusion_matrix(self):
        # format should be [[true_positive, false_negative], [false_positive, true_negative]]
        # TODO: build the confusion matrix as formatted above
        matrix = [[0, 0], [0, 0]]
        labels = zip(self.classifier_labels, self.actual_labels)
        for class_label, actual_label in labels:
            if class_label == 1 and actual_label == 1:
                #tp
                matrix[0][0] += 1
            elif class_label == 1 and actual_label == 0:
                #fp
                matrix[1][0] += 1
            elif class_label == 0 and actual_label == 1:
                #fn
                matrix[0][1] += 1
            else:
                #tn
                matrix[1][1] += 1
        print(matrix)
        return matrix

    def get_confustion_matrix(self):
        return self.confusion_matrix

    def precision(self):
        # precision is measured as: true_positive/ (true_positive + false_positive)
        # TODO: calculate and return precision
        if (self.confusion_matrix[0][0] + self.confusion_matrix[1][0]) == 0:
            return 0
        return self.confusion_matrix[0][0]/(self.confusion_matrix[0][0] + self.confusion_matrix[1][0])

    def recall(self):
        #recall is measured as: true_positive/ (true_positive + false_negative)
        # TODO: calculate and return recall
        if (self.confusion_matrix[0][0] + self.confusion_matrix[0][1]) == 0:
            return 0
        return self.confusion_matrix[0][0] / (self.confusion_matrix[0][0] + self.confusion_matrix[0][1])

    def accuracy(self):
        #accuracy is measured as:  correct_classifications / total_number_examples
        # TODO: calculate and return accuracy
        return (self.confusion_matrix[0][0] + self.confusion_matrix[1][1])/len(self.actual_labels)



class DecisionTree():
    """Class for automatic tree-building
    and classification."""

    def __init__(self, depth_limit=float('inf')):
        """Create a decision tree with an empty root
        and the specified depth limit."""
        self.root = None
        self.depth_limit = depth_limit

    def fit(self, features, classes):
        """
        Build the tree from root using __build_tree__().
        :param features: A numpy 2D list that contains the features or attributes of the data.
        :param classes: A numpy list that contains the classification or outcome of the data that
                        that is parallel to the features list.
        :return: There is nothing returned but you are to set the root of the tree so decsions can
                 be made later.
        """
        self.root = self.__build_tree__(features, classes)

    def __build_tree__(self, features, classes, depth=0):
        """Implement the above algorithm to build
        the decision tree using the given features and
        classes to build the decision functions."""
        # TODO: create simple tree by returning the root node
        #print(classes)
        left_features = []
        left_classes = []
        right_features = []
        right_classes = []
        info_gain = 0

        fc_list = zip(features, classes)
        val_list = [np.average(features, axis=0),
                    np.median(features, axis=0),
                    3.5]
        # f = lambda feature: feature[0] > feature[1]
        function_list = [lambda feature, avg, i: feature[i] > avg, lambda feature, med, i: feature[i] >= med,
                         lambda feature, gpa, i: feature[i] >= gpa]
        fv_list = zip(function_list, val_list)
        split_function = function_list[0]
        function_index = 0
        function_value = 0

        for i in range(len(features[0])):
            temp_left_features = []
            temp_left_classes = []
            temp_right_features = []
            temp_right_classes = []

            for func, val in fv_list:
                for record, c in fc_list:
                    #print(record)
                    #print(val)
                    #print(i)
                    if func(record, val[i], i):
                        temp_left_features.append(record)
                        temp_left_classes.append(c)
                    else:
                        temp_right_features.append(record)
                        temp_right_classes.append(c)
                #print(temp_right_classes)
                #print(temp_left_classes)
                #print(classes)
                temp_info_gain = information_gain(classes, [temp_left_classes, temp_right_classes])
                if temp_info_gain > info_gain:
                    info_gain = temp_info_gain
                    left_features = temp_left_features
                    left_classes = temp_left_classes
                    right_features = temp_right_features
                    right_classes = temp_right_classes
                    split_function = func
                    function_index = i
                    function_value = val[i]

        # we hit a leaf node if all elem in class are 0 or 1
        if sum(classes) == len(classes) and info_gain == 0:
            #if all elem are 1
            return DecisionNode(None, None, None, 1)
        elif sum(classes) == 0 and info_gain == 0:
            # if all elem are 0
            return DecisionNode(None, None, None, 0)
        elif info_gain == 0:
            #if not all 0 or 1 randomly choose a classification based on the chance in class
            cl = classes[random.randrange(len(classes))]
            return DecisionNode(None, None, None, cl)

        #if some info gain > 0 split and build tree on that split
        left_node = self.__build_tree__(left_features, left_classes)
        right_node = self.__build_tree__(right_features, right_classes)

        return DecisionNode(left_node, right_node, (split_function, function_value, function_index), None)

    def classify(self, features):
        """Use the fitted tree to
        classify a list of examples.
        Return a list of class labels."""
        class_labels = []
        class_labels = [self.root.decide(feature) for feature in features]
        return class_labels
