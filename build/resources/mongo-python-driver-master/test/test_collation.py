# Copyright 2016-present MongoDB, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test the collation module."""

import functools
import warnings

from pymongo import monitoring
from pymongo.collation import (
    Collation,
    CollationCaseFirst, CollationStrength, CollationAlternate,
    CollationMaxVariable)
from pymongo.errors import ConfigurationError
from pymongo.operations import (DeleteMany, DeleteOne, IndexModel, ReplaceOne,
                                UpdateMany, UpdateOne)
from pymongo.write_concern import WriteConcern
from test import unittest, client_context
from test.utils import EventListener, ignore_deprecations, rs_or_single_client


class TestCollationObject(unittest.TestCase):

    def test_constructor(self):
        self.assertRaises(TypeError, Collation, locale=42)
        # Fill in a locale to test the other options.
        _Collation = functools.partial(Collation, 'en_US')
        # No error.
        _Collation(caseFirst=CollationCaseFirst.UPPER)
        self.assertRaises(TypeError, _Collation, caseLevel='true')
        self.assertRaises(ValueError, _Collation, strength='six')
        self.assertRaises(TypeError, _Collation,
                          numericOrdering='true')
        self.assertRaises(TypeError, _Collation, alternate=5)
        self.assertRaises(TypeError, _Collation, maxVariable=2)
        self.assertRaises(TypeError, _Collation, normalization='false')
        self.assertRaises(TypeError, _Collation, backwards='true')

        # No errors.
        Collation('en_US', future_option='bar', another_option=42)
        collation = Collation(
            'en_US',
            caseLevel=True,
            caseFirst=CollationCaseFirst.UPPER,
            strength=CollationStrength.QUATERNARY,
            numericOrdering=True,
            alternate=CollationAlternate.SHIFTED,
            maxVariable=CollationMaxVariable.SPACE,
            normalization=True,
            backwards=True)

        self.assertEqual({
            'locale': 'en_US',
            'caseLevel': True,
            'caseFirst': 'upper',
            'strength': 4,
            'numericOrdering': True,
            'alternate': 'shifted',
            'maxVariable': 'space',
            'normalization': True,
            'backwards': True
        }, collation.document)

        self.assertEqual({
            'locale': 'en_US',
            'backwards': True
        }, Collation('en_US', backwards=True).document)


