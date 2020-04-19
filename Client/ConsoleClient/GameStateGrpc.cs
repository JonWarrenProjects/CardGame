// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: comms/GameState.proto
// </auto-generated>
#pragma warning disable 0414, 1591
#region Designer generated code

using grpc = global::Grpc.Core;

public static partial class GameService
{
  static readonly string __ServiceName = "GameService";

  static readonly grpc::Marshaller<global::HelloWorldRequest> __Marshaller_HelloWorldRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::HelloWorldRequest.Parser.ParseFrom);
  static readonly grpc::Marshaller<global::HelloWorldResponse> __Marshaller_HelloWorldResponse = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::HelloWorldResponse.Parser.ParseFrom);
  static readonly grpc::Marshaller<global::InitialStateRequest> __Marshaller_InitialStateRequest = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::InitialStateRequest.Parser.ParseFrom);
  static readonly grpc::Marshaller<global::InitialisationResponse> __Marshaller_InitialisationResponse = grpc::Marshallers.Create((arg) => global::Google.Protobuf.MessageExtensions.ToByteArray(arg), global::InitialisationResponse.Parser.ParseFrom);

  static readonly grpc::Method<global::HelloWorldRequest, global::HelloWorldResponse> __Method_HelloWorld = new grpc::Method<global::HelloWorldRequest, global::HelloWorldResponse>(
      grpc::MethodType.Unary,
      __ServiceName,
      "HelloWorld",
      __Marshaller_HelloWorldRequest,
      __Marshaller_HelloWorldResponse);

  static readonly grpc::Method<global::InitialStateRequest, global::InitialisationResponse> __Method_GetInitialGameState = new grpc::Method<global::InitialStateRequest, global::InitialisationResponse>(
      grpc::MethodType.Unary,
      __ServiceName,
      "GetInitialGameState",
      __Marshaller_InitialStateRequest,
      __Marshaller_InitialisationResponse);

  /// <summary>Service descriptor</summary>
  public static global::Google.Protobuf.Reflection.ServiceDescriptor Descriptor
  {
    get { return global::GameStateReflection.Descriptor.Services[0]; }
  }

  /// <summary>Base class for server-side implementations of GameService</summary>
  [grpc::BindServiceMethod(typeof(GameService), "BindService")]
  public abstract partial class GameServiceBase
  {
    public virtual global::System.Threading.Tasks.Task<global::HelloWorldResponse> HelloWorld(global::HelloWorldRequest request, grpc::ServerCallContext context)
    {
      throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
    }

    public virtual global::System.Threading.Tasks.Task<global::InitialisationResponse> GetInitialGameState(global::InitialStateRequest request, grpc::ServerCallContext context)
    {
      throw new grpc::RpcException(new grpc::Status(grpc::StatusCode.Unimplemented, ""));
    }

  }

  /// <summary>Client for GameService</summary>
  public partial class GameServiceClient : grpc::ClientBase<GameServiceClient>
  {
    /// <summary>Creates a new client for GameService</summary>
    /// <param name="channel">The channel to use to make remote calls.</param>
    public GameServiceClient(grpc::ChannelBase channel) : base(channel)
    {
    }
    /// <summary>Creates a new client for GameService that uses a custom <c>CallInvoker</c>.</summary>
    /// <param name="callInvoker">The callInvoker to use to make remote calls.</param>
    public GameServiceClient(grpc::CallInvoker callInvoker) : base(callInvoker)
    {
    }
    /// <summary>Protected parameterless constructor to allow creation of test doubles.</summary>
    protected GameServiceClient() : base()
    {
    }
    /// <summary>Protected constructor to allow creation of configured clients.</summary>
    /// <param name="configuration">The client configuration.</param>
    protected GameServiceClient(ClientBaseConfiguration configuration) : base(configuration)
    {
    }

    public virtual global::HelloWorldResponse HelloWorld(global::HelloWorldRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
    {
      return HelloWorld(request, new grpc::CallOptions(headers, deadline, cancellationToken));
    }
    public virtual global::HelloWorldResponse HelloWorld(global::HelloWorldRequest request, grpc::CallOptions options)
    {
      return CallInvoker.BlockingUnaryCall(__Method_HelloWorld, null, options, request);
    }
    public virtual grpc::AsyncUnaryCall<global::HelloWorldResponse> HelloWorldAsync(global::HelloWorldRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
    {
      return HelloWorldAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
    }
    public virtual grpc::AsyncUnaryCall<global::HelloWorldResponse> HelloWorldAsync(global::HelloWorldRequest request, grpc::CallOptions options)
    {
      return CallInvoker.AsyncUnaryCall(__Method_HelloWorld, null, options, request);
    }
    public virtual global::InitialisationResponse GetInitialGameState(global::InitialStateRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
    {
      return GetInitialGameState(request, new grpc::CallOptions(headers, deadline, cancellationToken));
    }
    public virtual global::InitialisationResponse GetInitialGameState(global::InitialStateRequest request, grpc::CallOptions options)
    {
      return CallInvoker.BlockingUnaryCall(__Method_GetInitialGameState, null, options, request);
    }
    public virtual grpc::AsyncUnaryCall<global::InitialisationResponse> GetInitialGameStateAsync(global::InitialStateRequest request, grpc::Metadata headers = null, global::System.DateTime? deadline = null, global::System.Threading.CancellationToken cancellationToken = default(global::System.Threading.CancellationToken))
    {
      return GetInitialGameStateAsync(request, new grpc::CallOptions(headers, deadline, cancellationToken));
    }
    public virtual grpc::AsyncUnaryCall<global::InitialisationResponse> GetInitialGameStateAsync(global::InitialStateRequest request, grpc::CallOptions options)
    {
      return CallInvoker.AsyncUnaryCall(__Method_GetInitialGameState, null, options, request);
    }
    /// <summary>Creates a new instance of client from given <c>ClientBaseConfiguration</c>.</summary>
    protected override GameServiceClient NewInstance(ClientBaseConfiguration configuration)
    {
      return new GameServiceClient(configuration);
    }
  }

  /// <summary>Creates service definition that can be registered with a server</summary>
  /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
  public static grpc::ServerServiceDefinition BindService(GameServiceBase serviceImpl)
  {
    return grpc::ServerServiceDefinition.CreateBuilder()
        .AddMethod(__Method_HelloWorld, serviceImpl.HelloWorld)
        .AddMethod(__Method_GetInitialGameState, serviceImpl.GetInitialGameState).Build();
  }

  /// <summary>Register service method with a service binder with or without implementation. Useful when customizing the  service binding logic.
  /// Note: this method is part of an experimental API that can change or be removed without any prior notice.</summary>
  /// <param name="serviceBinder">Service methods will be bound by calling <c>AddMethod</c> on this object.</param>
  /// <param name="serviceImpl">An object implementing the server-side handling logic.</param>
  public static void BindService(grpc::ServiceBinderBase serviceBinder, GameServiceBase serviceImpl)
  {
    serviceBinder.AddMethod(__Method_HelloWorld, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::HelloWorldRequest, global::HelloWorldResponse>(serviceImpl.HelloWorld));
    serviceBinder.AddMethod(__Method_GetInitialGameState, serviceImpl == null ? null : new grpc::UnaryServerMethod<global::InitialStateRequest, global::InitialisationResponse>(serviceImpl.GetInitialGameState));
  }

}
#endregion