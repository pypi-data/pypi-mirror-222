#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class UserMailboxAddModel:
    login: str = None
    password: str = None
    smtpHost: str = None
    smtpPort: int = None
    imapHost: str = None
    imapPort: int = None
    isDisabled: bool = None
    signature: str = None
