import pandas as pd 
import numpy as np 

class FinancialMetrics:

	def __init__(self, price_data):
		self.price_data = price_data

		self.returns = None
		self.mean_returns = None
		self.cov_matrix = None

	
	def calculate_metrics(self):

		self.returns = self.price_data.pct_change(fill_method=None).dropna()
		print("[SYSTEM] Daily returns acquired!")

		self.mean_returns = self.returns.mean()*252
		print("[SYSTEM] Mean retruns acquired!")

		self.cov_matrix = self.returns.cov()*252

