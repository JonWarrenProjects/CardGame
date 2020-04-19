# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: comms/GameState.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='comms/GameState.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x15\x63omms/GameState.proto\"!\n\x11HelloWorldRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"%\n\x12HelloWorldResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x15\n\x13InitialStateRequest\"N\n\x16InitialisationResponse\x12\x11\n\tplayer_id\x18\x01 \x01(\t\x12!\n\rinitial_state\x18\x02 \x01(\x0b\x32\n.GameState\"^\n\tGameState\x12\x13\n\x0bturn_number\x18\x01 \x01(\x03\x12\x14\n\x0cplayer_money\x18\x02 \x01(\x03\x12\x13\n\x04hand\x18\x03 \x03(\x0b\x32\x05.Card\x12\x11\n\tdeck_size\x18\x04 \x01(\x03\"\x15\n\x04\x43\x61rd\x12\r\n\x05index\x18\x01 \x01(\x03\x32\x8a\x01\n\x0bGameService\x12\x35\n\nHelloWorld\x12\x12.HelloWorldRequest\x1a\x13.HelloWorldResponse\x12\x44\n\x13GetInitialGameState\x12\x14.InitialStateRequest\x1a\x17.InitialisationResponseb\x06proto3'
)




_HELLOWORLDREQUEST = _descriptor.Descriptor(
  name='HelloWorldRequest',
  full_name='HelloWorldRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='HelloWorldRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=58,
)


_HELLOWORLDRESPONSE = _descriptor.Descriptor(
  name='HelloWorldResponse',
  full_name='HelloWorldResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='HelloWorldResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=97,
)


_INITIALSTATEREQUEST = _descriptor.Descriptor(
  name='InitialStateRequest',
  full_name='InitialStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=120,
)


_INITIALISATIONRESPONSE = _descriptor.Descriptor(
  name='InitialisationResponse',
  full_name='InitialisationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='player_id', full_name='InitialisationResponse.player_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='initial_state', full_name='InitialisationResponse.initial_state', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=122,
  serialized_end=200,
)


_GAMESTATE = _descriptor.Descriptor(
  name='GameState',
  full_name='GameState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='turn_number', full_name='GameState.turn_number', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_money', full_name='GameState.player_money', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hand', full_name='GameState.hand', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deck_size', full_name='GameState.deck_size', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=202,
  serialized_end=296,
)


_CARD = _descriptor.Descriptor(
  name='Card',
  full_name='Card',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='index', full_name='Card.index', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=298,
  serialized_end=319,
)

_INITIALISATIONRESPONSE.fields_by_name['initial_state'].message_type = _GAMESTATE
_GAMESTATE.fields_by_name['hand'].message_type = _CARD
DESCRIPTOR.message_types_by_name['HelloWorldRequest'] = _HELLOWORLDREQUEST
DESCRIPTOR.message_types_by_name['HelloWorldResponse'] = _HELLOWORLDRESPONSE
DESCRIPTOR.message_types_by_name['InitialStateRequest'] = _INITIALSTATEREQUEST
DESCRIPTOR.message_types_by_name['InitialisationResponse'] = _INITIALISATIONRESPONSE
DESCRIPTOR.message_types_by_name['GameState'] = _GAMESTATE
DESCRIPTOR.message_types_by_name['Card'] = _CARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HelloWorldRequest = _reflection.GeneratedProtocolMessageType('HelloWorldRequest', (_message.Message,), {
  'DESCRIPTOR' : _HELLOWORLDREQUEST,
  '__module__' : 'comms.GameState_pb2'
  # @@protoc_insertion_point(class_scope:HelloWorldRequest)
  })
_sym_db.RegisterMessage(HelloWorldRequest)

HelloWorldResponse = _reflection.GeneratedProtocolMessageType('HelloWorldResponse', (_message.Message,), {
  'DESCRIPTOR' : _HELLOWORLDRESPONSE,
  '__module__' : 'comms.GameState_pb2'
  # @@protoc_insertion_point(class_scope:HelloWorldResponse)
  })
_sym_db.RegisterMessage(HelloWorldResponse)

InitialStateRequest = _reflection.GeneratedProtocolMessageType('InitialStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _INITIALSTATEREQUEST,
  '__module__' : 'comms.GameState_pb2'
  # @@protoc_insertion_point(class_scope:InitialStateRequest)
  })
_sym_db.RegisterMessage(InitialStateRequest)

InitialisationResponse = _reflection.GeneratedProtocolMessageType('InitialisationResponse', (_message.Message,), {
  'DESCRIPTOR' : _INITIALISATIONRESPONSE,
  '__module__' : 'comms.GameState_pb2'
  # @@protoc_insertion_point(class_scope:InitialisationResponse)
  })
_sym_db.RegisterMessage(InitialisationResponse)

GameState = _reflection.GeneratedProtocolMessageType('GameState', (_message.Message,), {
  'DESCRIPTOR' : _GAMESTATE,
  '__module__' : 'comms.GameState_pb2'
  # @@protoc_insertion_point(class_scope:GameState)
  })
_sym_db.RegisterMessage(GameState)

Card = _reflection.GeneratedProtocolMessageType('Card', (_message.Message,), {
  'DESCRIPTOR' : _CARD,
  '__module__' : 'comms.GameState_pb2'
  # @@protoc_insertion_point(class_scope:Card)
  })
_sym_db.RegisterMessage(Card)



_GAMESERVICE = _descriptor.ServiceDescriptor(
  name='GameService',
  full_name='GameService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=322,
  serialized_end=460,
  methods=[
  _descriptor.MethodDescriptor(
    name='HelloWorld',
    full_name='GameService.HelloWorld',
    index=0,
    containing_service=None,
    input_type=_HELLOWORLDREQUEST,
    output_type=_HELLOWORLDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetInitialGameState',
    full_name='GameService.GetInitialGameState',
    index=1,
    containing_service=None,
    input_type=_INITIALSTATEREQUEST,
    output_type=_INITIALISATIONRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GAMESERVICE)

DESCRIPTOR.services_by_name['GameService'] = _GAMESERVICE

# @@protoc_insertion_point(module_scope)
