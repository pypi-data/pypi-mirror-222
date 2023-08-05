/**
  *@file ${proto.cppFileName}.c
  *@brief generated code for ${proto.name} packet service
  *@author make_protocol.py
  *@date ${proto.genTime}
  */

/***********************************************************
        THIS FILE IS AUTOGENERATED. DO NOT MODIFY
***********************************************************/

#include "${proto.cppFileName}.h"
#include <assert.h>

//Define Standard packet IDs
% for packet in proto.packets:
%if packet.standard:
#define ${packet.globalName}_ID ${packet.packetId}
%endif
% endfor

//Define Struct IDs
% for packet in proto.structs:
#define ${packet.globalName}_ID ${packet.packetId}
% endfor

//Define packet IDs
% for packet in proto.packets:
%if not packet.standard:
#define ${packet.globalName}_ID ${packet.packetId}
%endif
% endfor

//Global descriptors
% for packet in proto.packets:
poly_packet_desc_t* ${packet.globalName};
% endfor

% for packet in proto.structs:
poly_packet_desc_t* ${packet.globalName};
% endfor

% for field in proto.fields:
poly_field_desc_t* ${field.globalName};
% endfor

//Global descriptors
% for packet in proto.packets:
poly_packet_desc_t _${packet.globalName};
% endfor

% for packet in proto.structs:
poly_packet_desc_t _${packet.globalName};
% endfor

% for field in proto.fields:
poly_field_desc_t _${field.globalName};
% endfor

poly_service_t ${proto.camelPrefix()}Packet::DESC_INDEX;
bool ${proto.cppFileName}::mDescriptorsBuilt = false;

/*******************************************************************************
  Service Functions
*******************************************************************************/

/**
  *@brief initializes ${proto.prefix}_protocol
  *@param interfaceCount number of interfaces to create
  */
${proto.cppFileName}::${proto.cppFileName}(int interfaceCount, int spoolSize)
{
  buildDescriptors();

  mRequest.build(NULL);
  mResponse.build(NULL);
  mDespool.build(NULL);

  MRT_MUTEX_CREATE(mMutex);


  //initialize core service
  poly_service_init(&mService,${len(proto.packets) + len(proto.structs)}, interfaceCount);

  //Register standard packet descriptors with the service
% for packet in proto.packets:
%if packet.standard:
  poly_service_register_desc(&mService, ${packet.globalName});
%endif
% endfor

  //Register Struct descriptors with the service
% for packet in proto.structs:
  poly_service_register_desc(&mService, ${packet.globalName});
% endfor

  //Register packet descriptors with the service
% for packet in proto.packets:
%if not packet.standard:
  poly_service_register_desc(&mService, ${packet.globalName});
%endif
% endfor

  poly_service_start(&mService, spoolSize);

}

${proto.cppFileName}::~${proto.cppFileName}()
{
  MRT_MUTEX_DELETE(mMutex);

  // poly_packet_clean(&mRequest.mPacket);
  // poly_packet_clean(&mResponse.mPacket);
  tearDown();
}

