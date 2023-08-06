#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2023-03-11 07:41:12
Last Modified by: Hanyu Wang
Last Modified time: 2023-03-19 13:13:15
"""


from MADBuf.Network import *
from MADBuf.Synthesis.TimingLabel import TimingLabel
from MADBuf.Synthesis.CutEnumeration.CleanupDanglingCuts import *
from MADBuf.Utils import *

class CutlessEnumerationImplOld_params:
    skip_feedthrough = True


def __expand_cut_at(g: BLIFGraph, signal_to_channel: dict, leaves: set, leaves_to_expand: str):

    # we can call it on multiple leaves
    new_leaves: set = set(list(leaves)[:])  # deep copy

    if isinstance(leaves_to_expand, set):
        for leaf in leaves_to_expand:
            new_leaves.remove(leaf)
            for h in g.node_fanins[leaf]:
                new_leaves.add(h)

    elif isinstance(leaves_to_expand, str):
        leaf = leaves_to_expand

        new_leaves: set = set(list(leaves)[:])  # deep copy
        new_leaves.remove(leaf)
        for h in g.node_fanins[leaf]:
            new_leaves.add(h)

    while True:
        updated = False
        for h in new_leaves:
            if h not in g.node_fanins:
                continue

            # do not skip the channels
            if h in signal_to_channel:
                continue

            # here the plus 1 is because we haven't remove h from leaves yet!
            if len(new_leaves.union(g.node_fanins[h])) <= len(new_leaves) + 1:
                new_leaves.remove(h)
                new_leaves = new_leaves.union(g.node_fanins[h])
                updated = True
                break
        if not updated:
            break

    return new_leaves


def __get_timing_labels(
    g: BLIFGraph,
    signal_to_channel: dict = {},
    cut_size_limit: int = 6,
    max_expansion_level: int = 0,
) -> tuple:
    """Get timing labels

    Args:
        g (BLIFGraph): the subject graph
        signal_to_channel (dict, optional): the mapping from signals to the channels. Defaults to {}.
        cut_size_limit (int, optional): the K value in K-LUT mapping. Defaults to 6.
        max_expansion_level (int, optional): the expansion level in which we torelant the cut size violation. Defaults to 0 (zero tolerance).

    Returns:
        tuple (dict, dict): (labels, cuts)
    """

    labels: dict = {}
    cuts: dict = {}

    for signal in g.topological_traversal():
        cuts[signal] = []

        if g.is_ci(signal):
            labels[signal] = TimingLabel(0)
            cuts[signal] = [Cut(signal, [signal])]
            continue

        assert signal in g.node_fanins

        # 
        if CutlessEnumerationImplOld_params.skip_feedthrough:
            if len(g.node_fanins[signal]) == 1:
                fanin = g.fanins(signal)[0]
                
                assert fanin in labels
                labels[signal] = labels[fanin]
                cuts[signal] = [Cut(signal, [fanin])]
                continue

        optimal_timing_label = TimingLabel()

        leaves: set = set(list(g.fanins(signal))[:])  # deep copy
        best_leaves: set = leaves.copy()  # deep copy
        cuts[signal].append(Cut(signal, leaves))

        # while len(leaves) <= cut_size_limit:
        curr_expansion_level = 0

        # we should also consider the constants
        while True:

            # we count the number of non-constant leaves
            num_leaves: int = 0
            for f in leaves:
                if f in g.const0 or f in g.constant1s():
                    continue
                num_leaves += 1

            # we stop when the number of leaves is larger than the limit
            if num_leaves > cut_size_limit:
                curr_expansion_level += 1

            else:
                curr_expansion_level = 0

            # break if the expansion level is larger than the limit
            if curr_expansion_level > max_expansion_level:
                break

            arrival_times: list = [(labels[f], f) for f in leaves]
            maximum_timing_label, f = max(arrival_times)

            # we only update the result if the cut is valid (curr_expansion_level = 0)
            if curr_expansion_level == 0:
                optimal_timing_label = min(
                    maximum_timing_label + 1, optimal_timing_label
                )
                best_leaves = leaves.copy()

            if maximum_timing_label == TimingLabel(0):
                break


            is_reaching_cis = False
            is_on_channel = False
            leaves_to_expand = set()
            for label, f in arrival_times:
                
                # we need to stop if we reach the CIs
                if f not in g.node_fanins:
                    is_reaching_cis = True
                    break

                # we need to remember the leaves that are on the channel
                if f in signal_to_channel:
                    is_on_channel = True

                # we only expand the leaves that have the maximum timing label
                if label == maximum_timing_label:
                    leaves_to_expand.add(f)

            if is_reaching_cis:
                break

            if is_on_channel:
                if curr_expansion_level == 0:
                    cuts[signal].append(Cut(signal, leaves))

            leaves = __expand_cut_at(g, signal_to_channel, leaves, leaves_to_expand)

        labels[signal] = optimal_timing_label
        cuts[signal].append(Cut(signal, best_leaves))

    return labels, cuts


def cutless_enumeration_impl_old(network: BLIFGraph, **kwargs) -> dict:
    """
    Cutless enumeration of cuts
    """

    signal_to_channel = (
        kwargs["signal_to_channel"] if "signal_to_channel" in kwargs else {}
    )
    lut_size_limit = kwargs["lut_size_limit"] if "lut_size_limit" in kwargs else 6
    verbose = kwargs["verbose"] if "verbose" in kwargs else False
    max_expansion_level = (
        kwargs["max_expansion_level"] if "max_expansion_level" in kwargs else 0
    )

    if signal_to_channel == None:
        signal_to_channel = {}

    labels, cuts = __get_timing_labels(
        network, signal_to_channel, lut_size_limit, max_expansion_level
    )

    if verbose:
        for signal in network.topological_traversal():
            print(
                f"labels = {labels[signal]}, cuts = {len(cuts[signal])}, signal = {signal}"
            )

    cuts = cleanup_dangling_cuts(cuts)

    return labels, cuts
