# coding: utf-8
from django.test import TestCase
from django.core.exceptions import ValidationError

from eventex.core.models import Speaker
from eventex.core.models import Contact


class SpeakerModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker(
            name='Fellipe Castro',
            slug='fellipe-castro',
            url='http://fellipecastro.com',
            description='Passionate software developer!')
        self.speaker.save()

    def test_create(self):
        'Speaker instance should be saved.'
        self.assertEqual(1, self.speaker.pk)

    def test_unicode(self):
        'Speaker string representation should be the name.'
        self.assertEqual(u'Fellipe Castro', unicode(self.speaker))


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Fellipe Castro',
            slug='fellipe-castro',
            url='http://fellipecastro.com',
            description='Passionate software developer!')

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='E',
            value='contact@fellipecastro.com')
        self.assertEqual(1, contact.pk)

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='P',
            value='21-996186180')
        self.assertEqual(1, contact.pk)

    def test_fax(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind='F',
            value='21-12345678')
        self.assertEqual(1, contact.pk)

    def test_kind(self):
        'Contact kind should be limited to E, P or F.'
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_unicode(self):
        'Contact string representation should be value'
        contact = Contact(
            speaker=self.speaker,
            kind='E',
            value='contact@fellipecastro.com')
        self.assertEqual(u'contact@fellipecastro.com', unicode(contact))
