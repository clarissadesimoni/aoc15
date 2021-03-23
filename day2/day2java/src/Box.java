import java.util.*;

public class Box {
    private int length, width, height;
    public Box(String line) {
        String[] items = line.split("x");
        this.length = Integer.parseInt(items[0]);
        this.width = Integer.parseInt(items[1]);
        this.height = Integer.parseInt(items[2]);
    }

    private List<Integer> getAreas() {
        List<Integer> res = new ArrayList<Integer>();
        res.add(this.length * this.width);
        res.add(this.length * this.height);
        res.add(this.width * this.height);
        return res;
    }

    public int getSurface() {
        List<Integer> a = this.getAreas();
        return 2 * a.stream().mapToInt(i -> i).sum() + a.stream().mapToInt(i -> i).min().getAsInt();
    }
}
