class Solution {
public:
    string winningPlayer(int x, int y) {
        int moves = 0;
        
        while (x > 0 && y >= 4) {
            x--;
            y -= 4;
            moves++;
        }

     return (moves % 2 == 1) ? "Alice" : "Bob";
    }
};