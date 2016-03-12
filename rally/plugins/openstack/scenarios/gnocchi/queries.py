
from rally import consts
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.gnocchi import utils as gnocchiutils
from rally.task import validation

class GnocchiQuery(gnocchiutils.GnocchiScenario):

    @validation.required_services(consts.Service.GNOCCHI)
    @validation.required_openstack(users=True)
    @scenario.configure()
    def aggregate_metrics(self, project_id=None, metric_name=None):
        """Aggregate metrics by calculating mean of a specific metric type"""

        import rpdb2; rpdb2.start_embedded_debugger("sumant")
        print "inside metrics mean"
        self._aggregate_metrics(project_id,metric_name)




