# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndata.proto\x12\x0e\x63om.learn.demo\".\n\x04\x44\x61ta\x12\x0b\n\x03min\x18\x02 \x01(\x05\x12\x0b\n\x03max\x18\x03 \x01(\x05\x12\x0c\n\x04PM25\x18\x04 \x01(\x05\"\x10\n\x02IP\x12\n\n\x02IP\x18\x01 \x01(\t\">\n\x08\x44\x61taList\x12#\n\x05\x64\x61tas\x18\x01 \x03(\x0b\x32\x14.com.learn.demo.Data\x12\r\n\x05situs\x18\x02 \x01(\t2I\n\x08\x44oFormat\x12=\n\x0bget_Weather\x12\x12.com.learn.demo.IP\x1a\x18.com.learn.demo.DataList\"\x00\x62\x06proto3')



_DATA = DESCRIPTOR.message_types_by_name['Data']
_IP = DESCRIPTOR.message_types_by_name['IP']
_DATALIST = DESCRIPTOR.message_types_by_name['DataList']
Data = _reflection.GeneratedProtocolMessageType('Data', (_message.Message,), {
  'DESCRIPTOR' : _DATA,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:com.learn.demo.Data)
  })
_sym_db.RegisterMessage(Data)

IP = _reflection.GeneratedProtocolMessageType('IP', (_message.Message,), {
  'DESCRIPTOR' : _IP,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:com.learn.demo.IP)
  })
_sym_db.RegisterMessage(IP)

DataList = _reflection.GeneratedProtocolMessageType('DataList', (_message.Message,), {
  'DESCRIPTOR' : _DATALIST,
  '__module__' : 'data_pb2'
  # @@protoc_insertion_point(class_scope:com.learn.demo.DataList)
  })
_sym_db.RegisterMessage(DataList)

_DOFORMAT = DESCRIPTOR.services_by_name['DoFormat']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DATA._serialized_start=30
  _DATA._serialized_end=76
  _IP._serialized_start=78
  _IP._serialized_end=94
  _DATALIST._serialized_start=96
  _DATALIST._serialized_end=158
  _DOFORMAT._serialized_start=160
  _DOFORMAT._serialized_end=233
# @@protoc_insertion_point(module_scope)
