/*
 * This file is part of the Intrepid project.
 * Copyright 2016 Roberto Bruttomesso <roberto.bruttomesso@gmail.com>.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are
 * met:
 *
 * * Redistributions of source code must retain the above copyright notice, this
 * list of conditions and the following disclaimer.
 *
 * * Redistributions in binary form must reproduce the above copyright notice,
 * this list of conditions and the following disclaimer in the documentation
 * and/or other materials provided with the distribution.
 *
 * * Neither the name of intrepid nor the names of its
 * contributors may be used to endorse or promote products derived from
 * this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE AUTHOR AND CONTRIBUTORS ``AS IS'' AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED. IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE FOR ANY
 * DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
 * SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 * CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

#ifndef SRC_API_INTREPID_H_
#define SRC_API_INTREPID_H_

#ifdef WIN32
#    define DLLEXPORT __declspec(dllexport)
#else
#    define DLLEXPORT
#endif

#define DEFINE_TYPE(T) typedef struct _ ## T *T

#ifdef __cplusplus
extern "C" {
#endif

DEFINE_TYPE(Int_ctx);
DEFINE_TYPE(Int_type);
DEFINE_TYPE(Int_engine_bmc);
DEFINE_TYPE(Int_engine_br);
DEFINE_TYPE(Int_simulator);
DEFINE_TYPE(Int_trace);
typedef unsigned Int_net;

typedef enum {
    INT_ENGINE_RESULT_UNKNOWN,
    INT_ENGINE_RESULT_REACHABLE,
    INT_ENGINE_RESULT_UNREACHABLE
} Int_engine_result;

DLLEXPORT
/**
 * @brief mk_ctx Creates a context
 * @return A new Intrepid context
 */
Int_ctx mk_ctx();

DLLEXPORT
/**
 * @brief del_ctx Frees memory of an Intrepid context
 * @param ctx the context to free
 */
void del_ctx(Int_ctx ctx);

DLLEXPORT
void throw_exception(const char* msg);

DLLEXPORT
void clear_exception();

DLLEXPORT
char* check_exception();

DLLEXPORT
void push_namespace(Int_ctx ctx, const char* name);

DLLEXPORT
void pop_namespace(Int_ctx ctx);

DLLEXPORT
Int_engine_bmc mk_engine_bmc(Int_ctx ctx);

DLLEXPORT
/**
 * @brief set_bmc_current_depth
 * @param engine the bmc engine to use
 * @param depth the depth to set
 */
void set_bmc_current_depth(Int_engine_bmc engine, unsigned depth);

DLLEXPORT
/**
 * @brief set_bmc_optimize
 * @param engine the bmc engine to use
 */
void set_bmc_optimize(Int_engine_bmc engine);

DLLEXPORT
/**
 * @brief bmc_add_target Adds a reachability target
 * @param ctx the context to use
 * @param engine
 */
void bmc_add_target(Int_ctx ctx, Int_engine_bmc engine, Int_net target);

DLLEXPORT
/**
 * @brief bmc_add_watch Adds a watched net
 * @param ctx the context to use
 * @param engine
 */
void bmc_add_watch(Int_ctx ctx, Int_engine_bmc engine, Int_net watch);

DLLEXPORT
/**
 * @brief bmc_reach_targets Tries to reach any previously added target,
 *        stops when the first is reached
 * @param engine the bmc engine to use
 * @return the result of the search
 */
Int_engine_result bmc_reach_targets(Int_engine_bmc engine);

DLLEXPORT
void bmc_remove_last_reached_targets(Int_engine_bmc engine);

DLLEXPORT
/**
 * @brief mk_engine_br Creates a Backward Reachability engine
 * @param ctx the context to use
 * @return the engine
 */
Int_engine_br mk_engine_br(Int_ctx ctx);

DLLEXPORT
/**
 * @brief br_add_target Adds a reachability target
 * @param ctx the context to use
 * @param engine
 */
