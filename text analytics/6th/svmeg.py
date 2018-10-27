__author__ = 'user'
# http://pythonprogramming.net/support-vector-machine-svm-example-tutorial-scikit-learn-python/
'''
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

digits = datasets.load_digits()

classifier = svm.SVC(gamma=0.01, C=100)

print(len(digits.data))

x, y = digits.data[15:], digits.target[15:]
classifier.fit(x, y)
print(digits.data[7])
print('Prediction:', classifier.predict(digits.data[1].reshape(1,-1)))

plt.imshow(digits.images[-2], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()

plt.figure()
plt.imshow(digits.images[-4])
plt.show()'''