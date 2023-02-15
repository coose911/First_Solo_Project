import unittest
from  models.member import Member
from controllers.member_controller import *



class TestMember(unittest.TestCase):

    def setUp(self):
        self.member = Member("Steve", "Rodgers", 31)

    
    def test_add_member(self):
        self.assertEqual("Steve", self.member.first_name)