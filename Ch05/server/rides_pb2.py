# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: server/rides.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12server/rides.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"$\n\x08Location\x12\x0b\n\x03lat\x18\x01 \x01(\x01\x12\x0b\n\x03lng\x18\x02 \x01(\x01\"e\n\x0cTrackRequest\x12\x0e\n\x06\x63\x61r_id\x18\x01 \x01(\x03\x12(\n\x04time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x1b\n\x08location\x18\x03 \x01(\x0b\x32\t.Location\"\x1e\n\rTrackResponse\x12\r\n\x05\x63ount\x18\x01 \x01(\x04\"\xa8\x01\n\x0cStartRequest\x12\x0e\n\x06\x63\x61r_id\x18\x01 \x01(\x03\x12\x11\n\tdriver_id\x18\x02 \x01(\t\x12\x15\n\rpassenger_ids\x18\x03 \x03(\t\x12\x17\n\x04type\x18\x04 \x01(\x0e\x32\t.RideType\x12\x1b\n\x08location\x18\x05 \x01(\x0b\x32\t.Location\x12(\n\x04time\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x1b\n\rStartResponse\x12\n\n\x02id\x18\x01 \x01(\t*!\n\x08RideType\x12\x0b\n\x07REGULAR\x10\x00\x12\x08\n\x04POOL\x10\x01\x32]\n\x05Rides\x12(\n\x05Start\x12\r.StartRequest\x1a\x0e.StartResponse\"\x00\x12*\n\x05Track\x12\r.TrackRequest\x1a\x0e.TrackResponse\"\x00(\x01\x62\x06proto3')

_RIDETYPE = DESCRIPTOR.enum_types_by_name['RideType']
RideType = enum_type_wrapper.EnumTypeWrapper(_RIDETYPE)
REGULAR = 0
POOL = 1


_LOCATION = DESCRIPTOR.message_types_by_name['Location']
_TRACKREQUEST = DESCRIPTOR.message_types_by_name['TrackRequest']
_TRACKRESPONSE = DESCRIPTOR.message_types_by_name['TrackResponse']
_STARTREQUEST = DESCRIPTOR.message_types_by_name['StartRequest']
_STARTRESPONSE = DESCRIPTOR.message_types_by_name['StartResponse']
Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), {
  'DESCRIPTOR' : _LOCATION,
  '__module__' : 'server.rides_pb2'
  # @@protoc_insertion_point(class_scope:Location)
  })
_sym_db.RegisterMessage(Location)

TrackRequest = _reflection.GeneratedProtocolMessageType('TrackRequest', (_message.Message,), {
  'DESCRIPTOR' : _TRACKREQUEST,
  '__module__' : 'server.rides_pb2'
  # @@protoc_insertion_point(class_scope:TrackRequest)
  })
_sym_db.RegisterMessage(TrackRequest)

TrackResponse = _reflection.GeneratedProtocolMessageType('TrackResponse', (_message.Message,), {
  'DESCRIPTOR' : _TRACKRESPONSE,
  '__module__' : 'server.rides_pb2'
  # @@protoc_insertion_point(class_scope:TrackResponse)
  })
_sym_db.RegisterMessage(TrackResponse)

StartRequest = _reflection.GeneratedProtocolMessageType('StartRequest', (_message.Message,), {
  'DESCRIPTOR' : _STARTREQUEST,
  '__module__' : 'server.rides_pb2'
  # @@protoc_insertion_point(class_scope:StartRequest)
  })
_sym_db.RegisterMessage(StartRequest)

StartResponse = _reflection.GeneratedProtocolMessageType('StartResponse', (_message.Message,), {
  'DESCRIPTOR' : _STARTRESPONSE,
  '__module__' : 'server.rides_pb2'
  # @@protoc_insertion_point(class_scope:StartResponse)
  })
_sym_db.RegisterMessage(StartResponse)

_RIDES = DESCRIPTOR.services_by_name['Rides']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _RIDETYPE._serialized_start=428
  _RIDETYPE._serialized_end=461
  _LOCATION._serialized_start=55
  _LOCATION._serialized_end=91
  _TRACKREQUEST._serialized_start=93
  _TRACKREQUEST._serialized_end=194
  _TRACKRESPONSE._serialized_start=196
  _TRACKRESPONSE._serialized_end=226
  _STARTREQUEST._serialized_start=229
  _STARTREQUEST._serialized_end=397
  _STARTRESPONSE._serialized_start=399
  _STARTRESPONSE._serialized_end=426
  _RIDES._serialized_start=463
  _RIDES._serialized_end=556
# @@protoc_insertion_point(module_scope)
