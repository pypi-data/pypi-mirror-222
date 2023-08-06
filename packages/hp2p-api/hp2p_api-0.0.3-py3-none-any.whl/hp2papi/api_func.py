#
# The MIT License
#
# Copyright (c) 2022 ETRI
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
import sys
aaa  = sys.path
from .classes import *
#from collections.abc import Callable
from typing import Callable
import grpc
from .api_pb2 import *
from .api_pb2_grpc import *


__notificationListeners = dict()
__grpcPort = 50051

def __SetGrpcPort(port: int) -> None:
    global __grpcPort
    __grpcPort = port

def __GrpcStart() -> None:
    server = grpc.aio.server(grpc.ThreadPoolExecutor(max_workers=10))
    add_Hp2pApiProtoServicer_to_server(Hp2pApiProtoServicer(), server)
    server.add_insecure_port('[::]:' + str(__grpcPort))
    server.start()
    print("Python gRPC Server is running on port " + str(__grpcPort))
    server.wait_for_termination()

def __Init():
    __GrpcStart()
    print("Peer API init.")

def __CheckRequest(req: Request, func: Callable[[Request], Response]) -> Response:
    if not req or not req.mandatoryCheck():
        return Response(ResponseCode.WrongRequest)
    
    return func(req)

def __Creation(req: CreationRequest) -> CreationResponse:
    if not req or not req.mandatoryCheck():
        return CreationResponse(code=ResponseCode.WrongRequest)
    
    return CreationResponse(code=ResponseCode.Success, overlayId="temp_overlay_id")

def __Query(overlayId: str = None, title: str = None, description: str = None) -> QueryResponse:
    response = QueryResponse(ResponseCode.Success)
    response.overlay = [
        Overlay("temp_overlay_id1", "temp_title1", "temp_description1", "temp_owner_id1"),
        Overlay("temp_overlay_id2", "temp_title2", "temp_description2", "temp_owner_id2", OverlayClosed.SetAccessKey),
    ]

    return response

def __Modification(req: ModificationRequest) -> Response:
    return Response(ResponseCode.Success)

def __Join(req: JoinRequest) -> JoinResponse:
    response = JoinResponse(ResponseCode.Success)
    response.startDateTime = "20230101090000"
    response.endDateTime = "20230101100000"
    response.sourceList = [ "user3" ]

    serviceControlChannel = ChannelServiceControl()
    serviceControlChannel.channelId = "chid1"

    faceChannel = ChannelFeatureBasedVideo()
    faceChannel.channelId = "chid2"
    faceChannel.sourceList = [ "user2", "test_user" ]
    faceChannel.mode = FeatureBasedVideoMode.KeypointsDescriptionMode
    faceChannel.resolution = "1024x1024"
    faceChannel.framerate = "30fps"
    faceChannel.keypointsType = "68points"
    
    audioChannel = ChannelAudio()
    audioChannel.channelId = "chid3"
    audioChannel.codec = AudioCodec.AAC
    audioChannel.sampleRate = AudioSampleRate.Is44100
    audioChannel.bitrate = AudioBitrate.Is128kbps
    audioChannel.mono = AudioChannelType.Stereo

    textChannel = ChannelText()
    textChannel.channelId = "chid4"
    textChannel.sourceList = [ "*" ]
    textChannel.format = TextFormat.Plain

    response.channelList = [ serviceControlChannel, faceChannel, audioChannel, textChannel ]
    
    return response

def __SearchPeer(req: SearchPeerRequest) -> SearchPeerResponse:
    response = SearchPeerResponse(ResponseCode.Success)

    peer1 = Peer("user1", "김철수")
    peer2 = Peer("user2", "박영희")
    peer3 = Peer("user3", "이영수")

    response.peerList = [ peer1, peer2, peer3 ]

    return response

def __SendData(req: SendDataRequest) -> Response:
    return Response(ResponseCode.Success)

def __Leave(req: LeaveRequest) -> Response:
    __DelNotificatonListener(req.overlayId, req.peerId)
    return Response(ResponseCode.Success)

def __Removal(req: RemovalRequest) -> Response:
    __DelNotificatonListener(req.overlayId, req.ownerId)
    return Response(ResponseCode.Success)

def __SetNotificatonListener(overlayId: str, peerId: str, func: Callable[[Notification], None]) -> bool:
    global __notificationListeners

    if not overlayId or not peerId or not func:
        return False

    if not callable(func):
        return False

    __notificationListeners[overlayId + peerId] = func

    print(__notificationListeners)

    __notificationListeners[overlayId + peerId](SessionChangeNotification(overlayId="temp_overlay_id", title="new_title", sourceList=["*"]))
    __notificationListeners[overlayId + peerId](PeerChangeNotification(overlayId="temp_overlay_id", peerId="new_peer", displayName="최백호", leave=False))
    __notificationListeners[overlayId + peerId](SessionTerminationNotification(overlayId="temp_overlay_id"))

    dataNoti = DataNotification(overlayId="temp_overlay_id")
    dataNoti.dataType = DataType.Text
    dataNoti.peerId = "user1"
    dataNoti.data = "안녕하세요~".encode()
    __notificationListeners[overlayId + peerId](dataNoti)

    return True

def __DelNotificatonListener(overlayId: str, peerId: str) -> bool:
    global __notificationListeners

    if not overlayId or not peerId:
        return False

    try:
        del __notificationListeners[overlayId + peerId]
        print("\nDelete notification listener.")
    except:
        return False

    return True
