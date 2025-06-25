namespace Perceptron.Gate;

public class Binary : IGate
{
    public int AND(int x1, int x2) => x1 & x2;

    public int NAND(int x1, int x2) => ~(x1 & x2);

    public int OR(int x1, int x2) => x1 | x2;

    public int XOR(int x1, int x2) => x1 ^ x2;
}