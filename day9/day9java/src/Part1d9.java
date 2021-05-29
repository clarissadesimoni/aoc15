import java.util.*;
import java.util.stream.Collectors;
import com.google.common.collect.Collections2;

public class Part1d9 {
    private int res;
    private Map<String,Map<String,Integer>> rides = new HashMap<String,Map<String,Integer>>();
    public Part1d9() {
        List<List<String>> data = new MyReader9().getData();
        for (List<String> list : data) {
            this.rides.put(list.get(0), new HashMap<String,Integer>());
            this.rides.put(list.get(1), new HashMap<String,Integer>());
        }
        for (List<String> list : data) {
            this.rides.get(list.get(0)).put(list.get(1), Integer.parseInt(list.get(2)));
            this.rides.get(list.get(1)).put(list.get(0), Integer.parseInt(list.get(2)));
        }
        // var cities = Object.keys(rides);
        // var perm = permutations(cities, cities.length);
        // var costs = perm.map(p => p.reduce(function(acc, curr, i) {return acc + (i == cities.length - 1 ? 0 : rides[curr][p[i + 1]]);}, 0))
        
        Set<String> cities = this.rides.keySet();
        Collection<List<String>> perm = Collections2.permutations(cities);
        List<Integer> costs = perm.stream().map(p -> {
            return p.stream().mapToInt(c -> {
                int currInd = p.indexOf(c);
                return currInd == cities.size() - 1 ? rides.get(c).get(p.get(currInd + 1));
            }).sum();
        }).collect(Collectors.toList());
    }

    public int getRes() {
        return this.res;
    }
}