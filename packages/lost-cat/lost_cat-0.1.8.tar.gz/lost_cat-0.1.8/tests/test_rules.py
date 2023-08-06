"""A test case for the path utils module"""
import logging
import re
import unittest
from lost_cat.utils.rules_utils import Rule, RuleState, RuleEngine, RulesTool

logger = logging.getLogger(__name__)

class TestRulesModule(unittest.TestCase):
    """A container class for the rule modeule test cases"""


    @classmethod
    def setUpClass(cls):
        """ Set up for Trie Unit Tests..."""
        cls.phrases = [
            "Top Drawer:	High quality, exceptional; something that's very valuable.",
            "A Chip on Your Shoulder:	Being angry about something that happened in the past.",
            "Par For the Course:	What you would expect to happen; something normal or common.",
            "In a Pickle:	Being in a difficult predicament; a mess; an undesirable situation.",
            "Heads Up:	Used as an advanced warning. To become keenly aware.",
            "On the Same Page:	Thinking alike or understanding something in a similar way with others.",
            "Elvis Has Left The Building:	Something that is all over.",
            "Keep Your Eyes Peeled:	To be watchful; paying careful attention to something.",
            "Rain on Your Parade:	To spoil someone's fun or plans; ruining a pleasurable moment",
            "A Hundred and Ten Percent:	Someone who gives more than what seems to be possible.",
        ]

    @classmethod
    def tearDownClass(cls):
        """ Tear down for Trie Unit Tests"""
        pass

    def test_rule(self):
        """check the simple rule class"""

        rule = Rule( idx=1,
            name="Has Something",
            engine=RuleEngine.CONTAINS,
            expr="something",
            tags=[{
                "key": "somthing",
                "value": True,
                # "regex"
            }],
            stop=True,
            state=RuleState.SINGLE,
            options={
                "ignorecase": True
            }
        )

        result = rule.run(phrase=self.phrases[0])
        print(result)


    def test_rules(self):
        """Check the runner against a sequence of rules"""

        rule = Rule( idx=1,
            name="Has Something",
            engine=RuleEngine.CONTAINS,
            expr="something",
            tags=[{
                "key": "somthing",
                "value": True,
                # "regex"
            }],
            stop=True,
            state=RuleState.SINGLE,
            options={
                "ignorecase": True
            }
        )

        rules = RulesTool()
        rules.add_rule(rule=rule)

        results = rules.run(phrases=self.phrases)

        print(results)
