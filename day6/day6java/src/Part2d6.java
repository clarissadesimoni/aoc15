import java.util.*;

public class Part2d6 {
    private int res = 0;
    private int[][] grid = new int[1000][1000];
    public Part2d6() {
        for (int i = 0; i < grid.length; i++) Arrays.fill(grid[i], 0);
        List<String> data = new MyReader6().getData();
        for (String line : data) {
            String[] items = line.split(" ");
            String command = items[0] + (items[0].equals("toggle") ? "" : " " + items[1]);
            String[] startStr = items[items.length - 3].split(",");
            String[] endStr = items[items.length - 1].split(",");
            int startX = Integer.parseInt(startStr[0]);
            int startY = Integer.parseInt(startStr[1]);
            int endX = Integer.parseInt(endStr[0]);
            int endY = Integer.parseInt(endStr[1]);
            switch (command) {
                case "toggle":
                    for (int i = startY; i <= endY; i++)
                        for (int j = startX; j <= endX; j++)
                            grid[i][j] += 2;
                        break;
                case "turn on":
                    for (int i = startY; i <= endY; i++)
                        for (int j = startX; j <= endX; j++)
                            grid[i][j] += 1;
                    break;
                case "turn off":
                    for (int i = startY; i <= endY; i++)
                        for (int j = startX; j <= endX; j++)
                            grid[i][j] = Math.max(0, grid[i][j] - 1);
                    break;
            }
        }
        for (int i = 0; i < grid.length; i++) for (int j = 0; j < grid[i].length; j++) this.res += grid[i][j];
    }

    public int getRes() {
        return this.res;
    }
}