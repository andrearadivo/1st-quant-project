import numpy as np 

class PortfolioOptimizer:

	"""Executes Monte Carlo simulations to maximize Sharpe ratio under volatility constraints."""

	def __init__(self, mean_return, cov_matrix, num_portfolios = 100000, max_volatility_allowed = 1.0, risk_free_rate = 0.04):
		self.mean_return = mean_return
		self.cov_matrix = cov_matrix
		self.num_portfolios = num_portfolios
		self.max_volatility_allowed = max_volatility_allowed
		self.risk_free_rate = risk_free_rate

		self.all_returns = np.zeros(num_portfolios)
		self.all_volatilities = np.zeros(num_portfolios)
		self.all_sharpes = np.zeros(num_portfolios)


	def simulate_portfolios(self):

		"""
        Runs vectorized Monte Carlo simulations for maximum performance.
        Returns: (best_weights, best_returns, best_volatility, best_sharpe).
        """

		print("[SYSTEM] Starting vectorized simulations...")
		num_assets = len(self.mean_return)

		weights = np.random.random((self.num_portfolios, num_assets))
		weights = weights/ weights.sum(axis = 1, keepdims = True)

		self.all_returns = np.dot(weights, self.mean_return)
		self.all_volatilities = np.sqrt((weights*np.dot(weights,self.cov_matrix)).sum(axis=1))
		self.all_sharpes = (self.all_returns - self.risk_free_rate)/self.all_volatilities

		valid_sharpes = np.where(self.all_volatilities <= self.max_volatility_allowed, self.all_sharpes, -np.inf)
		best_idx = np.argmax(valid_sharpes)

		best_weights = weights[best_idx]
		best_returns = self.all_returns[best_idx]
		best_volatility = self.all_volatilities[best_idx]
		best_sharpe = self.all_sharpes[best_idx]

		return best_weights, best_returns, best_volatility, best_sharpe
