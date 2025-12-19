from flask import Flask,render_template,request,session
import plotly.graph_objs as go
import numpy as np

app = Flask(__name__)
app.secret_key = b'Clustering'

@app.route("/",methods=['GET','POST'])
def homepage():
    resultplot = None
    dataset = request.form.get("dataset")
    action = request.form.get("action")
    X=None
    Y=None
    
    NDpoints=20
    NCluster=5
    n=None
    score=None
    besteff = None

    if dataset and action!="classify":
        if dataset=="uniform":
            NDpoints = int(request.form.get("NDPointsUniform"))
            NCluster = int(request.form.get("NClusterUniform"))
            CSp = int(request.form.get("ClusterSpreadUniform"))
            Clv = float(request.form.get("ClustervarianceUniform"))

            X,Y = generatedata(NDpoints,NCluster,CSp,Clv)
        if dataset=="normal":
            NDpoints = int(request.form.get("NDPointsNormal"))
            NCluster = int(request.form.get("NClusterNormal"))
            CSp = int(request.form.get("ClusterSpreadNormal"))
            Clv = float(request.form.get("ClustervarianceNormal"))

            X,Y = generatedatarotated(NDpoints,NCluster,CSp,Clv)
        session["X"] = X.tolist()
        session["Y"] = Y.tolist()

    fig = go.Figure(
        data=go.Scatter(
            x=X,
            y=Y,
            mode="markers",
            marker=dict(size=6),
            hovertemplate="x=%{x:.2f}<br>y=%{y:.2f}<extra></extra>"
        )
    )

    fig.update_yaxes(scaleanchor="x", scaleratio=1)
    config={"scrollZoom":True,"modeBarButtonsToRemove": [
         "select2d", "lasso2d", "zoomIn2d", "zoomOut2d"
    ]}
    fig.update_layout(
        title="Data Generated",
        margin=dict(l=30, r=30, t=40, b=30),
        dragmode="pan"
    )

    if action == "classify":
        if "X" in session and "Y" in session:
            X = np.array(session["X"])
            Y = np.array(session["Y"])

        labels,n,score,besteff = classify(X,Y,NCluster)
        titley = "Classified Data"

        unique_labels = np.unique(labels)
        traces = []

        for lab in unique_labels:
            mask = labels == lab
            traces.append(
                go.Scatter(
                    x=X[mask],
                    y=Y[mask],
                    mode="markers",
                    name=f"Cluster Id {lab+1}",
                    marker=dict(size=7),
                    hovertemplate=(
                        "x=%{x:.2f}<br>"
                        "y=%{y:.2f}<br>"
                        f"cluster={lab+1}<extra></extra>"
                    )
                )
            )
        fig = go.Figure(data=traces)
        fig.update_yaxes(scaleanchor="x", scaleratio=1)
        fig.update_layout(
            title=titley,
            margin=dict(l=30, r=30, t=40, b=30),
            dragmode="pan"
        )


    resultplot = fig.to_html(
        full_html=False,
        include_plotlyjs="cdn",
        config=config  # important
    )
    return render_template('index.html',plot_html=resultplot,selecteddata=dataset,n=n,score=score,besteff=besteff)


def generatedata(NDpoints,N,ClusterSpread,ClusterVariance):
    NCluster = N
    xChoices = ClusterSpread*N*[i for i in range(1,2*N+1,2)]
    yChoices = ClusterSpread*N*[i for i in range(1,2*N+1,2)]

    x = np.zeros(0)
    y = np.zeros(0)

    for i in range(NCluster):
        xs = ClusterVariance*np.random.rand(NDpoints)
        ys = ClusterVariance*np.random.rand(NDpoints)

        xchoice = np.random.choice(xChoices)
        ychoice = np.random.choice(yChoices)

        xChoices.remove(xchoice)
        yChoices.remove(ychoice)

        x = np.concatenate((x,xs+xchoice))
        y = np.concatenate((y,ys+ychoice))

    return x,y

def generatedatarotated(NDpoints,N,ClusterSpread,ClusterVariance):
    NCluster = N
    x = np.zeros(0)
    y = np.zeros(0)
    dtheta=2*np.pi/NCluster
    thetas = np.arange(0,(2*np.pi),dtheta)

    for i in range(NCluster):
        xs = ClusterVariance*np.random.randn(NDpoints)+ClusterSpread
        ys = ClusterVariance*np.random.randn(NDpoints)

        xrot,yrot = rotatearrays(xs,ys,thetas[i])
        x=np.concatenate((x,xrot))
        y=np.concatenate((y,yrot))
    return x,y

def rotatearrays(x,y,theta):
    xrotated = x*np.cos(theta) - y*np.sin(theta)
    yrotated = y*np.cos(theta) + x*np.sin(theta)
    return xrotated,yrotated
    
def classify(X, Y, NCluster, maxIter=5):
    X = np.column_stack((X, Y))
    Npoints = X.shape[0] // NCluster
    Nsamples = Npoints * NCluster
    maxNClusters = NCluster + 3

    best_labels = None
    best_n = None
    best_score = np.inf

    for n in range(2, maxNClusters + 1):
        C = np.random.randn(n, 2)
        tag = np.zeros(Nsamples, dtype=int)

        for _ in range(maxIter):
            for j in range(Nsamples):
                d2 = np.zeros(n)
                for k in range(n):
                    d2[k] = np.sum((X[j] - C[k]) ** 2)

                tag[j] = np.argmin(d2)
                C[tag[j]] = (C[tag[j]] + X[j]) / 2

        J = np.zeros(n)
        for m in range(n):
            diff = X[tag == m] - C[m]
            J[m] = np.sum(np.sum(diff ** 2, axis=1))

        sJ = np.sum(J)

        if sJ < best_score:
            best_score = sJ
            best_labels = tag.copy()
            best_n = n
            best_eff_n = len(set(best_labels))

    return best_labels, best_n, best_score, best_eff_n

if __name__=="__main__":
    app.run(debug=True)