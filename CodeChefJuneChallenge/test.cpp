/* Enter your code here. Read input from STDIN. Print output to STDOUT */
#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
#include<sstream>
using namespace std;
void sort(int,int);
vector<int> v,v2;
long long inversions=0;
void merge(int,int,int);
int main()
    
{
 
    string tmp;
 //   vector<int> v;
 int t,n,i;
    getline(cin,tmp);
stringstream ssss(tmp);
        
//ss<<tmp;
    ssss>>t;
 //   cout<<t<<endl;
    for(;t>0;t--)
    {
    
	getline(cin,tmp);
        stringstream sss(tmp);
    	
        // int count=0; 
        sss>>n;
        getline(cin,tmp);
stringstream ss(tmp);        
//cout<<n<<endl;
        
        v.resize(n);
	v.clear();
        for(i=0;i<n;i++)ss>>v[i];
    sort(0,n-1);
        cout<<inversions<<endl;
        inversions=0;
        
    }
    return 0;
}



void sort(int p,int r)
{if(p<r)
{
     int q=(p+r)/2;
     sort(p,q);
     sort(q+1,r);
     merge(p,q,r);}
     }


void merge(int p,int q,int r)
{
     //cout<<"p: "<<p<<" q: "<<q<<" r: "<<r<<endl;
     v2.clear();v2.resize(r-p+3);
     int i=p,j=q+1,k;
     for(k=0;i<=q&&j<=r;k++)
     {
                      if(v[i]<=v[j]){v2[k]=v[i];i++;}
                      else{v2[k]=v[j];j++;inversions+=q-i+1;}
                      }
     while(i<=q){v2[k]=v[i];i++;k++;}
     while(j<=r){v2[k]=v[j];j++;k++;}
     for(i=p;i<=r;i++)v[i]=v2[i-p];
     //cout<<v[p]<<v[q]<<v[r]<<endl;
}