import numpy as np
import matplotlib.pyplot as plt
# import matplotlib as mpl

# BEST WAY
plt.plot([0, 6], [150,0], 'og--')
# WORST WAY
plt.plot([0, 10], [150,0], 'or--') 
# NOW
plt.plot([0, 1, 2], [150,115,100], 'ob-') 
# LEFT
plt.plot([0, 1, 2], [150,140,100], 'oc-') 


# DAILY WRKDONE
days = (1,2,3,4,5,6,7,8,9,10)
workdone = [35, 15, 0, 0, 0 ,0 ,0 ,0 ,0 ,0]
y_pos = np.arange(len(days))
plt.bar(y_pos, workdone, align="center", color="yellow",edgecolor = "black") 
plt.xticks(y_pos, days)

# AXIS
plt.grid()
plt.axis([0,10,0,160])
plt.xlabel('Days')
plt.ylabel('Remaining effort (hours)')
plt.title('Burn-down chart')

#SHOW
plt.show()
