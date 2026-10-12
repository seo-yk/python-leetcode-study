class Solution {
    public boolean judgeCircle(String moves) {
        int curRow = 0;
        int curCol = 0;

        for(Character d: moves.toCharArray()){
            String dirs = "RLUD";
            int nd = dirs.indexOf(d);

            int[] dr = {0, 0, -1, 1};
            int[] dc = {1, -1, 0, 0};

            curRow += dr[nd];
            curCol += dc[nd];
        }

        if(curRow == 0 && curCol == 0){
            return true;
        }else{
            return false;
        }
        
    }
}