from flask import Flask,render_template,request,session
from flask_session import Session
import plotly.graph_objs as go
import plotly.io as pio
import json
import numpy as np

app = Flask(__name__)
app.secret_key = b'PCA_Animation'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app) 

@app.route('/',methods=['GET'])
def main():
    return render_template('home.html')

@app.route('/home',methods=['GET','POST'])
def homepage():
    resultplot=""
    if request.method == "POST":
        action = request.form.get('action')

        if action=='generate':
            fig,config=plotds()

            # Getting Input Whether it is of Ellipse / Rectangle / Linear
            datagentype=request.form.get("tab-group")

            if datagentype=="ellipse": # If Ellipse
                N=int(request.form.get("NData1")) # type: ignore
                xmean=request.form.get("MeanFocii").split(sep=',') # type: ignore
                xvar=request.form.get("Spread").split(sep=',') # type: ignore
                xtilt=float(request.form.get("Tilt1")) # type: ignore
                XD,YD=datagenellipse(N,xmean,xvar,xtilt)
                fig,config=plotds(XD,YD)


            elif datagentype=="rectangle": # If Rectangle
                N=int(request.form.get("NData2")) # type: ignore
                xstartV=request.form.get("startV").split(sep=',') # type: ignore
                xlb=request.form.get("lb").split(sep=',') # type: ignore
                xtilt=request.form.get("Tilt2")
                xtilt=0 if not xtilt else float(xtilt)
                XD,YD=datagenrectangle(N,xstartV,xlb,xtilt)
                fig,config=plotds(XD,YD)
                

            elif datagentype=="line": # If Line
                N=int(request.form.get("NData3")) # type: ignore
                xslope=float(request.form.get("slope")) # type: ignore
                xintercept=float(request.form.get("intercept")) # type: ignore
                XD,YD=datagenline(N,xslope,xintercept)
                fig,config=plotds(XD,YD)


            # Plot into HTML
            resultplot = fig.to_html(
                full_html=False,
                include_plotlyjs="cdn",
                config=config  # important
            )

            session['plot_json'] = pio.to_json(fig)
            session['xdata'] = XD.tolist() if XD is not None else []
            session['ydata'] = YD.tolist() if YD is not None else []

                
        
        elif action == 'animate':
            plot_json = session.get('plot_json')
            XD = np.array(session.get('xdata')) if session.get('xdata') is not None else None
            YD = np.array(session.get('ydata')) if session.get('ydata') is not None else None

            if plot_json and XD is not None:
                fig = pio.from_json(plot_json)

                # -------------------------------
                # CENTER DATA
                # -------------------------------
                Xc = XD - np.mean(XD)
                Yc = YD - np.mean(YD)
                points = np.vstack((Xc, Yc)).T  # (N, 2)

                cov = np.cov(Xc, Yc)
                evals, evecs = np.linalg.eigh(cov)
                u_opt = evecs[:, np.argmax(evals)]
                best_angle = np.arctan2(u_opt[1], u_opt[0])

                # Starting lines
                fig.add_trace(go.Scatter(
                    x=Xc,
                    y=Yc,
                    mode='markers',
                    marker=dict(color='blue', size=6),
                    name='Data'
                ))

                # Principal axis
                fig.add_trace(go.Scatter(
                    x=[None],
                    y=[None],
                    mode='lines',
                    line=dict(color='red', width=3),
                    name='Principal Axis'
                ))

                # Black lines for support
                fig.add_trace(go.Scatter(
                    x=[None],
                    y=[None],
                    mode='lines',
                    line=dict(color='black', width=1),
                    name='Perpendicular Error',
                    showlegend=False
                ))

                frames = []

                for i in range(11):
                    angle = (i / 10.0) * best_angle
                    u = np.array([np.cos(angle), np.sin(angle)])

                    # Projections
                    proj_len = points @ u
                    projections = np.outer(proj_len, u)

                    # Residual error
                    residuals = points - projections
                    error = np.sum(np.linalg.norm(residuals, axis=1)**2)

                    # Black color lines
                    perp_x, perp_y = [], []
                    for p, proj in zip(points, projections):
                        perp_x += [p[0], proj[0], None]
                        perp_y += [p[1], proj[1], None]

                    frames.append(go.Frame(
                        data=[
                            # Trace 0: points
                            go.Scatter(x=Xc, y=Yc),

                            # Trace 1: axis
                            go.Scatter(
                                x=[-10*u[0], 10*u[0]],
                                y=[-10*u[1], 10*u[1]]
                            ),

                            # Trace 2: perpendiculars
                            go.Scatter(
                                x=perp_x,
                                y=perp_y,
                                mode='lines',            
                                line=dict(
                                    color='black',       
                                    width=1              
                                )
                            )
                        ],
                        name=f'frame{i}',
                        layout=go.Layout(
                            title_text=f"PCA Optimization | Squared Error = {error:.2f}"
                        )
                    ))

                fig.frames = frames

                fig.update_layout(
                    width=1500*(2/3),
                    height=1300/1.5,
                    autosize=False,
                    updatemenus=[{
                        "buttons": [
                            {
                                "args": [None, {
                                    "frame": {"duration": 1000, "redraw": True},
                                    "fromcurrent": True
                                }],
                                "label": "Slow",
                                "method": "animate"
                            },
                            {
                                "args": [None, {
                                    "frame": {"duration": 500, "redraw": True},
                                    "fromcurrent": True
                                }],
                                "label": "Medium",
                                "method": "animate"
                            },
                            {
                                "args": [None, {
                                    "frame": {"duration": 200, "redraw": True},
                                    "fromcurrent": True
                                }],
                                "label": "Fast",
                                "method": "animate"
                            }
                        ],
                        "type": "buttons",
                        "x": 1.15,
                        "y": 0
                    }]
                )


                resultplot = fig.to_html(
                    full_html=False,
                    include_plotlyjs="cdn",
                    config={'scrollZoom': True}
                )



    return render_template('index.html',results=resultplot)

