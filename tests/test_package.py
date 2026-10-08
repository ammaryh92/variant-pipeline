import importlib.metadata


def test_package_is_installed():
    version = importlib.metadata.version("variant_pipeline")
    assert isinstance(version, str)
    assert len(version) > 0
