
import java.util.*; 

public class missingValue{
    static int missedValue (ArrayList<Integer> nums){
        Collections.sort(nums);
        int first = nums.get(0); 
        while (nums.contains(first + 1)){
            first += 1; 
        }
        return first + 1; 
    }
    static int sum(ArrayList<Integer> nums){
        int total = 0; 
        for(int x : nums){
            total += x; 
        }
        return total; 
    }
    static int missValue (ArrayList<Integer> nums){
        int n = nums.size() + 1; 
        int total = n * (n + 1) / 2; 
        int curr = sum(nums); 
        return total - curr; 
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        int n = sc.nextInt(); 
        ArrayList<Integer> nums = new ArrayList<>(); 
        for(int i = 0; i < n ; i++){
            int ele = sc.nextInt(); 
            nums.add(ele); 
        }
        int result = missedValue(nums); 
        int result1 = missValue(nums); 
        System.out.println(result);
        System.out.println(result1);
        sc.close(); 
    }
}

