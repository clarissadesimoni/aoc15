import java.util.*;
import java.util.stream.Collectors;

public class Part2d5 {
    private int res;
    public Part2d5() {
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

    private boolean containsRepeatingCouple(String string) {
        boolean found = false;
        for (int i = 0; i < string.length() - 1; i++) {
            List<Integer> occ = listOccurrences(string, string.substring(i, i + 2));
            List<Integer> occNew = occ.stream().filter(o -> !occ.contains(o - 1)).collect(Collectors.toList());
            found = occNew.size() - 1 > 0;
            if (found) break;
        }
        return found;
    }
    
    private boolean containsAlternatingLetter(String string) {
        boolean found = false;
        for (var i = 0; i < string.length() - 2; i++) {
            found = string.charAt(i) == string.charAt(i + 2);
            if (found) break;
        }
        return found;
    }

    private boolean isNice(String string) {
        return this.containsRepeatingCouple(string) && this.containsAlternatingLetter(string);
    }

    public int getRes() {
        return this.res;
    }
}