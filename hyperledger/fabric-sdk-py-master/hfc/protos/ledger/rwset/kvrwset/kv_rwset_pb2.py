# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hfc/protos/ledger/rwset/kvrwset/kv_rwset.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hfc/protos/ledger/rwset/kvrwset/kv_rwset.proto',
  package='kvrwset',
  syntax='proto3',
  serialized_pb=_b('\n.hfc/protos/ledger/rwset/kvrwset/kv_rwset.proto\x12\x07kvrwset\"\x80\x01\n\x07KVRWSet\x12\x1e\n\x05reads\x18\x01 \x03(\x0b\x32\x0f.kvrwset.KVRead\x12\x33\n\x12range_queries_info\x18\x02 \x03(\x0b\x32\x17.kvrwset.RangeQueryInfo\x12 \n\x06writes\x18\x03 \x03(\x0b\x32\x10.kvrwset.KVWrite\"e\n\x0bHashedRWSet\x12)\n\x0chashed_reads\x18\x01 \x03(\x0b\x32\x13.kvrwset.KVReadHash\x12+\n\rhashed_writes\x18\x02 \x03(\x0b\x32\x14.kvrwset.KVWriteHash\"8\n\x06KVRead\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x07version\x18\x02 \x01(\x0b\x32\x10.kvrwset.Version\"8\n\x07KVWrite\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x11\n\tis_delete\x18\x02 \x01(\x08\x12\r\n\x05value\x18\x03 \x01(\x0c\"A\n\nKVReadHash\x12\x10\n\x08key_hash\x18\x01 \x01(\x0c\x12!\n\x07version\x18\x02 \x01(\x0b\x32\x10.kvrwset.Version\"F\n\x0bKVWriteHash\x12\x10\n\x08key_hash\x18\x01 \x01(\x0c\x12\x11\n\tis_delete\x18\x02 \x01(\x08\x12\x12\n\nvalue_hash\x18\x03 \x01(\x0c\",\n\x07Version\x12\x11\n\tblock_num\x18\x01 \x01(\x04\x12\x0e\n\x06tx_num\x18\x02 \x01(\x04\"\xc4\x01\n\x0eRangeQueryInfo\x12\x11\n\tstart_key\x18\x01 \x01(\t\x12\x0f\n\x07\x65nd_key\x18\x02 \x01(\t\x12\x15\n\ritr_exhausted\x18\x03 \x01(\x08\x12(\n\traw_reads\x18\x04 \x01(\x0b\x32\x13.kvrwset.QueryReadsH\x00\x12?\n\x13reads_merkle_hashes\x18\x05 \x01(\x0b\x32 .kvrwset.QueryReadsMerkleSummaryH\x00\x42\x0c\n\nreads_info\"/\n\nQueryReads\x12!\n\x08kv_reads\x18\x01 \x03(\x0b\x32\x0f.kvrwset.KVRead\"Z\n\x17QueryReadsMerkleSummary\x12\x12\n\nmax_degree\x18\x01 \x01(\r\x12\x11\n\tmax_level\x18\x02 \x01(\r\x12\x18\n\x10max_level_hashes\x18\x03 \x03(\x0c\x42o\n2org.hyperledger.fabric.protos.ledger.rwset.kvrwsetZ9github.com/hyperledger/fabric/protos/ledger/rwset/kvrwsetb\x06proto3')
)




_KVRWSET = _descriptor.Descriptor(
  name='KVRWSet',
  full_name='kvrwset.KVRWSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='reads', full_name='kvrwset.KVRWSet.reads', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='range_queries_info', full_name='kvrwset.KVRWSet.range_queries_info', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='writes', full_name='kvrwset.KVRWSet.writes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=188,
)


_HASHEDRWSET = _descriptor.Descriptor(
  name='HashedRWSet',
  full_name='kvrwset.HashedRWSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hashed_reads', full_name='kvrwset.HashedRWSet.hashed_reads', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hashed_writes', full_name='kvrwset.HashedRWSet.hashed_writes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=190,
  serialized_end=291,
)


_KVREAD = _descriptor.Descriptor(
  name='KVRead',
  full_name='kvrwset.KVRead',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='kvrwset.KVRead.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='kvrwset.KVRead.version', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=293,
  serialized_end=349,
)


_KVWRITE = _descriptor.Descriptor(
  name='KVWrite',
  full_name='kvrwset.KVWrite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='kvrwset.KVWrite.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_delete', full_name='kvrwset.KVWrite.is_delete', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='kvrwset.KVWrite.value', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=351,
  serialized_end=407,
)


