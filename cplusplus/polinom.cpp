#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

class Polinom{
    private:
        vector<double> P = {};
    public:
        Polinom(const vector<double>& L){
            P = L;
        }
        Polinom& operator += (const Polinom& L){ // q += r
            *this = *this+L;
            return *this; 
        };
        Polinom& operator -= (const Polinom& L){ // q += r
            *this = *this-L;
            return *this; 
        };
        Polinom& operator *= (const Polinom& L){ // q += r
            *this = *this*L;
            return *this; 
        };
        Polinom operator - (){
            int size = P.size();
            vector<double> d(size, 0);
            for(int i = 0; i < size; i++){
                d[i]= P[i]*(-1);
            }
            return Polinom(d);
        }
        friend ostream& operator << (ostream& out, const Polinom& Poli);
        friend Polinom operator + (const Polinom& p1, const Polinom& p2);
        friend Polinom operator - (const Polinom& p1, const Polinom& p2);
        friend Polinom operator * (const Polinom& p1, const Polinom& p2);
        friend int max(int a, int b);
        double operator() (double x){
            double rez = P[P.size()-1];
            //cout << "rez = " << rez << endl;
            for(int i = P.size()-2; i>=0; i--){
                rez = P[i]+x*rez;
                //cout << "rez = " << rez << endl;
            }
            return rez;
        }
        Polinom derivative(){
            vector<double> D = {};
            for(int i = 1; i<P.size(); i++){
                //cout << "check" << endl;
                D.push_back(i*P[i]);
            }
            Polinom Poli = Polinom(D);
            return Poli;
        }
};

int min(int a, int b){
    if(a<b){return a;}
    else{return b;}
}

ostream& operator << (ostream& out, const Polinom& Poli) {
    /*for(int i = 0; i < Poli.P.size(); i++){
        out << Poli.P[i] << " ";
    }
    out << endl; 
    return out;*/
    for(int i = Poli.P.size(); i>0; i--){
        if(i==1){out << Poli.P[i-1];}
        if(i==2){out << Poli.P[i-1] << "x + ";}
        if(i>2){out << Poli.P[i-1] << "x^"<< i-1 << " + ";}
    }
    return out;
}

Polinom operator + (const Polinom& p1, const Polinom& p2 ){
            int a = p1.P.size();
            int b = p2.P.size();
            int minn = min(a, b);
            vector<double> p3 = {};
            for(int i = 0; i<minn; i++){
                p3.push_back(p1.P[i]+p2.P[i]);
            }
            if(a>b){
                for(int i = minn; i<a; i++){
                    p3.push_back(p1.P[i]);
                }
            }
            else{
                for(int i = minn; i<b; i++){
                    p3.push_back(p2.P[i]);
                }               
            }
            Polinom Poli = Polinom(p3);
            return Poli;
        }

Polinom operator - (const Polinom& p1, const Polinom& p2 ){
            int a = p1.P.size();
            int b = p2.P.size();
            int minn = min(a, b);
            vector<double> p3 = {};
            for(int i = 0; i<minn; i++){
                p3.push_back(p1.P[i]-p2.P[i]);
            }
            if(a>b){
                for(int i = minn; i<a; i++){
                    p3.push_back(p1.P[i]);
                }
            }
            else{
                for(int i = minn; i<b; i++){
                    p3.push_back(-p2.P[i]);
                }               
            }
            Polinom Poli = Polinom(p3);
            return Poli;
        }
        
Polinom operator * (const Polinom& p1, const Polinom& p2 ){
            int a = p1.P.size();
            //cout << "a = " << a << endl;
            int b = p2.P.size();
            //cout << "b = " << b << endl;
            vector<double> p3(a+b-1,0);
            for(int i = 0; i<a; i++){
                for(int j = 0; j<b; j++){
                    p3[i+j]+=p1.P[i]*p2.P[j];
                    //cout << "p3[" << i+j << "] = " << p3[i+j] << endl;
                }
            }
            Polinom Poli = Polinom(p3);
            return Poli;
        }

int main(){
    vector<double> a = {0., 1., -0.5, 1./3., -0.25, 0.2};
    vector<double> b = {1., 0., -1./6., 0., 1./120., 0., -1./5040.};
    Polinom P(a);
    cout << " P is " << P << endl;
    cout << "P(0.1) = " << P(0.1) << endl;
    cout << "P(0) = " << P(0.) << endl;
    cout << "P(-0.1) = " << P(-0.1) << endl;
    cout << "P(0.05) = " << P(0.05) << endl;
    cout << "for ln we had good result" << endl;
    cout << "Derivetive for P is " << P.derivative() << endl;
    cout << "P*(-1) is " << -P << endl;
    Polinom Q(b);
    cout << "Q is " << Q << endl;
    cout << "Q(0.1) = " << Q(0.1) << endl;
    cout << "Q(0) = " << Q(0.) << endl;
    cout << "Q(-0.1) = " << Q(-0.1) << endl;
    cout << "Q(0.05) = " << Q(0.05) << endl;
    cout << "P(0.05) = " << P(0.05) << endl;
    cout << "for sinx/x we had bad result(" << endl;
    cout << "Derivetive for Q is " << Q.derivative() << endl;
    cout << "Q*(-1) is " << -Q << endl;
    ///
    cout << "P+Q is " << P+Q << endl;
    cout << "P-Q is " << P-Q << endl;
    cout << "P+=Q is " << (P+=Q) << endl;
    cout << "P-=Q is " << (P-=Q) << endl;
    cout << "P is " << P  << endl;
    cout << "Q is " << Q << endl;
    cout << "P*Q is " << P*Q << endl;
    cout << "P*=Q is " << (P+=Q) << endl;
    return 0;
}
