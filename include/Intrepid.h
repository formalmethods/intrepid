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
DEFINE_TYPE(Int_counterexample);
typedef unsigned Int_net;
typedef unsigned Int_value;

typedef enum {
    INT_ENGINE_RESULT_UNKNOWN,
    INT_ENGINE_RESULT_REACHABLE,
    INT_ENGINE_RESULT_UNREACHABLE
} Int_engine_result;

typedef enum {
    INT_KIND_UNKNOWN,
    INT_KIND_INPUT,
    INT_KIND_NUMBER,
    INT_KIND_AND,
    INT_KIND_OR,
    INT_KIND_NOT,
    INT_KIND_IFF,
    INT_KIND_XOR,
    INT_KIND_ADD,
    INT_KIND_SUB,
    INT_KIND_MUL,
    INT_KIND_DIV,
    INT_KIND_MOD,
    INT_KIND_EQ,
    INT_KIND_LEQ,
    INT_KIND_LT,
    INT_KIND_GEQ,
    INT_KIND_GT,
    INT_KIND_ITE,
} Int_net_kind;

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
void throw_exception(char* msg);

DLLEXPORT
void clear_exception();

DLLEXPORT
char* check_exception();

DLLEXPORT
void push_namespace(Int_ctx ctx, const char* name);

DLLEXPORT
void pop_namespace(Int_ctx ctx);

DLLEXPORT
Int_engine_bmc mk_engine_bmc(Int_ctx ctx,
                             unsigned last_depth);

DLLEXPORT
/**
 * @brief set_bmc_current_depth
 * @param engine the bmc engine to use
 * @param depth the depth to set
 */
void set_bmc_current_depth(Int_engine_bmc engine, unsigned depth);

DLLEXPORT
/**
 * @brief bmc_add_target Adds a reachability target
 * @param ctx the context to use
 * @param engine
 */
void bmc_add_target(Int_ctx ctx, Int_engine_bmc engine, Int_net target);

DLLEXPORT
/**
 * @brief bmc_reach_targets Tries to reach any previously added target,
 *        stops when the first is reached
 * @param engine the bmc engine to use
 * @return the result of the search
 */
Int_engine_result bmc_reach_targets(Int_engine_bmc engine);

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
 * @brief br_reach_targets Tries to reach any previously added target,
 *        stops when the first is reached
 * @param engine the backward reach engine to use
 * @return the result of the search
 */
Int_engine_result br_reach_targets(Int_engine_br engine);

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
 * @brief bmc_get_counterexample Return the counterexample for a reached target
 * @param ctx the context to use
 * @param target the reached target in a previous call to bmc
 * @return the counterexample that shows reachability of target
 */
Int_counterexample bmc_get_counterexample(Int_ctx ctx,
                                          Int_engine_bmc,
                                          Int_net target);

DLLEXPORT
/**
 * @brief br_get_counterexample Return the counterexample for a reached target
 * @param ctx the context to use
 * @param target the reached target in a previous call to br
 * @return the counterexample that shows reachability of target
 */
Int_counterexample br_get_counterexample(Int_ctx ctx,
                                         Int_engine_br,
                                         Int_net target);

DLLEXPORT
/**
 * @brief counterexample_get_value_for_net Gets the value of a net at a
 *                                         certain depth in the counterexample
 * @param ctx the context to use
 * @param cex the counterexample to inspect
 * @param net the net to use
 * @param depth the depth at which to retrieve the value
 * @return the value of net at depth
 */
Int_value counterexample_get_value_for_net(Int_ctx ctx,
                                           Int_counterexample cex,
                                           Int_net net,
                                           unsigned depth);

DLLEXPORT
/**
 * @brief counterexample_get_max_depth Gets the max depth of the counterexample
 * @param cex the counterexample to inspect
 * @return the max depth
 */
unsigned counterexample_get_max_depth(Int_counterexample cex);

DLLEXPORT
/**
 * @brief value_get_as_string Returns the numeric value into a string
 * @param ctx the context to use
 * @param value the value to retrieve
 * @param OUTPUT the string representation of value
 */
void value_get_as_string(Int_ctx ctx, Int_value value, char* OUTPUT);

DLLEXPORT
/**
 * @brief mk_simulator Creates a simulator
 * @param ctx the context to use
 * @return a simulator
 */
Int_simulator mk_simulator(Int_ctx ctx);

DLLEXPORT
/**
 * @brief simulator_add_target Adds a target to a simulator
 * @param simulator the simulator to use
 * @param target the target to add
 */
void simulator_add_target(Int_ctx ctx, Int_simulator simulator, Int_net target);

DLLEXPORT
/**
 * @brief simulator_simulate Simulate the given targets using the provided
 *        counterexample, up to the provided depth
 * @param simulator the simulator to use
 * @param cex the cex to simulate
 * @param depth the last depth to simulate
 */
void simulator_simulate(Int_simulator simulator,
                        Int_counterexample cex,
                        unsigned depth);

DLLEXPORT
/**
 * @brief simulator_last_reached_targets_number Return the number of last
 *        reached targets during the last simulation run
 * @param ctx the context to use
 * @param simulator the simulator to use
 * @return the number of reached targets computed by simulation
 */
unsigned simulator_last_reached_targets_number(Int_simulator simulator);

DLLEXPORT
/**
 * @brief simulator_last_reached_target Return the n-th last reached target
 * @param simulator the simulator to use
 * @param n the number of target to get
 * @return the n-th last reached target during simulation
 */
Int_net simulator_last_reached_target(Int_simulator simulator, unsigned n);

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
 * @brief mk_double_type Creates an double type
 * @param ctx the context to use
 * @return a double type
 */
Int_type mk_double_type(Int_ctx ctx);

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
 * @brief mk_iff logical iff
 * @param ctx the context to use
 * @param x
 * @param y
 * @return x iff y
 */
Int_net mk_iff(Int_ctx ctx, Int_net x, Int_net y);

DLLEXPORT
/**
 * @brief mk_eq equates two nets of type integer, real, or double
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

#ifdef __cplusplus
}  // extern "C"
#endif

#endif  // SRC_API_INTREPID_H_
