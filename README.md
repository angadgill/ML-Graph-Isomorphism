# ML-Graph-Isomorphism
The purpose of this project was to study the graph isomorphism problem and attempt to predict graph isomorphism in polynomial time using machine learning methods.  

## The Idea
We assume that, given the right data, machine learning models will be able to distinguish isomorphic graph pairs from non-isomorphic graph pairs. If the features required for such a model to work can be calculated in polynomial time, then we would have a polynomial time method for graph isomorphism (at least when we use the model to predict, perhaps not when we train the model). We trained a machine learning model which uses graph features to determine isomorphism and one neural network model which uses only the adjacency matrix to determine isomorphism. 

## The models
Our machine learning models are contained in the `scripts/model/` folder. We created one Logistic Regression model using [SciKit Learn](http://scikit-learn.org/) library and two neural network models using the [Keras](http://keras.io) library. The models were trained and tested using synthesized graphs, including Pairs of Iso-spectral Non-isomorphic Graphs (PING) which are crucial for training a machine learning model of this nature. Our code for PING is available in `scripts/graphScripts/ping.py`  

## The results
We found that the Logistic Regression model achieved 66% accuracy in determining isomorphism while the neural network models achieved 99.9% accuracy. The almost perfect prediction capability of the neural network model warrants further investigation. It may very well be that our dataset is not representative and that we need to add more (and bigger) graphs to it.  

Model Accuracy | 300 11-node graph pairs | 300 101-node graph pairs | 900 301-node graph pairs
------------- | ------------- | ------------- | ------------- 
Logistic Regression | 66% | 66% | 66%
Neural Network | 99.9% | 99.9% | 99.9%


