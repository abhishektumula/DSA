
function missingValues (nums){
    if(nums.length == 0){
        return 0
    }
    nums.sort();
    let first = nums.at(0) 
    while(nums.includes(first + 1)){
        first += 1; 
    }
    return first + 1
}

const readline = require('readline'); 
const rd = readline.createInterface({
    input : process.stdin,
    output :  process.stdout, 
})

let nums = []
let n; 
rd.on("line", (line) => {
    if (n == null){
        n = Number(line.trim()); 
    }else{
        if(nums.length != n){
            nums.push(Number(line.trim()))
        }
        else{
            rd.close(); 
        }
    }
    if(nums.length == n){
        console.log(`missing value is ${missingValues(nums)}`); 
        rd.close(); 
    }
})
