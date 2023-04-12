// Online C++ compiler to run C++ program online
#include <iostream>

using namespace std;

class Rational {
    private:
        int x;
        int y;
    public:
        Rational(int a=0, int b=1){
            if (b>0) {x=a; y=b;}
            else {x=-a; y=-b;}
        }
        friend ostream& operator << (ostream& out, const Rational& r);
        Rational& operator ++ () { // ++A
            x+=y;
            return *this;
        }
        Rational& operator -- () { // --A
            x-=y;
            return *this;
        }
        Rational operator - () { // -A
            return Rational(-x, y);
        }
        Rational operator ++ (int) { // A++
            Rational tmp(*this);
            x+=y;
            return tmp;
        }
        Rational operator -- (int) { // A-- почему нельзя вернуть ссылку
            Rational tmp(*this);
            x-=y;
            return tmp;
        }
        friend Rational operator + (const Rational& q1, const Rational& q2 ); 
        friend Rational operator - (const Rational& q1, const Rational& q2 ); 
        friend Rational operator * (const Rational& q1, const Rational& q2 ); 
        friend Rational operator / (const Rational& q1, const Rational& q2 ); 
        Rational operator += (Rational& r) { 
            Rational tmp(*this);
            *this = Rational(tmp + r);
            return *this;
        }
};

ostream& operator << (ostream& out, const Rational& r) {
    out << r.x; 
    if( r.y > 1 && r.x != 0 ) out << "/" << r.y;
    return out;
}

Rational operator + (const Rational& q1, const Rational& q2 ){
            Rational q(q1.x*q2.y + q1.y*q2.x, q1.y*q2.y);
            return q;
        }
Rational operator - (const Rational& q1, const Rational& q2 ){
            Rational q(q1.x*q2.y - q1.y*q2.x, q1.y*q2.y);
            return q;
        }
Rational operator * (const Rational& q1, const Rational& q2 ){
            Rational q(q1.x*q2.x, q1.y*q2.y);
            return q;
        }
Rational operator / (const Rational& q1, const Rational& q2 ){
            Rational q(q1.x*q2.y, q1.y*q2.x);
            return q;
        }

        

int main(){
    Rational Q(1,-3);
    cout << "Q= " << Q << endl;
    cout << "-Q= " << -Q << endl;
    cout << "++Q " << ++Q << endl;
    cout << "--Q " << --Q << endl;
    cout << "Q++ " << Q++ << endl;
    cout << "Q-- " << Q-- << endl;
    cout << "Q= " << Q << endl;
    Rational Q2(5);
    cout << "Q2= " << Q2 << endl;
    cout << "Q + Q2= "<< (Q + Q2) << endl;
    cout << "Q - Q2= "<< (Q - Q2) << endl;
    cout << "Q * Q2= "<< (Q * Q2) << endl;
    cout << "Q / Q2= "<< (Q / Q2) << endl;
    Rational Q3(-7);
    cout << "Q= " << Q << endl;
    cout << "Q3= " << Q3 << endl;
    cout << "Q3+=Q " << endl;
    cout << "Q3= " << Q3 << endl;
    Rational Q4;
    cout << Q4 << endl;
    
    
    return 0;
}