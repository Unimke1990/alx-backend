#!/usr/bin/env python3
"""module defines the function index_range"""


def index_range(page, page_size):
    """returns turple of size two containing start and end indexes"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)