#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class UserViewAddModel:
    commentIds: list = None
