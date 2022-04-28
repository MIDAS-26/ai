from collections import defaultdict
import heapq
    
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def createEdge(self,u,v,cost):
        self.graph[u].append((v,cost))
        
    def get_path(self,parent,node):
        path = []
        path.append(node)
        
        while node in parent:
            path.append(parent[node])
            node = parent[node]
        
        return path[::-1] # reverse the list
    
    def UCS(self,start,goal,g,parent):
        open_list = []
        closed_list = []
        g[start] = 0
        heapq.heappush(open_list,(g[start],start))
        found = False
        print()
        
        while len(open_list)>0 and not found:
            print("-"*30)
            print("Open List : ",end='')
            for node in open_list:
                print(node[1],'(',node[0],')',' ',end='')
            print()
            
            print("Closed List : ",end='')
            for node in closed_list:
                print(node,'(',g[node],')',' ',end='')
            print()
            
            best = heapq.heappop(open_list)

            print("Node selected for expansion : ", end='')
            print(best[1],'(',best[0],')')
            print("-"*30)
            print()
            best_node = best[1]
            closed_list.append(best_node)
            if best_node == goal:
                found = True
                path = self.get_path(parent,best_node)
                print('\nPath : ',path)
                print('Path Cost : ',g[best_node])
                break
                
            else:
                for (successor,cost) in self.graph[best_node]:
                    new_g = g[best_node] + cost
                    is_present = False
                    for i,node in enumerate(open_list):
                        if node[1] == successor:
                            is_present = True
                            old_g = node[0]
                            if new_g < old_g:
                                g[successor] = new_g
                                parent[successor] = best_node
                                open_list[i] = (new_g,successor)
                                heapq.heapify(open_list)
                            break
                            
                    if not is_present:
                        for node in closed_list:
                            if node==successor :
                                is_present = True
                                old_g = g[successor]
                                if new_g < old_g :
                                    g[successor] = new_g
                                    parent[successor] = best_node
                                break
                        
                    if not is_present:
                        parent[successor] = best_node
                        g[successor] = new_g
                        heapq.heappush(open_list,(g[successor],successor))
      
        return found

graph = Graph()                        
num_edges = int(input("Enter the number of edges in graph : "))

for e in range(num_edges):
    u = int(input("Enter from node : "))
    v = int(input("Enter to node : "))
    cost = int(input("Enter edge cost : "))
    graph.createEdge(u,v,cost)

g = {}
parent = {}
start = int(input("Enter start node : "))
goal = int(input("Enter goal node : "))

if graph.UCS(start,goal,g,parent):
    print("\nThe goal node was found !!")
else:
    print("\nThe goal node was NOT found !!")
    