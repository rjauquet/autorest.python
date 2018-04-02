﻿# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

import unittest
import subprocess
import sys
import isodate
import tempfile
import json
from datetime import date, datetime, timedelta
import os
from os.path import dirname, pardir, join, realpath

cwd = dirname(realpath(__file__))
log_level = int(os.environ.get('PythonLogLevel', 30))

tests = realpath(join(cwd, pardir, "Expected", "AcceptanceTests"))
sys.path.append(join(tests, "BodyDateTime"))

from msrest.serialization import Deserializer
from msrest.exceptions import DeserializationError, SerializationError

from bodydatetime import AutoRestDateTimeTestService

import pytest

class TestDatetime(object):

    @pytest.mark.asyncio
    async def test_datetime(self):
        client = AutoRestDateTimeTestService(base_url="http://localhost:3000")

        max_date = isodate.parse_datetime("9999-12-31T23:59:59.999999Z")
        min_date = isodate.parse_datetime("0001-01-01T00:00:00Z")

        dt = await client.datetime_model.get_utc_lowercase_max_date_time_async()
        assert dt ==  max_date
        dt = await client.datetime_model.get_utc_uppercase_max_date_time_async()
        assert dt ==  max_date
        dt = await client.datetime_model.get_utc_min_date_time_async()
        assert dt ==  min_date

        await client.datetime_model.get_local_negative_offset_min_date_time_async()

        with pytest.raises(DeserializationError):
            await client.datetime_model.get_local_negative_offset_lowercase_max_date_time_async()

        with pytest.raises(DeserializationError):
            await client.datetime_model.get_local_negative_offset_uppercase_max_date_time_async()

        with pytest.raises(DeserializationError):
            await client.datetime_model.get_local_positive_offset_min_date_time_async()

        await client.datetime_model.get_local_positive_offset_lowercase_max_date_time_async()
        await client.datetime_model.get_local_positive_offset_uppercase_max_date_time_async()

        await client.datetime_model.get_null_async()

        with pytest.raises(DeserializationError):
            await client.datetime_model.get_overflow_async()

        with pytest.raises(DeserializationError):
            await client.datetime_model.get_invalid_async()

        with pytest.raises(DeserializationError):
            await client.datetime_model.get_underflow_async()

        await client.datetime_model.put_utc_max_date_time_async(max_date)
        await client.datetime_model.put_utc_min_date_time_async(min_date)

        with pytest.raises(SerializationError):
            await client.datetime_model.put_local_positive_offset_min_date_time_async(
                isodate.parse_datetime("0001-01-01T00:00:00+14:00"))

        await client.datetime_model.put_local_negative_offset_min_date_time_async(
            isodate.parse_datetime("0001-01-01T00:00:00-14:00"))

        with pytest.raises(SerializationError):
            await client.datetime_model.put_local_negative_offset_max_date_time_async(
                isodate.parse_datetime("9999-12-31T23:59:59.999999-14:00"))

        await client.datetime_model.put_local_positive_offset_max_date_time_async(
            isodate.parse_datetime("9999-12-31T23:59:59.999999+14:00"))