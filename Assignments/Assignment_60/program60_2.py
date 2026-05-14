#########################################################################
# Problem Statement :
#       Write a python program to demonstrate different activation function
#       1. Sigmoid
#       2. ReLU
#       3. tanh
#########################################################################

import numpy as np
import math
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------
#   Step 1 : Define Activation Function (Sigmoid)
#-------------------------------------------------------------------------

def sigmoid(z):
    ans = 1 / (1 + math.exp(-z))
    return ans

def plot_sigmoid():

    z_values = np.linspace(-10, 10, 200)

    sigmoid_values = 1 / (1 + np.exp(-z_values))

    plt.figure(figsize=(8, 5))
    plt.plot(z_values, sigmoid_values, label="Sigmoid Function", linewidth=2, color="blue")

    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.axhline(y=1, color="black", linewidth=0.5)
    plt.axvline(x=0, color="gray", linestyle="--")


    plt.title("Sigmoid Activation Function", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output (Probability)", fontsize=14)

    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    plt.show()

#-------------------------------------------------------------------------
#   Step 2 : Define Activation Function (ReLu)
#-------------------------------------------------------------------------

def relu(z):
    ans = max(0,z)
    return ans

def plot_relu():

    # Generate range of values fro Z
    z_values = np.linspace(-10, 10, 200)

    # Apply ReLU on all values 
    relu_values = np.maximum(0, z_values)

    # plot Graph
    plt.figure(figsize =(8, 5))
    plt.plot(z_values, relu_values, label="ReLU Function", linewidth=2, color="green")

    # Axex lines  
    plt.axhline(y=0, color="black", linewidth=0.5)
    plt.axvline(x=0, color="gray", linestyle="--")


    # Lables and title
    plt.title("ReLU Activation Function", fontsize=16)
    plt.xlabel("Input (z)", fontsize=14)
    plt.ylabel("Output ", fontsize=14)

    # Grid and legend
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()

    # Show Graph
    plt.show() 



#-------------------------------------------------------------------------
#   Step 3 : Define Activation Function (tanh)
#-------------------------------------------------------------------------

def tanh(z):
    ans = (math.exp(z) - math.exp(-z)) / (math.exp(z) + math.exp(-z))
    return ans

def plot_tanh():
    z_values = np.linspace(10, -10, 200)

    tanh_values = np.tanh(z_values)

    plt.plot(z_values, tanh_values)
    plt.title("tanh activation function")
    plt.xlabel("x")
    plt.ylabel("tanh(x)")
    plt.grid(True)

    plt.show()


def single_neuron(inputs, weights, bias):

    print("Inputs  (x) :",inputs)
    print("Weights (w) :",weights)
    print("bias    (b) :",bias)

    z = sum(x*w for x, w in zip(inputs, weights)) + bias

    return z

def main():

    # Example inputs
    inputs = [1.0, 2.0, 3.0]

    # Weights
    weights = [0.6, 0.4, -0.2]

    # bias
    bias = 0.5

    print("------------- Using Sigmoid Activation Function -------------")

    #Forward Pass
    z = single_neuron(inputs, weights, bias)
    y_hat = sigmoid(z)

    print("weighted sum :",z)
    print("Final y_hat : ",y_hat)

    plot_sigmoid()


    print("\n------------- Using ReLU Activation Function -------------")

    #Forward Pass
    z = single_neuron(inputs, weights, bias)
    y_hat = relu(z)

    print("weighted sum :",z)
    print("Final y_hat  :",y_hat)

    plot_relu()


    print("\n------------- Using tanh Activation Function -------------")

    #Forward Pass
    z = single_neuron(inputs, weights, bias)
    y_hat = tanh(z)

    print("weighted sum :",z)
    print("Final y_hat  :",y_hat)

    plot_tanh()

if __name__ == "__main__":
    main()
    