def raisesConfigurationErrorForOldMongoDB(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if client_context.version.at_least(3, 3, 9):
            return func(self, *args, **kwargs)
        else:
            with self.assertRaises(ConfigurationError):
                return func(self, *args, **kwargs)
    return wrapper


class TestCollation(unittest.TestCase):

    @classmethod
    @client_context.require_connection
    def setUpClass(cls):
        cls.listener = EventListener()
        cls.saved_listeners = monitoring._LISTENERS
        monitoring._LISTENERS = monitoring._Listeners([], [], [], [])
        cls.client = rs_or_single_client(event_listeners=[cls.listener])
        cls.db = cls.client.pymongo_test
        cls.collation = Collation('en_US')
        cls.warn_context = warnings.catch_warnings()
        cls.warn_context.__enter__()
        warnings.simplefilter("ignore", DeprecationWarning)

    @classmethod
    def tearDownClass(cls):
        monitoring._LISTENERS = cls.saved_listeners
        cls.warn_context.__exit__()
        cls.warn_context = None

    def tearDown(self):
        self.listener.results.clear()

    def last_command_started(self):
        return self.listener.results['started'][-1].command

    def assertCollationInLastCommand(self):
        self.assertEqual(
            self.collation.document,
            self.last_command_started()['collation'])

    @raisesConfigurationErrorForOldMongoDB
    def test_create_collection(self):
        self.db.test.drop()
        self.db.create_collection('test', collation=self.collation)
        self.assertCollationInLastCommand()

        # Test passing collation as a dict as well.
        self.db.test.drop()
        self.listener.results.clear()
        self.db.create_collection('test', collation=self.collation.document)
        self.assertCollationInLastCommand()

    def test_index_model(self):
        model = IndexModel([('a', 1), ('b', -1)], collation=self.collation)
        self.assertEqual(self.collation.document, model.document['collation'])

    @raisesConfigurationErrorForOldMongoDB
    def test_create_index(self):
        self.db.test.create_index('foo', collation=self.collation)
        ci_cmd = self.listener.results['started'][0].command
        self.assertEqual(
            self.collation.document,
            ci_cmd['indexes'][0]['collation'])

    @raisesConfigurationErrorForOldMongoDB
    def test_ensure_index(self):
        self.db.test.ensure_index('foo', collation=self.collation)
        ci_cmd = self.listener.results['started'][0].command
        self.assertEqual(
            self.collation.document,
            ci_cmd['indexes'][0]['collation'])

    @raisesConfigurationErrorForOldMongoDB
    def test_aggregate(self):
        self.db.test.aggregate([{'$group': {'_id': 42}}],
                               collation=self.collation)
        self.assertCollationInLastCommand()

    @raisesConfigurationErrorForOldMongoDB
    @ignore_deprecations
    def test_count(self):
        self.db.test.count(collation=self.collation)
        self.assertCollationInLastCommand()

        self.listener.results.clear()
        self.db.test.find(collation=self.collation).count()
        self.assertCollationInLastCommand()

    @raisesConfigurationErrorForOldMongoDB
    def test_count_documents(self):
        self.db.test.count_documents({}, collation=self.collation)
        self.assertCollationInLastCommand()

    @raisesConfigurationErrorForOldMongoDB
    def test_distinct(self):
        self.db.test.distinct('foo', collation=self.collation)
        self.assertCollationInLastCommand()

        self.listener.results.clear()
        self.db.test.find(collation=self.collation).distinct('foo')
        self.assertCollationInLastCommand()

    @raisesConfigurationErrorForOldMongoDB
    def test_find_command(self):
        self.db.test.insert_one({'is this thing on?': True})
        self.listener.results.clear()
        next(self.db.test.find(collation=self.collation))
        self.assertCollationInLastCommand()

    @raisesConfigurationErrorForOldMongoDB
    def test_explain_command(self):
        self.listener.results.clear()
        self.db.test.find(collation=self.collation).explain()
        # The collation should be part of the explained command.
        self.assertEqual(
            self.collation.document,
            self.last_command_started()['explain']['collation'])

    @raisesConfigurationErrorForOldMongoDB
    @client_context.require_version_max(4, 1, 0, -1)
    def test_group(self):
        self.db.test.group('foo', {'foo': {'$gt': 42}}, {},
                           'function(a, b) { return a; }',
                           collation=self.collation)
        self.assertCollationInLastCommand()

    @raisesConfigurationErrorForOldMongoDB
    def test_map_reduce(self):
        self.db.test.map_reduce('function() {}', 'function() {}', 'output',
                                collation=self.collation)
        self.assertCollationInLastCommand()

    @raisesConfigurationErrorForOldMongoDB
    def test_delete(self):
        self.db.test.delete_one({'foo': 42}, collation=self.collation)
        command = self.listener.results['started'][0].command
        self.assertEqual(
            self.collation.document,
            command['deletes'][0]['collation'])

        self.listener.results.clear()
        self.db.test.delete_many({'foo': 42}, collation=self.collation)
        command = self.listener.results['started'][0].command
        self.assertEqual(
            self.collation.document,
            command['deletes'][0]['collation'])

        self.listener.results.clear()
        self.db.test.remove({'foo': 42}, collation=self.collation)
        command = self.listener.results['started'][0].command
        self.assertEqual(
            self.collation.document,
            command['deletes'][0]['collation'])

    @raisesConfigurationErrorForOldMongoDB
    def test_update(self):
        self.db.test.update({'foo': 42}, {'$set': {'foo': 'bar'}},
                            collation=self.collation)
        command = self.listener.results['started'][0].command
        self.assertEqual(
            self.collation.document,
            command['updates'][0]['collation'])

        self.listener.results.clear()
        self.db.test.save({'_id': 12345}, collation=self.collation)
        command = self.listener.results['started'][0].command
        self.assertEqual(
            self.collation.document,
            command['updates'][0]['collation'])

        self.listener.results.clear()
        self.db.test.replace_one({'foo': 42}, {'foo': 43},
                                 collation=self.collation)
        command = self.listener.results['started'][0].command
        self.assertEqual(
            self.collation.document,
            command['updates'][0]['collation'])

        self.listener.results.clear()
        self.db.test.update_one({'foo': 42}, {'$set': {'foo': 43}},
                                collation=self.collation)
        command = self.listener.results['started'][0].command
        self.assertEqual(
            self.collation.document,
            command['updates'][0]['collation'])

        self.listener.results.clear()
        self.db.test.update_many({'foo': 42}, {'$set': {'foo': 43}},
                                 collation=self.collation)
        command = self.listener.results['started'][0].command
        self.assertEqual(
            self.collation.document,
            command['updates'][0]['collation'])

    @raisesConfigurationErrorForOldMongoDB
    def test_find_and(self):
        self.db.test.find_and_modify({'foo': 42}, {'$set': {'foo': 43}},
                                     collation=self.collation)
        self.assertCollationInLastCommand()

        self.listener.results.clear()
        self.db.test.find_one_and_delete({'foo': 42}, collation=self.collation)
        self.assertCollationInLastCommand()

        self.listener.results.clear()
        self.db.test.find_one_and_update({'foo': 42}, {'$set': {'foo': 43}},
                                         collation=self.collation)
        self.assertCollationInLastCommand()

        self.listener.results.clear()
        self.db.test.find_one_and_replace({'foo': 42}, {'foo': 43},
                                          collation=self.collation)
        self.assertCollationInLastCommand()

    @raisesConfigurationErrorForOldMongoDB
    def test_bulk_write(self):
        self.db.test.collection.bulk_write([
            DeleteOne({'noCollation': 42}),
            DeleteMany({'noCollation': 42}),
            DeleteOne({'foo': 42}, collation=self.collation),
            DeleteMany({'foo': 42}, collation=self.collation),
            ReplaceOne({'noCollation': 24}, {'bar': 42}),
            UpdateOne({'noCollation': 84}, {'$set': {'bar': 10}}, upsert=True),
            UpdateMany({'noCollation': 45}, {'$set': {'bar': 42}}),
            ReplaceOne({'foo': 24}, {'foo': 42}, collation=self.collation),
            UpdateOne({'foo': 84}, {'$set': {'foo': 10}}, upsert=True,
                      collation=self.collation),
            UpdateMany({'foo': 45}, {'$set': {'foo': 42}},
                       collation=self.collation)
        ])

        delete_cmd = self.listener.results['started'][0].command
        update_cmd = self.listener.results['started'][1].command

        def check_ops(ops):
            for op in ops:
                if 'noCollation' in op['q']:
                    self.assertNotIn('collation', op)
                else:
                    self.assertEqual(self.collation.document,
                                     op['collation'])

        check_ops(delete_cmd['deletes'])
        check_ops(update_cmd['updates'])

    @raisesConfigurationErrorForOldMongoDB
    def test_bulk(self):
        bulk = self.db.test.initialize_ordered_bulk_op()
        bulk.find({'noCollation': 42}).remove_one()
        bulk.find({'noCollation': 42}).remove()
        bulk.find({'foo': 42}, collation=self.collation).remove_one()
        bulk.find({'foo': 42}, collation=self.collation).remove()
        bulk.find({'noCollation': 24}).replace_one({'bar': 42})
        bulk.find({'noCollation': 84}).upsert().update_one(
            {'$set': {'foo': 10}})
        bulk.find({'noCollation': 45}).update({'$set': {'bar': 42}})
        bulk.find({'foo': 24}, collation=self.collation).replace_one(
            {'foo': 42})
        bulk.find({'foo': 84}, collation=self.collation).upsert().update_one(
            {'$set': {'foo': 10}})
        bulk.find({'foo': 45}, collation=self.collation).update({
            '$set': {'foo': 42}})
        bulk.execute()

        delete_cmd = self.listener.results['started'][0].command
        update_cmd = self.listener.results['started'][1].command

        def check_ops(ops):
            for op in ops:
                if 'noCollation' in op['q']:
                    self.assertNotIn('collation', op)
                else:
                    self.assertEqual(self.collation.document,
                                     op['collation'])

        check_ops(delete_cmd['deletes'])
        check_ops(update_cmd['updates'])

    @client_context.require_version_max(3, 3, 8)
    def test_mixed_bulk_collation(self):
        bulk = self.db.test.initialize_unordered_bulk_op()
        bulk.find({'foo': 42}).upsert().update_one(
            {'$set': {'bar': 10}})
        bulk.find({'foo': 43}, collation=self.collation).remove_one()
        with self.assertRaises(ConfigurationError):
            bulk.execute()
        self.assertIsNone(self.db.test.find_one({'foo': 42}))

    @raisesConfigurationErrorForOldMongoDB
    def test_indexes_same_keys_different_collations(self):
        self.db.test.drop()
        usa_collation = Collation('en_US')
        ja_collation = Collation('ja')
        self.db.test.create_indexes([
            IndexModel('fieldname', collation=usa_collation),
            IndexModel('fieldname', name='japanese_version',
                       collation=ja_collation),
            IndexModel('fieldname', name='simple')
        ])
        indexes = self.db.test.index_information()
        self.assertEqual(usa_collation.document['locale'],
                         indexes['fieldname_1']['collation']['locale'])
        self.assertEqual(ja_collation.document['locale'],
                         indexes['japanese_version']['collation']['locale'])
        self.assertNotIn('collation', indexes['simple'])
        self.db.test.drop_index('fieldname_1')
        indexes = self.db.test.index_information()
        self.assertIn('japanese_version', indexes)
        self.assertIn('simple', indexes)
        self.assertNotIn('fieldname', indexes)

    def test_unacknowledged_write(self):
        unacknowledged = WriteConcern(w=0)
        collection = self.db.get_collection(
            'test', write_concern=unacknowledged)
        with self.assertRaises(ConfigurationError):
            collection.update_one(
                {'hello': 'world'}, {'$set': {'hello': 'moon'}},
                collation=self.collation)
        bulk = collection.initialize_ordered_bulk_op()
        bulk.find({'hello': 'world'}, collation=self.collation).update_one(
            {'$set': {'hello': 'moon'}})
        with self.assertRaises(ConfigurationError):
            bulk.execute()
        update_one = UpdateOne({'hello': 'world'}, {'$set': {'hello': 'moon'}},
                               collation=self.collation)
        with self.assertRaises(ConfigurationError):
            collection.bulk_write([update_one])

    @raisesConfigurationErrorForOldMongoDB
    def test_cursor_collation(self):
        self.db.test.insert_one({'hello': 'world'})
        next(self.db.test.find().collation(self.collation))
        self.assertCollationInLastCommand()
