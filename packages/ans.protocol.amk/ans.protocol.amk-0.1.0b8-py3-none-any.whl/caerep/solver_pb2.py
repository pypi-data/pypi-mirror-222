# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: caerep.solver.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from caerep import common_pb2 as caerep_dot_common__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x63\x61\x65rep.solver.proto\x12\x1a\x61ns.protocol.caerep.solver\x1a\x13\x63\x61\x65rep.common.proto\x1a\x19google/protobuf/any.proto\"I\n\x14ManualMemorySettings\x12\x18\n\x10workspace_memory\x18\x01 \x01(\x05\x12\x17\n\x0f\x64\x61tabase_memory\x18\x02 \x01(\x05\"?\n\x12ManualUnixSettings\x12\x11\n\tuser_name\x18\x01 \x01(\t\x12\x16\n\x0eworking_folder\x18\x02 \x01(\t\"\xb5\x01\n\x13\x42\x61\x63kgroundSolveData\x12\x15\n\rsolve_manager\x18\x01 \x01(\t\x12\r\n\x05queue\x18\x02 \x01(\t\x12\x0f\n\x07license\x18\x03 \x01(\t\x12\x19\n\x11\x63ustom_executable\x18\x04 \x01(\t\x12L\n\x14manual_unix_settings\x18\x05 \x01(\x0b\x32..ans.protocol.caerep.solver.ManualUnixSettings\"6\n\x0fGPUAcceleration\x12\x0e\n\x06\x64\x65vice\x18\x01 \x01(\t\x12\x13\n\x0bnum_devices\x18\x02 \x01(\x05\"\xc6\x03\n\x0fProcessControls\x12\x19\n\x11\x64istributed_solve\x18\x01 \x01(\x08\x12\x14\n\x0cis_rsm_solve\x18\x02 \x01(\x08\x12P\n\x16manual_memory_settings\x18\x03 \x01(\x0b\x32\x30.ans.protocol.caerep.solver.ManualMemorySettings\x12\x16\n\x0emax_processors\x18\x04 \x01(\x05\x12\x1c\n\x14\x61\x64\x64itional_arguments\x18\x05 \x01(\t\x12N\n\x15\x62\x61\x63kground_solve_data\x18\x06 \x01(\x0b\x32/.ans.protocol.caerep.solver.BackgroundSolveData\x12\x45\n\x10gpu_acceleration\x18\x07 \x01(\x0b\x32+.ans.protocol.caerep.solver.GPUAcceleration\x12\x10\n\x08is_local\x18\x08 \x01(\x08\x12\x17\n\x0fhybrid_parallel\x18\t \x01(\x08\x12\x1b\n\x13threads_per_process\x18\n \x01(\x05\x12\x1b\n\x13number_of_processes\x18\x0b \x01(\x05\"\xa6\x02\n\x0c\x41nalysisType\"\x95\x02\n\x04\x45num\x12\n\n\x06STATIC\x10\x00\x12\x0c\n\x08HARMONIC\x10\x01\x12\r\n\tTRANSIENT\x10\x02\x12\x0c\n\x08SPECTRUM\x10\x03\x12\x0c\n\x08\x42UCKLING\x10\x04\x12\t\n\x05MODAL\x10\x05\x12\x13\n\x0fINITIAL_CONTACT\x10\x06\x12\x07\n\x03MBD\x10\x07\x12\t\n\x05SHAPE\x10\x08\x12\x15\n\x11RESPONSE_SPECTRUM\x10\t\x12\x0c\n\x08\x45XPLICIT\x10\n\x12\x15\n\x11\x44\x45SIGN_ASSESSMENT\x10\x0b\x12\x15\n\x11\x43ONDENSE_GEOMETRY\x10\x0c\x12\x19\n\x15TOPOLOGY_OPTIMIZATION\x10\r\x12\x11\n\rCMS_EXPANSION\x10\x0e\x12\x13\n\x0f\x43OUPLED_PHYSICS\x10\x0f\"\x99\x01\n\x0bPhysicsType\"\x89\x01\n\x04\x45num\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nMECHANICAL\x10\x01\x12\x0b\n\x07THERMAL\x10\x02\x12\x11\n\rELECTRIC_COND\x10\x04\x12\x13\n\x0f\x45LECTROMAGNETIC\x10\x08\x12\x10\n\x0c\x45XPLICIT_CDI\x10\x10\x12\x10\n\x0c\x43USTOMIZABLE\x10 \x12\x0b\n\x03\x41LL\x10\x80\x80\x80\x80\x02\"3\n\rFEDisplayType\"\"\n\x04\x45num\x12\t\n\x05LINES\x10\x00\x12\x0f\n\x0bPOINTS_ONLY\x10\x01\"&\n\x0c\x46\x45\x43onnectors\x12\x16\n\x0estep_selection\x18\x01 \x01(\x05\"\xd3\x04\n\tSolverRep\x12\x44\n\ranalysis_type\x18\x01 \x01(\x0e\x32-.ans.protocol.caerep.solver.AnalysisType.Enum\x12\x14\n\x0cphysics_type\x18\x02 \x01(\r\x12\x1a\n\x12solver_target_name\x18\x03 \x01(\t\x12\x41\n\x0csolver_units\x18\x04 \x01(\x0e\x32+.ans.protocol.caerep.common.UnitSystem.Enum\x12\x45\n\x10process_controls\x18\x05 \x01(\x0b\x32+.ans.protocol.caerep.solver.ProcessControls\x12/\n\x11\x61nalysis_settings\x18\x06 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x17\n\x0funknown_pointer\x18\x08 \x01(\t\x12?\n\rfe_connectors\x18\t \x01(\x0b\x32(.ans.protocol.caerep.solver.FEConnectors\x12\x19\n\x11working_directory\x18\n \x01(\t\x12\x0f\n\x07jobname\x18\x0b \x01(\t\x12 \n\x18is_am_process_simulation\x18\x0c \x01(\x08\x12\x1c\n\x14license_feature_name\x18\r \x01(\t\x12\x1a\n\x12skip_solve_command\x18\x0e \x01(\x08\x12\x1d\n\x15\x61pp_working_directory\x18\x0f \x01(\t\x12\x12\n\nis_coupled\x18\x10 \x01(\x08\x42\x1fH\x03\xaa\x02\x1a\x41ns.Protocol.CAERep.Solverb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'caerep.solver_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\003\252\002\032Ans.Protocol.CAERep.Solver'
  _MANUALMEMORYSETTINGS._serialized_start=99
  _MANUALMEMORYSETTINGS._serialized_end=172
  _MANUALUNIXSETTINGS._serialized_start=174
  _MANUALUNIXSETTINGS._serialized_end=237
  _BACKGROUNDSOLVEDATA._serialized_start=240
  _BACKGROUNDSOLVEDATA._serialized_end=421
  _GPUACCELERATION._serialized_start=423
  _GPUACCELERATION._serialized_end=477
  _PROCESSCONTROLS._serialized_start=480
  _PROCESSCONTROLS._serialized_end=934
  _ANALYSISTYPE._serialized_start=937
  _ANALYSISTYPE._serialized_end=1231
  _ANALYSISTYPE_ENUM._serialized_start=954
  _ANALYSISTYPE_ENUM._serialized_end=1231
  _PHYSICSTYPE._serialized_start=1234
  _PHYSICSTYPE._serialized_end=1387
  _PHYSICSTYPE_ENUM._serialized_start=1250
  _PHYSICSTYPE_ENUM._serialized_end=1387
  _FEDISPLAYTYPE._serialized_start=1389
  _FEDISPLAYTYPE._serialized_end=1440
  _FEDISPLAYTYPE_ENUM._serialized_start=1406
  _FEDISPLAYTYPE_ENUM._serialized_end=1440
  _FECONNECTORS._serialized_start=1442
  _FECONNECTORS._serialized_end=1480
  _SOLVERREP._serialized_start=1483
  _SOLVERREP._serialized_end=2078
# @@protoc_insertion_point(module_scope)
