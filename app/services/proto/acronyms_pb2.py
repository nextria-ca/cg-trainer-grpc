# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: acronyms.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'acronyms.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x61\x63ronyms.proto\x12\x08\x61\x63ronyms\x1a\x1fgoogle/protobuf/timestamp.proto\"\x17\n\tIdRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x07\n\x05\x45mpty\"\xbd\x01\n\x07\x41\x63ronym\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nacronym_en\x18\x02 \x01(\t\x12\x12\n\nacronym_fr\x18\x03 \x01(\t\x12\x0f\n\x07text_en\x18\x04 \x01(\t\x12\x0f\n\x07text_fr\x18\x05 \x01(\t\x12-\n\tcreate_dt\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12-\n\tupdate_dt\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"P\n\x15\x41\x63ronymWithTrainsetId\x12\"\n\x07\x61\x63ronym\x18\x01 \x01(\x0b\x32\x11.acronyms.Acronym\x12\x13\n\x0btrainset_id\x18\x02 \x01(\x05\"J\n\x13ModelWithTrainsetId\x12\x1e\n\x05model\x18\x01 \x01(\x0b\x32\x0f.acronyms.Model\x12\x13\n\x0btrainset_id\x18\x02 \x01(\x05\"C\n\x15TrainsetIdWithModelId\x12\x13\n\x0btrainset_id\x18\x01 \x01(\x05\x12\x15\n\rbase_model_id\x18\x02 \x01(\x05\"\xc9\x01\n\x10\x41\x63ronymTrainData\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nacronym_id\x18\x02 \x01(\x05\x12\x13\n\x0bprovided_by\x18\x03 \x01(\t\x12\x1f\n\x17generated_bytrainset_id\x18\x04 \x01(\x05\x12\x0f\n\x07text_en\x18\x05 \x01(\t\x12\x0f\n\x07text_fr\x18\x06 \x01(\t\x12\x0e\n\x06reason\x18\x07 \x01(\t\x12-\n\tcreate_dt\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"j\n\x0fTrainsetContent\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x13\n\x0btrainset_id\x18\x02 \x01(\x05\x12\x12\n\nacronym_id\x18\x03 \x01(\x05\x12\x14\n\x0ctraindata_id\x18\x04 \x01(\x05\x12\x0c\n\x04role\x18\x05 \x01(\t\"\xdb\x01\n\x08Trainset\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x10\n\x08last_run\x18\x02 \x01(\t\x12\x1a\n\x12\x62\x61se_model_inst_id\x18\x03 \x01(\x05\x12\x19\n\x11new_model_inst_id\x18\x04 \x01(\x05\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12-\n\tcreate_dt\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07version\x18\x07 \x01(\t\x12\x12\n\ncreated_by\x18\x08 \x01(\t\x12\x11\n\tis_active\x18\t \x01(\x08\"\xa8\x01\n\x05Model\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\t\x12-\n\tcreate_dt\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ncheckpoint\x18\x05 \x01(\x05\x12\r\n\x05score\x18\x06 \x01(\x02\x12\x12\n\ndepartment\x18\x07 \x01(\t\x12\x0e\n\x06status\x18\x08 \x01(\t\".\n\x0b\x41\x63ronymList\x12\x1f\n\x04list\x18\x01 \x03(\x0b\x32\x11.acronyms.Acronym\"@\n\x14\x41\x63ronymTrainDataList\x12(\n\x04list\x18\x01 \x03(\x0b\x32\x1a.acronyms.AcronymTrainData\">\n\x13TrainsetContentList\x12\'\n\x04list\x18\x01 \x03(\x0b\x32\x19.acronyms.TrainsetContent\"0\n\x0cTrainsetList\x12 \n\x04list\x18\x01 \x03(\x0b\x32\x12.acronyms.Trainset\"*\n\tModelList\x12\x1d\n\x04list\x18\x01 \x03(\x0b\x32\x0f.acronyms.Model2\xab\x03\n\x0e\x41\x63ronymService\x12\x30\n\x06\x63reate\x12\x11.acronyms.Acronym\x1a\x11.acronyms.Acronym\"\x00\x12\x33\n\x07get_all\x12\x0f.acronyms.Empty\x1a\x15.acronyms.AcronymList\"\x00\x12\x30\n\x06update\x12\x11.acronyms.Acronym\x1a\x11.acronyms.Acronym\"\x00\x12<\n\x06\x64\x65lete\x12\x1f.acronyms.AcronymWithTrainsetId\x1a\x0f.acronyms.Empty\"\x00\x12\x35\n\tget_by_id\x12\x13.acronyms.IdRequest\x1a\x11.acronyms.Acronym\"\x00\x12G\n\x0f\x61\x64\x64_to_trainset\x12\x1f.acronyms.AcronymWithTrainsetId\x1a\x11.acronyms.Acronym\"\x00\x12\x42\n\x12get_by_trainset_id\x12\x13.acronyms.IdRequest\x1a\x15.acronyms.AcronymList\"\x00\x32\xd8\x02\n\x17\x41\x63ronymTrainDataService\x12\x42\n\x06\x63reate\x12\x1a.acronyms.AcronymTrainData\x1a\x1a.acronyms.AcronymTrainData\"\x00\x12<\n\x07get_all\x12\x0f.acronyms.Empty\x1a\x1e.acronyms.AcronymTrainDataList\"\x00\x12\x42\n\x06update\x12\x1a.acronyms.AcronymTrainData\x1a\x1a.acronyms.AcronymTrainData\"\x00\x12\x37\n\x06\x64\x65lete\x12\x1a.acronyms.AcronymTrainData\x1a\x0f.acronyms.Empty\"\x00\x12>\n\tget_by_id\x12\x13.acronyms.IdRequest\x1a\x1a.acronyms.AcronymTrainData\"\x00\x32\xe1\x03\n\x0fTrainsetService\x12\x32\n\x06\x63reate\x12\x12.acronyms.Trainset\x1a\x12.acronyms.Trainset\"\x00\x12\x34\n\x07get_all\x12\x0f.acronyms.Empty\x1a\x16.acronyms.TrainsetList\"\x00\x12\x32\n\x06update\x12\x12.acronyms.Trainset\x1a\x12.acronyms.Trainset\"\x00\x12/\n\x06\x64\x65lete\x12\x12.acronyms.Trainset\x1a\x0f.acronyms.Empty\"\x00\x12\x36\n\tget_by_id\x12\x13.acronyms.IdRequest\x1a\x12.acronyms.Trainset\"\x00\x12;\n\x0fsave_checkpoint\x12\x12.acronyms.Trainset\x1a\x12.acronyms.Trainset\"\x00\x12\x43\n\nset_active\x12\x1f.acronyms.TrainsetIdWithModelId\x1a\x12.acronyms.Trainset\"\x00\x12\x45\n\x14get_by_base_model_id\x12\x13.acronyms.IdRequest\x1a\x16.acronyms.TrainsetList\"\x00\x32\xd0\x02\n\x16TrainsetContentService\x12@\n\x06\x63reate\x12\x19.acronyms.TrainsetContent\x1a\x19.acronyms.TrainsetContent\"\x00\x12;\n\x07get_all\x12\x0f.acronyms.Empty\x1a\x1d.acronyms.TrainsetContentList\"\x00\x12@\n\x06update\x12\x19.acronyms.TrainsetContent\x1a\x19.acronyms.TrainsetContent\"\x00\x12\x36\n\x06\x64\x65lete\x12\x19.acronyms.TrainsetContent\x1a\x0f.acronyms.Empty\"\x00\x12=\n\tget_by_id\x12\x13.acronyms.IdRequest\x1a\x19.acronyms.TrainsetContent\"\x00\x32\x8e\x02\n\x0cModelService\x12,\n\x06\x63reate\x12\x0f.acronyms.Model\x1a\x0f.acronyms.Model\"\x00\x12\x31\n\x07get_all\x12\x0f.acronyms.Empty\x1a\x13.acronyms.ModelList\"\x00\x12,\n\x06update\x12\x0f.acronyms.Model\x1a\x0f.acronyms.Model\"\x00\x12:\n\x06\x64\x65lete\x12\x1d.acronyms.ModelWithTrainsetId\x1a\x0f.acronyms.Empty\"\x00\x12\x33\n\tget_by_id\x12\x13.acronyms.IdRequest\x1a\x0f.acronyms.Model\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'acronyms_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_IDREQUEST']._serialized_start=61
  _globals['_IDREQUEST']._serialized_end=84
  _globals['_EMPTY']._serialized_start=86
  _globals['_EMPTY']._serialized_end=93
  _globals['_ACRONYM']._serialized_start=96
  _globals['_ACRONYM']._serialized_end=285
  _globals['_ACRONYMWITHTRAINSETID']._serialized_start=287
  _globals['_ACRONYMWITHTRAINSETID']._serialized_end=367
  _globals['_MODELWITHTRAINSETID']._serialized_start=369
  _globals['_MODELWITHTRAINSETID']._serialized_end=443
  _globals['_TRAINSETIDWITHMODELID']._serialized_start=445
  _globals['_TRAINSETIDWITHMODELID']._serialized_end=512
  _globals['_ACRONYMTRAINDATA']._serialized_start=515
  _globals['_ACRONYMTRAINDATA']._serialized_end=716
  _globals['_TRAINSETCONTENT']._serialized_start=718
  _globals['_TRAINSETCONTENT']._serialized_end=824
  _globals['_TRAINSET']._serialized_start=827
  _globals['_TRAINSET']._serialized_end=1046
  _globals['_MODEL']._serialized_start=1049
  _globals['_MODEL']._serialized_end=1217
  _globals['_ACRONYMLIST']._serialized_start=1219
  _globals['_ACRONYMLIST']._serialized_end=1265
  _globals['_ACRONYMTRAINDATALIST']._serialized_start=1267
  _globals['_ACRONYMTRAINDATALIST']._serialized_end=1331
  _globals['_TRAINSETCONTENTLIST']._serialized_start=1333
  _globals['_TRAINSETCONTENTLIST']._serialized_end=1395
  _globals['_TRAINSETLIST']._serialized_start=1397
  _globals['_TRAINSETLIST']._serialized_end=1445
  _globals['_MODELLIST']._serialized_start=1447
  _globals['_MODELLIST']._serialized_end=1489
  _globals['_ACRONYMSERVICE']._serialized_start=1492
  _globals['_ACRONYMSERVICE']._serialized_end=1919
  _globals['_ACRONYMTRAINDATASERVICE']._serialized_start=1922
  _globals['_ACRONYMTRAINDATASERVICE']._serialized_end=2266
  _globals['_TRAINSETSERVICE']._serialized_start=2269
  _globals['_TRAINSETSERVICE']._serialized_end=2750
  _globals['_TRAINSETCONTENTSERVICE']._serialized_start=2753
  _globals['_TRAINSETCONTENTSERVICE']._serialized_end=3089
  _globals['_MODELSERVICE']._serialized_start=3092
  _globals['_MODELSERVICE']._serialized_end=3362
# @@protoc_insertion_point(module_scope)
