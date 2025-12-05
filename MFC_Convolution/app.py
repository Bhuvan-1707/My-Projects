from flask import Flask,render_template,request,session
import matplotlib.pyplot as plt

app = Flask(__name__)
app.secret_key = b'Convolution'

@app.route('/',methods=['GET'])
def main():
    return render_template('home.html')

@app.route('/home',methods=['GET','POST'])
def homepage():
    results = None
    if request.method=='POST':
        vectorlist1 = request.form.getlist('vector1data')
        vectorlist2 = request.form.getlist('vector2data')

        actionvariable = request.form.get('action')
        if actionvariable == 'L':
            results = linearconvolute(get_vectors(vectorlist1,vectorlist2))
            session['last_results'] = results
        if actionvariable == 'C':
            results = circularconvolute(get_vectors(vectorlist1,vectorlist2))
            session['last_results'] = results
        if actionvariable == 'Plot':
            results = session.get('last_results', None)
            results = plotting_result(results)
            session['last_results'] = results
    return render_template('index.html',results=results)

def get_vectors(vectorlist1,vectorlist2):
    def to_int_list(lst):
        out = []
        for x in lst:
            x = x.strip()
            if x and (x.lstrip('-').isdigit()):
                out.append(int(x))
        return out
    
    v1 = to_int_list(vectorlist1)
    v2 = to_int_list(vectorlist2)

    results = {
            "vector1": v1,
            "vector2": v2
    }

    return results

def linearconvolute(results):
    # Brute Force Approach
    v1 = results['vector1']
    v2 = results['vector2']

    L = len(v1)
    M = len(v2)
    N = L+M-1
    y = [0]*N

    for i in range(N):
        for j in range(L):
            if(0<=(i-j)<M):
                y[i] += v1[j]*v2[i-j]
    results['L'] = y
    return results

def circularconvolute(results):
    # Brute Force Approach
    v1 = results['vector1']
    v2 = results['vector2']

    L = len(v1)
    M = len(v2)
    N = max(L,M)
    y = [0]*N
    # Padding min vector
    if L<M:
        v1.extend([0]*(M-L))
    if M<L:
        v2.extend([0]*(L-M))

    for i in range(N):
        for j in range(N):
            y[i]+=v1[j]*v2[(i-j)%N]
    results['C'] = y
    return results

def plotting_result(results):
    results['Plot'] = "True"
    keylist = list(results.keys())
    conv = results[keylist[0]]
    v1 = results[keylist[1]]
    v2 = results[keylist[2]]
    print(v1,v2,conv)

    fig = plt.figure()
    plt.stem([i+1 for i in range(len(v1))],v1,linefmt='g-',markerfmt='g',basefmt='')
    plt.stem([i+1 for i in range(len(v2))],v2,linefmt='r-',markerfmt='r',basefmt='')
    plt.stem([i+1 for i in range(len(conv))],conv,linefmt='b--',basefmt='')
    plt.legend(['V1','V2','Result'])
    plt.savefig('static/images/plot.png')
    return results

app=app