_KVREADHASH = _descriptor.Descriptor(
  name='KVReadHash',
  full_name='kvrwset.KVReadHash',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_hash', full_name='kvrwset.KVReadHash.key_hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='kvrwset.KVReadHash.version', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=409,
  serialized_end=474,
)


_KVWRITEHASH = _descriptor.Descriptor(
  name='KVWriteHash',
  full_name='kvrwset.KVWriteHash',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key_hash', full_name='kvrwset.KVWriteHash.key_hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_delete', full_name='kvrwset.KVWriteHash.is_delete', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_hash', full_name='kvrwset.KVWriteHash.value_hash', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=476,
  serialized_end=546,
)


_VERSION = _descriptor.Descriptor(
  name='Version',
  full_name='kvrwset.Version',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_num', full_name='kvrwset.Version.block_num', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tx_num', full_name='kvrwset.Version.tx_num', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=548,
  serialized_end=592,
)


_RANGEQUERYINFO = _descriptor.Descriptor(
  name='RangeQueryInfo',
  full_name='kvrwset.RangeQueryInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_key', full_name='kvrwset.RangeQueryInfo.start_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_key', full_name='kvrwset.RangeQueryInfo.end_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='itr_exhausted', full_name='kvrwset.RangeQueryInfo.itr_exhausted', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='raw_reads', full_name='kvrwset.RangeQueryInfo.raw_reads', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reads_merkle_hashes', full_name='kvrwset.RangeQueryInfo.reads_merkle_hashes', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='reads_info', full_name='kvrwset.RangeQueryInfo.reads_info',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=595,
  serialized_end=791,
)


_QUERYREADS = _descriptor.Descriptor(
  name='QueryReads',
  full_name='kvrwset.QueryReads',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='kv_reads', full_name='kvrwset.QueryReads.kv_reads', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=793,
  serialized_end=840,
)


_QUERYREADSMERKLESUMMARY = _descriptor.Descriptor(
  name='QueryReadsMerkleSummary',
  full_name='kvrwset.QueryReadsMerkleSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max_degree', full_name='kvrwset.QueryReadsMerkleSummary.max_degree', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_level', full_name='kvrwset.QueryReadsMerkleSummary.max_level', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_level_hashes', full_name='kvrwset.QueryReadsMerkleSummary.max_level_hashes', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=842,
  serialized_end=932,
)

_KVRWSET.fields_by_name['reads'].message_type = _KVREAD
_KVRWSET.fields_by_name['range_queries_info'].message_type = _RANGEQUERYINFO
_KVRWSET.fields_by_name['writes'].message_type = _KVWRITE
_HASHEDRWSET.fields_by_name['hashed_reads'].message_type = _KVREADHASH
_HASHEDRWSET.fields_by_name['hashed_writes'].message_type = _KVWRITEHASH
_KVREAD.fields_by_name['version'].message_type = _VERSION
_KVREADHASH.fields_by_name['version'].message_type = _VERSION
_RANGEQUERYINFO.fields_by_name['raw_reads'].message_type = _QUERYREADS
_RANGEQUERYINFO.fields_by_name['reads_merkle_hashes'].message_type = _QUERYREADSMERKLESUMMARY
_RANGEQUERYINFO.oneofs_by_name['reads_info'].fields.append(
  _RANGEQUERYINFO.fields_by_name['raw_reads'])
_RANGEQUERYINFO.fields_by_name['raw_reads'].containing_oneof = _RANGEQUERYINFO.oneofs_by_name['reads_info']
_RANGEQUERYINFO.oneofs_by_name['reads_info'].fields.append(
  _RANGEQUERYINFO.fields_by_name['reads_merkle_hashes'])
_RANGEQUERYINFO.fields_by_name['reads_merkle_hashes'].containing_oneof = _RANGEQUERYINFO.oneofs_by_name['reads_info']
_QUERYREADS.fields_by_name['kv_reads'].message_type = _KVREAD
DESCRIPTOR.message_types_by_name['KVRWSet'] = _KVRWSET
DESCRIPTOR.message_types_by_name['HashedRWSet'] = _HASHEDRWSET
DESCRIPTOR.message_types_by_name['KVRead'] = _KVREAD
DESCRIPTOR.message_types_by_name['KVWrite'] = _KVWRITE
DESCRIPTOR.message_types_by_name['KVReadHash'] = _KVREADHASH
DESCRIPTOR.message_types_by_name['KVWriteHash'] = _KVWRITEHASH
DESCRIPTOR.message_types_by_name['Version'] = _VERSION
DESCRIPTOR.message_types_by_name['RangeQueryInfo'] = _RANGEQUERYINFO
DESCRIPTOR.message_types_by_name['QueryReads'] = _QUERYREADS
DESCRIPTOR.message_types_by_name['QueryReadsMerkleSummary'] = _QUERYREADSMERKLESUMMARY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

