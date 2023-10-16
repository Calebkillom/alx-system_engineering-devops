#!/usr/bin/python3
"""
Validating that my server is visible in DataDog
Under the hostname XX-web-01
"""
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.hosts_api import HostsApi


configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = HostsApi(api_client)
    response = api_instance.list_hosts(
        filter="env:ci",
    )

    print(response)
