from gomatic import PipelineMaterial, ExecTask
import re


class GomaticPipeline:
    def __init__(self, configurator, environment):
        self.configurator = configurator
        self.environment = environment

    def to_material(self):
        return PipelineMaterial(self.pipeline, self.stage)

    def dependency_label_variable(self):
        suffix = re.sub('[^\w]+', '_', self.pipeline)
        return 'GO_DEPENDENCY_LABEL_' + suffix.upper()


class FirstExamplePipeline(GomaticPipeline):

    def prepare(self):
        self.pipeline_group = 'First_Example'
        self.pipeline_name = 'First_Pipeline'
        self.repository = 'https://github.com/rbenv/rbenv'
        self.stage_name = 'Clone'
        self.job_name = 'Silly_Output'

    def configure(self):
        self.pipeline = self.configurator \
            .ensure_pipeline_group(self.pipeline_group) \
            .ensure_replacement_of_pipeline(self.pipeline_name)

        self.pipeline.set_git_url(self.repository)

        self.stage = self.pipeline \
            .ensure_stage(self.stage_name) \
            .set_clean_working_dir()

        self.job = self.stage \
            .ensure_job(self.job_name) \
            .ensure_resource("gocd")

        self.job.add_task(ExecTask(['/bin/sh', '-c', 'echo "Foo!"']))

        return self


class SecondExamplePipeline(GomaticPipeline):

    def prepare(self):
        self.pipeline_group = 'Second_Example'
        self.pipeline_name = 'Second_Pipeline'
        self.repository = 'https://github.com/rbenv/rbenv'
        self.stage_name = 'Clone'
        self.job_name = 'Silly_Output'

    def set_dependency(self, dependency_ref):
        self.dependency_ref = dependency_ref
        return self

    def configure(self):
        self.pipeline = self.configurator \
            .ensure_pipeline_group(self.pipeline_group) \
            .ensure_replacement_of_pipeline(self.pipeline_name)

        self.pipeline.set_git_url(self.repository)

#        self.pipeline.ensure_material(self.dependency_ref.to_material)

        self.stage = self.pipeline \
            .ensure_stage(self.stage_name) \
            .set_clean_working_dir()

        self.job = self.stage \
            .ensure_job(self.job_name) \
            .ensure_resource("gocd")

        self.job.add_task(ExecTask(['/bin/sh', '-c', 'echo "Bar!"']))
#        self.job.add_task(ExecTask(['/bin/sh', '-c', 'echo "Dependency variable is %s"' % self.dependency_ref.dependency_label_variable()]))

        return self