KVRWSet = _reflection.GeneratedProtocolMessageType('KVRWSet', (_message.Message,), dict(
  DESCRIPTOR = _KVRWSET,
  __module__ = 'hfc.protos.ledger.rwset.kvrwset.kv_rwset_pb2'
  # @@protoc_insertion_point(class_scope:kvrwset.KVRWSet)
  ))
_sym_db.RegisterMessage(KVRWSet)

HashedRWSet = _reflection.GeneratedProtocolMessageType('HashedRWSet', (_message.Message,), dict(
  DESCRIPTOR = _HASHEDRWSET,
  __module__ = 'hfc.protos.ledger.rwset.kvrwset.kv_rwset_pb2'
  # @@protoc_insertion_point(class_scope:kvrwset.HashedRWSet)
  ))
_sym_db.RegisterMessage(HashedRWSet)

KVRead = _reflection.GeneratedProtocolMessageType('KVRead', (_message.Message,), dict(
  DESCRIPTOR = _KVREAD,
  __module__ = 'hfc.protos.ledger.rwset.kvrwset.kv_rwset_pb2'
  # @@protoc_insertion_point(class_scope:kvrwset.KVRead)
  ))
_sym_db.RegisterMessage(KVRead)

KVWrite = _reflection.GeneratedProtocolMessageType('KVWrite', (_message.Message,), dict(
  DESCRIPTOR = _KVWRITE,
  __module__ = 'hfc.protos.ledger.rwset.kvrwset.kv_rwset_pb2'
  # @@protoc_insertion_point(class_scope:kvrwset.KVWrite)
  ))
_sym_db.RegisterMessage(KVWrite)

KVReadHash = _reflection.GeneratedProtocolMessageType('KVReadHash', (_message.Message,), dict(
  DESCRIPTOR = _KVREADHASH,
  __module__ = 'hfc.protos.ledger.rwset.kvrwset.kv_rwset_pb2'
  # @@protoc_insertion_point(class_scope:kvrwset.KVReadHash)
  ))
_sym_db.RegisterMessage(KVReadHash)

KVWriteHash = _reflection.GeneratedProtocolMessageType('KVWriteHash', (_message.Message,), dict(
  DESCRIPTOR = _KVWRITEHASH,
  __module__ = 'hfc.protos.ledger.rwset.kvrwset.kv_rwset_pb2'
  # @@protoc_insertion_point(class_scope:kvrwset.KVWriteHash)
  ))
_sym_db.RegisterMessage(KVWriteHash)

Version = _reflection.GeneratedProtocolMessageType('Version', (_message.Message,), dict(
  DESCRIPTOR = _VERSION,
  __module__ = 'hfc.protos.ledger.rwset.kvrwset.kv_rwset_pb2'
  # @@protoc_insertion_point(class_scope:kvrwset.Version)
  ))
_sym_db.RegisterMessage(Version)

RangeQueryInfo = _reflection.GeneratedProtocolMessageType('RangeQueryInfo', (_message.Message,), dict(
  DESCRIPTOR = _RANGEQUERYINFO,
  __module__ = 'hfc.protos.ledger.rwset.kvrwset.kv_rwset_pb2'
  # @@protoc_insertion_point(class_scope:kvrwset.RangeQueryInfo)
  ))
_sym_db.RegisterMessage(RangeQueryInfo)

QueryReads = _reflection.GeneratedProtocolMessageType('QueryReads', (_message.Message,), dict(
  DESCRIPTOR = _QUERYREADS,
  __module__ = 'hfc.protos.ledger.rwset.kvrwset.kv_rwset_pb2'
  # @@protoc_insertion_point(class_scope:kvrwset.QueryReads)
  ))
_sym_db.RegisterMessage(QueryReads)

QueryReadsMerkleSummary = _reflection.GeneratedProtocolMessageType('QueryReadsMerkleSummary', (_message.Message,), dict(
  DESCRIPTOR = _QUERYREADSMERKLESUMMARY,
  __module__ = 'hfc.protos.ledger.rwset.kvrwset.kv_rwset_pb2'
  # @@protoc_insertion_point(class_scope:kvrwset.QueryReadsMerkleSummary)
  ))
_sym_db.RegisterMessage(QueryReadsMerkleSummary)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n2org.hyperledger.fabric.protos.ledger.rwset.kvrwsetZ9github.com/hyperledger/fabric/protos/ledger/rwset/kvrwset'))
# @@protoc_insertion_point(module_scope)