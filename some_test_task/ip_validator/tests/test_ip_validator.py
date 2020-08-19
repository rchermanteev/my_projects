from ..app.ip_validator import Validate


class TestValidator:
    def test_validate_one_ipv4(self, param_to_test_validate_one_ipv4):
        validator = Validate()
        ip, check = param_to_test_validate_one_ipv4
        assert validator.validateone(ip) == check

    def test_validate_one_ipv6(self, param_to_test_validate_two_ipv6):
        validator = Validate()
        ip, check = param_to_test_validate_two_ipv6
        assert validator.validatetwo(ip) == check

    def test_validateIPAddress(self, param_ips_to_smoke_test_validateIPAddress):
        validator = Validate()
        ips = [param_ips_to_smoke_test_validateIPAddress[i][0] for i in
               range(len(param_ips_to_smoke_test_validateIPAddress))]

        checks = [param_ips_to_smoke_test_validateIPAddress[i][1] for i in
                  range(len(param_ips_to_smoke_test_validateIPAddress))]

        res_valid_list = validator.validateIPAddress(ips)

        for i in range(len(res_valid_list)):
            assert checks[i] == res_valid_list[i][1] or checks[i].find(res_valid_list[i][1]) != -1
