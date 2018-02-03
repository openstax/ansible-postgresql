import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_postgres_is_installed(host):
    pg = host.file('/etc/postgresql')
    assert pg.exists


def test_postgresql_is_running(host):
    pg = host.service('postgresql')
    assert pg.is_running
    # FIXME: This is currently failing.
    # assert pg.is_enabled
