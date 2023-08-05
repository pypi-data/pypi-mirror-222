# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analysis_settings.ansys.structural.response_spectrum.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from analysis_settings.ansys import common_pb2 as analysis__settings_dot_ansys_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:analysis_settings.ansys.structural.response_spectrum.proto\x12\x41\x61ns.protocol.analysis_settings.ansys.structural.response_spectrum\x1a$analysis_settings.ansys.common.proto\"E\n\x14ModesCombinationType\"-\n\x04\x45num\x12\x08\n\x04NONE\x10\x00\x12\x08\n\x04SRSS\x10\x01\x12\x07\n\x03\x43QC\x10\x02\x12\x08\n\x04ROSE\x10\x03\":\n\x0cSpectrumType\"*\n\x04\x45num\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06SINGLE\x10\x01\x12\x0c\n\x08MULTIPLE\x10\x02\"A\n\x13RigidResponseEffect\"*\n\x04\x45num\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06SINGLE\x10\x01\x12\x0c\n\x08MULTIPLE\x10\x02\"\xeb\x01\n\x07\x44\x61mping\x12N\n\x08\x63onstant\x18\x01 \x01(\x0b\x32<.ans.protocol.analysis_settings.ansys.common.ConstantDamping\x12\x46\n\x04\x62\x65ta\x18\x02 \x01(\x0b\x32\x38.ans.protocol.analysis_settings.ansys.common.BetaDamping\x12H\n\x05\x61lpha\x18\x03 \x01(\x0b\x32\x39.ans.protocol.analysis_settings.ansys.common.AlphaDamping\"\x9b\x02\n\x0eOutputControls\x12h\n\x06\x66ields\x18\x01 \x01(\x0b\x32X.ans.protocol.analysis_settings.ansys.structural.response_spectrum.OutputControls.Fields\x12M\n\x08settings\x18\x02 \x01(\x0b\x32;.ans.protocol.analysis_settings.ansys.common.OutputSettings\x1aP\n\x06\x46ields\x12\x0e\n\x06stress\x18\x01 \x01(\x08\x12\x0e\n\x06strain\x18\x02 \x01(\x08\x12\x10\n\x08velocity\x18\x03 \x01(\x08\x12\x14\n\x0c\x61\x63\x63\x65leration\x18\x04 \x01(\x08\"\xe1\x07\n\x08Settings\x12j\n\x0foutput_controls\x18\x01 \x01(\x0b\x32Q.ans.protocol.analysis_settings.ansys.structural.response_spectrum.OutputControls\x12P\n\rpost_settings\x18\x02 \x01(\x0b\x32\x39.ans.protocol.analysis_settings.ansys.common.PostSettings\x12[\n\x07\x64\x61mping\x18\x03 \x01(\x0b\x32J.ans.protocol.analysis_settings.ansys.structural.response_spectrum.Damping\x12P\n\rfile_controls\x18\x04 \x01(\x0b\x32\x39.ans.protocol.analysis_settings.ansys.common.FileControls\x12\x17\n\x0fnumber_of_modes\x18\x05 \x01(\x05\x12|\n\x16modes_combination_type\x18\x06 \x01(\x0e\x32\\.ans.protocol.analysis_settings.ansys.structural.response_spectrum.ModesCombinationType.Enum\x12k\n\rspectrum_type\x18\x07 \x01(\x0e\x32T.ans.protocol.analysis_settings.ansys.structural.response_spectrum.SpectrumType.Enum\x12z\n\x15rigid_response_effect\x18\x08 \x01(\x0e\x32[.ans.protocol.analysis_settings.ansys.structural.response_spectrum.RigidResponseEffect.Enum\x12\x1b\n\x13missing_mass_effect\x18\t \x01(\x08\x12!\n\x19has_rigid_response_effect\x18\n \x01(\x08\x12\x1f\n\x17missing_mass_effect_zpa\x18\x0b \x01(\x01\x12!\n\x19rigid_response_effect_zpa\x18\x0c \x01(\x01\x12(\n rigid_response_effect_freq_begin\x18\r \x01(\x01\x12&\n\x1erigid_response_effect_freq_end\x18\x0e \x01(\x01\x12\x12\n\nsend_ecalc\x18\x0f \x01(\x08\x42\x44H\x03\xaa\x02?Ans.Protocol.AnalysisSettings.ANSYS.Structural.ResponseSpectrumb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'analysis_settings.ansys.structural.response_spectrum_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\003\252\002?Ans.Protocol.AnalysisSettings.ANSYS.Structural.ResponseSpectrum'
  _MODESCOMBINATIONTYPE._serialized_start=167
  _MODESCOMBINATIONTYPE._serialized_end=236
  _MODESCOMBINATIONTYPE_ENUM._serialized_start=191
  _MODESCOMBINATIONTYPE_ENUM._serialized_end=236
  _SPECTRUMTYPE._serialized_start=238
  _SPECTRUMTYPE._serialized_end=296
  _SPECTRUMTYPE_ENUM._serialized_start=254
  _SPECTRUMTYPE_ENUM._serialized_end=296
  _RIGIDRESPONSEEFFECT._serialized_start=298
  _RIGIDRESPONSEEFFECT._serialized_end=363
  _RIGIDRESPONSEEFFECT_ENUM._serialized_start=254
  _RIGIDRESPONSEEFFECT_ENUM._serialized_end=296
  _DAMPING._serialized_start=366
  _DAMPING._serialized_end=601
  _OUTPUTCONTROLS._serialized_start=604
  _OUTPUTCONTROLS._serialized_end=887
  _OUTPUTCONTROLS_FIELDS._serialized_start=807
  _OUTPUTCONTROLS_FIELDS._serialized_end=887
  _SETTINGS._serialized_start=890
  _SETTINGS._serialized_end=1883
# @@protoc_insertion_point(module_scope)
