using Azure;
using Azure.AI.OpenAI;
using OpenAI.Chat;

using static System.Environment;
using System.Text.Json;

async Task RunAsync()
{
    // 환경 변수에서 OpenAI 엔드포인트 검색
    var endpoint = GetEnvironmentVariable("AZURE_OPENAI_ENDPOINT") ?? "https://ai-juhyung10213018ai549704168155.openai.azure.com/";
    if (string.IsNullOrEmpty(endpoint))
    {
        Console.WriteLine("Please set the AZURE_OPENAI_ENDPOINT environment variable.");
        return;
    }

    var key = GetEnvironmentVariable("AZURE_OPENAI_KEY") ?? "YOUR_KEY";
    if (string.IsNullOrEmpty(key))
    {
        Console.WriteLine("Please set the AZURE_OPENAI_KEY environment variable.");
        return;
    }

    AzureKeyCredential credential = new AzureKeyCredential(key);

    // AzureOpenAIClient 초기화
    AzureOpenAIClient azureClient = new(new Uri(endpoint), credential);

    // 지정된 배포 이름으로 ChatClient 초기화
    ChatClient chatClient = azureClient.GetChatClient("gpt-4");

    // 채팅 메시지 목록 만들기
    var messages = new List<ChatMessage>
    {
        UserChatMessage.CreateUserMessage("Hello, how are you?")
    };

    // 채팅 완료 옵션 만들기
    var options = new ChatCompletionOptions
    {
        Temperature = (float)0.7,
        MaxOutputTokenCount = 800,

        TopP = (float)0.95,
        FrequencyPenalty = (float)0,
        PresencePenalty = (float)0
    };

    try
    {
        // 채팅 완료 요청 만들기
        ChatCompletion completion = await chatClient.CompleteChatAsync(messages, options);

        // 응답 인쇄
        if (completion != null)
        {
            Console.WriteLine(JsonSerializer.Serialize(completion, new JsonSerializerOptions() { WriteIndented = true }));
        }
        else
        {
            Console.WriteLine("No response received.");
        }
    }
    catch (Exception ex)
    {
        Console.WriteLine($"An error occurred: {ex.Message}");
    }
}

await RunAsync();