void br_add_target(Int_ctx ctx, Int_engine_br engine, Int_net target);

DLLEXPORT
/**
 * @brief br_add_watch Adds a watched net
 * @param ctx the context to use
 * @param engine
 */
void br_add_watch(Int_ctx ctx, Int_engine_br engine, Int_net watch);

DLLEXPORT
/**
 * @brief br_reach_targets Tries to reach any previously added target,
 *        stops when the first is reached
 * @param engine the backward reach engine to use
 * @return the result of the search
 */
Int_engine_result br_reach_targets(Int_engine_br engine);

DLLEXPORT
void br_remove_last_reached_targets(Int_engine_br engine);

DLLEXPORT
/**
 * @brief bmc_last_reached_targets_number
 * @param engine the engine to use
 * @return the number of reached targets from the last call
 */
unsigned bmc_last_reached_targets_number(Int_engine_bmc engine);

DLLEXPORT
/**
 * @brief bmc_last_reached_target
 * @param engine the engine to use
 * @param n the number of reached target
 * @return the reached target
 */
Int_net bmc_last_reached_target(Int_engine_bmc engine, unsigned n);

DLLEXPORT
/**
 * @brief br_last_reached_targets_number
 * @param engine the engine to use
 * @return the number of reached targets from the last call
 */
unsigned br_last_reached_targets_number(Int_engine_br engine);

DLLEXPORT
/**
 * @brief br_last_reached_target
 * @param engine the engine to use
 * @param n the number of reached target
 * @return the reached target
 */
Int_net br_last_reached_target(Int_engine_br engine, unsigned n);

DLLEXPORT
/**
 * @brief bmc_get_trace Return the trace for a reached target
 * @param ctx the context to use
 * @param bmc the bmc engine to use
 * @param target the reached target in a previous call to bmc
 * @return the trace that shows reachability of target
 */
Int_trace bmc_get_trace(Int_ctx ctx,
                        Int_engine_bmc bmc,
                        Int_net target);

DLLEXPORT
/**
 * @brief br_get_trace Return the trace for a reached target
 * @param ctx the context to use
 * @param br the backward reach engine to use
 * @param target the reached target in a previous call to br
 * @return the trace that shows reachability of target
 */
Int_trace br_get_trace(Int_ctx ctx,
                       Int_engine_br br,
                       Int_net target);

DLLEXPORT
/**
 * @brief trace_get_value_for_net 
 * 
 * Internally stores the value of a net at a certain depth in 
 * the trace for later retrieval with function value_at
 *
 * @param ctx the context to use
 * @param cex the trace to inspect
 * @param net the net to use
 * @param depth the depth at which to retrieve the value
 * @return the length of the value to fetch
 */
unsigned trace_prepare_value_for_net(Int_ctx ctx,
                                     Int_trace cex,
                                     Int_net net,
                                     unsigned depth);

DLLEXPORT
/**
 * @brief prepare_value_for_net
 *
 * Internally stores the value of a net for later retrieval
 * with function value_at
 *
 * @param ctx the context to use
 * @param net the net to use
 * @return the length of the value to fetch
 */
unsigned prepare_value_for_net(Int_ctx ctx, Int_net net);

DLLEXPORT
char value_at(unsigned i);

DLLEXPORT
/**
 * @brief trace_get_max_depth Gets the max depth of the trace
 * @param cex the trace to inspect
 * @return the max depth
 */
unsigned trace_get_max_depth(Int_trace trace);

DLLEXPORT
Int_trace mk_trace(Int_ctx ctx);

DLLEXPORT
void trace_set_value(Int_ctx ctx, Int_trace trace, Int_net net,
                     unsigned depth, const char* value);

DLLEXPORT
unsigned trace_get_watched_nets_number(Int_trace trace);

DLLEXPORT
Int_net trace_get_watched_net(Int_trace trace, unsigned i);

DLLEXPORT
/**
 * @brief mk_simulator Creates a simulator
 * @param ctx the context to use
 * @return a simulator
 */
