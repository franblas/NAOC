from ..server.regions_pak import regions_pak

def region_list_request_handler(packet,gameclient):
  return regions_pak()
