'''
Test markdown.py with unittest
To run tests:
    python test_markdown_unittest.py
'''

import unittest
from markdown_adapter import run_markdown

class TestMarkdownPy(unittest.TestCase):

    def setUp(self):
        pass

    def test_non_marked_lines(self):
        '''
        Non-marked lines should only get 'p' tags around all input
        '''
        self.assertEqual(
                run_markdown('this line has no special handling'),
                '<p>this line has no special handling</p>')

    def test_em(self):
        '''
        Text surrounded by asterisks should be wrapped in 'em' tags
        '''
        self.assertEqual(
                run_markdown("*this should be wrapped in 'em' tags*"),
                "<p><em>this should be wrapped in 'em' tags</em></p>")

    def test_strong(self):
        '''
        Text surrounded by double asterisks should be wrapped in 'strong' tags
        '''
        self.assertEqual(
                run_markdown("**this should be wrapped in 'strong' tags**"),
                "<p><strong>this should be wrapped in 'strong' tags</strong></p>")

    def test_code(self):
        '''
        Text surrounded by tick marks (`) should be wrapped in 'code' tags
        '''
        self.assertEqual(
            run_markdown("`this should be wrapped in 'code' tags`"),
            "<p><code>this should be wrapped in 'code' tags</code></p>")

    def test_h(self):
        '''
        Lines that start with 1 to 6 hash marks (#) = the HTML header level
        '''
        for n in range(1,7):
            self.assertEqual(
                run_markdown('%s this should be wrapped in header level %d tags'%('#'*n,n)),
                '<p><h%d>this should be wrapped in header level %d tags</h%d></p>'%(n,n,n))

    def test_blockquote(self):
        '''
        Lines that start with angle-brackets (>) should be wrapped in 'blockquote' tags
        '''
        self.assertEqual(
                run_markdown("> This should be wrapped in 'blockquote' tags"),
                "<p><blockquote>This should be wrapped in 'blockquote' tags</blockquote></p>")

if __name__ == '__main__':
    unittest.main()