def datagenellipse(N,xmean,xvar,xtilt):
    XData = (float(xvar[0])*np.random.randn(N))+(np.ones(N)*float(xmean[0]))
    YData = (float(xvar[1])*np.random.randn(N))+(np.ones(N)*float(xmean[1]))
    XData = np.cos(np.deg2rad(xtilt))*XData - np.sin(np.deg2rad(xtilt))*YData
    YData = np.sin(np.deg2rad(xtilt))*XData + np.cos(np.deg2rad(xtilt))*YData
    return XData,YData

def datagenrectangle(N,xstartV,xlb,xtilt):
    XData = np.random.uniform(float(xstartV[0]),float(xstartV[0])+float(xlb[0]),N)
    YData = np.random.uniform(float(xstartV[1]),float(xstartV[1])+float(xlb[1]),N)
    XData = np.cos(np.deg2rad(xtilt))*XData - np.sin(np.deg2rad(xtilt))*YData
    YData = np.sin(np.deg2rad(xtilt))*XData + np.cos(np.deg2rad(xtilt))*YData
    return XData,YData

def datagenline(N,slope,intercept):
    Xstart = np.random.randint(-5,5,1)
    Xrange = np.random.randint(4,8,1)
    XData = np.random.uniform(Xstart,Xrange+Xstart,N)
    YData = intercept*np.ones(N) + slope*XData
    return XData,YData

def plotds(X=[],Y=[]):
    fig = go.Figure(
        data=go.Scatter(
            x=X,
            y=Y,
            mode="markers",
            name="Data",
            marker=dict(size=6),
            hovertemplate="x=%{x:.2f}<br>y=%{y:.2f}<extra></extra>"
        )
    )
    fig.add_trace(go.Scatter(
        x=[None], y=[None], mode="lines", name="Principal Axis",
        line=dict(color="red", width=3)
    ))
    fig.update_xaxes(
        zeroline=True,
        zerolinewidth=3,
        zerolinecolor="black"
    )
    fig.update_yaxes( 
        scaleanchor="x",
        scaleratio=1,
        zeroline=True,
        zerolinewidth=3,
        zerolinecolor="black"
    )

    config={"scrollZoom":True,"modeBarButtonsToRemove": [
         "select2d", "lasso2d", "zoomIn2d", "zoomOut2d"
    ]}
    fig.update_layout(
        title="Data Generated",
        width=1500*(2/3),
        height=1300/1.5,
        margin=dict(l=30, r=30, t=40, b=30),
        dragmode="pan",
        autosize=False
    )
    return fig,config

if __name__ == "__main__":
    app.run(debug=True)
