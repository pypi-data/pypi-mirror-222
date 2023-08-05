#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

from oslo_policy import policy


def policy_and(*args):
    return ' and '.join(args)


def policy_or(*args):
    return ' or '.join(args)


# TODO(amotoki): Define these in neutron-lib once what constants are required
# from stadium and 3rd party projects.
# As of now, the following are candidates.
RULE_ADMIN_OR_OWNER = 'rule:admin_or_owner'
RULE_ADMIN_ONLY = 'rule:admin_only'
RULE_ANY = 'rule:regular_user'
RULE_ADVSVC = 'rule:context_is_advsvc'
RULE_ADMIN_OR_NET_OWNER = 'rule:admin_or_network_owner'
RULE_ADMIN_OR_NET_OWNER_OR_ADVSVC = policy_or(RULE_ADMIN_OR_NET_OWNER,
                                              RULE_ADVSVC)
RULE_ADMIN_OR_PARENT_OWNER = 'rule:admin_or_ext_parent_owner'

# Generic policy check string for system administrators. These are the people
# who need the highest level of authorization to operate the deployment.
# They're allowed to create, read, update, or delete any system-specific
# resource. They can also operate on project-specific resources where
# applicable (e.g., removing networks or routers)
SYSTEM_ADMIN = 'role:admin and system_scope:all'

# Generic policy check string for system users who don't require all the
# authorization that system administrators typically have. This persona, or
# check string, typically isn't used by default, but it's existence it useful
# in the event a deployment wants to offload some administrative action from
# system administrator to system members
SYSTEM_MEMBER = 'role:member and system_scope:all'

# Generic policy check string for read-only access to system-level resources.
# This persona is useful for someone who needs access for auditing or even
# support. These users are also able to view project-specific resources where
# applicable (e.g., listing all networks in the deployment, regardless of the
# project they belong to).
SYSTEM_READER = 'role:reader and system_scope:all'

# This check string is reserved for actions that require the highest level of
# authorization on a project or resources within the project (e.g., setting the
# creating QoS policies)
PROJECT_ADMIN = 'role:admin and project_id:%(project_id)s'

# This check string is the primary use case for typical end-users, who are
# working with resources that belong to a project (e.g., creating ports and
# routers).
PROJECT_MEMBER = 'role:member and project_id:%(project_id)s'

# This check string should only be used to protect read-only project-specific
# resources. It should not be used to protect APIs that make writable changes
# (e.g., updating a router or deleting a port).
PROJECT_READER = 'role:reader and project_id:%(project_id)s'

# The following are common composite check strings that are useful for
# protecting APIs designed to operate with multiple scopes (e.g., a system
# administrator should be able to delete any router in the deployment, a
# project member should only be able to delete routers in their project).
SYSTEM_ADMIN_OR_PROJECT_MEMBER = (
    '(' + SYSTEM_ADMIN + ') or (' + PROJECT_MEMBER + ')')
SYSTEM_OR_PROJECT_READER = (
    '(' + SYSTEM_READER + ') or (' + PROJECT_READER + ')')

# Additional rules needed in Neutron
RULE_NET_OWNER = 'rule:network_owner'
RULE_PARENT_OWNER = 'rule:ext_parent_owner'
RULE_SG_OWNER = 'rule:sg_owner'

rules = [
    policy.RuleDefault(
        'context_is_admin',
        'role:admin',
        description='Rule for cloud admin access'),
    policy.RuleDefault(
        'owner',
        'tenant_id:%(tenant_id)s',
        description='Rule for resource owner access'),
    policy.RuleDefault(
        'admin_or_owner',
        policy_or('rule:context_is_admin',
                  'rule:owner'),
        description='Rule for admin or owner access'),
    policy.RuleDefault(
        'context_is_advsvc',
        'role:advsvc',
        description='Rule for advsvc role access'),
    policy.RuleDefault(
        'admin_or_network_owner',
        policy_or('rule:context_is_admin',
                  'tenant_id:%(network:tenant_id)s'),
        description='Rule for admin or network owner access'),
    policy.RuleDefault(
        'admin_owner_or_network_owner',
        policy_or('rule:owner',
                  RULE_ADMIN_OR_NET_OWNER),
        description=('Rule for resource owner, '
                     'admin or network owner access')),
    policy.RuleDefault(
        'network_owner',
        'tenant_id:%(network:tenant_id)s',
        description='Rule for network owner access'),
    policy.RuleDefault(
        'admin_only',
        'rule:context_is_admin',
        description='Rule for admin-only access'),
    policy.RuleDefault(
        'regular_user',
        '',
        description='Rule for regular user access'),
    # TODO(amotoki): Should be renamed to shared_network? It seems clearer.
    policy.RuleDefault(
        'shared',
        'field:networks:shared=True',
        description='Rule of shared network'),
    policy.RuleDefault(
        'default',
        RULE_ADMIN_OR_OWNER,
        description='Default access rule'),
    policy.RuleDefault(
        'admin_or_ext_parent_owner',
        policy_or('rule:context_is_admin',
                  'tenant_id:%(ext_parent:tenant_id)s'),
        description='Rule for common parent owner check'),
    policy.RuleDefault(
        'ext_parent_owner',
        'tenant_id:%(ext_parent:tenant_id)s',
        description='Rule for common parent owner check'),
    policy.RuleDefault(
        name='sg_owner',
        check_str='tenant_id:%(security_group:tenant_id)s',
        description='Rule for security group owner access'),
]


def list_rules():
    return rules
