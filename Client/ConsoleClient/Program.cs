using System;

using Grpc.Core;

namespace ConsoleClient
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            Channel channel = new Channel("127.0.0.1:50051", ChannelCredentials.Insecure);
            var client = new GameService.GameServiceClient(channel);

            string name = "Jan Frederick";
            var response = client.HelloWorld(new HelloWorldRequest { Name = name });
            Console.WriteLine(response.Message);

            var gameStateResponse = client.GetInitialGameState(new InitialStateRequest());
            Console.WriteLine(gameStateResponse.PlayerId);
        }
    }
}
