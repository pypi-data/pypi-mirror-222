#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class ObjectTypeBimInfoExtendedModel:
    id: int = None
    objectTypeId: int = None
    icon: str = None
    hint: str = None
    showCreateBtn: bool = None
    calcElementState: bool = None
