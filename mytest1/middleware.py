# -*- coding: utf-8 -*-

"""
Author:        Wang Chao <yueyoum@gmail.com>
Filename:      middleware.py
Date created:  2016-06-20 18:11:01
Description:

"""

import time

class TimeMeasureRequestMiddleware(object):
    def process_request(self, request):
        request._time_measure_star_at = time.time()

class TimeMeasureResponseMiddleware(object):
    def process_response(self, request, response):
        time_passed = time.time() - request._time_measure_star_at
        print "[TIME MEASURE] {0}: {1}".format(request.path, time_passed)

        return response

