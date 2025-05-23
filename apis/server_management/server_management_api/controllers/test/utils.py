# Copyright (C) 2015, Wazuh Inc.
# Created by Wazuh, Inc. <info@wazuh.com>.
# This program is a free software; you can redistribute it and/or modify it under the terms of GPLv2

from wazuh.core.config.client import Config
from wazuh.core.config.models.indexer import IndexerConfig, IndexerNode
from wazuh.core.config.models.server import ServerConfig
from wazuh.core.results import AffectedItemsWazuhResult


def get_default_configuration():
    """Get default configuration for the tests."""
    return Config(
        server=ServerConfig(),
        indexer=IndexerConfig(hosts=[IndexerNode(host='example', port=1516)], username='wazuh', password='wazuh'),
    )


class CustomAffectedItems(AffectedItemsWazuhResult):
    """Mock custom values that are needed in controller tests."""

    def __init__(self, empty: bool = False):
        if not empty:
            super().__init__(dikt={'dikt_key': 'dikt_value'}, affected_items=[{'id': '001'}])
        else:
            super().__init__()

    def __getitem__(self, key):
        return self.render()[key]
