import java.util.*;
import java.util.function.IntBinaryOperator;

// CREDITS TO REDDIT USER u/twisted_tree

public class Part1d7 {
    private int res;
    private static HashMap<String, IntBinaryOperator> ops = new HashMap<String, IntBinaryOperator>();
    private static HashMap<String, Node> vars = new HashMap<String, Node>();
    public Part1d7() {
        List<String[]> data = new MyReader7().getData();
        ops.put("AND", (a, b) -> a & b);
        ops.put("OR", (a, b) -> a | b);
        ops.put("LSHIFT", (a, b) -> a << b);
        ops.put("RSHIFT", (a, b) -> a >> b);

        for (String[] line : data) {
            String[] split = line[0].split(" ");
            Node var = new Node();
            if (split.length == 1) {
                var.setValue(getValue(split[0]));
                vars.put(line[1], var);
            } else if (split[0].equals("NOT")) {
                var.setValue(new Negation(getValue(split[1])));
                vars.put(line[1], var);
            } else {
                var.setValue(new Operator(split[1], getValue(split[0]), getValue(split[2])));
                vars.put(line[1], var);
            }
        }
        this.res = Part1d7.vars.get("a").getValue();
    }

    public int getRes() {
        return this.res;
    }

    static Element getValue(String s) {
        if (s.matches("\\d+")) {
            return new Literal(Integer.parseInt(s));
        } else {
            return new LazyNode(s);
        }
    }

    interface Element {
        int getValue();
    }

    static class Node implements Element {
        Element value;
        Integer cached = null;

        public void setValue(Element value) {
            this.value = value;
        }

        @Override
        public int getValue() {
            if (cached == null)
                cached = value.getValue() & 0xffff;
            return cached;
        }
    }

    static class LazyNode implements Element {
        String name;

        public LazyNode(String name) {
            this.name = name;
        }

        @Override
        public int getValue() {
            return vars.get(name).getValue();
        }
    }

    static class Literal implements Element {
        int value;

        public Literal(int value) {
            this.value = value;
        }

        @Override
        public int getValue() {
            return value;
        }
    }

    static class Negation implements Element {
        Element orig;

        public Negation(Element orig) {
            this.orig = orig;
        }

        @Override
        public int getValue() {
            return ~orig.getValue();
        }
    }

    static class Operator implements Element {
        IntBinaryOperator op;
        String title;
        Element left, right;

        public Operator(String title, Element left, Element right) {
            this.title = title;
            op = ops.get(title);
            this.left = left;
            this.right = right;
        }

        @Override
        public int getValue() {
            return op.applyAsInt(left.getValue(), right.getValue());
        }
    }
}