void ${proto.cppFileName}::buildDescriptors()
{
  // only allow this to be done once
  if(mDescriptorsBuilt)
    return;

    //Build Standard Packet Descriptors
    % for packet in proto.packets:
    %if packet.standard:
    ${packet.globalName} = poly_packet_desc_init(&_${packet.globalName} ,${packet.globalName}_ID,"${packet.name}", ${len(packet.fields)});
    %endif
    % endfor

    //Build Struct Descriptors
    % for packet in proto.structs:
    ${packet.globalName} = poly_packet_desc_init(&_${packet.globalName} ,${packet.globalName}_ID,"${packet.name}", ${len(packet.fields)});
    % endfor

    //Build Packet Descriptors
    % for packet in proto.packets:
    %if not packet.standard:
    ${packet.globalName} = poly_packet_desc_init(&_${packet.globalName} ,${packet.globalName}_ID,"${packet.name}", ${len(packet.fields)});
    %endif
    % endfor

    //Build Field Descriptors
  % for field in proto.fields:
    ${field.globalName} = poly_field_desc_init( &_${field.globalName} ,"${field.name}", TYPE_${field.type.upper()}, ${field.arrayLen}, ${field.format.upper()});
  % endfor

  % for packet in proto.packets:
  % if len(packet.fields) > 0:
    //Setting Field Descriptors for packet: ${packet.name}
    % for field in packet.fields:
    poly_packet_desc_add_field(${packet.globalName} , ${field.globalName} , ${str(field.isRequired).lower()} );
    % endfor
  % endif

  % endfor

  % for packet in proto.structs:
  % if len(packet.fields) > 0:
    //Setting Field Descriptors for struct: ${packet.name}
    % for field in packet.fields:
    poly_packet_desc_add_field(${packet.globalName} , ${field.globalName} , ${str(field.isRequired).lower()} );
    % endfor
  % endif

  % endfor

  /************************************************************************
                        Descriptor Index
  ************************************************************************/
  poly_service_init(&${proto.camelPrefix()}Packet::DESC_INDEX,${len(proto.packets) + len(proto.structs)}, 0);

  //Register standard packet descriptors with the service
% for packet in proto.packets:
%if packet.standard:
  poly_service_register_desc(&${proto.camelPrefix()}Packet::DESC_INDEX, ${packet.globalName});
%endif
% endfor

  //Register Struct descriptors with the service
% for packet in proto.structs:
  poly_service_register_desc(&${proto.camelPrefix()}Packet::DESC_INDEX, ${packet.globalName});
% endfor

  //Register packet descriptors with the service
% for packet in proto.packets:
%if not packet.standard:
  poly_service_register_desc(&${proto.camelPrefix()}Packet::DESC_INDEX, ${packet.globalName});
%endif
% endfor


  mDescriptorsBuilt = true;

}


void ${proto.cppFileName}::tearDown()
{
  //deinit Packet Descriptors
% for packet in proto.packets:
  ${packet.globalName} = poly_packet_desc_deinit(&_${packet.globalName});
% endfor

}

HandlerStatus_e ${proto.cppFileName}::dispatch(${proto.camelPrefix()}Packet& packet, ${proto.camelPrefix()}Packet& response)
{

  HandlerStatus_e ${proto.prefix}_status;
  logIncomingPacket(packet);

  //Dispatch packet
  switch(packet.mPacket.mDesc->mTypeId)
  {
    case ${proto.prefix.upper()}_PACKET_PING_ID:
      response.build(${proto.prefix.upper()}_PACKET_ACK);
      ${proto.prefix}_status = PingHandler(packet, response);
      break;
    case ${proto.prefix.upper()}_PACKET_ACK_ID:
      ${proto.prefix}_status = AckHandler(packet);
      break;
% for packet in proto.packets:
% if not packet.standard:
    case ${packet.globalName}_ID:
    %if packet.hasResponse:
     response.build(${packet.response.globalName});
     ${proto.prefix}_status = ${packet.name}Handler(packet , response );
    %else:
      ${proto.prefix}_status = ${packet.name}Handler(packet);
    %endif
      break;
% endif
% endfor
    default:
      //we should never get here
      assert(false);
      break;
  }

  //If this packet doe not have an explicit response and AutoAck is enabled, create an ack packet
  if(( mService.mAutoAck ) & (!response.mPacket.mBuilt) && (!(packet.mPacket.mHeader.mToken & POLY_ACK_FLAG)))
  {
    response.build(${proto.prefix.upper()}_PACKET_ACK);
  }


  //If the packet was not handled, throw it to the default handler
  if(${proto.prefix}_status == PACKET_NOT_HANDLED)
  {
    ${proto.prefix}_status = defaultHandler(packet, response);
  }


  return ${proto.prefix}_status;
}

/**
  *@brief attempts to process data in buffers and parse out packets
  */
