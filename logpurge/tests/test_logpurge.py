from datetime import date, timedelta
import os
from scripttest import TestFileEnvironment
import tempfile
from unittest import TestCase



class TestLogPurge(TestCase):

    def setUp(self):
        self.tempdir = os.path.join(tempfile.gettempdir(), 'logpurge_tests')
        self.env = TestFileEnvironment(base_path=self.tempdir)

    def test_file_removal(self):
        for i in range(0,100):
            date_ = date.today() - timedelta(days=i * 7)
            filename = 'somefile{0}-{1}'.format(i, date_)
            open(os.path.join(self.tempdir, filename), 'a').close()

        args = ['-d',
                self.tempdir,
                '-f']
        args_str = ' '.join(args)
        results = self.env.run(
            'python ./logpurge/__init__.py ' + args_str,
            cwd=os.getcwd())
        results = self.env.run('bash -c "ls {0} | wc -l"'.format(self.tempdir)).stdout
        self.assertEqual(results, '40\n')
