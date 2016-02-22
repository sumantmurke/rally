

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
