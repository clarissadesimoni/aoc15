import java.util.*;
import java.util.stream.Collectors;

public class Part1d5 {
    private int res;
    public Part1d5() {
        List<String> input = new MyReader5().getData();
        this.res = input.stream().filter(l -> this.isNice(l)).collect(Collectors.toList()).size();
    }

    private List<Integer> listOccurrences(String string, String substring) {
        List<Integer> count = new ArrayList<Integer>();
        if (string.contains(substring))
            for (int i = 0; i < string.length(); i++)
                if (string.substring(i).startsWith(substring))
                    count.add(i);
        return count;
    }

    private boolean contains3vowels(String string) {
        List<String> vowels = List.of("a", "e", "i", "o", "u");
        return vowels.stream().mapToInt(v -> this.listOccurrences(string, v).size()).sum() >= 3;
    }

    private boolean containsDoubles(String string) {
        List<String> alphabet = List.of("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z");
        boolean found = false;
        for (String l : alphabet) {
            found = this.listOccurrences(string, l + l).size() >= 1;
            if (found) break;
        }
        return found;
    }

    private boolean containsNoNaughty(String string) {
        List<String> naughty = List.of("ab", "cd", "pq", "xy");
        return naughty.stream().allMatch(n -> !string.contains(n));
    }

    private boolean isNice(String string) {
        return this.contains3vowels(string) && this.containsDoubles(string) && this.containsNoNaughty(string);
    }

    public int getRes() {
        return this.res;
    }
}