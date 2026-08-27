"""
Main orchestrator for the Portfolio Optimization project.
Combines data ingestion, mathematical optimization, and visualization.
"""

from data_ingestion import MarketData
from financial_core import FinancialMetrics
from optimizer import PortfolioOptimizer
from visualizer import PortfolioVisualizer

def main():

	assets = ['URTH','VOO','QQQ','TLT','PLTR']
	start_date = '2021-01-01'
	end_date = '2026-08-23'

	downloader = MarketData(assets,start_date,end_date) #downloader
	price_chart, assets = downloader.download_data()

	if price_chart is not None: 
		
		engine = FinancialMetrics(price_chart)
		engine.calculate_metrics()

		simulator = PortfolioOptimizer(engine.mean_returns,engine.cov_matrix, 100000, 1.00,0.04)
		weights, returns, volatility, sharpe = simulator.simulate_portfolios()

		if returns is None:
			print("\n" + "!"*40)
			print(" [WARNING] OPTIMIZATION FAILED")
			print("!"*40)
			print("No portfolio could be generated within the given volatility limits.")
			print("Action required: Increase your target volatility or add lower-risk assets (e.g., Bonds) to your ticker list.")
			print("!"*40 + "\n")
		
		else:
			print("\n" + "="*40)
			print("    OPTIMIZED PORTFOLIO (MAX SHARPE)")
			print("="*40)
			print(f"Expected Returns:  {returns:.2%}")
			print(f"Risk (Volatility): {volatility:.2%}")
			print(f"Sharpe ratio:   {sharpe:.2f}")
			print("-" * 40)
			print("Ideal Allocation:")
			for k in range(len(assets)):
				
				print(f"-{assets[k]}  {weights[k]:.2%}")

			print("="*40 + "\n")

			visualizer = PortfolioVisualizer(simulator)
			visualizer.plot_efficient_frontier(volatility,returns)

if __name__ == "__main__":
    main()