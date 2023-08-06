#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass
from lementpro.data.pagingmodel import PagingModel
from lementpro.data.usergatepagingmetadata import UserGatePagingMetadata


@dataclass
class UserGateSearchResultPagingModel:
    paging: PagingModel = None
    total: int = None
    data: list = None
    metadata: UserGatePagingMetadata = None
