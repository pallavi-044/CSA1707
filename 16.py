import numpy as np

def sigmoid(x): return 1/(1+np.exp(-x))

# Training data (AND gate)
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[0],[0],[1]])

np.random.seed(1)
w = 2*np.random.random((2,1))-1
b = 0

for _ in range(5000):
    out = sigmoid(np.dot(X,w)+b)
    error = y - out
    w += np.dot(X.T, error* out*(1-out))
    b += np.sum(error* out*(1-out))

a = int(input("Enter first input (0/1): "))
c = int(input("Enter second input (0/1): "))
pred = sigmoid(np.dot([a,c],w)+b)
print("Predicted Output:", round(pred.item()))
