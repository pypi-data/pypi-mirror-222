from koalak.plugin_manager import PluginManager, abstract


def test_plugin_manager_instances_without_arguments():
    plugins = PluginManager()

    @plugins.mkbaseplugin
    class BasePlugin:
        @abstract
        def compute(self, x):
            pass

    class DoublePlugin(BasePlugin):
        name = "double"

        def compute(self, x):
            return x * 2

    class AddFivePlugin(BasePlugin):
        name = "add_five"

        def compute(self, x):
            return x + 5

    instances = list(plugins.instances())
    assert len(instances) == 2

    double_plugin = instances[0]
    assert isinstance(double_plugin, DoublePlugin)
    assert double_plugin.compute(2) == 4

    add_five_plugin = instances[1]
    assert isinstance(add_five_plugin, AddFivePlugin)
    assert add_five_plugin.compute(2) == 7


def test_plugin_manager_instances_with_arguments():
    plugins = PluginManager()

    @plugins.mkbaseplugin
    class BasePlugin:
        def __init__(self, x):
            self.x = x

        @abstract
        def compute(self):
            pass

    class DoublePlugin(BasePlugin):
        name = "double"

        def compute(self):
            return self.x * 2

    class AddFivePlugin(BasePlugin):
        name = "add_five"

        def compute(
            self,
        ):
            return self.x + 5

    instances = list(plugins.instances(2))
    assert len(instances) == 2

    double_plugin = instances[0]
    assert isinstance(double_plugin, DoublePlugin)
    assert double_plugin.compute() == 4

    add_five_plugin = instances[1]
    assert isinstance(add_five_plugin, AddFivePlugin)
    assert add_five_plugin.compute() == 7
