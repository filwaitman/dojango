# -*- encoding: utf-8 -*-

def version_tuple(s):
    return tuple([int(x) for x in s.split("-")[0].split(".")])  # Deal with remainder for versions like "1.5.0-jsonrpc"
