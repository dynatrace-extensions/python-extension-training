from dynatrace_extension import Extension, Status, StatusValue

from test_ext.helpers.utils import greet
from test_ext.helpers.api import get_fact


class ExtensionImpl(Extension):

    def initialize(self):
        self.extension_name = "test_ext"

    def query(self):
        """
        The query method is automatically scheduled to run every minute
        """
        self.logger.info("query method started for test_ext.")

        for endpoint in self.activation_config["endpoints"]:
            url = endpoint["url"]
            user = endpoint["user"]
            password = endpoint["password"]
            self.logger.debug(f"Running endpoint with url '{url}'")

            # Your extension code goes here, e.g.
            # response = requests.get(url, auth=(user, password))

            # Report metrics with
            self.report_metric("my_metric", 1, dimensions={"my_dimension": "dimension1"})

        self.logger.info("query method ended for test_ext.")

    def fastcheck(self) -> Status:
        """
        This is called when the extension runs for the first time.
        If this AG cannot run this extension, raise an Exception or return StatusValue.ERROR!
        """
        return Status(StatusValue.OK)


def main():
    # ExtensionImpl().run()
    get_fact()


if __name__ == '__main__':
    main()
