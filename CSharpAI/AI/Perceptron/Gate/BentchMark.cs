using BenchmarkDotNet.Attributes;
using BenchmarkDotNet.Running;

namespace Perceptron.Gate;

public class Benchmark
{
    private readonly Binary binaryGate = new Binary();
    private readonly Perceptron perceptronGate = new Perceptron();
    private readonly Random random = new Random();

    [Benchmark]
    public void BenchmarkBinaryAND()
    {
        for (int i = 0; i < 10000000; i++)
        {
            int x1 = random.Next(0, 2);
            int x2 = random.Next(0, 2);
            binaryGate.AND(x1, x2);
        }
    }

    [Benchmark]
    public void BenchmarkPerceptronAND()
    {
        for (int i = 0; i < 10000000; i++)
        {
            int x1 = random.Next(0, 2);
            int x2 = random.Next(0, 2);
            perceptronGate.AND(x1, x2);
        }
    }
}