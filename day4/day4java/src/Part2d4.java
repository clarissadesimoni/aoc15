import java.security.*;

public class Part2d4 {
    private int res = 1;
    public Part2d4() {
        String data = new MyReader4().getData();
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            String pass = data + this.res;
            md.update(pass.getBytes());
            byte byteData[] = md.digest();
            StringBuffer sb = new StringBuffer();
            for (int i = 0; i < byteData.length; i++)
                sb.append(Integer.toString((byteData[i] & 0xff) + 0x100, 16).substring(1));
            while (!sb.toString().startsWith("000000")) {
                this.res++;
                pass = data + this.res;
                md.update(pass.getBytes());
                byteData = md.digest();
                sb = new StringBuffer();
                for (int i = 0; i < byteData.length; i++)
                    sb.append(Integer.toString((byteData[i] & 0xff) + 0x100, 16).substring(1));
            }
        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        }
    }

    public int getRes() {
        return this.res;
    }
}