public class Part1d1 {
    private int res = 0;
    public Part1d1() {
        String data = new MyReader1().getData();
        for (int i = 0; i < data.length(); i++) {
            if (data.charAt(i) == '(') this.res++;
            else if (data.charAt(i) == ')') this.res--;
        }
    }

    public int getRes() {
        return this.res;
    }
}
