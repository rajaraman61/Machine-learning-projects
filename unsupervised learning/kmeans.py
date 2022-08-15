# import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint
from sklearn.cluster import KMeans, k_means

# Fetch files
mall_customers = pd.read_csv('../data/mall_customers.csv')

# pprint(mall_customers.head(5))
# pprint(mall_customers.shape)
# pprint(mall_customers.isnull().sum())

# Feature Selection
X = mall_customers.iloc[:, [3, 4]].values
# pprint(X)

# Build the model
'''
    Kmeans Algorithm to decide the optimum cluster number, KMeans using Elbow method - to figure
    out K for Kmeans, Elbow method on Kmeans ++ calculation
'''

models = []
wcss = []
'''
    We always assume the max number of cluster would be 10, we can judge te number of clusters by doing  averaging
'''
for x in range(1, 11):
    kmeans = KMeans(n_clusters=x, init='k-means++', random_state=0)
    kmeans.fit(X)
    models.append(kmeans)

for x in models:
    wcss.append(x.inertia_)

# Plot & Visualize
# plt.plot(range(1,11), wcss)
# plt.title('The Elbow method')
# plt.xlabel('no of clusters')
# plt.ylabel('wcss')
# plt.show()  K MEANS | SVM 


# Finally we got that k = 5
k_means_model = KMeans(n_clusters=5, init='k-means++', random_state=0)
y_kmeans = k_means_model.fit_predict(X)
print(k_means_model.inertia_)
# Visualize
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label='Cluster one')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label='Cluster two')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label='Cluster three')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label='Cluster four')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label='Cluster five')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 100, c = 'yellow', label='Centroind')

plt.title('Clusters of customers')
plt.xlabel('Annual Incosme ($)')
plt.ylabel('Spending score (1-100)')
plt.legend()
plt.show()


# cluster 1 - earning high but spending less
# cluster 2 - average in terms of earning and spending
# cluster 3 - earning high and also spending high [Target SET]
# cluster 4 - earning less but spending more 
# cluster 5 - earning less spending less