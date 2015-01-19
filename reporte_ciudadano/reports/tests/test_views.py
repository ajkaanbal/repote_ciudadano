# -*- coding: utf-8 -*-
import json
from django.core.urlresolvers import reverse
from django.utils.http import urlencode
from django.test import TestCase

from reports.models import Report
# Create your tests here.


class ReportsApiTests(TestCase):
    def setUp(self):

        report_1 = {
            'kind': 0,
            'description': u'Yo propongo que...',
            'address': u'Colima, México',
            'name': 'Juan Perez',
            'email': 'juan@perez.com',
            'phone': '5555555555'
        }

        report_2 = {
            'kind': 1,
            'description': u'Yo sueño que...',
            'address': u'Colima, Colima',
            'name': u'Miguel Juarez',
            'email': 'miguel@mail.com',
            'phone': '4444444444'
        }

        Report.objects.get_or_create(**report_1)
        Report.objects.get_or_create(**report_2)

    def test_create(self):
        data = {
            'kind': 1,
            'description': u'Yo sueño con...',
            'address': u'Colima, México',
            'name': u'María Lopez',
            'email': 'maria@mail.com',
            'phone': '55555555'
        }
        create_url = reverse('report-list')
        response = self.client.post(create_url, data)
        data_response = json.loads(response.content)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(data_response.get('kind'), data.get('kind'))
        self.assertEquals(data_response.get('description'), data.get('description'))
        self.assertEquals(data_response.get('address'), data.get('address'))
        self.assertEquals(data_response.get('name'), data.get('name'))
        self.assertEquals(data_response.get('email'), data.get('email'))
        self.assertEquals(data_response.get('phone'), data.get('phone'))

    def test_list(self):
        list_url = reverse('report-list')
        response = self.client.get(list_url)

        self.assertEquals(Report.objects.count(), 2)
        self.assertContains(response, 'Miguel Juarez')
        self.assertContains(response, 'Juan Perez')

    def test_detail(self):

        data = {
            'kind': 0,
            'description': u'Yo propongo que...',
            'address': u'Colima, México',
            'name': 'Juan Perez',
            'email': 'juan@perez.com',
            'phone': '5555555555'
        }

        details_url = reverse('report-detail', args=[1])
        response = self.client.get(details_url)
        data_response = json.loads(response.content)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(data_response.get('kind'), data.get('kind'))
        self.assertEquals(data_response.get('description'), data.get('description'))
        self.assertEquals(data_response.get('address'), data.get('address'))
        self.assertEquals(data_response.get('name'), data.get('name'))
        self.assertEquals(data_response.get('email'), data.get('email'))
        self.assertEquals(data_response.get('phone'), data.get('phone'))

    def test_delete(self):
        delete_url = reverse('report-detail', args=[1])
        response = self.client.delete(delete_url)
        self.assertEquals(response.status_code, 204)
        self.assertEquals(Report.objects.count(), 1)

    def test_update(self):
        update_url = reverse('report-detail', args=[1])
        data = {
            'kind': 0,
            'description': u'Yo propongo que...',
            'address': u'Colima, México',
            'name': u'Rubén Jimenez',
            'email': 'ruben@mail.com',
            'phone': '5454545454'
        }
        encoded_data = urlencode(data)
        response = self.client.put(
            update_url,
            encoded_data,
            content_type='application/x-www-form-urlencoded'
        )
        data_response = json.loads(response.content)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Report.objects.count(), 2)
        self.assertEquals(data_response.get('name'), data.get('name'))
        self.assertEquals(data_response.get('email'), data.get('email'))
        self.assertEquals(data_response.get('phone'), data.get('phone'))
