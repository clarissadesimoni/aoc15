import java.util.*;
import java.util.stream.Collectors;

public class Part2d9 {
    private int res;
    private Map<String,Map<String,Integer>> rides = new HashMap<String,Map<String,Integer>>();
    public Part2d9() {
        List<List<String>> data = new MyReader9().getData();
        for (List<String> list : data) {
            this.rides.put(list.get(0), new HashMap<String,Integer>());
            this.rides.put(list.get(1), new HashMap<String,Integer>());
        }
        for (List<String> list : data) {
            this.rides.get(list.get(0)).put(list.get(1), Integer.parseInt(list.get(2)));
            this.rides.get(list.get(1)).put(list.get(0), Integer.parseInt(list.get(2)));
        }
    }

    public int getRes() {
        return this.res;
    }
}