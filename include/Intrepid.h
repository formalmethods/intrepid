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
DEFINE_TYPE(Int_circuit);
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
/**
 * @brief mk_circuit Creates an empty circuit
 * @param ctx the context to use
 * @param name the unique name id of a circuit
 * @return an empty circuit
 */
Int_circuit mk_circuit(Int_ctx ctx, const char* name);

DLLEXPORT
/**
 * @brief mk_circuit_from_st_string creates a circuit out of a IEC 61131 ST program as string
 * @param ctx the context to use
 * @param ststr the string encoding the program
 * @return the created circuit
 */
Int_circuit mk_circuit_from_st_string(Int_ctx ctx, const char* ststr);

DLLEXPORT
/**
 * @brief mk_circuit_from_st_file create a circuit from a IEC 61131 ST program on a file
 * @param ctx the context to use
 * @param filename the path to the ST program
 * @return the create circuit
 */
Int_circuit mk_circuit_from_st_file(Int_ctx ctx, const char* filename);

DLLEXPORT
/**
 * @brief mk_circuit_miter Merges the two circuits in order
 *        to create a miter. All the inputs are equated,
 *        assuming that their order corresponds by creation.
 *        Corresponding outputs are set as different, and
 *        added as assertions in the miter
 *
 * @param ctx the context to use
 * @param circ1 the first circuit
 * @param circ2 the second circuit
 * @return the miter circuit, which could be used for equivalence checking
 */
Int_circuit mk_circuit_miter(Int_ctx ctx,
                             Int_circuit circ1,
                             Int_circuit circ2);

DLLEXPORT
/**
 * @brief mk_circuit_miter_map Merges the two circuits in order
 *        to create a miter. Basically all the inputs are
 *        equated, according to the provided mapping, while
 *        the corresponding outputs are set as different, and
 *        added as assertions in the miter
 *
 * @param ctx the context to use
 * @param circ1 the first circuit
 * @param circ2 the second circuit
 * @param inputs1 the list of inputs to equate from circuit1
 * @param inputs2 the list of inputs to equate from circuit2
 * @param inputs_size the size of the two input lists
 * @param outputs1 the list of outputs to equate from circuit1
 * @param outputs2 the list of outputs to equate from circuit2
 * @param outputs_size the size of the two outputs lists
 * @return the miter circuit, which could be used for equivalence checking
 */
Int_circuit mk_circuit_miter_map(Int_ctx ctx,
                                 Int_circuit circ1,
                                 Int_circuit circ2,
                                 const Int_net* inputs1,
                                 const Int_net* inputs2,
                                 unsigned inputs_size,
                                 const Int_net* outputs1,
                                 const Int_net* outputs2,
                                 unsigned outputs_size);

DLLEXPORT
/**
 * @brief mk_engine_bmc Creates a BMC engine
 * @param ctx the context to use
 * @param circ the circuit to use
 * @param last_depth the last depth that will be used while calling the engine
 * @return the engine
 */
