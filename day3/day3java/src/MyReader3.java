import java.io.*;

public class MyReader3 {
    private static final String fileDir = "/Users/clarissadesimoni/Desktop/aoc15/day3/";
    private String data;
    public MyReader3() {
        try {
            BufferedReader br = new BufferedReader(new FileReader(fileDir + "day3.txt"));
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