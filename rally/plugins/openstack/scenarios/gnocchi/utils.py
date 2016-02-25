

from rally.task import atomic
from rally.task import utils as bench_utils
from rally.plugins.openstack import scenario

class GnocchiScenario(scenario.OpenStackScenario):
    """Base class for gnocchi scenarios and basic atomic actions """

    @atomic.action_timer("gnocchi.list_metrics")
    def _list_metrics(self):
        """Get list of metrics from gnocchi api
        :param query: query for gnocchi api
        :returns: list of all metrics
        """
        self.clients("gnocchi").metric.list()


    @atomic.action_timer("gnocchi.list_resources")
    def _list_resources(self):
        """Get list of resources from gnocchi api
        :returns: list of all resources
        """

        lis = self.clients("gnocchi").resource.list()
        print lis
