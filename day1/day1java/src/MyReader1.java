import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class MyReader1 {
    private static final String fileDir = "/Users/clarissadesimoni/Desktop/aoc15/day1/";
    private String data;
    public MyReader1() {
        try {
            BufferedReader br = new BufferedReader(new FileReader(fileDir + "day1.txt"));
            StringBuilder sb = new StringBuilder();
            String line;
            while((line = br.readLine()) != null) {
                sb.append(line);
            }
            this.data = sb.toString();
            br.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public String getData() {
        return this.data;
    }
}