Int_simulator mk_simulator(Int_ctx ctx);

DLLEXPORT
/**
 * @brief simulator_add_target Adds a net to watch during simulation
 * @param simulator the simulator to use
 * @param watch the watch to add
 */
void simulator_add_watch(Int_ctx ctx, Int_simulator simulator, Int_net watch);

DLLEXPORT
/**
 * @brief simulator_simulate Simulate the given targets using the provided
 *        trace, up to the provided depth
 * @param simulator the simulator to use
 * @param trace the trace to simulate
 * @param depth the last depth to simulate
 */
void simulator_simulate(Int_simulator simulator,
                        Int_trace trace,
                        unsigned depth);

DLLEXPORT
/**
 * @brief mk_boolean_type Creates a Boolean type
 * @param ctx the context to use
 * @return A Boolean type
 */
Int_type mk_boolean_type(Int_ctx ctx);

DLLEXPORT
/**
 * @brief mk_int8_type Creates an int8 type
 * @param ctx the context to use
 * @return an int8 type
 */
Int_type mk_int8_type(Int_ctx ctx);

DLLEXPORT
/**
 * @brief mk_int16_type Creates an int16 type
 * @param ctx the context to use
 * @return an int16 type
 */
Int_type mk_int16_type(Int_ctx ctx);

DLLEXPORT
/**
 * @brief mk_int32_type Creates an int32 type
 * @param ctx the context to use
 * @return an int32 type
 */
Int_type mk_int32_type(Int_ctx ctx);

DLLEXPORT
/**
 * @brief mk_uint8_type Creates an int8 type
 * @param ctx the context to use
 * @return an uint8 type
 */
Int_type mk_uint8_type(Int_ctx ctx);

DLLEXPORT
/**
 * @brief mk_uint16_type Creates an int16 type
 * @param ctx the context to use
 * @return an uint16 type
 */
Int_type mk_uint16_type(Int_ctx ctx);

DLLEXPORT
/**
 * @brief mk_uint32_type Creates an int32 type
 * @param ctx the context to use
 * @return an uint32 type
 */
Int_type mk_uint32_type(Int_ctx ctx);

DLLEXPORT
/**
 * @brief mk_real_type Creates an real type
 * @param ctx the context to use
 * @return a real type
 */
Int_type mk_real_type(Int_ctx ctx);

DLLEXPORT
/**
 * @brief mk_float16_type Creates a floating point 16 type
 * @param ctx the context to use
 * @return a float 16 type
 */
Int_type mk_float16_type(Int_ctx ctx);

DLLEXPORT
/**
 * @brief mk_float32_type Creates a floating point 32 type
 * @param ctx the context to use
 * @return a float 32 type
 */
Int_type mk_float32_type(Int_ctx ctx);

DLLEXPORT
/**
 * @brief mk_float64_type Creates a floating point 64 type
 * @param ctx the context to use
 * @return a float 64 type
 */
Int_type mk_float64_type(Int_ctx ctx);

DLLEXPORT
/**
 * @brief mk_undef creates an undef net
 * @param ctx the context to use
 * @return an undef net
 */
Int_net mk_undef(Int_ctx ctx);

DLLEXPORT
/**
 * @brief mk_true creates a true net
 * @param ctx the context to use
 * @return a true net
 */
Int_net mk_true(Int_ctx ctx);

DLLEXPORT
/**
 * @brief mk_false creates a false net
 * @param ctx the context to use
 * @return a true net
 */
Int_net mk_false(Int_ctx ctx);

DLLEXPORT
/**
 * @brief mk_number creates a number
 * @param value decimal value of the number
 * @param type the type of the number
 * @return the net corresponding to the number
 */
Int_net mk_number(Int_ctx ctx, const char* value, Int_type type);

DLLEXPORT
/**
 * @brief mk_not logical not
 * @param ctx the context to use
 * @param x
 * @return not x
 */
