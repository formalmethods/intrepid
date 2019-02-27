"""
Copyright (C) 2017 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>

This file is distributed under the terms of the 3-clause BSD License.
A copy of the license can be found in the root directory or at
https://opensource.org/licenses/BSD-3-Clause.

Author: Roberto Bruttomesso <roberto.bruttomesso@gmail.com>
  Date: 27/03/2017

This module implements infrastructure for creating nets and engines
"""

import intrepyd as ip
import intrepyd.api
import intrepyd.engine
import intrepyd.simulator
import intrepyd.trace
import collections

class Context(object):
    """
    An intrepyd context
    """
    def __init__(self):
        self.ctx = ip.api.mk_ctx()
        self.inputs = collections.OrderedDict()
        self.outputs = collections.OrderedDict()
        self.latches = {}
        self.nets = {}
        self.net2name = {}
        self.input2type = {}
        self.booleantype = ip.api.mk_boolean_type(self.ctx)
        self.int8type = ip.api.mk_int8_type(self.ctx)
        self.int16type = ip.api.mk_int16_type(self.ctx)
        self.int32type = ip.api.mk_int32_type(self.ctx)
        self.uint8type = ip.api.mk_uint8_type(self.ctx)
        self.uint16type = ip.api.mk_uint16_type(self.ctx)
        self.uint32type = ip.api.mk_uint32_type(self.ctx)
        self.realtype = ip.api.mk_real_type(self.ctx)
        self.float16type = ip.api.mk_float16_type(self.ctx)
        self.float32type = ip.api.mk_float32_type(self.ctx)
        self.float64type = ip.api.mk_float64_type(self.ctx)
        self.undef = ip.api.mk_undef(self.ctx)
        self.true = ip.api.mk_true(self.ctx)
        self.false = ip.api.mk_false(self.ctx)
        self.namespaces = []

    def __del__(self):
        ip.api.del_ctx(self.ctx)

    def push_namespace(self, name):
        ip.api.push_namespace(self.ctx, name)
        self.namespaces.append(name)

    def pop_namespace(self):
        ip.api.pop_namespace(self.ctx)
        if len(self.namespaces) == 0:
            raise Exception('Cannot pop namespace, empty list')
        return self.namespaces.pop()

    def mk_boolean_type(self):
       return self.booleantype

    def mk_int8_type(self):
        return self.int8type

    def mk_int16_type(self):
        return self.int16type

    def mk_int32_type(self):
        return self.int32type

    def mk_uint8_type(self):
        return self.uint8type

    def mk_uint16_type(self):
        return self.uint16type

    def mk_uint32_type(self):
        return self.uint32type

    def mk_real_type(self):
        return self.realtype

    def mk_float16_type(self):
        return self.float16type

    def mk_float32_type(self):
        return self.float32type

    def mk_float64_type(self):
        return self.float64type

    def mk_undef(self):
        return self.undef

    def mk_true(self, name=None):
        return self._register(self.true, name)

    def mk_false(self, name=None):
        return self._register(self.false, name)

    def mk_number(self, value, type_, name=None):
        return self._register(ip.api.mk_number(self.ctx, value, type_), name)

    def mk_not(self, x, name=None):
        return self._register(ip.api.mk_not(self.ctx, x), name=name)

    def mk_and(self, x, y, name=None):
        return self._register(ip.api.mk_and(self.ctx, x, y), name=name)

    def mk_or(self, x, y, name=None):
        return self._register(ip.api.mk_or(self.ctx, x, y), name=name)

    def mk_xor(self, x, y, name=None):
        return self._register(ip.api.mk_xor(self.ctx, x, y), name=name)

    def mk_implies(self, x, y, name=None):
        return self._register(ip.api.mk_or(self.ctx, ip.api.mk_not(self.ctx, x), y), name=name)

    def mk_iff(self, x, y, name=None):
        return self._register(ip.api.mk_iff(self.ctx, x, y), name=name)

    def mk_eq(self, x, y, name=None):
        return self._register(ip.api.mk_eq(self.ctx, x, y), name=name)

    def mk_leq(self, x, y, name=None):
        return self._register(ip.api.mk_leq(self.ctx, x, y), name=name)

    def mk_lt(self, x, y, name=None):
        return self._register(ip.api.mk_lt(self.ctx, x, y), name=name)

    def mk_geq(self, x, y, name=None):
        return self._register(ip.api.mk_geq(self.ctx, x, y), name=name)

    def mk_gt(self, x, y, name=None):
        return self._register(ip.api.mk_gt(self.ctx, x, y), name=name)

    def mk_neq(self, x, y, name=None):
        return self._register(ip.api.mk_neq(self.ctx, x, y), name=name)

    def mk_add(self, x, y, name=None):
        return self._register(ip.api.mk_add(self.ctx, x, y), name=name)

    def mk_mul(self, x, y, name=None):
        return self._register(ip.api.mk_mul(self.ctx, x, y), name=name)

    def mk_div(self, x, y, name=None):
        return self._register(ip.api.mk_div(self.ctx, x, y), name=name)

    def mk_mod(self, x, y, name=None):
        return self._register(ip.api.mk_mod(self.ctx, x, y), name=name)

    def mk_sub(self, x, y, name=None):
        return self._register(ip.api.mk_sub(self.ctx, x, y), name=name)

    def mk_minus(self, x, name=None):
        return self._register(ip.api.mk_minus(self.ctx, x), name=name)

    def mk_ite(self, i, t, e, name=None):
        return self._register(ip.api.mk_ite(self.ctx, i, t, e), name=name)

    def mk_input(self, name, type_):
        return self._register_input(ip.api.mk_input(self.ctx, name, type_), type_, name=name)

    def mk_output(self, x, name=None):
        ip.api.mk_output(self.ctx, x)
        self._register_output(x, name=name)

    def mk_latch(self, name, type_):
        return self._register_latch(ip.api.mk_latch(self.ctx, name, type_), name=name)

    def set_latch_init_next(self, latch, init, next):
        ip.api.set_latch_init_next(self.ctx, latch, init, next)

    def mk_substitute(self, term, newTerm, oldTerm):
        return ip.api.mk_substitute(self.ctx, term, newTerm, oldTerm)

    def mk_assumption(self, net):
        ip.api.mk_assumption(self.ctx, net)

    def mk_cast_to_int8(self, net):
        return ip.api.mk_cast_to_int8(self.ctx, net)

    def mk_cast_to_int16(self, net):
        return ip.api.mk_cast_to_int16(self.ctx, net)

    def mk_cast_to_int32(self, net):
        return ip.api.mk_cast_to_int32(self.ctx, net)

    def mk_cast_to_uint8(self, net):
        return ip.api.mk_cast_to_uint8(self.ctx, net)

    def mk_cast_to_uint16(self, net):
        return ip.api.mk_cast_to_uint16(self.ctx, net)

    def mk_cast_to_uint32(self, net):
        return ip.api.mk_cast_to_uint32(self.ctx, net)

    def mk_bmc(self):
        return ip.engine.Bmc(self.ctx)

    def mk_optimizing_bmc(self):
        return ip.engine.OptimizingBmc(self.ctx)

    def mk_backward_reach(self):
        return ip.engine.BackwardReach(self.ctx)

    def mk_simulator(self):
        return ip.simulator.Simulator(self.ctx)

    def mk_trace(self):
        return ip.trace.Trace(self.ctx)

    def to_string(self, net):
        """
        Returns the given net as a string, as given from the underlying smt-solver.
        """
        size = ip.api.prepare_value_for_net(self.ctx, net)
        value = ''
        for i in range(size):
            value += ip.api.value_at(i)
        return value

    def get_default_value(self, type_):
        """
        Returns a default value for the given type
        """
        if type_ == self.booleantype:
            return 'F'
        elif type_ in [self.float16type, self.float32type, self.float64type, self.realtype]:
            return '0.0'
        assert type_ in [self.int8type, self.int16type, self.int32type, self.uint8type, self.uint16type, self.uint32type]
        return '0'

    def _current_namespace_prefix(self):
        result = ''
        for namespace in self.namespaces:
            result += namespace + '.'
        return result

    def _register(self, rawnet, name):
        if rawnet in self.net2name:
            return rawnet
        if name is None:
            name = '__n' + str(rawnet)
        name = self._current_namespace_prefix() + name
        if name in self.nets:
            raise Exception('Name already used: ' + name)
        self.nets[name] = rawnet
        self.net2name[rawnet] = name
        return rawnet

    def _register_input(self, rawnet, type_, name):
        rawnet = self._register(rawnet, name)
        self.inputs[name] = rawnet
        self.input2type[rawnet] = type_
        return rawnet

    def _register_latch(self, rawnet, name):
        rawnet = self._register(rawnet, name)
        self.latches[name] = rawnet
        return rawnet

    def _register_output(self, rawnet, name):
        if name is None:
            name = '__o' + str(rawnet)
        rawnet = self._register(rawnet, name)
        self.outputs[name] = rawnet
