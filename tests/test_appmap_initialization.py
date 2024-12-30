import unittest
from unittest.mock import patch

class TestAppMapInitialization(unittest.TestCase):
    @patch('appmap.start')
    def test_appmap_initialization(self, mock_appmap_start):
        # Import the commands module to trigger the initialization
        import maltego_trx.commands

        # Check if appmap.start() was called
        mock_appmap_start.assert_called_once()

if __name__ == '__main__':
    import appmap
    appmap.start()
    unittest.main()