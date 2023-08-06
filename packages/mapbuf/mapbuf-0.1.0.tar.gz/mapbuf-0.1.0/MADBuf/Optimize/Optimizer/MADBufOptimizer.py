#!/usr/bin/env python
# -*- encoding=utf8 -*-

"""
Author: Hanyu Wang
Created time: 2023-03-18 21:50:41
Last Modified by: Hanyu Wang
Last Modified time: 2023-03-19 02:10:46
"""

from MADBuf.Utils import *
from MADBuf.Optimize.Constructor import *
from MADBuf.Optimize.Constraints import *
from MADBuf.Optimize.Variables import *
from MADBuf.Optimize.ModelUtils import *
from MADBuf.Optimize.Solver import *
from MADBuf.Optimize.Optimizer.OptimizerBase import *
from MADBuf.Optimize.Optimizer.OptimizerDFGBase import *

from copy import deepcopy


class MADBufOptimizer(DFGOptimizer):
    def __init__(self, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)

        self.lps: list
        self.model: gp.Model

        self.signal_to_variable: dict

        self.parse_lps(*args, **kwargs)
        self.parse_signal_to_variable(*args, **kwargs)

    def parse_lps(self, *args, **kwargs):

        # get the LPs to be optimized, if not specified, raise an exception
        lps: list = get_value_from_kwargs(
            kwargs,
            [
                "lps",
                "lp",
                "dynamatic_lps",
            ],
            None,
        )
        if lps is None:
            raise Exception("LPs are not specified")

        self.lps = lps

        model = load_model(self.lps, verbose=self.verbose)
        remove_timing_constraints(model)

        self.model = model

    def parse_signal_to_variable(self, *args, **kwargs):

        self.signal_to_variable = get_signal_to_variable(
            self.model,
            signal_to_channel=self.signal_to_channel,
            dfg_mapped=self.dfg_mapped,
            mapping=self.mapping,
            verbose=False
        )

    def build_model(self, *args, **kwargs):

        add_timing_constraints(
            self.model,
            self.graph,
            self.signal_to_cuts,
            self.signal_to_variable,
            **kwargs
        )

        # refine model: we should not buffer the channel between Memory Controller and Memory
        add_memory_constraints(self.model, **kwargs)

        lp_filename = get_value_from_kwargs(
            kwargs,
            [
                "lp_filename",
                "lp_file",
                "lp",
            ],
            None,
        )

        if lp_filename is not None:

            if not lp_filename.endswith(".lp"):
                raise Exception("LP filename should end with .lp")

            print(f"write LP to {lp_filename} ", end="...", flush=True)
            self.model.write(lp_filename)
            print_green("DONE")

    def get_solution_tuple(self, *args, **kwargs):
        buffers = retrieve_buffers_from_dynamatic_variables(self.model)
        buffer_slots = retrieve_buffers_to_n_slots_from_dynamatic_variables(self.model)
        signal_to_cut = retrieve_cuts(self.model, self.signal_to_cuts)
        signal_to_label = retrieve_timing_labels(self.model)

        # dfg = duplicate_dfg(self.dfg)
        # dfg = self.dfg.copy()
        # insert_buffers_in_dfg(dfg, buffers, buffer_slots, verbose=True)
        return buffers, buffer_slots, signal_to_cut, signal_to_label
