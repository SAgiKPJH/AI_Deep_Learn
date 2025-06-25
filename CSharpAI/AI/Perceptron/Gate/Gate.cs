namespace Perceptron.Gate;

public class Perceptron : IGate
{
    public int AND(int x1, int x2)
    {
        double[] w = { 0.5, 0.5 };
        double b = -0.7;
        double tmp = x1 * w[0] + x2 * w[1] + b;
        return tmp <= 0 ? 0 : 1;
    }

    public int NAND(int x1, int x2)
    {
        double[] w = { -0.5, -0.5 };
        double b = 0.7;
        double tmp = x1 * w[0] + x2 * w[1] + b;
        return tmp <= 0 ? 0 : 1;
    }

    public int OR(int x1, int x2)
    {
        double[] w = { 0.5, 0.5 };
        double b = -0.2;
        double tmp = x1 * w[0] + x2 * w[1] + b;
        return tmp <= 0 ? 0 : 1;
    }

    public int XOR(int x1, int x2)
    {
        int s1 = NAND(x1, x2);
        int s2 = OR(x1, x2);
        return AND(s1, s2);
    }
}