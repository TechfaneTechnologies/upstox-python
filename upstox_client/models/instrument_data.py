# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InstrumentData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'segment': 'str',
        'exchange': 'str',
        'isin': 'str',
        'expiry': 'datetime',
        'country': 'str',
        'latency': 'str',
        'description': 'str',
        'currency': 'str',
        'weekly': 'bool',
        'instrument_key': 'str',
        'exchange_token': 'str',
        'trading_symbol': 'str',
        'short_name': 'str',
        'tick_size': 'float',
        'lot_size': 'int',
        'instrument_type': 'str',
        'freeze_quantity': 'float',
        'underlying_key': 'str',
        'underlying_type': 'str',
        'underlying_symbol': 'str',
        'last_trading_date': 'datetime',
        'strike_price': 'float',
        'price_quote_unit': 'str',
        'qty_multiplier': 'int',
        'minimum_lot': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'week_days': 'str',
        'general_denominator': 'float',
        'general_numerator': 'float',
        'price_numerator': 'float',
        'price_denominator': 'float',
        'mtf_enabled': 'bool',
        'mtf_bracket': 'float',
        'security_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'segment': 'segment',
        'exchange': 'exchange',
        'isin': 'isin',
        'expiry': 'expiry',
        'country': 'country',
        'latency': 'latency',
        'description': 'description',
        'currency': 'currency',
        'weekly': 'weekly',
        'instrument_key': 'instrument_key',
        'exchange_token': 'exchange_token',
        'trading_symbol': 'trading_symbol',
        'short_name': 'short_name',
        'tick_size': 'tick_size',
        'lot_size': 'lot_size',
        'instrument_type': 'instrument_type',
        'freeze_quantity': 'freeze_quantity',
        'underlying_key': 'underlying_key',
        'underlying_type': 'underlying_type',
        'underlying_symbol': 'underlying_symbol',
        'last_trading_date': 'last_trading_date',
        'strike_price': 'strike_price',
        'price_quote_unit': 'price_quote_unit',
        'qty_multiplier': 'qty_multiplier',
        'minimum_lot': 'minimum_lot',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'week_days': 'week_days',
        'general_denominator': 'general_denominator',
        'general_numerator': 'general_numerator',
        'price_numerator': 'price_numerator',
        'price_denominator': 'price_denominator',
        'mtf_enabled': 'mtf_enabled',
        'mtf_bracket': 'mtf_bracket',
        'security_type': 'security_type'
    }

    def __init__(self, name=None, segment=None, exchange=None, isin=None, expiry=None, country=None, latency=None, description=None, currency=None, weekly=None, instrument_key=None, exchange_token=None, trading_symbol=None, short_name=None, tick_size=None, lot_size=None, instrument_type=None, freeze_quantity=None, underlying_key=None, underlying_type=None, underlying_symbol=None, last_trading_date=None, strike_price=None, price_quote_unit=None, qty_multiplier=None, minimum_lot=None, start_time=None, end_time=None, week_days=None, general_denominator=None, general_numerator=None, price_numerator=None, price_denominator=None, mtf_enabled=None, mtf_bracket=None, security_type=None):  # noqa: E501
        """InstrumentData - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._segment = None
        self._exchange = None
        self._isin = None
        self._expiry = None
        self._country = None
        self._latency = None
        self._description = None
        self._currency = None
        self._weekly = None
        self._instrument_key = None
        self._exchange_token = None
        self._trading_symbol = None
        self._short_name = None
        self._tick_size = None
        self._lot_size = None
        self._instrument_type = None
        self._freeze_quantity = None
        self._underlying_key = None
        self._underlying_type = None
        self._underlying_symbol = None
        self._last_trading_date = None
        self._strike_price = None
        self._price_quote_unit = None
        self._qty_multiplier = None
        self._minimum_lot = None
        self._start_time = None
        self._end_time = None
        self._week_days = None
        self._general_denominator = None
        self._general_numerator = None
        self._price_numerator = None
        self._price_denominator = None
        self._mtf_enabled = None
        self._mtf_bracket = None
        self._security_type = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if segment is not None:
            self.segment = segment
        if exchange is not None:
            self.exchange = exchange
        if isin is not None:
            self.isin = isin
        if expiry is not None:
            self.expiry = expiry
        if country is not None:
            self.country = country
        if latency is not None:
            self.latency = latency
        if description is not None:
            self.description = description
        if currency is not None:
            self.currency = currency
        if weekly is not None:
            self.weekly = weekly
        if instrument_key is not None:
            self.instrument_key = instrument_key
        if exchange_token is not None:
            self.exchange_token = exchange_token
        if trading_symbol is not None:
            self.trading_symbol = trading_symbol
        if short_name is not None:
            self.short_name = short_name
        if tick_size is not None:
            self.tick_size = tick_size
        if lot_size is not None:
            self.lot_size = lot_size
        if instrument_type is not None:
            self.instrument_type = instrument_type
        if freeze_quantity is not None:
            self.freeze_quantity = freeze_quantity
        if underlying_key is not None:
            self.underlying_key = underlying_key
        if underlying_type is not None:
            self.underlying_type = underlying_type
        if underlying_symbol is not None:
            self.underlying_symbol = underlying_symbol
        if last_trading_date is not None:
            self.last_trading_date = last_trading_date
        if strike_price is not None:
            self.strike_price = strike_price
        if price_quote_unit is not None:
            self.price_quote_unit = price_quote_unit
        if qty_multiplier is not None:
            self.qty_multiplier = qty_multiplier
        if minimum_lot is not None:
            self.minimum_lot = minimum_lot
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if week_days is not None:
            self.week_days = week_days
        if general_denominator is not None:
            self.general_denominator = general_denominator
        if general_numerator is not None:
            self.general_numerator = general_numerator
        if price_numerator is not None:
            self.price_numerator = price_numerator
        if price_denominator is not None:
            self.price_denominator = price_denominator
        if mtf_enabled is not None:
            self.mtf_enabled = mtf_enabled
        if mtf_bracket is not None:
            self.mtf_bracket = mtf_bracket
        if security_type is not None:
            self.security_type = security_type

    @property
    def name(self):
        """Gets the name of this InstrumentData.  # noqa: E501


        :return: The name of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstrumentData.


        :param name: The name of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def segment(self):
        """Gets the segment of this InstrumentData.  # noqa: E501


        :return: The segment of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._segment

    @segment.setter
    def segment(self, segment):
        """Sets the segment of this InstrumentData.


        :param segment: The segment of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._segment = segment

    @property
    def exchange(self):
        """Gets the exchange of this InstrumentData.  # noqa: E501


        :return: The exchange of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this InstrumentData.


        :param exchange: The exchange of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def isin(self):
        """Gets the isin of this InstrumentData.  # noqa: E501


        :return: The isin of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this InstrumentData.


        :param isin: The isin of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._isin = isin

    @property
    def expiry(self):
        """Gets the expiry of this InstrumentData.  # noqa: E501


        :return: The expiry of this InstrumentData.  # noqa: E501
        :rtype: datetime
        """
        return self._expiry

    @expiry.setter
    def expiry(self, expiry):
        """Sets the expiry of this InstrumentData.


        :param expiry: The expiry of this InstrumentData.  # noqa: E501
        :type: datetime
        """

        self._expiry = expiry

    @property
    def country(self):
        """Gets the country of this InstrumentData.  # noqa: E501


        :return: The country of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this InstrumentData.


        :param country: The country of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def latency(self):
        """Gets the latency of this InstrumentData.  # noqa: E501


        :return: The latency of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._latency

    @latency.setter
    def latency(self, latency):
        """Sets the latency of this InstrumentData.


        :param latency: The latency of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._latency = latency

    @property
    def description(self):
        """Gets the description of this InstrumentData.  # noqa: E501


        :return: The description of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this InstrumentData.


        :param description: The description of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def currency(self):
        """Gets the currency of this InstrumentData.  # noqa: E501


        :return: The currency of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InstrumentData.


        :param currency: The currency of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def weekly(self):
        """Gets the weekly of this InstrumentData.  # noqa: E501


        :return: The weekly of this InstrumentData.  # noqa: E501
        :rtype: bool
        """
        return self._weekly

    @weekly.setter
    def weekly(self, weekly):
        """Sets the weekly of this InstrumentData.


        :param weekly: The weekly of this InstrumentData.  # noqa: E501
        :type: bool
        """

        self._weekly = weekly

    @property
    def instrument_key(self):
        """Gets the instrument_key of this InstrumentData.  # noqa: E501


        :return: The instrument_key of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._instrument_key

    @instrument_key.setter
    def instrument_key(self, instrument_key):
        """Sets the instrument_key of this InstrumentData.


        :param instrument_key: The instrument_key of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._instrument_key = instrument_key

    @property
    def exchange_token(self):
        """Gets the exchange_token of this InstrumentData.  # noqa: E501


        :return: The exchange_token of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._exchange_token

    @exchange_token.setter
    def exchange_token(self, exchange_token):
        """Sets the exchange_token of this InstrumentData.


        :param exchange_token: The exchange_token of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._exchange_token = exchange_token

    @property
    def trading_symbol(self):
        """Gets the trading_symbol of this InstrumentData.  # noqa: E501


        :return: The trading_symbol of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._trading_symbol

    @trading_symbol.setter
    def trading_symbol(self, trading_symbol):
        """Sets the trading_symbol of this InstrumentData.


        :param trading_symbol: The trading_symbol of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._trading_symbol = trading_symbol

    @property
    def short_name(self):
        """Gets the short_name of this InstrumentData.  # noqa: E501


        :return: The short_name of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """Sets the short_name of this InstrumentData.


        :param short_name: The short_name of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._short_name = short_name

    @property
    def tick_size(self):
        """Gets the tick_size of this InstrumentData.  # noqa: E501


        :return: The tick_size of this InstrumentData.  # noqa: E501
        :rtype: float
        """
        return self._tick_size

    @tick_size.setter
    def tick_size(self, tick_size):
        """Sets the tick_size of this InstrumentData.


        :param tick_size: The tick_size of this InstrumentData.  # noqa: E501
        :type: float
        """

        self._tick_size = tick_size

    @property
    def lot_size(self):
        """Gets the lot_size of this InstrumentData.  # noqa: E501


        :return: The lot_size of this InstrumentData.  # noqa: E501
        :rtype: int
        """
        return self._lot_size

    @lot_size.setter
    def lot_size(self, lot_size):
        """Sets the lot_size of this InstrumentData.


        :param lot_size: The lot_size of this InstrumentData.  # noqa: E501
        :type: int
        """

        self._lot_size = lot_size

    @property
    def instrument_type(self):
        """Gets the instrument_type of this InstrumentData.  # noqa: E501


        :return: The instrument_type of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._instrument_type

    @instrument_type.setter
    def instrument_type(self, instrument_type):
        """Sets the instrument_type of this InstrumentData.


        :param instrument_type: The instrument_type of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._instrument_type = instrument_type

    @property
    def freeze_quantity(self):
        """Gets the freeze_quantity of this InstrumentData.  # noqa: E501


        :return: The freeze_quantity of this InstrumentData.  # noqa: E501
        :rtype: float
        """
        return self._freeze_quantity

    @freeze_quantity.setter
    def freeze_quantity(self, freeze_quantity):
        """Sets the freeze_quantity of this InstrumentData.


        :param freeze_quantity: The freeze_quantity of this InstrumentData.  # noqa: E501
        :type: float
        """

        self._freeze_quantity = freeze_quantity

    @property
    def underlying_key(self):
        """Gets the underlying_key of this InstrumentData.  # noqa: E501


        :return: The underlying_key of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._underlying_key

    @underlying_key.setter
    def underlying_key(self, underlying_key):
        """Sets the underlying_key of this InstrumentData.


        :param underlying_key: The underlying_key of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._underlying_key = underlying_key

    @property
    def underlying_type(self):
        """Gets the underlying_type of this InstrumentData.  # noqa: E501


        :return: The underlying_type of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._underlying_type

    @underlying_type.setter
    def underlying_type(self, underlying_type):
        """Sets the underlying_type of this InstrumentData.


        :param underlying_type: The underlying_type of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._underlying_type = underlying_type

    @property
    def underlying_symbol(self):
        """Gets the underlying_symbol of this InstrumentData.  # noqa: E501


        :return: The underlying_symbol of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._underlying_symbol

    @underlying_symbol.setter
    def underlying_symbol(self, underlying_symbol):
        """Sets the underlying_symbol of this InstrumentData.


        :param underlying_symbol: The underlying_symbol of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._underlying_symbol = underlying_symbol

    @property
    def last_trading_date(self):
        """Gets the last_trading_date of this InstrumentData.  # noqa: E501


        :return: The last_trading_date of this InstrumentData.  # noqa: E501
        :rtype: datetime
        """
        return self._last_trading_date

    @last_trading_date.setter
    def last_trading_date(self, last_trading_date):
        """Sets the last_trading_date of this InstrumentData.


        :param last_trading_date: The last_trading_date of this InstrumentData.  # noqa: E501
        :type: datetime
        """

        self._last_trading_date = last_trading_date

    @property
    def strike_price(self):
        """Gets the strike_price of this InstrumentData.  # noqa: E501


        :return: The strike_price of this InstrumentData.  # noqa: E501
        :rtype: float
        """
        return self._strike_price

    @strike_price.setter
    def strike_price(self, strike_price):
        """Sets the strike_price of this InstrumentData.


        :param strike_price: The strike_price of this InstrumentData.  # noqa: E501
        :type: float
        """

        self._strike_price = strike_price

    @property
    def price_quote_unit(self):
        """Gets the price_quote_unit of this InstrumentData.  # noqa: E501


        :return: The price_quote_unit of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._price_quote_unit

    @price_quote_unit.setter
    def price_quote_unit(self, price_quote_unit):
        """Sets the price_quote_unit of this InstrumentData.


        :param price_quote_unit: The price_quote_unit of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._price_quote_unit = price_quote_unit

    @property
    def qty_multiplier(self):
        """Gets the qty_multiplier of this InstrumentData.  # noqa: E501


        :return: The qty_multiplier of this InstrumentData.  # noqa: E501
        :rtype: int
        """
        return self._qty_multiplier

    @qty_multiplier.setter
    def qty_multiplier(self, qty_multiplier):
        """Sets the qty_multiplier of this InstrumentData.


        :param qty_multiplier: The qty_multiplier of this InstrumentData.  # noqa: E501
        :type: int
        """

        self._qty_multiplier = qty_multiplier

    @property
    def minimum_lot(self):
        """Gets the minimum_lot of this InstrumentData.  # noqa: E501


        :return: The minimum_lot of this InstrumentData.  # noqa: E501
        :rtype: int
        """
        return self._minimum_lot

    @minimum_lot.setter
    def minimum_lot(self, minimum_lot):
        """Sets the minimum_lot of this InstrumentData.


        :param minimum_lot: The minimum_lot of this InstrumentData.  # noqa: E501
        :type: int
        """

        self._minimum_lot = minimum_lot

    @property
    def start_time(self):
        """Gets the start_time of this InstrumentData.  # noqa: E501


        :return: The start_time of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InstrumentData.


        :param start_time: The start_time of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this InstrumentData.  # noqa: E501


        :return: The end_time of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this InstrumentData.


        :param end_time: The end_time of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._end_time = end_time

    @property
    def week_days(self):
        """Gets the week_days of this InstrumentData.  # noqa: E501


        :return: The week_days of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._week_days

    @week_days.setter
    def week_days(self, week_days):
        """Sets the week_days of this InstrumentData.


        :param week_days: The week_days of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._week_days = week_days

    @property
    def general_denominator(self):
        """Gets the general_denominator of this InstrumentData.  # noqa: E501


        :return: The general_denominator of this InstrumentData.  # noqa: E501
        :rtype: float
        """
        return self._general_denominator

    @general_denominator.setter
    def general_denominator(self, general_denominator):
        """Sets the general_denominator of this InstrumentData.


        :param general_denominator: The general_denominator of this InstrumentData.  # noqa: E501
        :type: float
        """

        self._general_denominator = general_denominator

    @property
    def general_numerator(self):
        """Gets the general_numerator of this InstrumentData.  # noqa: E501


        :return: The general_numerator of this InstrumentData.  # noqa: E501
        :rtype: float
        """
        return self._general_numerator

    @general_numerator.setter
    def general_numerator(self, general_numerator):
        """Sets the general_numerator of this InstrumentData.


        :param general_numerator: The general_numerator of this InstrumentData.  # noqa: E501
        :type: float
        """

        self._general_numerator = general_numerator

    @property
    def price_numerator(self):
        """Gets the price_numerator of this InstrumentData.  # noqa: E501


        :return: The price_numerator of this InstrumentData.  # noqa: E501
        :rtype: float
        """
        return self._price_numerator

    @price_numerator.setter
    def price_numerator(self, price_numerator):
        """Sets the price_numerator of this InstrumentData.


        :param price_numerator: The price_numerator of this InstrumentData.  # noqa: E501
        :type: float
        """

        self._price_numerator = price_numerator

    @property
    def price_denominator(self):
        """Gets the price_denominator of this InstrumentData.  # noqa: E501


        :return: The price_denominator of this InstrumentData.  # noqa: E501
        :rtype: float
        """
        return self._price_denominator

    @price_denominator.setter
    def price_denominator(self, price_denominator):
        """Sets the price_denominator of this InstrumentData.


        :param price_denominator: The price_denominator of this InstrumentData.  # noqa: E501
        :type: float
        """

        self._price_denominator = price_denominator

    @property
    def mtf_enabled(self):
        """Gets the mtf_enabled of this InstrumentData.  # noqa: E501


        :return: The mtf_enabled of this InstrumentData.  # noqa: E501
        :rtype: bool
        """
        return self._mtf_enabled

    @mtf_enabled.setter
    def mtf_enabled(self, mtf_enabled):
        """Sets the mtf_enabled of this InstrumentData.


        :param mtf_enabled: The mtf_enabled of this InstrumentData.  # noqa: E501
        :type: bool
        """

        self._mtf_enabled = mtf_enabled

    @property
    def mtf_bracket(self):
        """Gets the mtf_bracket of this InstrumentData.  # noqa: E501


        :return: The mtf_bracket of this InstrumentData.  # noqa: E501
        :rtype: float
        """
        return self._mtf_bracket

    @mtf_bracket.setter
    def mtf_bracket(self, mtf_bracket):
        """Sets the mtf_bracket of this InstrumentData.


        :param mtf_bracket: The mtf_bracket of this InstrumentData.  # noqa: E501
        :type: float
        """

        self._mtf_bracket = mtf_bracket

    @property
    def security_type(self):
        """Gets the security_type of this InstrumentData.  # noqa: E501


        :return: The security_type of this InstrumentData.  # noqa: E501
        :rtype: str
        """
        return self._security_type

    @security_type.setter
    def security_type(self, security_type):
        """Sets the security_type of this InstrumentData.


        :param security_type: The security_type of this InstrumentData.  # noqa: E501
        :type: str
        """

        self._security_type = security_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InstrumentData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InstrumentData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other