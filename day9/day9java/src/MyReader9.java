import java.io.*;
import java.util.*;

public class MyReader9 {
    private static final String fileDir = "/Users/clarissadesimoni/Desktop/aoc15/day9/";
    private List<List<String>> data = new ArrayList<List<String>>();
    public MyReader9() {
        try {
            BufferedReader br = new BufferedReader(new FileReader(fileDir + "day9.txt"));
            String line;
            while((line = br.readLine()) != null) {
                List<String> tmp = Arrays.asList(line.split("\s"));
                tmp.remove(3);
                tmp.remove(1);
                this.data.add(tmp);
            }
            br.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public List<List<String>> getData() {
        return this.data;
    }
}