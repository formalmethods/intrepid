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

#ifndef INTREPID_H_
#define INTREPID_H_

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
/**
 * @brief mk_circuit Creates a circuit
 * @param ctx the context to use
 * @param name the unique name id of a circuit
 * @return an empty circuit
 */
Int_circuit mk_circuit(Int_ctx ctx, const char* name);

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
                                 const Int_net* inputs1, const Int_net* inputs2, unsigned inputs_size,
                                 const Int_net* outputs1, const Int_net* outputs2, unsigned outputs_size);

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
 * @brief bmc_reach_targets Tries to reach any previously added target, stops when the first is reached
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
 * @brief br_reach_targets Tries to reach any previously added target, stops when the first is reached
 * @param engine the backward reach engine to use
 * @return the result of the search
 */
Int_engine_result br_reach_targets(Int_engine_br engine);

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
Int_net mk_input(Int_ctx ctx, Int_circuit circ, const char *name, Int_type type);

DLLEXPORT
/**
 * @brief mk_output Marks an existing net as begin an output
 * @param circ the circuit in which the output has to be made
 * @param name the unique name of the output
 * @param net the net to be marked
 */
void mk_output(Int_ctx, Int_circuit circ, const char* name, Int_net net);

DLLEXPORT
/**
 * @brief mk_latch Creates an uninitialized latch with no next state
 * @param ctx the context to use
 * @param circ the circuit on which to create the latch
 * @param name the unique name of this latch
 * @param type the data type of this latch
 * @return A net that encodes the latch
 */
Int_net mk_latch(Int_ctx ctx, Int_circuit circ, const char *name, Int_type type);

DLLEXPORT
/**
 * @brief set_latch_init_next Sets the initial state and the circuit attached to the next pin of the
 * 		  latch
 * @param ctx the context to use
 * @param circ the circuit on which to create the latch
 * @param latch the latch to initialize
 * @param init the initial state
 * @param next the circuit attached to the next pin of the latch
 */
void set_latch_init_next(Int_ctx ctx, Int_circuit circ, Int_net latch, Int_net init, Int_net next);

DLLEXPORT
/**
 * @brief get_inputs_size
 * @param circ
 * @return the number of inputs stored in the circuit
 */
unsigned get_inputs_size(Int_circuit circ);

DLLEXPORT
/**
 * @brief get_input
 * @param circ the circuit
 * @param n the number of input to retrieve
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
 * @brief is_undef checks if a net is undef
 * @param net the net to check
 * @return true iff the net is undef
 */
int is_undef(Int_ctx ctx, Int_net net);

DLLEXPORT
/**
 * @brief is_true checks if a net is true
 * @param net the net to check
 * @return true iff the net is true
 */
int is_true(Int_ctx ctx, Int_net net);

DLLEXPORT
/**
 * @brief is_false checks if a net is false
 * @param net the net to check
 * @return true iff the net is false
 */
int is_false(Int_ctx ctx, Int_net net);

DLLEXPORT
/**
 * @brief is_number checks if a net is a number
 * @param net the net to check
 * @return true iff the net is a number
 */
int is_number(Int_ctx ctx, Int_net net);

DLLEXPORT
/**
 * @brief is_not checks if a net is a not
 * @param ctx
 * @param x
 * @return true iff the net is a not
 */
int is_not(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_and checks if a net is an and
 * @param ctx
 * @param x
 * @return true iff the net is an and
 */
int is_and(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_or checks if a net is an or
 * @param ctx
 * @param x
 * @return true iff the net is an or
 */
int is_or(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_xor checks if a net is an xor
 * @param ctx
 * @param x
 * @return true iff the net is an xor
 */
int is_xor(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_iff checks if a net is an iff
 * @param ctx
 * @param x
 * @return true iff the net is an iff
 */
int is_iff(Int_ctx ctx, Int_net x);

DLLEXPORT
/**
 * @brief is_input checks if a net is an input of a circuit
 * @param circ the circuit in which the input lies
 * @param net the net to check
 * @return true iff the net is an input
 */
int is_input(Int_ctx ctx, Int_circuit circ, Int_net net);

DLLEXPORT
/**
 * @brief is_output checks if a net is an output of a circuit
 * @param circ the circuit in which the output lies
 * @param net the net to check
 * @return true iff the net is an output
 */
int is_output(Int_ctx ctx, Int_circuit circ, Int_net net);

DLLEXPORT
/**
 * @brief is_latch checks if a net is an latch of a circuit
 * @param circ the circuit in which the latch lies
 * @param net the net to check
 * @return true iff the net is an latch
 */
int is_latch(Int_ctx ctx, Int_circuit circ, Int_net net);

DLLEXPORT
/**
 * @brief get_latch_init retrieves the initial state of a latch
 * @param circ the circuit in which the latch lies
 * @param latch the latch to inspect
 * @return the net corresponding to the initial state
 */
Int_net get_latch_init(Int_ctx, Int_circuit circ, Int_net latch);

DLLEXPORT
/**
 * @brief get_latch_next retrieves the net at the next pin of a latch
 * @param circ the circuit in which the latch lies
 * @param latch the latch to inspect
 * @return the net corresponding to the next pin
 */
Int_net get_latch_next(Int_ctx, Int_circuit circ, Int_net latch);

#ifdef __cplusplus
}  // extern "C"
#endif

#endif  // INTREPID_H_