void ${proto.cppFileName}::process()
{
  MRT_MUTEX_LOCK(mMutex);
  HandlerStatus_e ${proto.prefix}_status = PACKET_NOT_HANDLED;

  if(poly_service_try_parse(&mService, &mRequest.mPacket) == PACKET_VALID)
  {
    //if we get here, then the inner packet was built by the parser
    mRequest.mPacket.mBuilt = true;

    ${proto.prefix}_status = dispatch(mRequest,mResponse);

    //If a response has been build and the ${proto.prefix}_status was not set to ignore, we send a response on the intrface it came from
    if(( ${proto.prefix}_status == PACKET_HANDLED) && (mResponse.mPacket.mBuilt) && ((mRequest.mPacket.mHeader.mToken & POLY_ACK_FLAG)==0) )
    {
      //set response token with ack flag
			mResponse.mPacket.mHeader.mToken = mRequest.mPacket.mHeader.mToken | POLY_ACK_FLAG;

      ${proto.prefix}_status = poly_service_spool(&mService, mResponse.mPacket.mInterface, &mResponse.mPacket);

      if(${proto.prefix}_status == PACKET_SPOOLED)
      {
        mResponse.mPacket.mSpooled = true;
      }
    }

    //Clean the packets
    mRequest.clean();
    mResponse.clean();
  }

  //despool any packets ready to go out
  for(int i=0; i < mService.mInterfaceCount; i++)
  {
    if(poly_service_despool_interface(&mService.mInterfaces[i], &mDespool.mPacket))
    {
      mBufferLen = mDespool.packEncoded(mBuffer);
      txPacket(mDespool);
      logOutgoingPacket(mDespool);
      txBytes(mBuffer, mBufferLen);
    }
  }

  /*NOTE: we do not clean mDespool, because it is also referencing a packet owned by the spool which is self-cleaning*/
  MRT_MUTEX_UNLOCK(mMutex);
}


void ${proto.cppFileName}::feed(int iface, uint8_t* data, int len)
{
  MRT_MUTEX_LOCK(mMutex);

  poly_service_feed(&mService,iface,data,len);

  MRT_MUTEX_UNLOCK(mMutex);
}

HandlerStatus_e ${proto.cppFileName}::handleJSON(const char* req, int len, char* resp)
{
  ${proto.camelPrefix()}Packet packet;
  ${proto.camelPrefix()}Packet response;

  //reset states of static packets
  HandlerStatus_e ${proto.prefix}_status = PACKET_NOT_HANDLED;
  packet.mPacket.mBuilt = false;
  packet.mPacket.mSpooled = false;
  response.mPacket.mSpooled = false;
  response.mPacket.mBuilt = false;


  if(poly_service_parse_json(&mService, &packet.mPacket, req, len) == PACKET_VALID)
  {
    //if we get here, then the inner packet was built by the parser
    packet.mPacket.mBuilt = true;

    ${proto.prefix}_status = dispatch(packet,response);


    //If a response has been build and the ${proto.prefix}_status was not set to ignore, we send a response on the intrface it came from
    if(( ${proto.prefix}_status == PACKET_HANDLED) && (response.mPacket.mBuilt) )
    {
      //set response token with ack flag
			response.mPacket.mHeader.mToken = packet.mPacket.mHeader.mToken | POLY_ACK_FLAG;
      poly_packet_print_json(&response.mPacket, resp, false);
    }

    //Clean the packets
    packet.clean();
    response.clean();

  }
  else
  {
    MRT_SPRINTF(resp,"{\"Error\":\"Parsing Error\"}");
  }

  return ${proto.prefix}_status;
}



HandlerStatus_e ${proto.cppFileName}::send(int iface, ${proto.camelPrefix()}Packet& packet)
{
  MRT_MUTEX_LOCK(mMutex);
  HandlerStatus_e ${proto.prefix}_status;

  ${proto.prefix}_status = poly_service_spool(&mService, iface, &packet.mPacket);

  if(${proto.prefix}_status == PACKET_SPOOLED)
  {
    packet.mPacket.mSpooled = true;
  }

  MRT_MUTEX_UNLOCK(mMutex);
  return ${proto.prefix}_status;
}


