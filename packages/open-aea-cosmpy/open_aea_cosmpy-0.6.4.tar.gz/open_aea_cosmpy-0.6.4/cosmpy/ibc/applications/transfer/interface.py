# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2018-2022 Fetch.AI Limited
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
"""Interface for the IBC Applications Transfer functionality of CosmosSDK."""

from abc import ABC, abstractmethod

from cosmpy.protos.ibc.applications.transfer.v1.query_pb2 import (
    QueryDenomTraceRequest,
    QueryDenomTraceResponse,
    QueryDenomTracesRequest,
    QueryDenomTracesResponse,
    QueryParamsRequest,
    QueryParamsResponse,
)


class IBCApplicationsTransfer(ABC):
    """IBC Applications Transfer abstract class."""

    @abstractmethod
    def DenomTrace(self, request: QueryDenomTraceRequest) -> QueryDenomTraceResponse:
        """
        DenomTrace queries a denomination trace information.

        :param request: QueryDenomTraceRequest
        :return: QueryDenomTraceResponse
        """

    @abstractmethod
    def DenomTraces(self, request: QueryDenomTracesRequest) -> QueryDenomTracesResponse:
        """
        DenomTraces queries all denomination traces.

        :param request: QueryDenomTracesRequest
        :return: QueryDenomTracesResponse
        """

    @abstractmethod
    def Params(self, request: QueryParamsRequest) -> QueryParamsResponse:
        """
        Params queries all parameters of the ibc-transfer module.

        :param request: QueryParamsRequest
        :return: QueryParamsResponse
        """
