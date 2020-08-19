from ..connector import ConnectorToVK
from ..config import TOKEN_VK


class TestConnectorVK:
    def test_single_instance(self):
        con1 = ConnectorToVK(TOKEN_VK)
        con2 = ConnectorToVK(TOKEN_VK)
        assert con1 == con2

    def test_get_profile(self):
        con = ConnectorToVK(TOKEN_VK)
        data = con.get_profile(210700286)
        assert data is not None
        assert data["response"][0]["first_name"] == "Lindsey"

    def test_get_friends(self):
        con = ConnectorToVK(TOKEN_VK)
        data = con.get_profile(6492)
        assert data is not None

    def test_get_wall(self):
        con = ConnectorToVK(TOKEN_VK)
        data = con.get_profile(-86529522)
        assert data is not None
