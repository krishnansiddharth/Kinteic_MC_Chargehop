import numpy as np


##Extract total time if charge reaches end residue
Len  = [4,8,12,16,20]
last_res =[157,293,429,565,701]
data=[]
for j in range(len(Len)): 
	input_dat = np.genfromtxt("trajectory_ctpr%d.dat"%Len[j],delimiter=",",skip_header = 1)
	print("trajectory_ctpr%d.dat"%Len[j])
	t_success =   []
	iRun      =   []
	t_sum     =   0
	N         =   0
	t_per_hop_sum =0
	hops      = 0
	for i in range(len(input_dat[:,1])):
		if input_dat[i,1]==last_res[j]:
			t_success.append([input_dat[i,0],input_dat[i,2]])
			N+=1
			t_sum+=float(input_dat[i,2])
		if input_dat[i,0]==2:
			t_per_hop_sum+=float(input_dat[i,2])
			hops+=1

	t_avg = t_sum/N
	t_avg_per_hop=t_per_hop_sum/hops
	err = (np.array(t_success)[:,1]).std()/len(np.array(t_success))
	print("Average time is %.3f ns"%t_avg)
	print("Average time per hop is %.3f ns"%t_avg_per_hop)
	print("Electron succesfully reaches end %d time"%N)
	data.append([Len[j],t_avg,err,t_avg_per_hop])
output_arr = np.array(data)	
np.savetxt("averages.dat", output_arr, fmt = "%s,%s,%s,%s", header="Length Time Standard_error Time_per_Hop")	
		
		
