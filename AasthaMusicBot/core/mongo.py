#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
# A Powerful Music Bot Property of  🅐Ⓓ🅐Ⓡ🅢Ⓗ✨🅣Ⓘ🅦Ⓐ🅡Ⓘ

# Kanged By © @Hitler_fed_owner
# Victor © @Hitler_fed
# Owner  🅐Ⓓ🅐Ⓡ🅢Ⓗ✨🅣Ⓘ🅦Ⓐ🅡Ⓘ
# Victor
# All rights reserved. Yukki

from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient

import config

_mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
_mongo_sync_ = MongoClient(config.MONGO_DB_URI)

mongodb = _mongo_async_.Alexa
pymongodb = _mongo_sync_.Alexa
