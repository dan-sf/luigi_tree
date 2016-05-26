import unittest
import mock
import socket
from luigi_tree import cli

class TestCheckServer(unittest.TestCase):
    def test_check_server_down(self):
        with mock.patch('socket.socket') as server_mock:
            connect_mock = mock.MagicMock()
            connect_mock.connect.side_effect = socket.error
            server_mock.return_value = connect_mock
            self.assertFalse(cli.check_server('foo', 'bar'))

    def test_check_server_up(self):
        with mock.patch('socket.socket', return_value=mock.MagicMock()) as server_mock:
            self.assertTrue(cli.check_server('foo', 'bar'))

class TestCMDLineParser(unittest.TestCase):
    def test_cmd_line_parser_default(self):
        args = cli.cmd_line_parser([])
        self.assertEqual(2, args.level)
        self.assertEqual(2, args.sleep)
        self.assertEqual('/tmp', args.output_dir)
        self.assertEqual('localhost', args.server)
        self.assertEqual(8082, args.port)

    def test_cmd_line_parser_custom(self):
        args = cli.cmd_line_parser(['--level', '5', '--sleep', '1', '--output-dir', '.'])
        self.assertEqual(5, args.level)
        self.assertEqual(1, args.sleep)
        self.assertEqual('.', args.output_dir)

class TestMain(unittest.TestCase):
    @mock.patch('sys.argv')
    @mock.patch('luigi.run')
    def test_main_server_down(self, luigi_mock, sys_mock):
        sys_mock = []
        expected = ['Root',
                    '--level', '2',
                    '--sleep', '2',
                    '--output-dir', '/tmp',
                   ]
        with mock.patch.object(cli, 'check_server', return_value=True):
            cli.main()
        luigi_mock.assert_called_once_with(expected)

    @mock.patch('sys.argv')
    @mock.patch('luigi.run')
    def test_main_server_up(self, luigi_mock, sys_mock):
        sys_mock = []
        expected = ['Root',
                    '--level', '2',
                    '--sleep', '2',
                    '--output-dir', '/tmp',
                    '--local-scheduler',
                   ]
        with mock.patch.object(cli, 'check_server', return_value=False):
            cli.main()
        luigi_mock.assert_called_once_with(expected)

if __name__ == '__main__':
    unittest.main()

