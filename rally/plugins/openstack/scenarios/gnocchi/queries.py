
from rally import consts
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.gnocchi import utils as gnocchiutils
from rally.task import validation

class GnocchiQuery(gnocchiutils.GnocchiScenario):

    @validation.required_services(consts.Service.GNOCCHI)
    @validation.required_openstack(users=True)
    @scenario.configure()
    def aggregate_metrics(self, metric_name=None, aggregation_type=None):
        """Aggregate metrics by calculating mean of a specific metric type"""

        import rpdb2; rpdb2.start_embedded_debugger("sumant")

        resource_list = self._search_resource()
        self._aggregate_metrics(metric_name, aggregation_type, resource_list)