Int_engine_bmc mk_engine_bmc(Int_ctx ctx,
                             Int_circuit circ,
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
 * @param circ the circuit to use
 * @return the engine
 */
Int_engine_br mk_engine_br(Int_ctx ctx, Int_circuit circ);

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
 * @param circ the circuit to use
 * @return a simulator
 */
Int_simulator mk_simulator(Int_ctx ctx, Int_circuit circ);

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
unsigned simulator_last_reached_targets(Int_simulator simulator);

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
 * @param circ the circuit on which to create the input
 * @param name the unique name of this input
 * @param type the data type of this input
 * @return A net that encodes an input
 */
Int_net mk_input(Int_ctx ctx, Int_circuit circ,
                 const char *name, Int_type type);

DLLEXPORT
/**
 * @brief mk_output Marks an existing net as begin an output
 * @param circ the circuit in which the output has to be made
 * @param name the unique name of the output
 * @param net the net to be marked
 */
void mk_output(Int_ctx, Int_circuit circ,
               const char* name, Int_net net);

DLLEXPORT
/**
 * @brief mk_latch Creates an uninitialized latch with no next state
 * @param ctx the context to use
 * @param circ the circuit on which to create the latch
 * @param name the unique name of this latch
 * @param type the data type of this latch
 * @return A net that encodes the latch
 */
Int_net mk_latch(Int_ctx ctx, Int_circuit circ,
                 const char *name, Int_type type);

DLLEXPORT
/**
 * @brief set_latch_init_next Sets the initial state and the circuit
 *        attached to the next pin of the latch
 * @param ctx the context to use
 * @param circ the circuit on which to create the latch
 * @param latch the latch to initialize
 * @param init the initial state
 * @param next the circuit attached to the next pin of the latch
 */
void set_latch_init_next(Int_ctx ctx, Int_circuit circ, Int_net latch,
                         Int_net init, Int_net next);

DLLEXPORT
/**
 * @brief get_input
 * @param circ the circuit
 * @param n the number of input to retrieve
 */
unsigned get_input(Int_circuit circ, unsigned n);

DLLEXPORT
/**
 * @brief get_inputs_size
 * @param circ
 * @return the number of inputs stored in the circuit
 */
unsigned get_inputs_size(Int_circuit circ);

DLLEXPORT
/**
 * @brief get_output
 * @param circ the circuit
 * @param n the number of output to retrieve
 */
unsigned get_output(Int_circuit circ, unsigned n);

DLLEXPORT
/**
 * @brief get_outputs_size
 * @param circ
 * @return the number of outputs stored in the circuit
 */
unsigned get_outputs_size(Int_circuit circ);

DLLEXPORT
/**
 * @brief get_output
 * @param circ the circuit
 * @param n the number of output to retrieve
 */
unsigned get_output(Int_circuit circ, unsigned n);

DLLEXPORT
/**
 * @brief get_assumptions_size
 * @param circ
 * @return the number of assumptions stored in the circuit
 */
unsigned get_assumptions_size(Int_circuit circ);

DLLEXPORT
/**
 * @brief get_assumption
 * @param circ the circuit
 * @param n the number of assumption to retrieve
 */
unsigned get_assumption(Int_circuit circ, unsigned n);

DLLEXPORT
/**
 * @brief get_proof_objectives_size
 * @param circ
 * @return the number of proof objectives stored in the circuit
 */
unsigned get_proof_objectives_size(Int_circuit circ);

DLLEXPORT
/**
 * @brief get_proof_objective
 * @param circ the circuit
 * @param n the number of proof objective to retrieve
 */
unsigned get_proof_objective(Int_circuit circ, unsigned n);

DLLEXPORT
/**
 * @brief get_test_objectives_size
 * @param circ
 * @return the number of test objectives stored in the circuit
 */
unsigned get_test_objectives_size(Int_circuit circ);

DLLEXPORT
/**
 * @brief get_test_objective
 * @param circ the circuit
 * @param n the number of test objective to retrieve
 */
unsigned get_test_objective(Int_circuit circ, unsigned n);

DLLEXPORT
/**
 * @brief is_boolean_type
 * @param t the type to check
 * @return true iff t is of boolean type
 */
int is_boolean_type(Int_type t);

DLLEXPORT
/**
 * @brief is_int8_type
 * @param t the type to check
 * @return true iff t is of int8 type
 */
int is_int8_type(Int_type t);

DLLEXPORT
/**
 * @brief is_int16_type
 * @param t the type to check
 * @return true iff t is of int16 type
 */
int is_int16_type(Int_type t);

DLLEXPORT
/**
 * @brief is_int32_type
 * @param t the type to check
 * @return true iff t is of int32 type
 */
int is_int32_type(Int_type t);

DLLEXPORT
/**
 * @brief is_uint8_type
 * @param t the type to check
 * @return true iff t is of uint8 type
 */
int is_uint8_type(Int_type t);

DLLEXPORT
/**
 * @brief is_uint16_type
 * @param t the type to check
 * @return true iff t is of uint16 type
 */
int is_uint16_type(Int_type t);

DLLEXPORT
/**
 * @brief is_uint32_type
 * @param t the type to check
 * @return true iff t is of uint32 type
 */
int is_uint32_type(Int_type t);

DLLEXPORT
/**
 * @brief is_real_type
 * @param t the type to check
 * @return true iff t is of real type
 */
int is_real_type(Int_type t);

DLLEXPORT
/**
 * @brief is_double_type
 * @param t the type to check
 * @return true iff t is of double type
 */
int is_double_type(Int_type t);

DLLEXPORT
/**
 * @brief is_undef checks if a net is undef
 * @param ctx the context to use
 * @param net the net to check
 * @return true iff the net is undef
 */
int is_undef(Int_ctx ctx, Int_net net);

DLLEXPORT
/**
 * @brief is_true checks if a net is true
 * @param ctx the context to use
 * @param net the net to check
 * @return true iff the net is true
 */
int is_true(Int_ctx ctx, Int_net net);

DLLEXPORT
/**
 * @brief is_false checks if a net is false
 * @param ctx the context to use
 * @param net the net to check
 * @return true iff the net is false
 */
int is_false(Int_ctx ctx, Int_net net);

DLLEXPORT
/**
 * @brief is_number checks if a net is a number
 * @param ctx the context to use
 * @param net the net to check
 * @return true iff the net is a number
 */
int is_number(Int_ctx ctx, Int_net net);

DLLEXPORT
/**
 * @brief is_not checks if a net is a not
 * @param ctx the context to use
 * @param x the net to check
 * @return true iff the net is a not
 */
int is_not(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_and checks if a net is an and
 * @param ctx the context to use
 * @param x the net to check
 * @return true iff the net is an and
 */
int is_and(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_or checks if a net is an or
 * @param ctx the context to use
 * @param x the net to check
 * @return true iff the net is an or
 */
int is_or(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_xor checks if a net is an xor
 * @param ctx the context to use
 * @param x the net to check
 * @return true iff the net is an xor
 */
int is_xor(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_iff checks if a net is an iff
 * @param ctx the context to use
 * @param x the net to check
 * @return true iff the net is an iff
 */
int is_iff(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_add checks if a net is an addition
 * @param ctx the context to use
 * @param x the net to check
 * @return true iff the net is an addition
 */
int is_add(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_mul checks if a net is a multiplication
 * @param ctx the context to use
 * @param x the net to check
 * @return true iff the net is a multiplication
 */
int is_mul(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_eq checks if a net is an equality
 * @param ctx the context to use
 * @param x the net to check
 * @return true iff the net is an equality
 */
int is_eq(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_leq checks if a net is a <=
 * @param ctx the context to use
 * @param x the net to check
 * @return true iff the net is a <=
 */
int is_leq(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_lt checks if a net is a <
 * @param ctx the context to use
 * @param x the net to check
 * @return true iff the net is a <
 */
int is_lt(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_geq checks if a net is a >=
 * @param ctx the context to use
 * @param x the net to check
 * @return true iff the net is a >=
 */
int is_geq(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_gt checks if a net is a >
 * @param ctx the context to use
 * @param x the net to check
 * @return true iff the net is a >
 */
int is_gt(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_input checks if a net is an input of a circuit
 * @param ctx the context to use
 * @param circ the circuit in which the input lies
 * @param net the net to check
 * @return true iff the net is an input
 */
int is_input(Int_ctx ctx, Int_circuit circ, Int_net net);

DLLEXPORT
/**
 * @brief is_output checks if a net is an output of a circuit
 * @param ctx the context to use
 * @param circ the circuit in which the output lies
 * @param net the net to check
 * @return true iff the net is an output
 */
int is_output(Int_ctx ctx, Int_circuit circ, Int_net net);

DLLEXPORT
/**
 * @brief is_latch checks if a net is an latch of a circuit
 * @param ctx the context to use
 * @param circ the circuit in which the latch lies
 * @param net the net to check
 * @return true iff the net is an latch
 */
int is_latch(Int_ctx ctx, Int_circuit circ, Int_net net);

DLLEXPORT
/**
 * @brief get_latch_init retrieves the initial state of a latch
 * @param ctx the context to use
 * @param circ the circuit in which the latch lies
 * @param latch the latch to inspect
 * @return the net corresponding to the initial state
 */
Int_net get_latch_init(Int_ctx, Int_circuit circ, Int_net latch);

DLLEXPORT
/**
 * @brief get_latch_next retrieves the net at the next pin of a latch
 * @param ctx the context to use
 * @param circ the circuit in which the latch lies
 * @param latch the latch to inspect
 * @return the net corresponding to the next pin
 */
Int_net get_latch_next(Int_ctx ctx, Int_circuit circ, Int_net latch);

DLLEXPORT
/**
 * @brief get_net_kind retrieves the net kind
 * @param ctx the context to use
 * @param x the net to use
 * @return the kind of the net
 */
Int_net_kind get_net_kind(Int_ctx ctx , Int_net x);

// DLLEXPORT
// /**
//  * @brief get_input_type retrieves the type an input net
//  * @param ctx the context to use
//  * @param circ the circuit to use
//  * @param x the net to use
//  * @param type output parameter, the type of x
//  */
// Int_type get_input_type(Int_ctx ctx, Int_circuit circ, Int_net x);

#ifdef __cplusplus
}  // extern "C"
#endif

#endif  // SRC_API_INTREPID_H_
