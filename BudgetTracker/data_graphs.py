import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tracker import BudgetTracker

class Graphs:
    def __init__(self, df):
        self.df = df
        sns.set_theme()
        
    def spend_by_category(self):
        # Bar plot of spend
        sns.set_style("darkgrid")
        fig, ax = plt.subplots()
        sns.barplot(x='Category', y='Amount', data=self.df, ax=ax)
        ax.set_title("Spending by Category")
        return fig
    
    def average_spend(self):
        sns.set_style("darkgrid")
        # Group by category and calculate average amount
        avg = self.df.groupby('category')['amount'].mean().reset_index()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(data=avg, x='amount', y='category', ax=ax)
        ax.set_title("Average Spend by Category")
        ax.set_xlabel("Average Spend")
        ax.set_ylabel("Category")
        # Layout fix and return figure
        fig.tight_layout()
        return fig

    def spend_over_time(self):
        # Line plot over time
        pass
    
    def monthly_spend(self):
        # Stacked bar plot or regular bar plot with x-axis as dates
        pass
        
    def category_stats(self):
        # Box Whiskey Plot showing median, range and outliers
        pass
    
    def cumulative_spend(self):
        # Growing expense curve
        pass
        
    def kde_plot(self):
        # Option, KDE of all purchases
        pass
    
    def rolling_spend(self):
        # Optional, this will should 30 day trend/patterns
        pass
    
    
        
    
    