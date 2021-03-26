import java.util.*;

public class Part1d8 {
    private int res;
    public Part1d8() {
        List<String> data = new MyReader8().getData();
        this.res = data.stream().mapToInt(string -> this.countChars(string)).sum();
    }

    private int countChars(String string) {
        int i = 0, code = 0, memory = 0;
        char[] hexChars = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'};
        while (i < string.length()) {
            if (string.charAt(i) == '\\') {
                if (string.charAt(i + 1) == 'x' && Arrays.binarySearch(hexChars, string.charAt(i + 2)) >= 0 && Arrays.binarySearch(hexChars, string.charAt(i + 3)) >= 0) {
                    memory += 3;
                    i += 3;
                } else {
                    memory += 1;
                    i += 1;
                }
            } else if (string.charAt(i) == '\"') code -= 1;
            code += 1;
            memory += 1;
            i += 1;
        }
        return memory - code;
    }

    public int getRes() {
        return this.res;
    }
}