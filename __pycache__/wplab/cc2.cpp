#include<bits/stdc++.h>
using namespace std;
#define ll long long int
int main()
{
    ll test;
    cin>>test;
    while(test--)
    {
        ll n,m;
        cin>>n>>m;
        ll degree[n+1];
        for(ll i=1;i<=n;i++){
            degree[i]=0;
        }
        for(ll i=0;i<m;i++)
        {
            ll x,y;
            cin>>x>>y;
            degree[x]+=1;
            degree[y]+=1;
        }
        for(ll i=1;i<=n;i++)
        {
            cout<<degree[i]<<" ";
        }
        cout<<endl;
        if(m&1)
        {
            ll remove_node=0;
            for(ll i=1;i<=n;i++)
            {
                if(degree[i]&1)
                {
                    remove_node=i;
                    break;
                }
            }
            //if there is a node with odd degree
            if(remove_node!=0)
            {
                cout<<"2"<<endl;
                for(ll i=1;i<=n;i++)
                {
                    if(remove_node==i)
                    {
                        cout<<"2"<<" ";
                    }
                    else
                    {
                        cout<<"1"<<" ";
                    }
                }
            }
            //if all nodes have even degree
            else
            {
                ll cnt=1;
                cout<<"3"<<endl;
                for(ll i=1;i<=n;i++)
                {
                    if(degree[i]==0){
                        cout<<"1"<<" ";
                    }
                    else if(cnt<=3){
                        cout<<cnt<<" ";
                        cnt++;
                    }
                    else{
                        cout<<"1"<<" ";
                    }
                }
            }
        }
        else
        {
            cout<<"1"<<endl;
            for(ll i=0;i<n;i++)
            {
                cout<<"1"<<" ";
            }
        }
        if(test)
        {
            cout<<endl;
        }
    }
    return 0;
}

