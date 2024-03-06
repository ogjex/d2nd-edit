import unittest
import os
import shutil

from backup_manager import BackupManager

class TestBackupManager(unittest.TestCase):
    default_game_file_folder = 'default_excel'

    def setUp(self):
        # Create temporary test folders and files
        self.source_folder = 'test_source'
        self.backup_folder = 'test_backup'
        os.makedirs(self.source_folder, exist_ok=True)
        os.makedirs(self.backup_folder, exist_ok=True)
        open(os.path.join(self.source_folder, 'test_file.txt'), 'w').close()

    def test_backup_game_files(self):
        # Test backup_txt method
        backup_manager = BackupManager()
        backup_manager.backup_game_files(TestBackupManager.default_game_file_folder, os.path.join(self.source_folder, 'test_file.txt'))
        self.assertTrue(os.path.exists(os.path.join(TestBackupManager.default_game_file_folder, 'test_file.txt')))

    def test_restore_default(self):
        # Test restore_default method
        backup_manager = BackupManager()
        backup_manager.backup_game_files(TestBackupManager.default_game_file_folder, os.path.join(self.source_folder, 'test_file.txt'))
        backup_manager.restore_default(TestBackupManager.default_game_file_folder, 'test_file.txt')
        self.assertTrue(os.path.exists(os.path.join(TestBackupManager.default_game_file_folder, 'test_file.txt')))

    def test_backup_folder(self):
        # Test backup_folder method
        backup_manager = BackupManager()
        backup_manager.backup_folder(self.source_folder, self.backup_folder)
        #self.assertTrue(os.path.exists(os.path.join(self.backup_folder, self.source_folder)))

    def tearDown(self):
        # Clean up temporary test folders and files
        shutil.rmtree(self.source_folder)
        shutil.rmtree(self.backup_folder)
        os.remove(os.path.join(TestBackupManager.default_game_file_folder, 'test_file.txt'))

if __name__ == '__main__':
    unittest.main()
