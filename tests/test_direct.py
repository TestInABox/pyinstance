import unittest

import six

import pyinstance


class TestDirect(unittest.TestCase):

    def test_direct_basic(self):
        session = "test_direct"
        instance = pyinstance.PyInstance(session)
        self.assertIsNotNone(instance)
        self.assertIsInstance(instance, pyinstance.PyInstance)
        self.assertEqual(instance.session, session)
        self.assertIn(session, pyinstance.PyInstance.pyinstances)
        self.assertEqual(
            id(instance),
            id(pyinstance.PyInstance.pyinstances[session]['instance'])
        )
        self.assertEqual(
            1,
            pyinstance.PyInstance.pyinstances[session]['counter']
        )
        instance.__del__()
        self.assertNotIn(session, pyinstance.PyInstance.pyinstances)

    def test_direct_multiple(self):
        session_names = [
            "test_direct_multiple_1",
            "test_direct_multiple_2",
            "test_direct_multiple_3"
        ]
        sessions = {
            s: pyinstance.PyInstance(s)
            for s in session_names
        }
        ids = [
            id(v)
            for k, v in six.iteritems(sessions)
        ]
        self.assertEqual(
            len(session_names),
            len(ids)
        )
        for k, v in six.iteritems(sessions):
            self.assertEqual(
                1,
                pyinstance.PyInstance.pyinstances[k]['counter']
            )
            self.assertIsInstance(
                pyinstance.PyInstance.pyinstances[k]['instance'],
                pyinstance.PyInstance
            )
            v.__del__()

    def test_direct_repeats(self):
        session_names = [
            ("test_direct_1", "test_direct_repeats_1"),
            ("test_direct_2", "test_direct_repeats_1"),
            ("test_direct_3", "test_direct_repeats_2")
        ]
        sessions = {
            t: pyinstance.PyInstance(s)
            for t, s in session_names
        }
        ids = [
            id(v)
            for k, v in six.iteritems(sessions)
        ]
        self.assertEqual(
            len(session_names),
            len(ids)
        )
        counts = {
        }
        for t, s in session_names:
            if s in counts:
                counts[s] = counts[s] + 1
            else:
                counts[s] = 1

        for t, s in session_names:
            self.assertIn(s, pyinstance.PyInstance.pyinstances)
            self.assertEqual(
                pyinstance.PyInstance.pyinstances[s]['counter'],
                counts[s]
            )
            self.assertIsInstance(
                pyinstance.PyInstance.pyinstances[s]['instance'],
                pyinstance.PyInstance
            )

        for k, v in six.iteritems(sessions):
            v.__del__()
