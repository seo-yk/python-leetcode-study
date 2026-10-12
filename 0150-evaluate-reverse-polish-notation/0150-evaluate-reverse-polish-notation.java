class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> dq = new ArrayDeque<>();
        for(String t : tokens){
            if(t.equals("+")){
                int a = dq.pop();
                int b = dq.pop();
                dq.push(a+b);
            }else if(t.equals("-")){
                int a = dq.pop();
                int b = dq.pop();
                dq.push(b-a);
            }else if(t.equals("*")){
                int a = dq.pop();
                int b = dq.pop();
                dq.push(a*b);
            }else if(t.equals("/")){
                int a = dq.pop();
                int b = dq.pop();
                dq.push(b/a);
            }else{
                dq.push(Integer.parseInt(t));
            }
        }
        return dq.pop();
    }
}