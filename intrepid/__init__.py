r"""
.___        __                        .__    .___
|   | _____/  |________   ____ ______ |__| __| _/
|   |/    \   __\_  __ \_/ __  \____ \|  |/ __ |
|   |   |  \  |  |  | \/\  ___/|  |_> >  / /_/ |
|___|___|  /__|  |__|    \___  >   __/|__\____ |
         \/                  \/|__|           \/

Intrepid is a scriptable model checker for Control
Engineering and Industrial Automation.
"""

from api import mk_ctx, del_ctx, mk_engine_bmc, set_bmc_current_depth, set_bmc_optimize,\
                bmc_add_target, bmc_reach_targets, mk_engine_br,\
                br_add_target, br_reach_targets, mk_boolean_type,\
                bmc_add_watch, br_add_watch,\
                mk_int8_type, mk_int16_type, mk_int32_type, mk_uint8_type,\
                mk_uint16_type, mk_uint32_type, mk_real_type, mk_double_type,\
                mk_undef, mk_true, mk_false, mk_number, mk_not, mk_and, mk_or,\
                mk_xor, mk_iff, mk_eq, mk_leq, mk_lt, mk_geq, mk_gt, mk_input,\
                mk_output, mk_latch, set_latch_init_next, mk_neq, mk_ite,\
                mk_add, mk_sub, mk_minus, mk_substitute,\
                mk_simulator, simulator_add_target, simulator_simulate,\
                simulator_last_reached_targets_number, simulator_last_reached_target,\
                bmc_last_reached_targets_number, br_last_reached_targets_number,\
                bmc_last_reached_target, br_last_reached_target,\
                bmc_get_counterexample, br_get_counterexample,\
                prepare_value_for_net, bmc_remove_last_reached_targets, br_remove_last_reached_targets,\
                counterexample_prepare_value_for_net, counterexample_get_max_depth,\
                mk_assumption, value_at,\
                push_namespace, pop_namespace,\
                INT_ENGINE_RESULT_UNKNOWN,\
                INT_ENGINE_RESULT_REACHABLE,\
                INT_ENGINE_RESULT_UNREACHABLE