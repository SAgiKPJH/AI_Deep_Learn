using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;

var modelId = "";
var endpoint = "";
var apiKey = "";

var builder = Kernel.CreateBuilder().AddAzureOpenAIChatCompletion(modelId, endpoint, apiKey);
builder.Services.AddLogging(services => services.AddConsole().SetMinimumLevel(LogLevel.Trace));
var kernel = builder.Build();

IChatCompletionService chatCompletion = kernel.GetRequiredService<IChatCompletionService>();
kernel.Plugins.AddFromType<>("Lights");