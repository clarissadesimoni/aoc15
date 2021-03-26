import java.io.*;
import java.util.*;

public class MyReader7 {
    private static final String fileDir = "/Users/clarissadesimoni/Desktop/aoc15/day7/";
    private List<String[]> data = new ArrayList<String[]>();
    public MyReader7() {
        try {
            BufferedReader br = new BufferedReader(new FileReader(fileDir + "day7.txt"));
            String line;
            while((line = br.readLine()) != null) {
                this.data.add(line.split("\s->\s"));
            }
            br.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public List<String[]> getData() {
        return this.data;
    }
}