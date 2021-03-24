import java.util.*;

public class Part2d3 {
    private int res;
    public Part2d3() {
        Set<String> houses = new HashSet<String>();
        houses.add("0, 0");
        String directions = new MyReader3().getData();
        int xs = 0, ys = 0, xr = 0, yr = 0;
        boolean santa = false;
        for (int i = 0; i < directions.length(); i++) {
            santa = !santa;
            if (santa) {
                if (directions.charAt(i) == '^') ys++;
                else if (directions.charAt(i) == 'v') ys--;
                else if (directions.charAt(i) == '>') xs++;
                else if (directions.charAt(i) == '<') xs--;
                houses.add(xs + ", " + ys);
            } else {
                if (directions.charAt(i) == '^') yr++;
                else if (directions.charAt(i) == 'v') yr--;
                else if (directions.charAt(i) == '>') xr++;
                else if (directions.charAt(i) == '<') xr--;
                houses.add(xr + ", " + yr);
            }
        }
        this.res = houses.size();
    }

    public int getRes() {
        return this.res;
    }
}