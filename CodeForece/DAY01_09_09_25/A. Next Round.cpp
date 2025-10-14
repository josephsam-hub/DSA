 #include<bits/stdc++.h>
 using namespace std;
 int main(){
    int n,k;
    cin>>n>>k;
    int sum=0;
    int content[n];
    for(int i=0;i<n;i++){
        cin>>content[i];
    }
    for (int i=0;i<n;i++){
        if(content[i] >= content[k-1] && content[i]>0){
         sum+=1;
    }}
    cout<<sum;
    return 0;
    
 }