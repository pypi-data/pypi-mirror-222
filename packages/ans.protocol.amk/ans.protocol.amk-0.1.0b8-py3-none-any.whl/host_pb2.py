# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: host.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nhost.proto\x12\x1e\x61ns.protocol.solver_proxy.host\x1a\x1bgoogle/protobuf/empty.proto\"\x17\n\x07ProxyId\x12\x0c\n\x04hash\x18\x01 \x01(\t\"_\n\x0eLicensingInput\x12\x39\n\x08proxy_id\x18\x01 \x01(\x0b\x32\'.ans.protocol.solver_proxy.host.ProxyId\x12\x12\n\ncapability\x18\x02 \x01(\x05\"\xa1\x01\n\x0cProgressInfo\x12\x39\n\x08proxy_id\x18\x01 \x01(\x0b\x32\'.ans.protocol.solver_proxy.host.ProxyId\x12\x17\n\x0foverall_percent\x18\x02 \x01(\x05\x12\x13\n\x0bsub_percent\x18\x03 \x01(\x05\x12\x12\n\nmessage_id\x18\x04 \x01(\t\x12\x14\n\x0cmessage_info\x18\x05 \x01(\t\"\xba\x04\n\x0bMessageInfo\x12\x39\n\x08proxy_id\x18\x01 \x01(\x0b\x32\'.ans.protocol.solver_proxy.host.ProxyId\x12\x19\n\x11primary_object_id\x18\x02 \x01(\x05\x12\x46\n\x08severity\x18\x03 \x01(\x0e\x32\x34.ans.protocol.solver_proxy.host.MessageInfo.Severity\x12J\n\x04type\x18\x04 \x01(\x0e\x32<.ans.protocol.solver_proxy.host.MessageInfo.MAPDLMessageType\x12\x18\n\x10\x65rror_identifier\x18\x05 \x01(\t\x12\x15\n\rcustom_string\x18\x06 \x01(\t\x12\x1a\n\x12related_object_ids\x18\x07 \x03(\x05\x12\x0f\n\x07node_id\x18\x08 \x01(\x05\x12\x12\n\nelement_id\x18\t \x01(\x05\x12\x10\n\x08\x64of_flag\x18\n \x01(\x05\x12\x0f\n\x07\x62ody_id\x18\x0b \x01(\x05\x12\x14\n\x0cgeometry_ids\x18\x0c \x03(\x05\"5\n\x08Severity\x12\x06\n\x02OK\x10\x00\x12\x08\n\x04INFO\x10\x01\x12\x0b\n\x07WARNING\x10\x02\x12\n\n\x06\x45RROR_\x10\x03\"_\n\x10MAPDLMessageType\x12\x08\n\x04NONE\x10\x00\x12\x0b\n\x07GENERIC\x10\x01\x12\r\n\tDOF_LIMIT\x10\x02\x12\x0f\n\x0bPIVOT_ERROR\x10\x03\x12\x14\n\x10\x44ISTORTION_ERROR\x10\x04\x32\xe3\x02\n\x04Host\x12W\n\rBorrowLicense\x12..ans.protocol.solver_proxy.host.LicensingInput\x1a\x16.google.protobuf.Empty\x12W\n\rReturnLicense\x12..ans.protocol.solver_proxy.host.LicensingInput\x1a\x16.google.protobuf.Empty\x12V\n\x0eUpdateProgress\x12,.ans.protocol.solver_proxy.host.ProgressInfo\x1a\x16.google.protobuf.Empty\x12Q\n\nLogMessage\x12+.ans.protocol.solver_proxy.host.MessageInfo\x1a\x16.google.protobuf.EmptyB \xaa\x02\x1d\x41ns.Protocol.SolverProxy.Hostb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'host_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\252\002\035Ans.Protocol.SolverProxy.Host'
  _PROXYID._serialized_start=75
  _PROXYID._serialized_end=98
  _LICENSINGINPUT._serialized_start=100
  _LICENSINGINPUT._serialized_end=195
  _PROGRESSINFO._serialized_start=198
  _PROGRESSINFO._serialized_end=359
  _MESSAGEINFO._serialized_start=362
  _MESSAGEINFO._serialized_end=932
  _MESSAGEINFO_SEVERITY._serialized_start=782
  _MESSAGEINFO_SEVERITY._serialized_end=835
  _MESSAGEINFO_MAPDLMESSAGETYPE._serialized_start=837
  _MESSAGEINFO_MAPDLMESSAGETYPE._serialized_end=932
  _HOST._serialized_start=935
  _HOST._serialized_end=1290
# @@protoc_insertion_point(module_scope)
