class Solution {
    public boolean isRobotBounded(String instructions) {
        int x = 0;
        int y = 0;
        int dir = 0;
        
        int[] dx = {0, 1, 0, -1}; //북, 동, 남, 서
        int[] dy = {-1, 0, 1, 0};
        
        int nx = x;
        int ny = y;
        for(char instruction: instructions.toCharArray()){
            if(instruction == 'L'){
                dir = (dir+3)%4;
            }else if(instruction == 'R'){
                dir = (dir+1)%4;
            }else if(instruction == 'G'){
                nx += dx[dir];
                ny += dy[dir];
            }
        }

        return (nx == x && ny == y) || dir != 0;
    }
}