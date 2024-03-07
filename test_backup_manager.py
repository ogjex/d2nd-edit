import unittest
import os
import shutil
from backup_manager import BackupManager

class TestBackupManager(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.your_backup_manager = BackupManager()
        
        # Create temporary test folders and files
        cls.default_game_file_folder = 'test_default_excel'
        cls.source_folder = 'test_char_source'
        cls.backup_folder = 'test_char_backup'
        os.makedirs(cls.default_game_file_folder, exist_ok=True)
        os.makedirs(cls.source_folder, exist_ok=True)
        os.makedirs(cls.backup_folder, exist_ok=True)
        open(os.path.join(cls.default_game_file_folder, 'game_test_file1.txt'), 'w').close()
        open(os.path.join(cls.default_game_file_folder, 'game_test_file2.txt'), 'w').close()
        open(os.path.join(cls.your_backup_manager.backup_game_file_folder, 'game_test_file1.txt'), 'w').close()
        open(os.path.join(cls.your_backup_manager.backup_game_file_folder, 'game_test_file2.txt'), 'w').close()
        open(os.path.join(cls.your_backup_manager.modded_game_file_folder, 'game_test_file1.txt'), 'w').close()
        open(os.path.join(cls.your_backup_manager.modded_game_file_folder, 'game_test_file2.txt'), 'w').close()
        open(os.path.join(cls.source_folder, 'test_file.txt'), 'w').close()
        open(os.path.join(cls.source_folder, 'test_file1.txt'), 'w').close()
        open(os.path.join(cls.source_folder, 'test_file2.txt'), 'w').close()
      
    def test_backup_game_files(self):
        # Test backup_txt method
        self.your_backup_manager.backup_game_files(os.path.join(self.source_folder, 'test_file.txt'))
        self.assertTrue(os.path.exists(os.path.join(self.your_backup_manager.backup_game_file_folder, 'test_file.txt')))
  
    def test_restore_default_with_specific_files(self):        
        self.your_backup_manager.restore_default(self.default_game_file_folder, 'game_test_file1.txt')
        self.assertFalse(os.path.exists(os.path.join(self.your_backup_manager.modded_game_file_folder, 'game_test_file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.your_backup_manager.modded_game_file_folder, 'game_test_file2.txt')))
    
    def test_restore_default_without_specific_files(self):  
        self.your_backup_manager.restore_default(self.default_game_file_folder)
        self.assertFalse(os.path.exists(os.path.join(self.your_backup_manager.modded_game_file_folder, 'game_test_file1.txt')))
        self.assertFalse(os.path.exists(os.path.join(self.your_backup_manager.modded_game_file_folder, 'game_test_file2.txt')))
    
    def test_backup_folder(self):
        # Test backup_folder method
        self.your_backup_manager.backup_folder(self.source_folder, self.backup_folder)
        #self.assertTrue(os.path.exists(os.path.join(self.backup_folder, self.source_folder)))
         
    def tearDown(self):
        # Clean up temporary test folders and files
        #shutil.rmtree(os.path.abspath(self.default_game_file_folder), ignore_errors=True)
        shutil.rmtree(os.path.abspath(self.source_folder), ignore_errors=True)
        shutil.rmtree(os.path.abspath(self.backup_folder), ignore_errors=True)
        
if __name__ == '__main__':
    unittest.main()

