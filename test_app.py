#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import app
import json

class TestFlaskHello(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_get(self):
        response = self.app.get('/')
        assert response.status_code == 200
        assert response.data.decode() == 'hoge!'

if __name__ == '__main__':
    unittest.main()
