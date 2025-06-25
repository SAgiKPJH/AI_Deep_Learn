using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Logging;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Connectors.OpenAI;
using SemanticKernal_Example;

var modelId = "gpt-4";
var endpoint = "https://ai-juhyung10213018ai549704168155.services.ai.azure.com/";
var apiKey = "YOUR_KEY";

var builder = Kernel.CreateBuilder().AddAzureOpenAIChatCompletion(modelId, endpoint, apiKey);
builder.Services.AddLogging(services => services.AddConsole().SetMinimumLevel(LogLevel.Trace));
var kernel = builder.Build();

IChatCompletionService chatCompletion = kernel.GetRequiredService<IChatCompletionService>();
kernel.Plugins.AddFromType<UserPlugin>("Users");

OpenAIPromptExecutionSettings openAIPromptExecutionSettings = new()
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto()
    //MaxTokens = 100,
    //Temperature = 0.7,
    //TopP = 1,
    //FrequencyPenalty = 0,
    //PresencePenalty = 0,
};

var history = new ChatHistory();
string? userInput;

do
{
    Console.WriteLine("User > ");
    userInput = Console.ReadLine();

    if (userInput is null)
        break;

    history.AddUserMessage(userInput);
    var result = await chatCompletion.GetChatMessageContentAsync(history, openAIPromptExecutionSettings, kernel);
    Console.WriteLine("Assistant > " + result);

    history.AddMessage(result.Role, result.Content ?? string.Empty);

} while (userInput is not null);