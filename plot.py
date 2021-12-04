import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def exp(x,b,c):
	return c*np.exp(-b*x)

input_dat = np.genfromtxt("averages.dat",delimiter=",")
time = np.array(input_dat[:,1])
i   = 0.16/time
Len = np.array(input_dat[:,0],dtype='int')
std  = input_dat[:,2]
crystal_len = np.array([3.76,7.52,11.28,15.04,18.8])
lineStyle_City_A={"linestyle":" ", "linewidth":2, "markeredgewidth":2, "elinewidth":2, "capsize":7}
popt, pcov = curve_fit(exp, crystal_len, i)
print(popt[0],popt[1])
#plt.plot(x,exp(x,popt[0],popt[1]),color="black",label=r"%.2fexp(%.2f x)"%(popt[1],popt[0]))
plt.scatter(crystal_len,i,s=100,color="black")
plt.yscale('log')
plt.errorbar(crystal_len,i,yerr=std,color="black")
print(std)
plt.ylabel("Current(nA)",fontsize=20)
plt.xlabel("Crystollographic length(nm)",fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20, width=2.5, length=10)

#plt.legend(fontsize=8)
#plt.legend()
plt.savefig("plot.pdf",text_bbox = "tight")
plt.figure()
#plt.plot(x,exp(x,popt[0],popt[1],popt[2]),color="black",label=r"%.2f*exp(%.2f x)+%.2f"%(popt[0],popt[1],popt[2]))
#plt.legend()
plt.scatter(crystal_len,i,color="blue")
plt.yscale('log')
#plt.errorbar(crystal_len,i,yerr=std,)
plt.ylabel("Current(nA)")
plt.xlabel("CTPRn")
plt.xticks(crystal_len,Len)
plt.savefig("plot2.pdf")
