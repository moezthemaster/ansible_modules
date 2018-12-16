class Zabbix:

    def __init__(self, hostname):
        self.hostname = hostname

    def link_template(self):
        result = "{} is linked".format(self.hostname)
        changed = True
        is_error = False
        return is_error, changed, result

    def unlink_template(self):
        result = "{} is unlinked".format(self.hostname)
        changed = True
        is_error = False
        return is_error, changed, result
