class Vertex:
	def __init__(self,node):
		self.id = node
		self.adjacent = {}

	def __str__(self):
		return str(self.id) + 'adjacent:' + str([x.id for x in self.adjacent])

	def add_neighbour(self,neighbour,weight=0):
		self.adjacent[neighbour] = weight

	def get_connections(self):
		return self.adjacent.keys()

	def get_id(self):
		return self.id

	def get_weight(self,neighbour):
		return self.adjacent[neighbour]


class Graph:
	def __init__(self):
		self.vert_dict = {}
		self.num_vertices = 0

	def __iter__(self):
		return iter(self.vert_dict.values())

	def add_vertex(self,node):
		self.num_vertices = self.num_vertices +1
		new_vertex = Vertex(node)
		self.vert_dict[node] = new_vertex
		return new_vertex

	def add_edge(self, frm ,to, cost_fwd=0,cost_bck=0):
		if frm not in self.vert_dict:
			self.add_vertex(frm)
		if to not in self.vert_dict:
			self.add_vertex(to)

		self.vert_dict[frm].add_neighbour(self.vert_dict[to],cost_fwd)
		self.vert_dict[to].add_neighbour(self.vert_dict[frm],cost_bck)

	def get_vertices(self):
		return self.vert_dict.keys()


if __name__ == '__main__':
	g = Graph()
	

	g.add_vertex('35')
	g.add_vertex('48')
	g.add_vertex('69')
	
	g.add_edge('35','69',3,6)
	g.add_edge('35','48',2,1)
	g.add_edge('48','69',5,10)

	for v in g:
		for w in v.get_connections():
			vid = v.get_id()
			wid = w.get_id()	
			print ('(%s,%s,%3d)' % (vid, wid, v.get_weight(w)))
	for v in g:
		print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))

