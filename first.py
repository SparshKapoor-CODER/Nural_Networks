inputs = [1 , 2 , 3, 2.5]  # intializing input values for a neural network



#initialising weights
weights1 = [0.2 , 0.8 , -0.6, 1.0]
weights2 = [0.5 , 0.91 , -0.87, 0.5]
weights3 = [0.26 , 0.27 , 0.17, 0.93]



# initialising biases
biase1 = 2
biase2 = 3
biase3 = 0.51




# calculating the value of an hidden layer  
# value = input * weight  + bias
hidden = [ (inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + biase1) , 
          (inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + biase2) , 
          (inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + biase3) ]



# printing the values of hidden layer
print(hidden)   



# initializing weightes of hidden layer
hiddenweights = [0.989 , 0.87, 0.265]


# initializing bias of hidden layer
hiddenbias = 5



# calculating output
output = hidden[0]*hiddenweights[0] + hidden[1]*hiddenweights[1] + hidden[2]*hiddenweights[2]  + hiddenbias




# printing output
print(output)
