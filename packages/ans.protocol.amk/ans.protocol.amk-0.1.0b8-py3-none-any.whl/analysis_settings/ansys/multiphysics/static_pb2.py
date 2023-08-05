# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: analysis_settings.ansys.multiphysics.static.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from analysis_settings.ansys import common_pb2 as analysis__settings_dot_ansys_dot_common__pb2
from analysis_settings.ansys import structural_pb2 as analysis__settings_dot_ansys_dot_structural__pb2
from analysis_settings.ansys import additive_pb2 as analysis__settings_dot_ansys_dot_additive__pb2
from common import quantity_pb2 as common_dot_quantity__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1analysis_settings.ansys.multiphysics.static.proto\x12\x39\x61ns.protocol.analysis_settings.ansys.multiphysics.static_\x1a$analysis_settings.ansys.common.proto\x1a(analysis_settings.ansys.structural.proto\x1a&analysis_settings.ansys.additive.proto\x1a\x15\x63ommon.quantity.proto\"\xd8\x01\n\x1bNonlinearAdaptivityControls\x12\x19\n\x11has_mesh_criteria\x18\x01 \x01(\x08\x12\x1b\n\x13num_sculpted_layers\x18\x02 \x01(\x05\x12\x16\n\x0e\x62oundary_angle\x18\x03 \x01(\x01\x12\x1a\n\x12remeshing_gradient\x18\x04 \x01(\x05\x12\x19\n\x11global_size_ratio\x18\x05 \x01(\x01\x12\x18\n\x10\x65\x64ge_split_angle\x18\x06 \x01(\x01\x12\x18\n\x10local_size_ratio\x18\x07 \x01(\x01\"\x9a\x03\n\x0eSolverControls\x12J\n\x04type\x18\x01 \x01(\x0e\x32<.ans.protocol.analysis_settings.ansys.common.SolverType.Enum\x12N\n\x0cweak_springs\x18\x02 \x01(\x0b\x32\x38.ans.protocol.analysis_settings.ansys.common.WeakSprings\x12\x19\n\x11large_deformation\x18\x03 \x01(\x08\x12`\n\x13newton_raphson_type\x18\x04 \x01(\x0e\x32\x43.ans.protocol.analysis_settings.ansys.common.NewtonRaphsonType.Enum\x12\x16\n\x0e\x66racture_solve\x18\x05 \x01(\x08\x12W\n\x0epivot_checking\x18\x06 \x01(\x0e\x32?.ans.protocol.analysis_settings.ansys.common.PivotChecking.Enum\"\xfd\x02\n\x0eOutputControls\x12`\n\x06\x66ields\x18\x01 \x01(\x0b\x32P.ans.protocol.analysis_settings.ansys.multiphysics.static_.OutputControls.Fields\x12M\n\x08settings\x18\x02 \x01(\x0b\x32;.ans.protocol.analysis_settings.ansys.common.OutputSettings\x1a\xb9\x01\n\x06\x46ields\x12\x0e\n\x06stress\x18\x01 \x01(\x08\x12\x0e\n\x06strain\x18\x02 \x01(\x08\x12\x0f\n\x07\x63ontact\x18\x03 \x01(\x08\x12\x11\n\treactions\x18\x04 \x01(\x08\x12\x13\n\x0bmax_results\x18\x05 \x01(\x08\x12\x14\n\x0cgeneral_misc\x18\x06 \x01(\x08\x12\x10\n\x08\x66racture\x18\x07 \x01(\x08\x12\x14\n\x0c\x65uler_angles\x18\x08 \x01(\x08\x12\x18\n\x10\x65lement_energies\x18\t \x01(\x08\"\xc1\x05\n\x0bStepControl\x12P\n\rstep_settings\x18\x01 \x01(\x0b\x32\x39.ans.protocol.analysis_settings.ansys.common.StepSettings\x12\x16\n\x0einertia_relief\x18\x02 \x01(\x08\x12P\n\rtime_stepping\x18\x03 \x01(\x0b\x32\x39.ans.protocol.analysis_settings.ansys.common.TimeStepping\x12g\n\x1bnonlinear_solution_controls\x18\x04 \x01(\x0b\x32\x42.ans.protocol.analysis_settings.ansys.structural.NonlinearControls\x12\x62\n\x0foutput_controls\x18\x05 \x01(\x0b\x32I.ans.protocol.analysis_settings.ansys.multiphysics.static_.OutputControls\x12V\n\x0e\x63reep_controls\x18\x06 \x01(\x0b\x32>.ans.protocol.analysis_settings.ansys.structural.CreepSettings\x12}\n\x1dnonlinear_adaptivity_controls\x18\x07 \x01(\x0b\x32V.ans.protocol.analysis_settings.ansys.multiphysics.static_.NonlinearAdaptivityControls\x12R\n\radditive_step\x18\x08 \x01(\x0b\x32;.ans.protocol.analysis_settings.ansys.additive.SequenceStep\"\x9b\x02\n\x1d\x41\x64\x64itiveManufacturingControls\x12\x45\n\x15reference_temperature\x18\x01 \x01(\x0b\x32&.ans.protocol.common.quantity.Quantity\x12\x17\n\x0flayers_to_build\x18\x02 \x01(\x05\x12L\n\x1c\x64irectional_cutoff_step_size\x18\x03 \x01(\x0b\x32&.ans.protocol.common.quantity.Quantity\x12L\n\x1c\x64irectional_cutoff_direction\x18\x04 \x01(\x0b\x32&.ans.protocol.common.quantity.Quantity\"\xcb\x07\n\x08Settings\x12]\n\rstep_controls\x18\x01 \x03(\x0b\x32\x46.ans.protocol.analysis_settings.ansys.multiphysics.static_.StepControl\x12P\n\rpost_settings\x18\x02 \x01(\x0b\x32\x39.ans.protocol.analysis_settings.ansys.common.PostSettings\x12\x62\n\x0fsolver_controls\x18\x03 \x01(\x0b\x32I.ans.protocol.analysis_settings.ansys.multiphysics.static_.SolverControls\x12P\n\rfile_controls\x18\x04 \x01(\x0b\x32\x39.ans.protocol.analysis_settings.ansys.common.FileControls\x12X\n\x11\x66racture_controls\x18\x05 \x01(\x0b\x32=.ans.protocol.analysis_settings.ansys.common.FractureSettings\x12Z\n\x10restart_controls\x18\x06 \x01(\x0b\x32@.ans.protocol.analysis_settings.ansys.structural.RestartControls\x12Z\n\x10restart_analysis\x18\x07 \x01(\x0b\x32@.ans.protocol.analysis_settings.ansys.structural.RestartAnalysis\x12\x62\n\x16rotordynamics_settings\x18\x08 \x01(\x0b\x32\x42.ans.protocol.analysis_settings.ansys.common.RotordynamicsSettings\x12m\n\x1cglobal_reference_temperature\x18\t \x01(\x0b\x32G.ans.protocol.analysis_settings.ansys.common.GlobalReferenceTemperature\x12s\n\x11\x61\x64\x64itive_controls\x18\n \x01(\x0b\x32X.ans.protocol.analysis_settings.ansys.multiphysics.static_.AdditiveManufacturingControlsB<H\x03\xaa\x02\x37\x41ns.Protocol.AnalysisSettings.ANSYS.Multiphysics.Staticb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'analysis_settings.ansys.multiphysics.static_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'H\003\252\0027Ans.Protocol.AnalysisSettings.ANSYS.Multiphysics.Static'
  _NONLINEARADAPTIVITYCONTROLS._serialized_start=256
  _NONLINEARADAPTIVITYCONTROLS._serialized_end=472
  _SOLVERCONTROLS._serialized_start=475
  _SOLVERCONTROLS._serialized_end=885
  _OUTPUTCONTROLS._serialized_start=888
  _OUTPUTCONTROLS._serialized_end=1269
  _OUTPUTCONTROLS_FIELDS._serialized_start=1084
  _OUTPUTCONTROLS_FIELDS._serialized_end=1269
  _STEPCONTROL._serialized_start=1272
  _STEPCONTROL._serialized_end=1977
  _ADDITIVEMANUFACTURINGCONTROLS._serialized_start=1980
  _ADDITIVEMANUFACTURINGCONTROLS._serialized_end=2263
  _SETTINGS._serialized_start=2266
  _SETTINGS._serialized_end=3237
# @@protoc_insertion_point(module_scope)
