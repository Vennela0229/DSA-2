class SegmentTree {

long[] tree;
long[] lazy;
int n;

SegmentTree(int n){

this.n=n;

tree=new long[4*n];
lazy=new long[4*n];

}

void pushDown(int node){

if(lazy[node]!=0){

tree[2*node]+=lazy[node];
tree[2*node+1]+=lazy[node];

lazy[2*node]+=lazy[node];
lazy[2*node+1]+=lazy[node];

lazy[node]=0;
}
}

void updateRange(
int node,
int l,
int r,
int ql,
int qr,
long val){

if(r<ql||l>qr)
return;

if(ql<=l&&r<=qr){

tree[node]+=val;
lazy[node]+=val;

return;
}

pushDown(node);

int mid=(l+r)/2;

updateRange(
2*node,l,mid,
ql,qr,val);

updateRange(
2*node+1,
mid+1,r,
ql,qr,val);

tree[node]=Math.max(
tree[2*node],
tree[2*node+1]);

}

long queryMax(
int node,
int l,
int r,
int ql,
int qr){

if(r<ql||l>qr)
return Long.MIN_VALUE;

if(ql<=l&&r<=qr)
return tree[node];

pushDown(node);

int mid=(l+r)/2;

return Math.max(

queryMax(
2*node,l,mid,
ql,qr),

queryMax(
2*node+1,
mid+1,r,
ql,qr));

}
}
