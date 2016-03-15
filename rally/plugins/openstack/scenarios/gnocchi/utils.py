

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

    @atomic.action_timer("gnocchi.metrics_mean")
    def _aggregate_metrics(self, metric_name, aggregation_type, resource_list):
        """query for aggregating list of metrics"""

        metric_list =  []
        for resource in resource_list:
            metric_dict = resource.get('metrics')
            if metric_dict.has_key(metric_name):
                metric_list.append(metric_dict.get(metric_name))

        self.clients("gnocchi").metric.aggregation(
            metrics=metric_list, query=None, aggregation=aggregation_type)

    def _build_query(self,project_id, metric_name, aggregation_type):

        query = {}

        if project_id:
            query['project_id'] = project_id
        if metric_name:
            query['metric_name'] = metric_name
        if aggregation_type:
            query['aggregation_type'] = aggregation_type
        else:
            query['aggregation_type'] = "mean"

        return query

    def _search_resource(self):

        project_id=self.context["tenant"]["id"]
        query={"=":{"project_id": project_id} }
        return self.clients("gnocchi").resource.search(query=query)

