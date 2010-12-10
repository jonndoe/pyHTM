'''
Created on Dec 7, 2010

@author: Jason Carver
'''
import unittest
from mock import Mock
from carver.htm.column import Column
from carver.htm import HTM
from carver.htm.cell import Cell
from carver.htm.config import config


class TestColumn(unittest.TestCase):


    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCreateSegment(self):
        h = HTM()
        h.initialize_input([[1,1,1],[1,1,1]])
        cell = Cell()
        startingSegments = config.getint('init','segments_per_cell')
        self.assertEqual(startingSegments, len(cell.segments))
        cell.create_segment(h)
        self.assertEqual(startingSegments+1, len(cell.segments))
        
        #make sure newly created segment has the right number of synapses
        self.assertNotEqual(0, len(cell.segments[-1].synapses))
        
    def testClockTick(self):
        c = Cell()
        self.assertFalse(c.active)
        self.assertFalse(c.learning)
        self.assertFalse(c.predicting)
        
        c.clockTick()
        
        self.assertFalse(c.wasActive)
        self.assertFalse(c.wasLearning)
        self.assertFalse(c.predicted)
        
        c.active=True
        c.clockTick()
        self.assert_(c.wasActive)
        self.assertFalse(c.wasLearning)
        self.assertFalse(c.predicted)
        
        c.learning=True
        c.clockTick()
        self.assertFalse(c.wasActive)
        self.assert_(c.wasLearning)
        self.assertFalse(c.predicted)
        
        c.predicting=True
        c.clockTick()
        self.assertFalse(c.wasActive)
        self.assertFalse(c.wasLearning)
        self.assert_(c.predicted)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInit']
    unittest.main()
