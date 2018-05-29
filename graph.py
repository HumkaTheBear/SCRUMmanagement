import numpy as np
import matplotlib.pyplot as plt
# import matplotlib as mpl

# BEST WAY
# x(from zero, to max days), y(total working hours, to zero)
plt.plot([0, 6], [150,0], 'og--')
# WORST WAY
# x(from zero, to max days), y(total working hours, to zero)
plt.plot([0, 10], [150,0], 'or--') 
# NOW EFFORT
# x(...), y(...)
plt.plot([0, 1, 2], [150,115,100], 'ob-') 
# LEFT
# x(days), y(hoursLeft)
plt.plot([0, 1, 2], [150+10,125+10,115+10], 'oc-') 

# DAILY WRKDONE
days = (1,2,3,4,5,6,7,8,9,10)
workdone = [35, 15, 0, 0, 0 ,0 ,0 ,0 ,0 ,0]
y_pos = np.arange(len(days))
plt.bar(y_pos, workdone, width=0.5, color="yellow",edgecolor = "black") 
plt.xticks(y_pos, days)

# AXIS
plt.grid()
plt.axis([0,10,0,160])
plt.xlabel('Days')
plt.ylabel('Remaining effort (hours)')
plt.title('Burn-down chart')

#SHOW
plt.show()
