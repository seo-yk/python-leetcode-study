class Solution {
    public String reverseWords(String s) {
        String[] strArr = s.trim().split("\\s+");
        
        if(strArr.length == 1){
            return strArr[0];
        }

        int left = 0;
        int right = strArr.length - 1;

        while (left < right){
            String temp = strArr[left];
            strArr[left] = strArr[right];
            strArr[right] = temp;

            left++;
            right--;
        }

        String answer = String.join(" ", strArr);
        return answer;
    }
}