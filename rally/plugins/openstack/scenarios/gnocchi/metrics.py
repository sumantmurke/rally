
from rally import consts
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.gnocchi import utils as gnocchiutils
from rally.task import validation

class GnocchiMetric(gnocchiutils.GnocchiScenario):
    """Benchmarking scenarios for Gnocchi Metric API"""
    @validation.required_services(consts.Service.GNOCCHI)
    @validation.required_openstack(users=True)
    @scenario.configure()
    def list_metrics(self):
        """list metrics by querrying the resources"""


        #query = self._make_general_query()
        self._list_metrics()
