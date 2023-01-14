# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 01:48:07 2022

@author: DELL
"""

import tkinter as tk
from tkinter import ttk
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
from matplotlib import pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Decision Tree Comparison")
        self.root.geometry("1000x2000")

        # Load the Iris dataset
        self.iris = datasets.load_iris()
        self.X = self.iris.data
        self.y = self.iris.target

        # Split the data into training and test sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2)

        # Create the decision tree models
        self.id3 = DecisionTreeClassifier(criterion="entropy")
        self.c45 = DecisionTreeClassifier(criterion="gini")
        self.cart = DecisionTreeClassifier(criterion="gini")
        self.dt = DecisionTreeClassifier()
        self.rf = RandomForestClassifier()
        self.ada = AdaBoostClassifier()
        self.gb = GradientBoostingClassifier()

        # Create the GUI
        self.create_widgets()

    def create_widgets(self):
        # Create the label for the dropdown menu
        self.model_label = tk.Label(self.root, text="Select a model:")
        self.model_label.pack()

        # Create the dropdown menu
        self.model_var = tk.StringVar(self.root)
        self.model_var.set("Decision Tree")
        self.model_dropdown = ttk.Combobox(self.root, textvariable=self.model_var, values=["Decision Tree", "Random Forest", "AdaBoost", "Gradient Boosting", "ID3", "C4.5", "CART"])
        self.model_dropdown.pack()

        # Create the "Train" button
        self.train_button = tk.Button(self.root, text="Train", command=self.train_model)
        self.train_button.pack()
        
        self.show_graph_button = tk.Button(self.root, text="Show Graph", command=self.show_graph)
        self.show_graph_button.pack()

        # Create the label for the accuracy display
        self.accuracy_label = tk.Label(self.root, text="Accuracy:")
        self.accuracy_label.pack()

        # Create the accuracy display
        self.accuracy_display = tk.Label(self.root, text="")
        self.accuracy_display.pack()
        
        self.show_iris_button = tk.Button(self.root, text="Show Iris Dataset", command=self.show_iris)
        self.show_iris_button.pack()

    def show_graph(self):
        self.reset()
        #Reset the display by deleting the current figure
        #for widget in self.root.winfo_children():
         #   widget.destroy()

        # Re-create the widgets
        #self.create_widgets()
        # Get the selected model from the dropdown menu
        model = self.model_var.get()
        
        # Train the selected model
        if model == "Decision Tree":
            tree = self.dt
        elif model == "Random Forest":
            tree = self.rf.estimators_[0]
        elif model == "AdaBoost":
            tree = self.ada.base_estimator_
        elif model == "Gradient Boosting":
            tree = self.gb.estimators_[0][0]
        elif model == "ID3":
            tree = self.id3
        elif model == "C4.5":
            tree = self.c45
        elif model == "CART":
            tree = self.cart
        else:
            return

    # Create the figure and axis for the plot
    
        fig, ax = pyplot.subplots(dpi=200)

    # Plot the tree
        plot_tree(tree, feature_names=self.iris.feature_names, ax=ax)
    
    # Create the canvas for the plot
        canvas = FigureCanvasTkAgg(fig, self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()
    def reset(self):
        # Reset the display by deleting the current figure
        for widget in self.root.winfo_children():
            widget.destroy()

        # Re-create the widgets
        self.create_widgets()
    def show_iris(self):
        # Reset the display by deleting the current widgets
        for widget in self.root.winfo_children():
            widget.destroy()

        # Re-create the widgets
        self.create_widgets()

        # Display the Iris dataset in some way (e.g. by adding it to the DOM or console logging it)
        iris_label = tk.Label(self.root, text=f"Iris dataset:\n{self.iris}")
        iris_label.pack()


    def train_model(self):
        self.reset()
    # Get the selected model from the dropdown menu
        model = self.model_var.get()

    # Train the selected model
        if model == "Decision Tree":
            self.dt.fit(self.X_train, self.y_train)
            predictions = self.dt.predict(self.X_test)
        elif model == "Random Forest":
            self.rf.fit(self.X_train, self.y_train)
            predictions = self.rf.predict(self.X_test)
        elif model == "AdaBoost":
            self.ada.fit(self.X_train, self.y_train)
            predictions = self.ada.predict(self.X_test)
        elif model == "Gradient Boosting":
            self.gb.fit(self.X_train, self.y_train)
            predictions = self.gb.predict(self.X_test)
        elif model == "ID3":
            self.id3.fit(self.X_train, self.y_train)
            predictions = self.id3.predict(self.X_test)
        elif model == "C4.5":
            self.c45.fit(self.X_train, self.y_train)
            predictions = self.c45.predict(self.X_test)
        elif model == "CART":
            self.cart = DecisionTreeClassifier(criterion="gini")
            self.cart.fit(self.X_train, self.y_train)
            predictions = self.cart.predict(self.X_test)

    # Calculate and display the accuracy
        accuracy = accuracy_score(self.y_test, predictions)
        self.accuracy_display.config(text=f"{accuracy:.2f}")

