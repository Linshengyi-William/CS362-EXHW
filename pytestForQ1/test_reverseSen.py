import pytest
import reverseSen


class TestReverseSentence:
    def test_correctResult1(self):
        string1 = "string a is this" 
        assert reverseSen.reverseSentence("this is a string") == string1

    def test_correctResult2(self):
        string2 = "William is name my"
        assert reverseSen.reverseSentence("my name is William") == string2

    def test_correctResult3(self):
        string3 = "failed to reverse"
        assert reverseSen.reverseSentence("failed to reverse") == string3
