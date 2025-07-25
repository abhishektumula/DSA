function TreeNode (val, left, right){
    this.val = val === undefined ? 0 : val 
    this.left = left === undefined ? null : left 
    this.right = right === undefined ? null : right 

}

/**
 * @param {TreeNode} treeStr
 * @return {Boolean} 
 */

function isSymmetric (treeStr){
    if (!treeStr){
        return true
    }

    function fn (p, q){
        if (!p && !q){
            return true
        }
        if (!p || !q) {
            return false 
        }

        if (p.val != q.val) {
            return false;
        }

        return fn(p.left, q.right) && fn(p.right, q.left)
    }


    return fn(treeStr.left, treeStr.right)

}