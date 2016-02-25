from rally import consts
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.gnocchi import utils as gnocchiutils
from rally.task import validation

class GnocchiResource(gnocchiutils.GnocchiScenario):
    """Benchmarking scenarios for Gnocchi Resource API"""

    @validation.required_services(consts.Service.GNOCCHI)
    @validation.required_openstack(users=True)
    @scenario.configure()
    def list_resources(self):
        """list all resources """

        self._list_resources()

