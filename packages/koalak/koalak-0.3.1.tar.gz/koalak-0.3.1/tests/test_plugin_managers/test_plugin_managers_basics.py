import pytest
from koalak.plugin_manager import PluginManager, abstract, field


def test_imports():
    from koalak.all import PluginManager as _PluginManager
    from koalak.all import abstract as _abstract
    from koalak.all import field as _field

    assert PluginManager is _PluginManager
    assert abstract is _abstract
    assert field is _field


def test_api_working():
    # Unamed plugins works
    PluginManager()

    # Named plugin works
    PluginManager("_koalak_unittest")


def test_unnamed_plugin_manager_without_framework():
    plugins = PluginManager()

    @plugins.mkbaseplugin
    class BasePlugin:
        pass

    class SimplePlugin(BasePlugin):
        name = "simple"

    assert plugins["simple"] is SimplePlugin
    assert "simple" in plugins
    assert SimplePlugin in plugins
    assert list(plugins) == [SimplePlugin]
    assert len(plugins) == 1


def test_named_plugin_manager_without_framework():
    plugins = PluginManager("plugin")

    @plugins.mkbaseplugin
    class BasePlugin:
        pass

    class SimplePlugin(BasePlugin):
        name = "simple"

    assert plugins["simple"] == SimplePlugin
    assert "simple" in plugins
    assert SimplePlugin in plugins
    assert list(plugins) == [SimplePlugin]


def test_two_plugins_without_framework():
    plugins = PluginManager("plugin")

    @plugins.mkbaseplugin
    class BasePlugin:
        pass

    class OnePlugin(BasePlugin):
        name = "one"

    class TwoPlugin(BasePlugin):
        name = "two"

    assert plugins["one"] == OnePlugin
    assert "one" in plugins
    assert OnePlugin in plugins

    assert plugins["two"] == TwoPlugin
    assert "two" in plugins
    assert TwoPlugin in plugins

    assert list(plugins) == [OnePlugin, TwoPlugin]
    assert len(plugins) == 2


# TODO: this test is working however, move it to framework and not plugin manager
@pytest.mark.skip
def test_plugin_manager_with_framework():
    framework = koalak.mkframework()
    plugins = framework.mkpluginmanager("tools")

    @plugins.mkbaseplugin
    class BasePlugin:
        pass

    class SimplePlugin(BasePlugin):
        name = "simple"

    assert plugins["simple"] == SimplePlugin
    assert "simple" in plugins
    assert SimplePlugin in plugins

    assert list(plugins) == [SimplePlugin]
    assert len(plugins) == 1
    assert framework.plugin_managers["tools"] is plugins
    assert len(framework.plugin_managers) == 1


# =============== #
# UTILS FONCTIONS #
# =============== #
def test__repr__and__str__():
    plugins = PluginManager()
    assert repr(plugins) == str(plugins) == "<PluginManager>"

    plugins = PluginManager("tools")
    assert repr(plugins) == str(plugins) == "<PluginManager [tools]>"
