import unittest
from zabaw.zabbix import Zabbix


class TestZabbix(unittest.TestCase):

    def test_link_hostname(self):
        zbx = Zabbix('dpgalx001')
        is_error, changed, result = zbx.link_template()
        assert not is_error
        assert changed
        assert result == "dpgalx001 is linked"

    def test_unlink_hostname(self):
        zbx = Zabbix('dpgalx001')
        is_error, changed, result = zbx.unlink_template()
        assert not is_error
        assert changed
        assert result == "dpgalx001 is unlinked"
