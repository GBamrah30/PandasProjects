# show a menu
# handle inputs for add,view, etc.
# instantiate the budgettrakcer class
from tracker import *

df = pd.read_csv('./BudgetTracker.csv')
for column in df.columns:
    print(f"{column}")