from pyethereum import tester

class TestSimpleContract(object):

    CONTRACT = 'contracts/simple.se'

    def setup_class(cls):
        cls.s = tester.state()
        cls.c = cls.s.abi_contract(cls.CONTRACT)
        cls.snapshot = cls.s.snapshot()

    def setup_method(self, method):
        self.s.revert(self.snapshot)

    def test_init(self):
        assert self.s.block.get_code(self.c.address) != ''
        assert self.s.block.get_storage_data(self.c.address, 0) == int(tester.a0, 16)
        assert self.s.block.get_storage_data(self.c.address, 1) == 1

    def test_incr(self):
        assert self.c.get_counter() == 1
        self.c.incr()
        assert self.c.get_counter() == 2
