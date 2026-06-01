class AVLNode {

    int key,height;
    AVLNode left,right;

    AVLNode(int key){
        this.key=key;
        height=1;
    }
}

class AVLTree{

int height(AVLNode n){
return n==null?0:n.height;
}

int balance(AVLNode n){
return n==null?0:
height(n.left)-height(n.right);
}

AVLNode rotateLeft(AVLNode x){

AVLNode y=x.right;
AVLNode t=y.left;

y.left=x;
x.right=t;

x.height=Math.max(
height(x.left),
height(x.right))+1;

y.height=Math.max(
height(y.left),
height(y.right))+1;

return y;
}

AVLNode rotateRight(AVLNode y){

AVLNode x=y.left;
AVLNode t=x.right;

x.right=y;
y.left=t;

y.height=Math.max(
height(y.left),
height(y.right))+1;

x.height=Math.max(
height(x.left),
height(x.right))+1;

return x;
}
}
