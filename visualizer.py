import matplotlib.pyplot as plt

class PortfolioVisualizer:

	"""Renders the Efficient Frontier chart using matplotlib."""

	def __init__(self, simulator_instance):
		self.simulator = simulator_instance

	def plot_efficient_frontier(self, opt_vol, opt_ret):

		"""Plots all simulated portfolios and highlights the optimal Max Sharpe point."""

		print("[SYSTEM] Generating Efficient Frontier chart...")

		plt.figure(figsize=(10,6))
		scatter = plt.scatter(
			self.simulator.all_volatilities,
			self.simulator.all_returns,
			c = self.simulator.all_sharpes, 
			cmap='viridis', 
			marker='o',
			s=10,
			alpha=0.3
		)
		plt.colorbar(scatter, label='Sharpe Ratio (Rendimento / Rischio)')

		plt.scatter(
            opt_vol, opt_ret, 
			facecolors='none', 
            edgecolors='black',
            linewidth = 1.5,
            marker='o', 
            s=120, 
            zorder=5, 
            label='Optimal allocation'
		)

		plt.scatter(
            opt_vol, opt_ret, 
            color='black', 
            marker='+',         
            s=50, 
            zorder=6
        )

		plt.annotate(
            'Max Sharpe', 
            xy=(opt_vol, opt_ret), 
            xytext=(opt_vol + 0.015, opt_ret - 0.005), 
            fontsize=9, 
            fontweight='normal',
            style='italic',      
            bbox=dict(boxstyle='round,pad=0.3', fc='white', ec='gray', alpha=0.8)
        )

		plt.legend(loc='upper left')

		plt.title('Monte Carlo Simulation: Efficient Frontier', fontsize=14)
		plt.xlabel('Volatilità Annualizzata (Rischio)', fontsize=12)
		plt.ylabel('Rendimento Atteso', fontsize=12)
		plt.grid(True, linestyle='--', alpha=0.5)

		plt.savefig("docs/efficient_frontier.png")
		plt.show()
