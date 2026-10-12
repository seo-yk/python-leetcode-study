class Solution {
    public int robotSim(int[] commands, int[][] obstacles) {
        HashSet<String> oSet = new HashSet<>();
        for(int[] obstacle: obstacles){
            oSet.add(obstacle[1] + "," + obstacle[0]);
        }
        
        int curRow = 0;
        int curCol = 0;
        int dir = 0;
        int maxDistance = 0;

        int[] dr = {1, 0, -1, 0};
        int[] dc = {0, 1, 0, -1};

        for(int command: commands){
            if(command < 0){
                if(command == -2){
                    // left
                    dir = (dir+3)%4;
                }else{
                    // right
                    dir = (dir+1)%4;
                }
            }else{
                for(int step = 0; step < command; step++){

                    int nr = curRow + dr[dir];
                    int nc = curCol + dc[dir];

                    if(oSet.contains(nr + "," + nc)){
                        break;
                    }

                    curRow = nr;
                    curCol = nc;
                    maxDistance = Math.max(maxDistance, curRow * curRow + curCol * curCol);
                }
            }
        }
        return maxDistance;
    }
}