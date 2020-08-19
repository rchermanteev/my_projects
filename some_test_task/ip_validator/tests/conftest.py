import pytest
import random


ipv4_list = [
            # Проверка на запись адреса в различных представлениях
            ("192.0.2.235", "Valid IPv4"), ("192.0.2.666", "Wrong IPv4"), ("0xC0.0x00.0x02.0xEB", "Valid IPv4"),
            ("4xC0.0x00.0x02.0xEB", "Wrong IPv4"), ("0300.0000.0002.0353", "Valid IPv4"),
            ("0300.0000.0002.0953", "Wrong IPv4"), ("0xC00002EB", "Valid IPv4"), ("0xC00002EU", "Wrong IPv4"),
            ("3221226219", "Valid IPv4"), ("3221226219000000", "Wrong IPv4"), ("030000001353", "Valid IPv4"),
            ("030000U01353", "Wrong IPv4"),
            # Специальные адреса
            ("0.0.0.0", "Valid IPv4"),
            ("0.0.0.0/8", "Valid IPv4"),
            ("100.64.0.0", "Valid IPv4"),
            ("198.18.0.0", "Valid IPv4"),
            ("255.255.255.255", "Valid IPv4"),
            # ipv6
            ("2001:0db8:0ffc:0008:0000:0000:0000:002f", "Wrong IPv4"),
            ("2001:0db8:0000:0000:0001:0000:0000:zzzz", "Wrong IPv4"),
            ("2001:db8::1:0:0:1", "Wrong IPv4"),
            ("2001:db8::1:0:0:z", "Wrong IPv4"),
            ]

ipv6_list = [
            # Проверка на запись адреса в различных формах
            ("2001:0db8:0ffc:0008:0000:0000:0000:002f", "Valid IPv6"),
            ("2001:0db8:0ffc:0008:0000:0000:0000:0z02", "Wrong IPv6"),
            ("2001:db8:ffc:8::2f", "Valid IPv6"),
            ("2001:db8:ffc:8::2z", "Wrong IPv6"),
            ("2001:0db8:0000:0000:0001:0000:0000:0001", "Valid IPv6"),
            ("2001:0db8:0000:0000:0001:0000:0000:zzzz", "Wrong IPv6"),
            ("2001:db8::1:0:0:1", "Valid IPv6"),
            ("2001:db8::1:0:0:z", "Wrong IPv6"),
            # Нотация стравнимая с ipv4
            ("::ffff:192.0.2.1", "Valid IPv6"),
            ("::ffff:192.0.2.zzz", "Wrong IPv6"),
            # Некоторые зарезервированные адреса
            ("::ffff:192.0.2.1", "Valid IPv6"),
            ("::", "Valid IPv6"),
            ("::1", "Valid IPv6"),
            ("64:ff9b::", "Valid IPv6"),
            ("2001::", "Valid IPv6"),
            ("2001:db8::", "Valid IPv6"),
            ("2002::", "Valid IPv6"),
            # Разный регистр
            ("2001:0Db8:0fFc:0008:0000:0000:0000:002F", "Valid IPv6"),
            # ipv4
            ("198.18.0.0", "Wrong IPv6"),
            ("0300.0000.0002.0353", "Wrong IPv6"),
            ("030000U01353", "Wrong IPv6"),
            ("192.0.2.666", "Wrong IPv6"),
]

parameters_ips = [3, 4, 5, 6, 7, 8, 15]
sum_ips = ipv4_list + ipv6_list


@pytest.fixture(scope="function", params=parameters_ips)
def param_ips_to_smoke_test_validateIPAddress(request):
    def get_generated_ips_list(number: int) -> list:
        random.seed(2019 + number)
        list_ids = []
        for i in range(number):
            rand_idx = random.randint(0, len(sum_ips)-1)
            list_ids.append(sum_ips[rand_idx])
        return list_ids
    return get_generated_ips_list(request.param)


@pytest.fixture(scope="function", params=ipv4_list, ids=lambda x: f"{x[0]}: {x[1]}")
def param_to_test_validate_one_ipv4(request):
    return request.param


@pytest.fixture(scope="function", params=ipv6_list, ids=lambda x: f"{x[0]}: {x[1]}")
def param_to_test_validate_two_ipv6(request):
    return request.param
