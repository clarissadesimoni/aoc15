import java.util.*;
import java.util.stream.Collectors;

public class Part1 {
    private int res;
    public Part1() {
        List<String> data = new MyReader().getData();
        List<Box> boxes = data.stream().map(l -> new Box(l)).collect(Collectors.toList());
        res = boxes.stream().mapToInt(b -> b.getSurface()).sum();
    }

    public int getRes() {
        return this.res;
    }
}