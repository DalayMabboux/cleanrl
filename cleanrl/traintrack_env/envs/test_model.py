import unittest

import model
from model import get_new_block, LocomotiveAction


class ModelTest(unittest.TestCase):
    def test_from_0_to_2(self):
        new_block = model.track_model[0][0][0]
        self.assertEqual(new_block, 2)

    def test_from_0_to_2_derailing(self):
        new_block = model.track_model[0][0][1]
        self.assertEqual(new_block, -1)

    def test_get_new_block_0_forward_2(self):
        track_switch_states = [0, 0, 0, 0]
        new_block = get_new_block(0, 0, track_switch_states)
        self.assertEqual(new_block, 2)


    def test_get_new_block_0_forward_2_error(self):
        track_switch_states = [0, 1,
                               0, 0]
        new_block = get_new_block(0, 0, track_switch_states)
        self.assertEqual(new_block, -1)

    def test_get_new_block_2_forward_3(self):
        track_switch_states = [0, 0, 1, 1]
        new_block = get_new_block(2, 0, track_switch_states)
        self.assertEqual(new_block, 3)

    def test_get_new_block_2_forward_4(self):
        track_switch_states = [0, 0, 1, 0]
        new_block = get_new_block(2, 0, track_switch_states)
        self.assertEqual(new_block, 4)

    def test_get_new_block_2_forward_5(self):
        track_switch_states = [0, 0, 0, 0]
        new_block = get_new_block(2, 0, track_switch_states)
        self.assertEqual(new_block, 5)

    def test_get_new_block_3_backward(self):
        track_switch_states = [0, 0, 1, 1]
        new_block = get_new_block(3, 1, track_switch_states)
        self.assertEqual(new_block, 2)

    def test_get_new_block_3_backward_fail(self):
        track_switch_states = [0, 0, 0, 1]
        new_block = get_new_block(3, 1, track_switch_states)
        self.assertEqual(new_block, -1)

    def test_get_new_block_3_backward_fail2(self):
        track_switch_states = [0, 0, 1, 0]
        new_block = get_new_block(3, 1, track_switch_states)
        self.assertEqual(new_block, -1)

    def test_get_new_block_4_forward2(self):
        track_switch_states = [0, 0, 0, 0]
        new_block = get_new_block(4, 0, track_switch_states)
        self.assertEqual(new_block, -1)

    def test_get_new_block_4_backward_2(self):
        track_switch_states = [0, 0, 1, 0]
        new_block = get_new_block(4, 1, track_switch_states)
        self.assertEqual(new_block, 2)

    def test_get_new_block_4_backward_2_fail(self):
        track_switch_states = [0, 0, 0, 0]
        new_block = get_new_block(4, 1, track_switch_states)
        self.assertEqual(new_block, -1)

    def test_get_new_block_5_foreward_error(self):
        track_switch_states = [0, 0, 0, 0]
        new_block = get_new_block(4, 0, track_switch_states)
        self.assertEqual(new_block, -1)

    def test_get_new_block_2_foreward_5(self):
        track_switch_states = [0, 0, 0, 0]
        new_block = get_new_block(2, 0, track_switch_states)
        self.assertEqual(new_block, 5)