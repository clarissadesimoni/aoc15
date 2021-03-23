import java.util.*;
import java.util.stream.Collectors;

public class Part1d2 {
    private int res;
    public Part1d2() {
        List<String> data = new MyReader2().getData();
        List<Box> boxes = data.stream().map(l -> new Box(l)).collect(Collectors.toList());
        res = boxes.stream().mapToInt(b -> b.getSurface()).sum();
    }

    public int getRes() {
        return this.res;
    }
}