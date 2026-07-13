#!/usr/bin/python

DOCUMENTATION = r'''
---
module: integration_report
short_description: Return the Capstan demo integration inventory
description:
  - Returns a deterministic list of services covered by this demo collection.
options:
  message:
    description:
      - Optional message included in the result.
    type: str
    default: Capstan integration demo is operational.
author:
  - Ziad Saleemi
'''

EXAMPLES = r'''
- name: Read integration report
  r92.capstan_demo.integration_report:
    message: Smoke test passed.
'''

RETURN = r'''
integrations:
  description: Integrations exercised by the collection.
  returned: always
  type: list
  elements: str
message:
  description: Supplied report message.
  returned: always
  type: str
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    module = AnsibleModule(
        argument_spec={
            'message': {
                'type': 'str',
                'default': 'Capstan integration demo is operational.',
            }
        },
        supports_check_mode=True,
    )
    module.exit_json(
        changed=False,
        message=module.params['message'],
        integrations=['eda', 'galaxy_ng', 'gatekeeper', 'quay'],
    )


if __name__ == '__main__':
    main()
