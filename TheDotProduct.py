import numpy as np
inputs = [1 , 2 , 3, 2.5]
weights = [
    [0.2 , 0.8 , -0.6, 1.0],
    [0.5 , 0.91 , -0.87, 0.5],
    [0.26 , 0.27 , 0.17, 0.93]
    ]
biases = [6 , 0.5 , 0.89]
hidden = np.dot(weights , inputs) + biases
hiddenweights = [0.989 , 0.87, 0.265]
hiddenbias = 5
output = np.dot(hidden, hiddenweights) + hiddenbias
print(output)
