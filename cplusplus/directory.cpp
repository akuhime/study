
#include <iostream>
#include <string>
#include <map>
using namespace std;
typedef map<string, string> directory;

void make_record(directory & d, string name, string number){
    directory:: iterator it;
    it = d.find(name);
    if(it == d.end()){ d[name] = number;}
    else{cout << "an attempt to rewrite. delete the old record and try again" << endl;}
}
void delete_record(directory & d, string name){
    directory:: iterator it;
    it = d.find(name);
    d.erase(it);
}
string find_number(directory & d, string name){
    directory:: iterator it;
    it = d.find(name);
    if(it == d.end()){ return "not found";}
    else{return d[name];}
}
void print_directory(directory & d){
    directory:: iterator it;
    it = d.begin();
    for(int i= 0; it!=d.end(); i++, it++){
        cout << it->first << "  " << it->second << endl;
    }
    
}

int main() {
    //cout << "begin" << endl;
    directory D;
    make_record(D, "Rabbit", "123456");
    make_record(D, "Wolf", "999999");
    make_record(D, "Pig", "454545");
    make_record(D, "Eagle", "177381");
    print_directory(D);
    cout << "delete Pig " << endl;
    delete_record(D, "Pig");
    print_directory(D);
    cout << "Eagle's number is " << find_number(D, "Eagle") << endl;
    return 0;
}