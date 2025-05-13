# show a menu
# handle inputs for add,view, etc.
# instantiate the budgettrakcer class
from tracker import *

df = pd.read_csv('./BudgetTracker.csv')
print(df.index.to_list())