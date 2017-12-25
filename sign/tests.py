# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from sign.models import Event

class ModelTest(TestCase):
    def setUp(self):
        pass
    def test_event_models(self):
        event=Event.objects.get('小米5发布会')
        self.assertEqual(event.address,'光谷金融港')
# Create your tests here.