Int_net mk_not(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief mk_and logical and
 * @param ctx the context to use
 * @param x
 * @param y
 * @return x and y
 */
Int_net mk_and(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
/**
 * @brief mk_or logical or
 * @param ctx the context to use
 * @param x
 * @param y
 * @return x or y
 */
Int_net mk_or(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
/**
 * @brief mk_xor logical xor
 * @param ctx the context to use
 * @param x
 * @param y
 * @return x or y
 */
Int_net mk_xor(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
/**
 * @brief mk_ite if then else
 * @param ctx the context to use
 * @param i boolean condition
 * @param t then branch
 * @param e else branch
 * @return t if i is true, e otherwise
 */
Int_net mk_ite(Int_ctx ctx, Int_net i, Int_net t, Int_net e);

DLLEXPORT
/**
 * @brief mk_iff logical iff
 * @param ctx the context to use
 * @param x
 * @param y
 * @return x iff y
 */
Int_net mk_iff(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
Int_net mk_minus(Int_ctx ctx, Int_net x);

DLLEXPORT
Int_net mk_add(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
Int_net mk_sub(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
Int_net mk_mul(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
Int_net mk_div(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
Int_net mk_mod(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
/**
 * @brief mk_eq equates two nets of type integer, real, or float
 * @param ctx the context to use
 * @param x
 * @param y
 * @return x = y
 */
Int_net mk_eq(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
/**
 * @brief mk_leq less than or equal predicate
 * @param ctx the context to use
 * @param x
 * @param y
 * @return x <= y
 */
Int_net mk_leq(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
/**
 * @brief mk_lt less than predicate
 * @param ctx the context to use
 * @param x
 * @param y
 * @return x < y
 */
Int_net mk_lt(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
/**
 * @brief mk_geq greater than or equal predicate
 * @param ctx the context to use
 * @param x
 * @param y
 * @return x >= y
 */
Int_net mk_geq(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
/**
 * @brief mk_gt greater than predicate
 * @param ctx the context to use
 * @param x
 * @param y
 * @return x > y
 */
Int_net mk_gt(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
/**
 * @brief mk_neq negated equality
 * @param ctx the context to use
 * @param x
 * @param y
 * @return x != y
 */
Int_net mk_neq(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
/**
 * @brief mk_input Creates an input
 * @param ctx the context to use
 * @param name the unique name of this input
 * @param type the data type of this input
 * @return A net that encodes an input
 */
Int_net mk_input(Int_ctx ctx, const char *name, Int_type type);

DLLEXPORT
/**
 * @brief mk_output Marks an existing net as begin an output
 * @param net the net to be marked
 */
void mk_output(Int_ctx, Int_net net);

DLLEXPORT
/**
 * @brief mk_assumption Marks an existing net as begin an assumption
 * @param net the net to be marked
 */
void mk_assumption(Int_ctx, Int_net net);

DLLEXPORT
/**
 * @brief mk_latch Creates an uninitialized latch with no next state
 * @param ctx the context to use
 * @param name the unique name of this latch
 * @param type the data type of this latch
 * @return A net that encodes the latch
 */
Int_net mk_latch(Int_ctx ctx, const char *name, Int_type type);

DLLEXPORT
/**
 * @brief set_latch_init_next Sets the initial state and the circuit
 *        attached to the next pin of the latch
 * @param ctx the context to use
 * @param latch the latch to initialize
 * @param init the initial state
 * @param next the circuit attached to the next pin of the latch
 */
void set_latch_init_next(Int_ctx ctx, Int_net latch,
                         Int_net init, Int_net next);

DLLEXPORT
Int_net mk_substitute(Int_ctx ctx, Int_net term,
                      Int_net new_subterm,
                      Int_net old_subterm);

DLLEXPORT
void apitrace_dump_to_file(const char* filename);

DLLEXPORT
void apitrace_print_to_stdout();

DLLEXPORT
void apitrace_print_to_stderr();

#ifdef __cplusplus
}  // extern "C"
#endif

#endif  // SRC_API_INTREPID_H_
