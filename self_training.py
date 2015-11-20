from __future__ import division
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


class Self_Train(object):
	"""

	"""
	def __init__(self, percent_propagate=0.25, learning_rate=1):
		"""

		:param percent_propagate: what percent of the unlabeled data should
			labels be propagated onto.
		:param learning_rate: how many of the most confident predictions should
			be propagated onto .
		:return:
		"""
		self.percent_propagate = percent_propagate
		self.learning_rate
		self.final_fit = None

	def fit(self, x, y, x_unlabeled):
		"""

		:param x_labeled:
		:param y:
		:param x_unlabeled:
		:return:
		"""
		num_unlabeled = x_unlabeled.shape[0]
		num_runs = int(round(num_unlabeled * self.percent_propagate / self.learning_rate))
		if num_runs <= 0:
			print "cannot run less than one time"

		# transform x
		scaler = StandardScaler()
		x_train = scaler.fit_transform(x)
		x_unlabeled = scaler.transform(x_unlabeled)

		for run in num_runs:
			# train model on x and y
			clf = LogisticRegression(penalty='l1')
			clf = clf.fit(x_train, y)

			# predict on unlabeled x
			y_hat = clf.predict(x_unlabeled)

			# find prediction with strongest confidence
			y_confidence = np.where(y_hat < 0.5, 1 - y_hat, y_hat)
			threshold = y_confidence.sort()[-1*self.learning_rate]
			propagate_indices = np.where(y_confidence > threshold)

			# append the propogated data and labels
			x_train = np.stack((x_train, x_unlabeled[propagate_indices, :]))
			y = np.stack((y, y_hat[propagate_indices]))

		return clf






