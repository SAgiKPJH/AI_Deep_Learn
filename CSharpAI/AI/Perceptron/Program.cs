using BenchmarkDotNet.Running;
using Perceptron.Gate;

Console.WriteLine("Perceptron Gate vs Binary Gate");
var summary = BenchmarkRunner.Run<Benchmark>();