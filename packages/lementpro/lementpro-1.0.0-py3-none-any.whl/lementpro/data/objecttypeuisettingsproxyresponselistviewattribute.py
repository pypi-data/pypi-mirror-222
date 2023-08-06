#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class ObjectTypeUiSettingsProxyResponseListViewAttribute:
    name: str = None
    attributeKnownId: str = None
    isSystem: bool = None
    hideIfNull: bool = None
    showName: bool = None
