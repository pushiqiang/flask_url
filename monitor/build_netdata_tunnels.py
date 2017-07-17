#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep
import multiprocessing
import os

from ansible.inventory import Inventory
from ansible.parsing.dataloader import DataLoader
from ansible.vars import VariableManager
from sshtunnel import SSHTunnelForwarder


def get_hosts(inventory_path):
    variable_manager = VariableManager()
    loader = DataLoader()

    inventory = Inventory(
        loader=loader,
        variable_manager=variable_manager,
        host_list=inventory_path,
    )
    for host in inventory.get_hosts():
        host_config = host.serialize()
        yield {
            'address': host_config['address'],
            'user': host_config['vars']['ansible_user'],
            'ssh_key_file': host_config['vars']['ansible_ssh_private_key_file'],
        }


def forward(ssh_username, ssh_server_ip, ssh_key, remote_port, to_local_port):
    # TODO: 加入ssh跳板的支持
    ssh_key_path = os.path.expanduser(ssh_key)
    with SSHTunnelForwarder(
        (ssh_server_ip, 22),
        ssh_username=ssh_username,
        ssh_pkey=ssh_key_path,
        remote_bind_address=('127.0.0.1', remote_port),
        local_bind_address=('127.0.0.1', to_local_port)
    ) as server:
        print(u'端口转发: %s:%s -> http://127.0.0.1:%s' % (
            ssh_server_ip, remote_port, server.local_bind_port))

        while True:
            # press Ctrl-C for stopping
            sleep(1)


def main():
    start_port = 5000
    for host in get_hosts('../deploy/production'):
        start_port += 1

        host['port'] = start_port
        process = multiprocessing.Process(target=forward, kwargs={
            'ssh_username': host['user'],
            'ssh_server_ip': host['address'],
            'ssh_key': host['ssh_key_file'],
            'remote_port': 5999,
            'to_local_port': start_port
        })
        process.start()


if __name__ == '__main__':
    print(u'============================================================')
    print(u'连接到所有的服务器，建立一个本地的端口映射，方便查看 netdata')
    print(u'============================================================')
    main()
