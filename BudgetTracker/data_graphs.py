import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Graphs:
    def __init__(self, df):
        self.df = df.copy()
        self.df['date'] = pd.to_datetime(self.df['date'])  # Ensure 'Date' is datetime once
        sns.set_theme()
        
    def spend_by_category(self):
        # Bar plot of spend
        sns.set_style('darkgrid')
        fig, ax = plt.subplots()
        sns.barplot(x='category', y='amount', data=self.df, ax=ax)
        ax.set_title("Spending by Category")
        ax.set_xlabel("Category")
        ax.set_ylabel("Amount Spent")
        fig.tight_layout()
        return fig
    
    def average_spend(self):
        # Horizontal bar plot
        sns.set_style('darkgrid')
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
        sns.set_style('darkgrid')
        fig, ax = plt.subplots(figsize=(10, 6))
        df_sorted = self.df.sort_values(by='date')
        sns.lineplot(x='date', y='amount', data=df_sorted, ax=ax)
        ax.set_title("Spend Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Amount Spent")
        fig.tight_layout()
        return fig
    
    def monthly_spend(self):
        sns.set_style('darkgrid')
        self.df['YearMonth'] = self.df['date'].dt.to_period('M').astype(str)
        monthly = self.df.groupby('YearMonth')['amount'].sum().reset_index()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='YearMonth', y='amount', data=monthly, ax=ax)
        ax.set_title("Monthly Spend")
        ax.set_xlabel("Month")
        ax.set_ylabel("Total Spend")
        plt.xticks(rotation=45)
        fig.tight_layout()
        return fig

    def category_stats(self):
        sns.set_style('darkgrid')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.boxplot(x='category', y='amount', data=self.df, ax=ax)
        ax.set_title("Spend Distribution by Category")
        ax.set_xlabel("Category")
        ax.set_ylabel("Amount")
        fig.tight_layout()
        return fig
    
    def cumulative_spend(self):
        sns.set_style('darkgrid')
        df_sorted = self.df.sort_values(by='date').copy()
        df_sorted['CumulativeSpend'] = df_sorted['amount'].cumsum()
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.lineplot(x='date', y='CumulativeSpend', data=df_sorted, ax=ax)
        ax.set_title("Cumulative Spend Over Time")
        ax.set_xlabel("Date")
        ax.set_ylabel("Cumulative Spend")
        fig.tight_layout()
        return fig
        
    def kde_plot(self):
        sns.set_style('darkgrid')
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.kdeplot(data=self.df, x='amount', ax=ax, fill=True)
        ax.set_title("Purchasing Density")
        ax.set_xlabel("Amount")
        fig.tight_layout()
        return fig
    
    #def rolling_spend(self):
        # Optional, this will should 30 day trend/patterns