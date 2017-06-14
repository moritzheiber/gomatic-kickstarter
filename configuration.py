#!/usr/bin/env python

import os
import urlparse
from gomatic import GoCdConfigurator, \
    HostRestClient

import pipelines


class Environment(object):
    def go_server_admin_password(self):
        return self._env_or_fail('GO_SERVER_ADMIN_PASSWORD')

    def go_server_admin_user(self):
        return os.getenv('GO_SERVER_ADMIN_USERNAME', 'admin')

    def go_server_host(self):
        url = self._go_server_url()
        return "%s:%s" % (url.hostname, url.port)

    def go_server_url(self):
        return self._go_server_url().geturl()

    def _go_server_url(self):
        return urlparse.urlparse(self._env_or_fail('GO_SERVER_URL'))

    def _env_or_fail(self, name):
        value = os.getenv(name)
        if value is None:
            raise Exception('Please set %s environment variable' % name)
        return value


env = Environment()

cfg = GoCdConfigurator(HostRestClient(
    env.go_server_host()
))

cfg.default_job_timeout = 10

example1 = pipelines.FirstExamplePipeline(cfg, env)
example2 = pipelines.SecondExamplePipeline(cfg, env)

for p in [example1, example2]:
    p.prepare()

example1.configure()
example2.set_dependency(example1.dependency_ref).configure()

# Upload to GoCD
cfg.save_updated_config()
