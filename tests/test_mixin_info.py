from src.mixin_info import MixinInfo


def test_mixininfo(capsys):

    class SomeClass(MixinInfo):

        def __init__(self, arg1, arg2):
            self.arg1 = arg1
            self.arg2 = arg2
            super().__init__()

    SomeClass("value1", "value2")
    message = capsys.readouterr()
    assert message.out.strip() == "SomeClass('value1', 'value2')"
