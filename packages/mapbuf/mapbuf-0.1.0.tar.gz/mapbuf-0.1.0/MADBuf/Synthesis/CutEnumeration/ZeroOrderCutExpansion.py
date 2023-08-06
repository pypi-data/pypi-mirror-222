#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2023-03-21 15:30:56
Last Modified by: Hanyu Wang
Last Modified time: 2023-03-21 18:11:42
"""

from MADBuf.Network import *
from MADBuf.Synthesis.TimingLabel import TimingLabel
from MADBuf.Utils import *
from MADBuf.Synthesis.CutEnumeration.ExpandCutBase import *
from MADBuf.Synthesis.CutEnumeration.RecoverChannels import *
from MADBuf.Synthesis.CutEnumeration.LabelPropagation import *


def zero_order_cut_expansion(
    g: BLIFGraph,
    signal: str,
    labels: dict,
    signal_to_channel: dict,
    cut_size_limit: int,
    max_expansion_level: int,
) -> list:
    def arrival_time(f: str) -> TimingLabel:
        assert f in labels
        return labels[f]

    return label_propagation(
        g, arrival_time, signal, cut_size_limit, max_expansion_level
    )
