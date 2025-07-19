class node():
    def __init__ (self,data):
        self.data = data
        self.right = None
        self.left = None

def searchh(inorder,left ,right,a):
    for i in range(len(inorder)):
        if inorder[i] == a:
            return i 


def buildtree(preorder,inorder,preidx,left,right):
    if left > right:
        return None
    root = preorder[preidx]
    root = node(root)
    preidx +=  1
    indx = searchh(inorder,left,right,preorder[preidx])
    root.left = buildtree(preorder,inorder,preidx,left,indx  - 1)
    root.right = buildtree(preorder,inorder,preidx,indx +1, right)
    return root
              
              