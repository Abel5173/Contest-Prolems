#include<iostream>
using namespace std;

int main(){
    int n;
    while(cin>>n && n != 0){
        int a[5];
        int cnt;
        int b;
        for(int i =0; i<n;i++){
            cin>>a[i];
            if(a[i]<=127){
               cnt++;
               b=i;
            }
        }
     if (cnt>1){
        cout<<"*"<<endl;
     }
     else if(b==0){
        cout<<"A"<<endl;
     }  else if(b==1){
        cout<<"B"<<endl;
     }  else if(b==2){
        cout<<"C"<<endl;
     }  else if(b==3){
        cout<<"D"<<endl;
     }  else if(b==4){
        cout<<"E"<<endl;
     }
    }
}
