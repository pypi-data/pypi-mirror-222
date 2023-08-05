# Copyright 2012 Red Hat, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo_config import cfg

from neutron.conf.agent import common as config
from neutron.conf.plugins.ml2.drivers import agent
from neutron.conf.plugins.ml2.drivers import ovs_conf

agent.register_agent_opts()
ovs_conf.register_ovs_agent_opts()
config.register_agent_state_opts_helper(cfg.CONF)
