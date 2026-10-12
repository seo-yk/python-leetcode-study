class Solution {
    public String toLowerCase(String s) {
        StringBuilder sb = new StringBuilder();
        for(Character c : s.toCharArray()){
            if(Character.isUpperCase(c)){
                c = Character.toLowerCase(c);
            }
            sb.append(c);
        }
        return sb.toString();
    }
}