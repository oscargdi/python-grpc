# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: com/grpc/services/hello.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from com.grpc.messages import hello_pb2 as com_dot_grpc_dot_messages_dot_hello__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63om/grpc/services/hello.proto\x12\x0c\x63om.services\x1a\x1d\x63om/grpc/messages/hello.proto2M\n\x07Greeter\x12\x42\n\x08SayHello\x12\x1a.com.messages.HelloRequest\x1a\x18.com.messages.HelloReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'com.grpc.services.hello_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_GREETER']._serialized_start=78
  _globals['_GREETER']._serialized_end=155
# @@protoc_insertion_point(module_scope)
