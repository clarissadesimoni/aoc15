import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*;

public class MyReader2 {
    private static final String fileDir = "/Users/clarissadesimoni/Desktop/aoc15/day2/";
    private List<String> data = new ArrayList<String>();
    public MyReader2() {
        try {
            BufferedReader br = new BufferedReader(new FileReader(fileDir + "day2.txt"));
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
