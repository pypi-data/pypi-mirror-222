# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import caerep_pb2 as caerep__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bproxy.proto\x12\x1f\x61ns.protocol.solver_proxy.proxy\x1a\x0c\x63\x61\x65rep.proto\"\x1d\n\tInputFile\x12\x10\n\x08\x63ontents\x18\x01 \x01(\t2\xa9\x01\n\tCAESolver\x12\x41\n\x05Solve\x12\x1b.ans.protocol.caerep.CAERep\x1a\x1b.ans.protocol.caerep.Output\x12Y\n\x0eWriteInputFile\x12\x1b.ans.protocol.caerep.CAERep\x1a*.ans.protocol.solver_proxy.proxy.InputFileB#H\x03\xaa\x02\x1e\x41ns.Protocol.SolverProxy.Proxyb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\003\252\002\036Ans.Protocol.SolverProxy.Proxy'
  _INPUTFILE._serialized_start=62
  _INPUTFILE._serialized_end=91
  _CAESOLVER._serialized_start=94
  _CAESOLVER._serialized_end=263
# @@protoc_insertion_point(module_scope)
