# Contextual multi-armed bandit project
Example of contextual MABs using the contextualbandits library. The project is divided into a simple and complex section.
In the simple jupyter, a simple non-contextual dataset is used to illustrate the typical methods such as e-greedy, UCB and Thompson sampling which
were implemented from scratch.
In the complex jupyter, a real dataset from Alibaba was used together with the contextualbandits library to illustrate an actual application for ad 
selection.

Complex dataset can be downloaded from https://github.com/openbenchmark/BARS/tree/master/ctr_prediction/datasets/Taobao

Important: the evaluation.py file of the contextualbandits module from https://github.com/david-cortes/contextualbandits was 
modified to store the cumulative reward during evaluation. 
Link to the modification: https://github.com/AlexSpacek/contextualbandits/commit/2a33f7667ddc2fd9c872116e8df503568aa60af6
