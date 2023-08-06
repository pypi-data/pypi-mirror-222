# -*- coding: utf-8 -*-
import json
from copy import deepcopy
from typing import Any

import azure.functions as func
from pip_services4_commons.convert import TypeCode
from pip_services4_components.refer import Descriptor, IReferences
from pip_services4_data.query import FilterParams, PagingParams
from pip_services4_data.validate import ObjectSchema, FilterParamsSchema, PagingParamsSchema

from pip_services4_azure.services.AzureFunctionController import AzureFunctionController
from test.Dummy import Dummy
from test.DummySchema import DummySchema
from test.IDummyService import IDummyService


class DummyAzureFunctionController(AzureFunctionController):

    def __init__(self):
        super(DummyAzureFunctionController, self).__init__('dummies')

        self.__service: IDummyService = None
        self.__headers: dict = {'Content-Type': 'application/json'}

        self._dependency_resolver.put('service',
                                      Descriptor('pip-services-dummies', 'service', 'default', '*', '*'))

    def _get_body_data(self, context: func.HttpRequest) -> dict:
        params = deepcopy(context.get_body())

        if params:
            params = json.loads(params)
        return params

    def set_references(self, references: IReferences):
        super(DummyAzureFunctionController, self).set_references(references)
        self.__service = self._dependency_resolver.get_one_required('service')

    def __get_page_by_filter(self, params: func.HttpRequest) -> func.HttpResponse:
        params = self._get_body_data(params)
        page = self.__service.get_page_by_filter(
            params.get('trace_id'),
            FilterParams.from_value(params.get('filter')),
            PagingParams.from_value(params.get('paging'))
        )

        page.data = list(map(lambda d: json.dumps(d.to_dict()), page.data))
        return func.HttpResponse(body=json.dumps(page.to_json()), headers=self.__headers)

    def __get_one_by_id(self, params: func.HttpRequest) -> func.HttpResponse:
        params = self._get_body_data(params)
        dummy = self.__service.get_one_by_id(
            params.get('trace_id'),
            params.get('dummy_id')
        )
        json_dummy = None if not dummy else json.dumps(dummy.to_dict())
        return func.HttpResponse(body=json_dummy, headers=self.__headers)

    def __create(self, params: func.HttpRequest) -> func.HttpResponse:
        params = self._get_body_data(params)
        dummy = self.__service.create(
            params.get('trace_id'),
            Dummy(**params.get('dummy'))
        )
        return func.HttpResponse(body=json.dumps(dummy.to_dict()), headers=self.__headers)

    def __update(self, params: func.HttpRequest) -> func.HttpResponse:
        params = self._get_body_data(params)
        dummy = self.__service.update(
            params.get('trace_id'),
            Dummy(**params.get('dummy'))
        )
        return func.HttpResponse(body=json.dumps(dummy.to_dict()), headers=self.__headers)

    def __delete_by_id(self, params: func.HttpRequest) -> func.HttpResponse:
        params = self._get_body_data(params)
        dummy = self.__service.delete_by_id(
            params.get('trace_id'),
            params.get('dummy_id'),
        )
        return func.HttpResponse(body=json.dumps(dummy.to_dict()), headers=self.__headers)

    def register(self):
        self._register_action(
            'get_dummies',
            ObjectSchema(True).with_optional_property('body',
                                                      ObjectSchema(True)
                                                      .with_optional_property("filter", FilterParamsSchema())
                                                      .with_optional_property("paging", PagingParamsSchema())
                                                      )
            , self.__get_page_by_filter
        )

        self._register_action(
            'get_dummy_by_id',
            ObjectSchema(True).with_optional_property("body",
                                                      ObjectSchema(True)
                                                      .with_optional_property("dummy_id", TypeCode.String)
                                                      ),
            self.__get_one_by_id)

        self._register_action(
            'create_dummy',
            ObjectSchema(True).with_required_property("body",
                                                      ObjectSchema(True)
                                                      .with_required_property("dummy", DummySchema())
                                                      ),
            self.__create)

        self._register_action(
            'update_dummy',
            ObjectSchema(True).with_optional_property("body",
                                                      ObjectSchema(True)
                                                      .with_optional_property("dummy", DummySchema())
                                                      ),
            self.__update)

        self._register_action(
            'delete_dummy',
            ObjectSchema(True).with_optional_property("body",
                                                      ObjectSchema(True)
                                                      .with_optional_property("dummy_id", TypeCode.String)
                                                      ),
            self.__delete_by_id)
