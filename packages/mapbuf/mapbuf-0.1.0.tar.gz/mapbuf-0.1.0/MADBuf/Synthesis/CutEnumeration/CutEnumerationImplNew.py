#!/usr/bin/env python
# -*- encoding=utf8 -*-

'''
Author: Hanyu Wang
Created time: 2023-03-28 00:23:19
Last Modified by: Hanyu Wang
Last Modified time: 2023-04-16 22:15:00
'''


from MADBuf.Network.BLIF import *
from MADBuf.Utils import *
from MADBuf.Synthesis.CutEnumeration.CleanupDanglingCuts import *
from MADBuf.Synthesis.CutEnumeration.CutSummary import *
from MADBuf.Synthesis.CutEnumeration.CutCompression import *
import pygraphviz as pgv

import random

class two_input_network_cut_enumeration_params:
    compress_cuts: bool = False

def two_input_network_cut_enumeration_impl(
    g: BLIFGraph, **kwargs
) -> dict:
    """Cut Enumeration (implementation)

    Args:
        g (BLIFGraph): the graph to be enumerated
        priority_cut_size_limit (int, optional): the maximum number of cuts to be stored at each node.
                                            Defaults to 20.
        lut_size_limit (int, optional): the LUT size. Defaults to 6.

    Returns:
        dict: _description_
    """
    cuts: dict = {}

    priority_cut_size_limit = get_value_from_kwargs(
        kwargs, ["priority_cut_size_limit", "num_cuts"], 20
    )
    lut_size_limit = get_value_from_kwargs(kwargs, ["lut_size_limit", "cut_size"], 6)
    signal_to_channel = get_value_from_kwargs(kwargs, ["signal_to_channel"], {})
    skip_feedthrough = get_value_from_kwargs(kwargs, ["skip_feedthrough"], False)

    def get_num_supports(cut: Cut):
        num_supports = 0
        for leaf in cut.leaves:
            if leaf not in g.constants():
                num_supports += 1
        return num_supports

    assert isinstance(g, BLIFGraph), "g must be a BLIFGraph"

    # initialize the cuts
    for n in g.topological_traversal():
        if n in g.constants():
            cuts[n] = [Cut(n, [])]
        else:
            cuts[n] = [Cut(n, [n])]

    total_roots = len(g.topological_traversal())
    curr_root = 0

    print_blue(f"[i]Cut enumeration, priority_cut_size_limit={priority_cut_size_limit}, lut_size_limit={lut_size_limit}")

    for n in g.topological_traversal():

        curr_root += 1
        print(f"Finding cuts for {curr_root:4d} / {total_roots:4d}", end="\r")

        if n in g.node_fanins:

            assert len(g.fanins(n)) > 0
            assert len(g.fanins(n)) <= 2

            if len(g.fanins(n)) == 1:
                fanin = list(g.fanins(n))[0]
                if skip_feedthrough:
                    pass
                else:
                    for cut in cuts[fanin]:
                        cuts[n].append(Cut(n, cut.leaves))

            elif len(g.fanins(n)) == 2:    
                fanin1 = list(g.fanins(n))[0]
                fanin2 = list(g.fanins(n))[1]

                for cut1 in cuts[fanin1]:
                    for cut2 in cuts[fanin2]:
                        c = cut1 + cut2
                        if get_num_supports(c) <= lut_size_limit:
                            c.root = n
                            cuts[n].append(c)

            # uniqify
            cuts[n] = list(set(cuts[n]))

    # auto compression
    if two_input_network_cut_enumeration_params.compress_cuts:
        cuts = compress_cuts(g, cuts, signal_to_channel, lut_size_limit=lut_size_limit)
    
    for n in g.topological_traversal():
        # random shuffle
        if priority_cut_size_limit is not None:
            random.shuffle(cuts[n])
            cuts[n] = cuts[n][:priority_cut_size_limit]
    
    # remove dangling cuts
    cuts = cleanup_dangling_cuts(cuts)
    print_green("\nDone")

    return cuts  # uniqify
