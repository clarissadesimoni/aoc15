public class Part2 {
    private int res = 0;
    public Part2() {
        int floor = 0;
        String data = new MyReader().getData();
        for (this.res = 0; this.res < data.length(); this.res++) {
            if (floor == -1) break;
            if (data.charAt(this.res) == '(') floor++;
            else if (data.charAt(this.res) == ')') floor--;
        }
    }

    public int getRes() {
        return this.res;
    }
}
