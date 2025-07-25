function TreeNode (val, left, right){
    this.val = (val === undefined ? 0 : val)
    this.left = left === undefined ? null : left
    this.right = right === undefined ? null : right

}


// @param {TreeNode} tree1
// @parm {TreeNode} tree2
// @return Boolean 

function isSameTree (p, q){
    if (!p && !q){
        return true 
    }
    if (!p || !q ){
        return false 
    }

    if (p.val != q.val){
        return False 
    }

    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
}
