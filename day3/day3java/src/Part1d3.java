import java.util.*;

public class Part1d3 {
    private int res;
    public Part1d3() {
        Set<String> houses = new HashSet<String>();
        houses.add("0, 0");
        String directions = new MyReader3().getData();
        int x = 0, y = 0;
        for (int i = 0; i < directions.length(); i++) {
            if (directions.charAt(i) == '^') y++;
            else if (directions.charAt(i) == 'v') y--;
            else if (directions.charAt(i) == '>') x++;
            else if (directions.charAt(i) == '<') x--;
            houses.add(x + ", " + y);
        }
        this.res = houses.size();
    }

    public int getRes() {
        return this.res;
    }
}