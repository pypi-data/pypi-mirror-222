import unittest
import os
import uuid
import random
import shutil

from drb.topics import resolver
from drb.topics.dao import ManagerDao
from drb.metadata import DrbMetadataResolver


class TestFileMetadata(unittest.TestCase):
    file_topic_id = None
    file_topic = None
    md_resolver = None
    resource_dir = None

    @classmethod
    def setUpClass(cls) -> None:
        mng = ManagerDao()
        cls.md_resolver = DrbMetadataResolver()

        cls.file_topic_id = '99e6ce18-276f-11ec-9621-0242ac130002'
        cls.file_topic = mng.get_drb_topic(uuid.UUID(cls.file_topic_id))

        cls.resource_dir = os.path.join(os.getcwd(), 'resources')
        os.mkdir(cls.resource_dir)

        cls.resource_file = os.path.join(cls.resource_dir, 'file.data')
        with open(cls.resource_file, 'wb') as file:
            file.write(os.urandom(25))

    @classmethod
    def tearDownClass(cls) -> None:
        if cls.resource_dir is not None:
            shutil.rmtree(cls.resource_dir)

    def test_file_metadata(self):
        path = self.resource_file
        topic, node = resolver.resolve(path)

        self.assertEqual(self.file_topic.id, topic.id)
        metadata = self.md_resolver.get_metadata(node, topic=topic)
        self.assertEqual(10, len(metadata.keys()))

        expected = node.name
        self.assertEqual(expected, metadata['name'].extract(node))

        expected = node @ 'size'
        self.assertEqual(expected, metadata['size'].extract(node))

        expected = node @ 'mode'
        self.assertEqual(expected, metadata['type'].extract(node))

        expected = node @ 'creation_time'
        self.assertEqual(expected, metadata['creationTime'].extract(node))

        expected = node @ 'last_modification_time'
        self.assertEqual(expected, metadata['modificationTime'].extract(node))

        expected = node @ 'last_access_time'
        self.assertEqual(expected, metadata['lastAccessTime'].extract(node))

        expected = node @ 'owner'
        self.assertEqual(expected, metadata['owner'].extract(node))

        expected = node @ 'group'
        self.assertEqual(expected, metadata['group'].extract(node))

        expected = node @ 'link_number'
        self.assertEqual(expected, metadata['nlink'].extract(node))

        expected = node @ 'inode'
        self.assertEqual(expected, metadata['inode'].extract(node))

    def test_dir_metadata(self):
        path = self.resource_dir
        topic, node = resolver.resolve(path)

        self.assertEqual(self.file_topic.id, topic.id)
        metadata = self.md_resolver.get_metadata(node, topic=topic)
        self.assertEqual(10, len(metadata.keys()))

        expected = node.name
        self.assertEqual(expected, metadata['name'].extract(node))

        expected = node @ 'size'
        self.assertEqual(expected, metadata['size'].extract(node))

        expected = node @ 'mode'
        self.assertEqual(expected, metadata['type'].extract(node))

        expected = node @ 'creation_time'
        self.assertEqual(expected, metadata['creationTime'].extract(node))

        expected = node @ 'last_modification_time'
        self.assertEqual(expected, metadata['modificationTime'].extract(node))

        expected = node @ 'last_access_time'
        self.assertEqual(expected, metadata['lastAccessTime'].extract(node))

        expected = node @ 'owner'
        self.assertEqual(expected, metadata['owner'].extract(node))

        expected = node @ 'group'
        self.assertEqual(expected, metadata['group'].extract(node))

        expected = node @ 'link_number'
        self.assertEqual(expected, metadata['nlink'].extract(node))

        expected = node @ 'inode'
        self.assertEqual(expected, metadata['inode'].extract(node))
