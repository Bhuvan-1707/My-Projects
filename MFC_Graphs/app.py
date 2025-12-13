from flask import Flask, render_template,request
import networkx as nx
import matplotlib.pyplot as plt
import random as r

app = Flask(__name__)
app.secret_key = b'24209-Graphs'

@app.route('/',methods=['GET','POST'])
def homepage():
    response=None
    err=None
    if request.method == 'POST':
        try:
            var = request.form.get("submission")
            bar = request.form.get("mansub")
            if var=="random-submit":
                nodes=int(request.form.get("numnodes"))
                edges=int(request.form.get("numedges"))
                response=manualgenerate(*randlistgenerate(nodes,edges))
            if bar=="manual-submit":
                outnodeinput = request.form.get("outgoing-input")
                innodeinput = request.form.get("incoming-input")
                if not outnodeinput or not innodeinput:
                    raise ValueError("Both outgoing and incoming node lists must be provided")
                outnodelist = list(map(int, outnodeinput.strip().split()))
                innodelist = list(map(int, innodeinput.strip().split()))
                if len(outnodelist) != len(innodelist):
                    raise ValueError("Outgoing and incoming node lists must have the same length")
                response = manualgenerate(outnodelist, innodelist)


        except ValueError as e:
            err=str(e)

    return render_template('index.html',results=response, error=err)

def manualgenerate(outlist,inlist,nodecount=None):
    if not outlist or not inlist:
        raise ValueError("Cannot generate graph from empty lists")
    if nodecount is None:
        nodecount = max(max(outlist), max(inlist))
    nxlist = [(outlist[i],inlist[i]) for i in range(len(outlist))]
    print(nxlist)
    G = nx.Graph()
    G.add_edges_from(nxlist)
    nx.draw(G)
    plt.savefig("static/images/graph.png",dpi=300,bbox_inches="tight")
    plt.clf()

    # Incident Matrix Creation
    incident_matrix = []
    for itertuple in nxlist:
        row = [1 if (iter+1) in itertuple else 0 for iter in range(nodecount)]
        if 1 in row:
            row[row.index(1)] = -1
        incident_matrix.append(row)
    
    # Adjacency Matrix Creation
    adjacency_matrix = nxlist_to_adjacency(nxlist,nodecount)

    # Degree Matrix Creation
    degree_matrix = adj_to_deg(adjacency_matrix,nodecount)

    # Laplacian Matrix
    Laplace_matrix = difmat(degree_matrix,adjacency_matrix)

    return {
        "IM":incident_matrix,
        "AM":adjacency_matrix,
        "DM":degree_matrix,
        "LM":Laplace_matrix
    }
    


def nxlist_to_adjacency(outinlist,n):
    adjacency = [[0 for _ in range(n)] for _ in range(n)]
    for i in outinlist:
        adjacency[i[0]-1][i[1]-1] = 1
        adjacency[i[1]-1][i[0]-1] = 1
    return adjacency

def adj_to_deg(adj,n):
    degree = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(len(adj)):
        degree[i][i] = sum(adj[i])
    return degree

def difmat(D,A):
    B = [[0]*len(D) for _ in range(len(D))]
    for i in range(len(D)):
        for j in range(len(D)):
            B[i][j]=D[i][j]-A[i][j]
    return B

def randlistgenerate(N,E):
    if E > N*(N-1)//2:
        raise ValueError(f"Cannot generate {E} edges for {N} nodes without duplicates. Max edges = {N*(N-1)//2}")

    outlist=[0]*E
    inlist=[0]*E
    edges = []
    for i in range(E):
        edge,ch=createrandedge(N)
        while checkedgeinedges(edge,edges) or ch!=0:
            edge,ch=createrandedge(N)
        edges.append(edge)
    for i in range(len(edges)):
        outlist[i] = edges[i][0]
        inlist[i] = edges[i][1]
    return [outlist,inlist,N]


def createrandedge(N):
    ch=False
    u = r.randint(1,N)
    v = r.randint(1,N)
    edge = (u,v)
    if u==v:
        ch = r.choice([1,2,3,4,5,6,7])
    return edge,ch

def checkedgeinedges(edge,edges):
    edgeback = (edge[1],edge[0])
    if edge in edges:
        return True
    if edgeback in edges:
        return True
    return False

if __name__ == "__main__":
    app.run(debug=True)