using Microsoft.SemanticKernel;
using System.ComponentModel;
using System.Text.Json.Serialization;

namespace SemanticKernal_Example;

public class UserPlugin
{
    private readonly List<User> _users =
    [
        new User { Id = 1, Name = "John Doe", Age = "25" },
        new User { Id = 2, Name = "Jane Doe", Age = "30" },
        new User { Id = 3, Name = "Sammy Doe", Age = "35" }
    ];

    [KernelFunction("get_users")]
    [Description("Get all users")]
    public async Task<List<User>> GetUsers() => await Task.FromResult(_users);

    [KernelFunction("get_user")]
    [Description("Get user by id")]
    public async Task<User?> GetUser(int id) => await Task.FromResult(_users.FirstOrDefault(x => x.Id == id));
}

public class User
{
    [JsonPropertyName("id")]
    public int Id { get; set; }
    [JsonPropertyName("name")]
    public string Name { get; set; } = string.Empty;
    [JsonPropertyName("age")]
    public string Age { get; set; } = string.Empty;
}