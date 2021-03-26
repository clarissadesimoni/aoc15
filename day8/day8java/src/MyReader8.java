import java.io.*;
import java.util.*;

public class MyReader8 {
    private static final String fileDir = "/Users/clarissadesimoni/Desktop/aoc15/day8/";
    private List<String> data = new ArrayList<String>();
    public MyReader8() {
        try {
            BufferedReader br = new BufferedReader(new FileReader(fileDir + "day8.txt"));
            String line;
            while((line = br.readLine()) != null) {
                this.data.add(line);
            }
            br.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public List<String> getData() {
        return this.data;
    }
}