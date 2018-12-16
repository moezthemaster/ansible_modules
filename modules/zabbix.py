from ansible.module_utils.basic import *
ANSIBLE_LIBRARIES = "/vagrant/ansible_modules"
sys.path.append(ANSIBLE_LIBRARIES)
#sys.path.insert(0, "/vagrant/ansible_modules")
from zabaw.zabbix import Zabbix


def link_template(params):
    hostname = params['hostname']
    zbx = Zabbix(hostname)
    result = zbx.link_template()
    return result


def unlink_template(params):
    hostname = params['hostname']
    zbx = Zabbix(hostname)
    result = zbx.unlink_template()
    return result


def main():
    fields = {
        "hostname": {"required": False, "type": "str"},
        "state": {
            "default": "present",
            "choices": ['present', 'absent'],
            "type": 'str'
        },
    }

    choice_map = {
        "present": link_template,
        "absent": unlink_template,
    }

    module = AnsibleModule(argument_spec=fields)
    is_error, has_changed, result = choice_map.get(
        module.params['state'])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error", meta=result)


if __name__ == '__main__':
    main()