HandlerStatus_e ${proto.cppFileName}::send(${proto.camelPrefix()}Packet& packet)
{
  return send(0, packet);
}


/*******************************************************************************
  Virtual

  Do not modify these, just subclass from the service class and override
*******************************************************************************/
/**
  *@brief Handler for receiving ping packets
  *@param ${proto.prefix}_ping ptr to incoming ping packet
  *@param ${proto.prefix}_ack ptr to repsonding ack
  *@return PACKET_HANDLED
  */
HandlerStatus_e ${proto.cppFileName}::PingHandler(${proto.camelPrefix()}Packet& ${proto.prefix}_ping, ${proto.camelPrefix()}Packet& ${proto.prefix}_ack)
{
  /* Ack token has already been set as ping token with POLY_ACK_FLAG*/
  uint32_t icd_hash = ${proto.prefix}_ping.getIcd();
  /* assert(icd_hash == ${proto.prefix.upper()}_SERVICE_HASH ); */

  return PACKET_HANDLED;
}

/**
  *@brief Handler for receiving ack packets
  *@param ${proto.prefix}_ack ptr to ack
  *@return PACKET_HANDLED
  */
HandlerStatus_e ${proto.cppFileName}::AckHandler(${proto.camelPrefix()}Packet& ${proto.prefix}_ack)
{
  return PACKET_HANDLED;
}

% for packet in proto.packets:
%if not packet.standard:
%if not packet.hasResponse:
/**
  *@brief Handler for receiving ${packet.name} packets
  *@param ${packet.name} incoming ${packet.name} packet
  *@return handling ${proto.prefix}_status
  */
HandlerStatus_e ${proto.cppFileName}::${packet.name}Handler(${proto.camelPrefix()}Packet& ${proto.prefix}_${packet.name})
%else:
/**
  *@brief Handler for receiving ${packet.name} packets
  *@param ${packet.name} incoming ${packet.name} packet
  *@param ${packet.response.name} ${packet.response.name} packet to respond with
  *@return handling ${proto.prefix}_status
  */
HandlerStatus_e ${proto.cppFileName}::${packet.name}Handler(${proto.camelPrefix()}Packet& ${proto.prefix}_${packet.name}, ${proto.camelPrefix()}Packet& ${proto.prefix}_${packet.response.name})
%endif
{
  /*  Get Required Fields in packet */
% for field in packet.fields:
%if field.isRequired:
  //${field.getDeclaration()};  //${field.desc}
%endif
%endfor

% for field in packet.fields:
%if field.isRequired:
  %if field.isArray:
  //${proto.prefix}_get${field.camel()}(${proto.prefix}_${packet.name}, ${field.name});
  %else:
  //${field.name} = ${proto.prefix}_get${field.camel()}(${proto.prefix}_${packet.name});
  %endif
%endif
% endfor
%if packet.hasResponse:
  /*    Set required Fields in response  */
% for field in packet.response.fields:
  //${proto.prefix}_set${field.camel()}(${proto.prefix}_${packet.response.name}, value );  //${field.desc}
%endfor
%endif


  /* NOTE : This function should not be modified! If needed,  It should be overridden in the application code */

  return PACKET_NOT_HANDLED;
}

%endif
% endfor


/**
  *@brief catch-all handler for any packet not yet handled
  *@param ${proto.prefix}_packet ptr to incoming message
  *@param ${proto.prefix}_response ptr to response
  *@return handling ${proto.prefix}_status
  */
HandlerStatus_e ${proto.cppFileName}::defaultHandler( ${proto.camelPrefix()}Packet& ${proto.prefix}Packet, ${proto.camelPrefix()}Packet& ${proto.prefix}Response)
{

  /* NOTE : This function should not be modified, when the callback is needed,
          ${proto.prefix}_default_handler  should be implemented in the user file
  */

  return PACKET_NOT_HANDLED;
}
