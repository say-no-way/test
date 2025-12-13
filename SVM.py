from sklearn import svm
from sklearn.datasets import make_classification, make_blobs, load_iris
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

# Toy data
def toy_data():
    X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, n_classes=2, n_clusters_per_class=1, random_state=42)
    return X, y

# Random data
def random_data():
    X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=42)
    return X, y

# Iris data
def iris_data():
    iris = load_iris()
    X = iris.data
    y = iris.target
    return X, y

# 1. SVM with different kernels and C values
def svm_experiment(X, y, kernel, C):
    clf = svm.SVC(kernel=kernel, C=C)
    clf.fit(X, y)
    return clf

# 2. Split iris_data into train and test sets and find best hyperparameters
def find_best_params(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
    
    best_score = 0
    best_params = {'kernel': None, 'C': None}
    
    kernels = ['linear', 'poly', 'rbf', 'sigmoid']
    Cs = [0.1, 1, 10, 100]
    
    for kernel in kernels:
        for C in Cs:
            clf = svm.SVC(kernel=kernel, C=C)
            clf.fit(X_train, y_train)
            score = clf.score(X_test, y_test)
            if score > best_score:
                best_score = score
                best_params['kernel'] = kernel
                best_params['C'] = C
    
    return best_params

# 3. Plot SVM classifier with support vectors on random data
def plot_svm(X, y, clf):
    plt.scatter(X[:, 0], X[:, 1], c=y, s=30, cmap=plt.cm.Paired)
    
    # Plot support vectors
    plt.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100, facecolors='none', edgecolors='k')
    
    # Create mesh to plot decision boundary
    ax = plt.gca()
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 50),
                         np.linspace(ylim[0], ylim[1], 50))
    
    Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    # Plot decision boundary and margins
    plt.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5,
                linestyles=['--', '-', '--'])
    
    plt.show()

# Experiment with toy_data
X_toy, y_toy = toy_data()
clf_toy = svm_experiment(X_toy, y_toy, kernel='linear', C=1)
print("Toy Data:")
print("Support vectors:")
print(clf_toy.support_vectors_)
plot_svm(X_toy, y_toy, clf_toy)

# Experiment with random_data
X_random, y_random = random_data()
clf_random = svm_experiment(X_random, y_random, kernel='linear', C=1)
print("Random Data:")
print("Support vectors:")
print(clf_random.support_vectors_)
plot_svm(X_random, y_random, clf_random)

# Experiment with iris_data and find best hyperparameters
X_iris, y_iris = iris_data()
best_params_iris = find_best_params(X_iris, y_iris)
print("Best hyperparameters for Iris Data:", best_params_iris)
