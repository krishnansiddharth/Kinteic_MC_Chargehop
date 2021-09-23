import graph
from common import *
import numpy as np
class proteinMC:

#	Initialize a class given a protein as an input parameter
	def __init__(self,params,rates_file):
		data = np.genfromtxt(rates_file,delimiter=",",skip_header=1,dtype='U8,f8,f8')
		self.protein= graph.Graph()
		for i in range(len(data)):
			r1,r2 = data[i][0].split("_")
			kf    = data[i][1]
			kb    = data[i][2]
			self.protein.add_edge(r1,r2,kf,kb)	
		self.tmax  = params['TMAX']
		self.start_res = params["SOURCE RESIDUE"]
		self.end_res   = params["DRAIN RESIDUE"]
	
	def tau_res(self,resID): #replace this with numpy package to make algorithm faster
		if resID in self.protein.get_vertices():
			v = self.protein.vert_dict[resID]
			tau_v = 0 
			 
			for w in v.get_connections():
				tau_v = tau_v+v.get_weight(w)
			return tau_v

	def probability(self,resID):
		v = self.protein.vert_dict[resID]
		tau = {}
		neighbours = v.get_connections()

		for w in range(len(neighbours)):
			if w==0:
				tau[neighbours[w]] = v.get_weight(neighbours[w])
			else:
				
				tau[neighbours[w]] =tau[neighbours[w-1]]+ v.get_weight(neighbours[w])	
		return tau
	
	def runMC(self,iRun=0):
		np.random.seed() #Generate a new seed for every run
		print('Starting MC run', iRun)
		t = 0
		e_site = self.start_res
		trajectory = []
		iHop       = [0]
		trajectory.append([iRun,e_site,iHop[0]])
		while t<self.tmax:
			tau      = self.probability(e_site)
			P,neighbours = (list(t) for t in zip(*sorted(zip(list(tau.values()),list(tau.keys())))))
			tau_site = self.tau_res(e_site)
			t_hop = 1.0/tau_site*np.random.exponential(1) #time which the electron spends on the residue
			hop_vertex =neighbours[np.searchsorted(np.array(P),tau_site*np.random.rand())]
			
			hop_site   = hop_vertex.get_id()
			t = t+t_hop	
			if t> self.tmax:
				t_hop = self.tmax -  iHop[-1]
				t = self.tmax
				iHop.append(t)	
				trajectory.append([iRun,hop_site,iHop[-1]])
				print("End of run"+ str(iRun)+", simulation maximum time reached")
				print(trajectory)
				return np.array(trajectory)		
					
			iHop.append(t)
			trajectory.append([iRun,hop_site,iHop[-1]])	
			e_site = hop_site	
			if hop_site==self.end_res:
				print("End of"+ str(iRun)+", electron reached end of protein at time "+ str(t) +"ns")
				print(trajectory)
				return np.array(trajectory)		
					
if __name__=="__main__":
#### Adjust the montecarlo parameters in params#######
	params= {'TMAX':100000,"SOURCE RESIDUE":'36', "DRAIN RESIDUE":'293',"nRuns":1} 
################
	mc    = proteinMC(params,'rates.txt')
	nRuns = params["nRuns"]  
	trajectory = mc.runMC()
	trajectory = np.concatenate(parallelMap(mc.runMC, cpu_count(), range(nRuns))) #Run in parallel and merge trajectories
	np.savetxt("trajectory.dat", trajectory, fmt = "%s,%s,%s", header="iElectron  Residue t[s]") #Save trajectories together 

__name__="__main__"
